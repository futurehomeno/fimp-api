# FIMP - Futurehome IoT Messaging Protocol 
### [(HTML version)](https://futurehomeno.github.io/fimp-api/#/)

* [Service overview](#service-overview)
* [Component discovery mechanism](#component-discovery-mechanism)
* [Adding / removing things to FH system](#adding--removing-things-to-fh-system)
* [Services](#services)

## Service overview

In FIMP, the functionality of everything that's considered a device is represented by services. These say something about the capabilities of the device, e.g. the service `out_bin_sw` indicates that some part of the device can be turned on / off. Similarly `out_lvl_sw` indicates that some part of the device accepts a value between a given min and max. Note that the services are not specific as to what part of the device they represent. An `out_bin_sw` might turn on / off part of the device, or the device itself.

Each service is further represented by interfaces, where a service must have at least one interface. An interface consist of three parts separated by a period:

 1. The first part of the interface is the **type**. From the perspective of the receiver, it can be either `cmd` - representing an incoming message, or `evt` - representing an outgoing message.

 2. The second part of the interface is the **attribute** which says something about the values supported by the interface. E.g. the `binary` attribute specifies that this interface only support boolean values. A service can have multiple interfaces with different attributes.

 3. The third part of the interface represents the **action** to perform in the case of a `cmd` interface, or the data in the case of `evt`. Typically this takes the form of getters ans setters.

Bringing it all together: the interface `cmd.binary.set` allows you to send a **command** to the **binary attribute** saying you want to **set** (change) it. Similarly, `evt.binary.report` says that there was an **event** (message received) on the **binary attribute** where a **report** was received.

Additionally, each service it will have its own unique address (topic) over which it can send / receive messages, e.g. `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:out_bin_switch/ad:11_0`. The address can be broken down into the following components:

Type | Sample values                  | Description
-----|--------------------------------|------------
pt   | j1, j1c1                       | Parser type, typically j1 (JSON v1) or j1c1 (JSON v1 compression type 1 (gzip)).
mt   | evt, cmd, rsp                  | Message type: cmd - command, evt - event, rsp - response to request.
rt   | ad, app, dev                   | Resource type: ad = adapter, app = application, dev = device.
rn   | zw, vinculum, zigbee, kind-owl | Resource name, i.e. the actual name of the rt.
sv   | out_bin_sw, out_lvl_sw, etc.   | Service name.
ad   |                                | The address of the preceding type.

Breaking down the example `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:out_bin_switch/ad:11_0`, this is the address specifying JSON v1 formatted events sent to a device using zwave with address 1, and the service `out_bin_sw` with address of 11_0. Note here that zwave actually has an address. This is normally set to 1, but in the case of the gateway having multiple instances of zwave, it can be another address.

Lastly, not that each interface within a service share the same address and that a service can never have more than one interface of the same type.

[FIMP message format](message-format.md)

[Topic examples](topics.md)

## Component discovery mechanism

The mechanism allows dynamically discover different system component like adapters and application.

[Component discovery flow and messages](component-discovery.md)

## Adding / removing things to FH system

Things can be added to FH ecosystem in 2 ways:

1. [Adding/removing a thing to FH system via adapter](thing-management.md)
2. [Connecting/disconnecting a system to FH system](system-management.md)

First method should be used to add a thing which isn't paired with underlying RF module, for instance: Z-Wave, Zigbee, Bluetooth

Second method should be used to connect a system which already has a number of connected devices, for instance: IKEA Trådfri, Phillips Hue, Sonos, etc.

Example: add z-wave device, remove z-wave device, add zigbee device, remove zigbee device.

## Services

List of all supported services with their documentation can be found in this [document](/services/services.md).
