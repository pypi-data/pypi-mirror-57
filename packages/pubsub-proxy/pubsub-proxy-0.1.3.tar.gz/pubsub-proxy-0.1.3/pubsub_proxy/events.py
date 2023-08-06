from io import BytesIO
from typing import Any, Dict, Optional, Tuple

from pubsub_proxy.proto.events_pb2 import Event


class PubSubEvent:
    def __init__(self, event_type) -> None:
        self.event_type = event_type
        self.timestamp = timestamp

    @property
    def subscription_key(self) -> Tuple[str, str]:
        raise NotImplementedError

    @classmethod
    def parse(
        cls,
        sender: str,
        sequence_number: int,
        event_key_address: str,
        event_type: str,
        event: Event,
        timestamp: int,
    ) -> Optional["PubSubEvent"]:
        raise NotImplementedError

    @property
    def message(self) -> Dict[str, Any]:
        raise NotImplementedError


class ReceivedPaymentEvent(PubSubEvent):
    def __init__(
        self,
        sender: str,
        sequence_number: int,
        timestamp: int,
        event_type: str,
        amount: int,
        payee: str,
        payer: str,
        subaddress: str,
    ) -> None:
        self.sender = sender
        self.sequence_number = sequence_number
        self.timestamp = timestamp
        self.event_type = event_type
        self.amount = amount
        self.payee = payee
        self.payer = payer
        self.subaddress = subaddress

    @property
    def subscription_key(self) -> Tuple[str, str]:
        return (self.event_type, self.payee)

    @classmethod
    def parse(
        cls,
        sender: str,
        sequence_number: int,
        timestamp: int,
        event_key_address: str,
        event_type: str,
        event: Event,
    ) -> Optional["ReceivedPaymentEvent"]:
        buffer = BytesIO(event.event_data)
        amount = int.from_bytes(buffer.read(8), byteorder="little")
        payer = buffer.read(32).hex()
        length = int.from_bytes(buffer.read(4), byteorder="little")
        subaddress = buffer.read(length).decode("utf8")
        return cls(
            sender,
            sequence_number,
            timestamp,
            event_type,
            amount,
            event_key_address,
            payer,
            subaddress,
        )

    @property
    def message(self) -> Dict[str, Any]:
        return dict(
            sender=self.sender,
            sequence_number=self.sequence_number,
            timestamp=self.timestamp,
            event_type="received",
            amount=self.amount,
            payee=self.payee,
            payer=self.payer,
            subaddress=self.subaddress,
        )


class SentPaymentEvent(PubSubEvent):
    def __init__(
        self,
        sender: str,
        sequence_number: int,
        timestamp: int,
        event_type: str,
        amount: int,
        payee: str,
        payer: str,
    ) -> None:
        self.sender = sender
        self.sequence_number = sequence_number
        self.timestamp = timestamp
        self.event_type = event_type
        self.amount = amount
        self.payee = payee
        self.payer = payer

    @property
    def subscription_key(self) -> Tuple[str, str]:
        return (self.event_type, self.payer)

    @classmethod
    def parse(
        cls,
        sender: str,
        sequence_number: int,
        timestamp: int,
        event_key_address: str,
        event_type: str,
        event: Event,
    ) -> Optional["SentPaymentEvent"]:
        buffer = BytesIO(event.event_data)
        amount = int.from_bytes(buffer.read(8), byteorder="little")
        payee = buffer.read(32).hex()
        return cls(
            sender, sequence_number, timestamp, event_type, amount, payee, sender
        )

    @property
    def message(self) -> Dict[str, Any]:
        return dict(
            sender=self.sender,
            sequence_number=self.sequence_number,
            timestamp=self.timestamp,
            event_type="sent",
            amount=self.amount,
            payee=self.payee,
            payer=self.payer,
        )


def parse_event(
    sender: str, sequence_number: int, event: Event, timestamp: int,
) -> Optional[PubSubEvent]:
    event_key_address = parse_event_key_address(event.key)
    event_type = parse_event_type(event.type_tag)
    event_class = {
        "LibraAccount.ReceivedPaymentEvent": ReceivedPaymentEvent,
        "LibraAccount.SentPaymentEvent": SentPaymentEvent,
    }.get(event_type)
    if event_class is None:
        return None
    return event_class.parse(
        sender, sequence_number, timestamp, event_key_address, event_type, event
    )


def get_block_timestamp(raw_data: bytes) -> Optional[int]:
    # TODO: remove explicit bytes manipulation and use lcs library
    buffer = BytesIO(raw_data)
    txn_type = int.from_bytes(buffer.read(4), byteorder="little")
    if txn_type != 2:
        return None
    length = int.from_bytes(buffer.read(4), byteorder="little")
    buffer.read(length)
    return int.from_bytes(buffer.read(8), byteorder="little")


def get_transaction_info(raw_data: bytes) -> Optional[Tuple[str, int]]:
    # TODO: remove explicit bytes manipulation and use lcs library
    buffer = BytesIO(raw_data)
    txn_type = int.from_bytes(buffer.read(4), byteorder="little")
    if txn_type != 0:
        return None
    address = buffer.read(32).hex()
    sequence_number = int.from_bytes(buffer.read(8), byteorder="little")
    return (address, sequence_number)


def parse_event_key_address(raw_data: bytes) -> str:
    # TODO: remove explicit bytes manipulation and use lcs library
    buffer = BytesIO(raw_data)
    salt = buffer.read(8)
    return buffer.read(32).hex()


def parse_event_type(raw_data: bytes) -> str:
    # TODO: remove explicit bytes manipulation and use lcs library
    buffer = BytesIO(raw_data)
    if int.from_bytes(buffer.read(4), byteorder="little") != 4:
        return ""
    address = buffer.read(32).hex()
    size = int.from_bytes(buffer.read(4), byteorder="little")
    module = buffer.read(size).decode("ascii")
    size = int.from_bytes(buffer.read(4), byteorder="little")
    event_name = buffer.read(size).decode("ascii")
    return f"{module}.{event_name}"
