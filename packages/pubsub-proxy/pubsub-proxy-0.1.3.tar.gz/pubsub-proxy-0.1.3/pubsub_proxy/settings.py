import json
from typing import Any, Dict


class Settings:
    def __init__(self, data: Dict[str, Any]):
        self.libra_node_uri = data["libra_node_uri"]
        self.batch_size = data["batch_size"]
        self.sync_interval_ms = data["sync_interval_ms"]
        self.log_file = data["log_file"]

        self.progress_storage_type = data["progress_storage_type"]
        self.progress_storage_config = data["progress_storage_config"]

        self.pubsub_type = data["pubsub_type"]
        self.pubsub_config = data["pubsub_config"]

        self.subscription_storage_type = data["subscription_storage_type"]
        self.subscription_storage_config = data["subscription_storage_config"]

    @classmethod
    def load_from_file(cls, file_path: str) -> "Settings":
        return cls(json.loads(open(file_path, "r").read()))
