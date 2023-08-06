import argparse
import logging
from pubsub_proxy import LibraPubSubProxy, Settings


def main():
    parser = argparse.ArgumentParser(
        description="daemon that proxies blockchain events to pubsub broker"
    )
    parser.add_argument(
        "config",
        metavar="c",
        type=str,
        help="pubsub daemon configuration file",
        default="configs/basic_testnet.json",
    )
    args = parser.parse_args()

    settings = Settings.load_from_file(args.config)
    logging.basicConfig(filename=settings.log_file, level=logging.INFO)
    LibraPubSubProxy(settings).start()


if __name__ == "__main__":
    main()
