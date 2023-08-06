import json
from typing import Any, Dict, Tuple

from pubsub_proxy.util import load_custom_backend


class BaseProgressStorage:
    """
    Base interface for ProgressStorage

    Used by daemon to track progress.
    Gets updated after successful enqueuing of messages to pubsub broker
    """

    def fetch_state(self) -> Tuple[int, int]:
        raise NotImplementedError

    def save_state(self, known_version: int, timestamp: int) -> None:
        raise NotImplementedError


class FileProgressStorage(BaseProgressStorage):
    def __init__(self, config: Dict[str, Any]) -> None:
        self.version = 0
        self.timestamp = 0
        self.path = config["path"]

    def fetch_state(self) -> Tuple[int, int]:
        try:
            with open(self.path, "r") as file:
                state = json.loads(file.read())
                self.version = state["version"]
                self.timestamp = state["timestamp"]
        except (FileNotFoundError, json.JSONDecodeError):
            ...
        return (self.version, self.timestamp)

    def save_state(self, version: int, timestamp: int) -> None:
        self.version = version
        self.timestamp = timestamp
        state = dict(version=self.version, timestamp=self.timestamp)
        with open(self.path, "w") as file:
            file.write(json.dumps(state))


def create_progress_storage(
    storage_type: str, config: Dict[str, Any]
) -> BaseProgressStorage:
    storage_class = {"file": FileProgressStorage}.get(storage_type)
    if storage_class is None:
        storage_class = load_custom_backend(storage_type)
    return storage_class(config)
