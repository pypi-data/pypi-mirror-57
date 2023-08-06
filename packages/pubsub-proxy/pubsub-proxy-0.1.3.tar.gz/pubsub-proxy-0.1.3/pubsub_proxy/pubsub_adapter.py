import json
from typing import Any, Dict, List

from pubsub_proxy.events import PubSubEvent
from pubsub_proxy.util import load_custom_backend


class BasePubSubClient:
    """
    Base interface for PubSubClient

    Used by daemon to enqueue new events as messages to preferred pubsub broker
    """

    def enqueue(self, events: List[PubSubEvent]) -> None:
        raise NotImplementedError


class LogPubSubClient(BasePubSubClient):
    """
    Dummy implementation of BasePubSubClient interface
    Logs observed events to file
    """

    def __init__(self, config: Dict[str, Any]) -> None:
        self.file_path = config["file_path"]

    def enqueue(self, events: List[PubSubEvent]) -> None:
        with open(self.file_path, "a") as log_file:
            for event in events:
                log_file.write(json.dumps(event.message) + "\n")


def create_pubsub_client(pubsub_type: str, config: Dict[str, Any]) -> BasePubSubClient:
    pubsub_class = {"logging": LogPubSubClient,}.get(pubsub_type)
    if pubsub_class is None:
        pubsub_class = load_custom_backend(pubsub_type)
    return pubsub_class(config)
