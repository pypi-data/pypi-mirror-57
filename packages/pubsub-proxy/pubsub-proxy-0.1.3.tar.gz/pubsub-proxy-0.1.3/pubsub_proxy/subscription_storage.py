from typing import Any, Dict, List

from pubsub_proxy.util import load_custom_backend


class BaseSubscriptionStorage:
    """
    Base interface for SubscriptionStorage

    Used by daemon to query active subscriptions
    """

    def contains(self, event_type: str, address: str) -> bool:
        raise NotImplementedError


class InMemorySubscriptionStorage(BaseSubscriptionStorage):
    """
    Implementation of BaseSubscriptionStorage interface
    that reads list of subscribers from static config
    """

    def __init__(self, config: Dict[str, Any]) -> None:
        self.accounts = set(config["accounts"])

    def contains(self, event_type: str, address: str) -> bool:
        return address in self.accounts


def create_subscription_storage(
    storage_type: str, config: Dict[str, Any]
) -> BaseSubscriptionStorage:
    storage_class = {"in_memory": InMemorySubscriptionStorage}.get(storage_type)
    if storage_class is None:
        storage_class = load_custom_backend(storage_type)
    return storage_class(config)
