import logging
import time
from typing import List, Dict, Tuple, Set

from grpc import insecure_channel

from pubsub_proxy.proto.admission_control_pb2_grpc import AdmissionControlStub
from pubsub_proxy.proto.get_with_proof_pb2 import UpdateToLatestLedgerRequest
from pubsub_proxy.events import (
    get_transaction_info,
    PubSubEvent,
    parse_event,
    get_block_timestamp,
)
from pubsub_proxy.progress_storage import create_progress_storage
from pubsub_proxy.pubsub_adapter import create_pubsub_client
from pubsub_proxy.subscription_storage import create_subscription_storage
from pubsub_proxy.settings import Settings


class LibraPubSubProxy:
    def __init__(self, settings: Settings) -> None:
        self.ac_client = AdmissionControlStub(insecure_channel(settings.libra_node_uri))

        self.progress_storage = create_progress_storage(
            settings.progress_storage_type, settings.progress_storage_config
        )
        self.subscription_storage = create_subscription_storage(
            settings.subscription_storage_type, settings.subscription_storage_config
        )
        self.pubsub_client = create_pubsub_client(
            settings.pubsub_type, settings.pubsub_config
        )
        self.known_version = None
        self.timestamp = None
        self.batch_size = settings.batch_size
        self.sync_interval_ms = settings.sync_interval_ms

    def start(self) -> None:
        self.known_version, self.timestamp = self.progress_storage.fetch_state()
        logging.info("pubsub-proxy started: known version is %s" % self.known_version)

        while True:
            try:
                events = self.sync()
                self.pubsub_client.enqueue(events)
                self.progress_storage.save_state(self.known_version, self.timestamp)
                logging.info(
                    "processed next chunk. New known version is %s" % self.known_version
                )
            except Exception as exc:
                logging.error("failed to perform sync: %s" % exc)
            time.sleep(self.sync_interval_ms / 1000)

    def sync(self) -> List[PubSubEvent]:
        request = UpdateToLatestLedgerRequest()
        request_item = request.requested_items.add()
        txn_request = request_item.get_transactions_request
        txn_request.start_version = self.known_version + 1
        txn_request.limit = self.batch_size
        txn_request.fetch_events = True

        response = (
            self.ac_client.UpdateToLatestLedger(request)
            .response_items[0]
            .get_transactions_response.txn_list_with_proof
        )
        new_events = []
        for idx, events in enumerate(response.events_for_versions.events_for_version):
            timestamp = get_block_timestamp(response.transactions[idx].transaction)
            if timestamp is not None:
                self.timestamp = timestamp
                continue

            info = get_transaction_info(response.transactions[idx].transaction)
            if info is None:
                continue
            sender, sequence_number = info

            for event in events.events:
                pubsub_event = parse_event(
                    sender, sequence_number, event, self.timestamp
                )

                if pubsub_event is not None and self.subscription_storage.contains(
                    *pubsub_event.subscription_key
                ):
                    new_events.append(pubsub_event)

        if len(response.transactions) > 0:
            first_version = response.first_transaction_version.value
            self.known_version = first_version + len(response.transactions) - 1

        return new_events
