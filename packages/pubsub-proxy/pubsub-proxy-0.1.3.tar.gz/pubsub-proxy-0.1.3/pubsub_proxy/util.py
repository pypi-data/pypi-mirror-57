import importlib


def load_custom_backend(path):
    parts = path.split(".")
    module = importlib.import_module(".".join(parts[:-1]))
    return getattr(module, parts[-1])
