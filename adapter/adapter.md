# Adapter

Technology adapter is a special case of an application running on the hub responsible for managing external physical devices, otherwise called things.
Their main role is to be an adapter between FIMP and a specific technology protocol while providing functionalities such as:

* pairing/including things into the network,
* unpairing/excluding things from the network,
* relaying commands to the things,
* relaying events from the things.

Adapters may use various communication technologies, such as Z-Wave and Zigbee wireless networks, direct connection through the local network or indirect through a third-party
cloud provider.

## Thing Management

For description of how to add and remove things from the system see the [thing management](/adapter/thing_management.md) documentation.

## Network Management

For description of how to get connection status or update network see the [network_management](/adapter/network_management.md) documentation.

## Additional Functionalities

An adapter may provide additional functionalities beyond what is defined in the FIMP protocol requirements.
Good examples are advanced configuration or methods specific to the technology, and should be outlined in the adapter documentation.
It is recommended that adapters follow guidelines for [common interfaces](/common_interfaces/common_interfaces.md) when implementing such functionalities.

