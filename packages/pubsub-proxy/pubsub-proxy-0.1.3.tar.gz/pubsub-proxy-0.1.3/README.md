# pubsub_proxy

## Summary

This project contains simple daemon that acts as a bridge between events on Libra blockchain and pub/sub broker of your choice


## Usage
Install pubsub_proxy package in your virtualenv<br />
Create configuration file. Example can be found in `configs/basic_testnet.json`<br />
To start daemon simply run:
```
pubsub-proxy `path_to_config`
```

## Configuration
- Format: json
- Parameters:
    * libra_node_uri: uri of Full Node used for tailing new events
    * batch_size: batch size of single request to full node
    * sync_interval_ms: time interval between queries to full node
    * pubsub_type: pub/sub type used to deliver new events<br />
        current available options: `logging`
    * pubsub_config: configuration of specific broker<br />
        *exact configuration depends on broker type*
    * progress_storage_type: type of storage used to store progress<br />
        current available options: `in_memory`
    * progress_storage_config: configuration of specific storage<br />
        *exact configuration depends on storage type*
    * subscription_storage_type: type of storage used to store subscriptions
    * subscription_storage_config: configuration of specific storage<br />
        *exact configuration depends on storage type*

Note: instead of using one of predefined backend types for pub/sub broker, progress storage or subscription storage,<br/>
you can always create custom implementation that implements base interface and pass it to configuration directly.
