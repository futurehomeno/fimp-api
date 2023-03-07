# Adapter

Technology adapter is a special case of an application running on the hub responsible for managing external physical devices, otherwise called things.
Their main role is to be an adapter between FIMP and a specific technology protocol while providing functionalities such as:

* pairing/including things into the network,
* unpairing/excluding things from the network,
* relaying commands to the things,
* relaying events from the things.

Adapters might use various communication technologies, such as Z-Wave and Zigbee wireless networks, direct connection through the local network or indirect through a third-party 
cloud provider.

## Adapter Service

For description of how to interact with the adapter on the highest level see the [adapter service](/adapter/adapter_service.md) documentation.

## Thing Management

For description of how to add and remove things from the system see the [thing management](/adapter/thing_management.md) documentation.

