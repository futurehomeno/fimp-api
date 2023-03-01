# Thing Management

The following document describes the interaction flows and FIMP specification used in management of things.

## Flows

### Network Inclusion

Network inclusion flow is used by wireless network adapters, such as Z-Wave and Zigbee, to include new devices into the network and add them to the system.

* Client sends `cmd.thing.inclusion` command to the adapter with `true` value to start inclusion process and switch adapter into pairing mode.
* User interacts with a physical device to switch it into pairing mode, e.g. clicks a button on a device three times in a quick sequence.
* At any time the adapter can generate `evt.thing.inclusion_status_report` event to report the current status of the inclusion process.
* If pairing of the device requires PIN and client support PIN request, the adapter generates `evt.thing.pin_needed` report.
    * Client sends `cmd.thing.pin` command with the PIN to the adapter.
* Once inclusion and interview of the device is finished adapter generates `evt.thing.inclusion_report` event with the thing specification.
* Client sends `cmd.thing.inclusion` command to the adapter with `false` value to stop the inclusion process. Regardless, adapter should cancel inclusion after a specified timeout.

### Smart Start Inclusion

Smart Start inclusion is a Z-Wave specific flow allowing to preliminarily add a device to a provisioning list so that it can be automatically included once the device is turned on.
See [Smart Start](/adapter/zwave_smart_start.md) documentation for more details.

### Custom Inclusion

Adapters utilizing custom protocol communication through local network or third-party cloud will have their own specific inclusion flow specified it in their own documentation.
Preliminary steps of such flows will often include authentication with a third-party system, specific configuration, and selecting devices to be connected to the system.
At the end of this process the adapter is always required to generate `evt.thing.inclusion_report` event with the thing specification.

### Network Exclusion

Network exclusion flow is used by wireless network adapters to exclude devices from the network and remove them from the system.

* Client sends `cmd.thing.exclusion` command to the adapter to start exclusion process and switch adapter into unpairing mode.
* User interacts with a physical device to switch it into unpairing mode, e.g. clicks a button on a device three times in a quick sequence.
* At any time the adapter can generate `evt.thing.exclusion_status_report` event to report the current status of the exclusion process.
* Once exclusion is finished adapter generates `evt.thing.exclusion_report` event with the excluded thing address.

### Forced Exclusion

If a device is offline and unreachable or the adapter does not support the network exclusion flow, the device can be force deleted from the system using this flow.

* Client sends `cmd.thing.delete` command to the adapter to force delete a thing.
* Adapter removes the thing from the network and generates `evt.thing.exclusion_report` event with the excluded thing address.

### Requesting Inclusion Report

* At any time a client can request inclusion report by sending `cmd.thing.get_inclusion_report` command to the adapter with a specified address of an already paired thing.
* Adapter generates `evt.thing.inclusion_report` event with the thing specification.

## FIMP Specification

### Topics

Every adapter should have unique resource name and use the following topics in accordance with [topic format](/fimp/topic_format.md):

`pt:j1/mt:cmd/rt:ad/rn:{RESOURCE_NAME}/ad:1`

`pt:j1/mt:evt/rt:ad/rn:{RESOURCE_NAME}/ad:1`

### Service name

Every adapter should define its own service name.

### Interfaces

| Type | Interface                         | Value type | Properties                                        | Description                                                                                                                 |
|------|-----------------------------------|------------|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.thing.inclusion               | bool       | `pin`, `force_non_secure`, `supports_pin_request` | For `true` starts and for `false` stops a thing inclusion process.                                                          |                         
| out  | evt.thing.inclusion_status_report | string     |                                                   | Returns stage of the ongoing inclusion process, see [`inclusion_status`](#definitions).                                     |
| out  | evt.thing.inclusion_report        | object     |                                                   | Reports thing specification, see [`inclusion_report`](#definitions).                                                        |
| in   | cmd.thing.get_inclusion_report    | string     |                                                   | Requests inclusion report for the provided thing address.                                                                   |
| out  | evt.thing.pin_needed              | null       |                                                   | Informs that PIN is required to continue a thing inclusion.                                                                 |
| in   | cmd.thing.pin                     | string     |                                                   | Provides PIN required for a thing inclusion.                                                                                |
| in   | cmd.thing.exclusion               | bool       |                                                   | For `true` starts and for `false` stops a thing exclusion process.                                                          | 
| out  | evt.thing.exclusion_status_report | string     |                                                   | Returns stage of the ongoing exclusion process,  see [`exclusion_status`](#definitions).                                    |
| out  | evt.thing.exclusion_report        | object     |                                                   | Reports thing exclusion, see [`thing_identifier`](#definitions).                                                            |
| in   | cmd.thing.delete                  | object     |                                                   | Requests thing deletion if device is offline or exclusion process is not supported, see [`thing_identifier`](#definitions). |

### Interface properties

| Name                   | Example   | Required | Description                                                                  |
|------------------------|-----------|----------|------------------------------------------------------------------------------|
| `pin`                  | `"12345"` | No       | PIN to be used during the inclusion process.                                 |
| `force_non_secure`     | `"true"`  | No       | Force non-secure inclusion process to pair the device.                       |
| `supports_pin_request` | `"true"`  | No       | Indicates that the client supports PIN request during the inclusion process. |

### Definitions

* `inclusion_status` is one of the following values: `ADD_NODE_STARTED`, `ADD_NODE_ADDED`, `ADD_NODE_PROTOCOL_DONE`, `ADD_NODE_GET_NODE_INFO`, `ADD_NODE_DONE`.

* `exclusion_status` is one of the following values:  `REMOVE_NODE_STARTED`, `REMOVE_NODE_DONE`.

* `thing_identifier` is an object with the following structure:

| Field   | Type   | Example | Description         |
|---------|--------|---------|---------------------|
| address | string | `24`    | Address of a thing. |

* `inclusion_report` is an object with the following structure:

| Field               | Type        | Example                        | Description                                                                                                                                                                              |
|---------------------|-------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| address             | string      | `24`                           | An arbitrary unique identifier of the thing within the adapter, equal to node ID in Z-Wave and UID in Zigbee.                                                                            |
| groups              | str_array   | `["ch_0", "ch_1"]`             | Groups are used to link multiple services into one logical group. Each group is effectively a separate device within a single thing, equal to channels in Z-Wave or endpoints in Zigbee. |
| services            | object      | `[{"name":"out_bin_switch"}]`  | An array of [`service_definition`](#definitions) objects for all services provided by the thing.                                                                                         |
| product_name        | string      | `"Fibaro Double Switch"`       | Optional initial human-readable name of the device as shown to the user. If empty falls back to product hash.                                                                            |
| product_hash        | string      | `"zw_134_3_116"`               | Product hash is a unique identifier of the product consisting of joined adapter, manufacturer and product identifiers.                                                                   |
| product_id          | string      | `"3_116"`                      | Name of identification of the model of the device.                                                                                                                                       |
| manufacturer_id     | string      | `"134"`                        | Name or identification of the manufacturer of the device.                                                                                                                                |
| device_id           | string      | `"123456-987654-4567-1234"`    | Optional unique identifier or serial number of the device.                                                                                                                               |
| hw_ver              | string      | `"1"`                          | Optional hardware version of the thing.                                                                                                                                                  |
| sw_ver              | string      | `"257"`                        | Optional software version of the thing.                                                                                                                                                  |
| comm_tech           | string      | `"zw"`                         | Technology used by the adapter to communicate with the device, one of `zw`, `zigbee`, `local_network`, `cloud` values.                                                                   |
| power_source        | string      | `"ac"`                         | Power source of the device. Possible values: "dc", "ac", "battery".                                                                                                                      |
| wakeup_interval     | int         | `3600`                         | Wakeup interval for battery powered devices in seconds.                                                                                                                                  |
| security            | string      | `"insecure"`                   | Level of communication security, either `insecure` or `secure`.                                                                                                                          |
| tech_specific_props | str_map     | `{"zw_lib_type": "3"}`         | Optional custom properties of the thing specific to the technology adapter.                                                                                                              |
| prop_set            | any_map_map | `{"set_a":{"prop_1":"val_1"}}` | Optional map of custom property sets of services specific to the technology adapter. These sets can be referenced from [`service_definition`](#definitions).                             |

* `service_definition` is an object with the following structure:

| Field        | Type      | Example                                          | Description                                                                                                                                              |
|--------------|-----------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| name         | string    | `"out_bin_switch"`                               | Name of the service, as specified in [device services](/device_services/device_services.md) documentation.                                               |
| address      | string    | `"/rt:dev/rn:zw/ad:1/sv:out_bin_switch/ad:21_0"` | An address of the service starting from a resource type segment. Service address segment should contain thing address and optional group identification. |
| groups       | str_array | `["ch_0"]`                                       | Groups to which the service belongs. It is recommended to never attach service to more than a single group.                                              |
| enabled      | bool      | `true`                                           | Indicates whether service is enabled or not.                                                                                                             |
| interfaces   | array     | `[{"msg_t":"evt.binary.report"}]`                | An array of [`interface_spec`](#definitions) objects for all interfaces provided by the service.                                                         |
| props        | any_map   | `{"sup_units": ["W"]}`                           | A map of service properties.                                                                                                                             |
| prop_set_ref | string    | `"set_a"`                                        | Reference to a property set defined in `prop_set`(#definitions). These are technology specific and for informational purpose only.                       |

* `interface_spec` is an object with the following structure:

| Field   | Type   | Example            | Description                                                                                                                           |
|---------|--------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| int_t   | string | `"out"`            | Type of the interface, either `in` for incoming messages or `out` for outgoing messages.                                              |
| msg_t   | string | `"evt.pd7.notify"` | Message type or in other words interface name, see [interface format](/fimp/message_format.md#interface-format) for more information. |
| val_t   | string | `"object"`         | Value type, see [value types ](/fimp/message_format.md#value-types) for more information.                                             |
| version | string | `"1"`              | Supported version of the protocol.                                                                                                    |

### Examples

* Example of a command to start network inclusion process:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.thing.inclusion",
  "val_t": "bool",
  "val": true,
  "props": {
    "supports_pin_request": "true"
  },
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of a command to stop an ongoing network inclusion process:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.thing.inclusion",
  "val_t": "bool",
  "val": false,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of an event indicating the need of providing a PIN to continue the inclusion process:

```json
{
  "serv": "zwave-ad",
  "type": "evt.thing.pin_needed",
  "val_t": "string",
  "val": null,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:evt/rt:ad/rn:zw/ad:1"
}
```

* Example of a command providing a PIN required to continue the inclusion process:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.thing.pin",
  "val_t": "string",
  "val": "12345",
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of an event indicating the current status of the inclusion process:

```json
{
  "serv": "zwave-ad",
  "type": "evt.thing.inclusion_status_report",
  "val_t": "null",
  "val": "ADD_NODE_GET_NODE_INFO",
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:evt/rt:ad/rn:zw/ad:1"
}
```

* Example of a thing inclusion report:

```json
{
  "serv": "zwave-ad",
  "type": "evt.thing.inclusion_report",
  "val_t": "object",
  "val": {
    "address": "21",
    "groups": [
      "ch_0"
    ],
    "product_name": "",
    "product_hash": "zw_134_3_116",
    "product_id": "3_116",
    "manufacturer_id": "134",
    "device_id": "",
    "hw_ver": "1",
    "sw_ver": "257",
    "comm_tech": "zw",
    "power_source": "ac",
    "wakeup_interval": -1,
    "security": "insecure",
    "services": [
      {
        "name": "out_bin_switch",
        "address": "/rt:dev/rn:zw/ad:1/sv:out_bin_switch/ad:21_0",
        "groups": [
          "ch_0"
        ],
        "enabled": true,
        "interfaces": [
          {
            "intf_t": "out",
            "msg_t": "evt.binary.report",
            "val_t": "bool",
            "ver": "1"
          },
          {
            "intf_t": "in",
            "msg_t": "cmd.binary.set",
            "val_t": "bool",
            "ver": "1"
          },
          {
            "intf_t": "in",
            "msg_t": "cmd.binary.get_report",
            "val_t": "null",
            "ver": "1"
          }
        ],
        "props": {
          "is_secure": false,
          "is_unsecure": true
        },
        "prop_set_ref": "nif_0"
      }
    ],
    "tech_specific_props": {
      "zw_lib_type": "3",
      "zw_product_id": "116",
      "zw_product_type": "3",
      "zw_protocol_ver": "1062",
      "zw_sleep_capable": "0"
    },
    "prop_set": {
      "nif_0": {
        "zw_generic_dev_class": "16",
        "zw_installer_icon": "1792",
        "zw_node_type": "0",
        "zw_plus_version": "1",
        "zw_role_type": "5",
        "zw_specific_dev_class": "1",
        "zw_supported_cc": []
      }
    }
  },
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:evt/rt:ad/rn:zw/ad:1"
}
```

* Example of a command requesting inclusion report for an already paired thing:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.thing.get_inclusion_report",
  "val_t": "string",
  "val": "21",
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of a command to start network exclusion process:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.thing.exclusion",
  "val_t": "bool",
  "val": true,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of a command to stop an ongoing network exclusion process:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.thing.exclusion",
  "val_t": "bool",
  "val": false,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of an event confirming successful exclusion process:

```json
{
  "serv": "zwave-ad",
  "type": "evt.thing.exclusion_report",
  "val_t": "object",
  "val": {
    "address": "21"
  },
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:evt/rt:ad/rn:zw/ad:1"
}
```

* Example of an event confirming successful exclusion process:

```json
{
  "serv": "zigbee",
  "type": "cmd.thing.delete",
  "val_t": "object",
  "val": {
    "address": "21"
  },
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zigbee/ad:1"
}
```
