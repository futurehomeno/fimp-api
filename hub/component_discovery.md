# Component Discovery

Every application or adapter running on the hub must participate in the system component discovery mechanism.
In order to discover all applications and adapters a discovery request message is sent to a well known address `pt:j1/mt:cmd/rt:discovery`.
Whenever an application or adapter receives a discovery request it has to respond with a discovery event to a well known address `pt:j1/mt:evt/rt:discovery`.

> **Important!** System component discovery protocol is experimental and can be modified in a backwards in-compatible way.

## FIMP Specification

### Topics

`pt:j1/mt:cmd/rt:discovery`

`pt:j1/mt:evt/rt:discovery`

### Service name

`system`

### Interfaces

| Type | Interface             | Value type | Description                                                                                          |
|------|-----------------------|------------|------------------------------------------------------------------------------------------------------|
| in   | cmd.discovery.request | null       | Requests a discovery report from all system components.                                              |
| out  | evt.discovery.report  | object     | Reports component specification. See [`discovery_report`](#definitions) definition for more details. |

### Definitions

* `discovery_report` is an object with the following structure:

| Field                    | Type   | Example                           | Description                                                                                 |
|--------------------------|--------|-----------------------------------|---------------------------------------------------------------------------------------------|
| package_name             | string | `"zwave-ad"`                      | Package name of the component, might be different than resource name.                       |
| resource_name            | string | `"zw"`                            | Resource name of the component.                                                             |
| resource_type            | string | `"ad"`                            | Resource type of the component. Must be either `app` for applications or `ad` for adapters. |
| instance_id              | string | `"1"`                             | Resource address of the component.                                                          |
| version                  | string | `"1.3.0"`                         | Version of the component.                                                                   |
| resource_full_name       | string | `"Z-Wave adapter"`                | Display name of the component as shown in the registry.                                     |
| description              | string | `"Connects Z-Wave devices."`      | Short description of the component as shown in the registry.                                |
| author                   | string | `"dev@futurehome.no"`             | Email address of the author of the component as shown in the registry.                      |
| doc_url                  | string | `"https://support.futurehome.no"` | Optional URL to the online documentation of the component.                                  |
| app_info                 | object | `{"services":{}}`                 | Additional application information, present when `resource_type` is `app`.                  |
| adapter_info             | object | `{"technology":"zw"}`             | Additional adapter information, present when `resource_type` is `ad`.                       |
| is_instance_configurable | bool   | `false`                           | If true, the instance ID can be configured and changed.                                     |
| config_required          | bool   | `false`                           | If true, the component requires configuration before it can be used.                        |

* `adapter_info` is an object with the following structure:

| Field                   | Type    | Example                          | Description                                                        |
|-------------------------|---------|----------------------------------|--------------------------------------------------------------------|
| services                | string  | `[{"name":"zwave-ad"}}]`         | An array of [`service_spec`](#definitions) definitions.            |
| technology              | string  | `zw`                             | One of `zw`, `zigbee`, `local_network`, `cloud`.                   |
| network_management_type | string  | `inclusion_exclusion`            | One of `inclusion_exclusion`, `inclusion_dev_remove`, `full_sync`. |
| fw_version              | string  | `"v0.2.52"`                      | Optional version of the firmware used by the adapter.              |
| hw_dependency           | str_map | `{"serial_port":"/dev/ttyUSB1"}` | Optional hardware dependencies of the adapter.                     |

* `app_info` is an object with the following structure:

| Field    | Type   | Example                  | Description                                             |
|----------|--------|--------------------------|---------------------------------------------------------|
| services | string | `[{"name":"vinculum"}}]` | An array of [`service_spec`](#definitions) definitions. |

* `service_spec` is an object with the following structure:

| Field      | Type   | Example                        | Description                                                                     |
|------------|--------|--------------------------------|---------------------------------------------------------------------------------|
| name       | string | `"vinculum"`                   | A name of the service. Can be equal to the resource name for most applications. |
| address    | string | `"rt:app/rn:vinculum/ad:1"`    | An address of the service.                                                      |
| enabled    | bool   | `true`                         | Set to `true` if service is enabled.                                            |
| interfaces | object | `[{"msg_t":"evt.pd7.notify"}]` | An array of [`interface_spec`](#definitions) definitions.                       |

* `interface_spec` is an object with the following structure:

| Field   | Type   | Example            | Description                                                                                                                           |
|---------|--------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| int_t   | string | `"out"`            | Type of the interface, either `in` for incoming messages or `out` for outgoing messages.                                              |
| msg_t   | string | `"evt.pd7.notify"` | Message type or in other words interface name, see [interface format](/fimp/message_format.md#interface-format) for more information. |
| val_t   | string | `"object"`         | Value type, see [value types ](/fimp/message_format.md#value-types) for more information.                                             |
| version | string | `"1"`              | Supported version of the protocol.                                                                                                    |

### Examples

* Example of a system component discovery request:

```json
{
  "serv": "system",
  "type": "cmd.discovery.request",
  "val_t": "null",
  "val": null,
  "tags": null,
  "props": null,
  "ver": "1",
  "src": "-",
  "ctime": "2019-05-27T17:01:17.148+05:00",
  "uid": "8d7941e6-5a82-4f88-8403-63a0bd543e2a",
  "topic": "pt:j1/mt:cmd/rt:discovery"
}
```

* Example of a discovery report for an adapter:

```json
{
  "type": "evt.discovery.report",
  "serv": "system",
  "val_t": "object",
  "val": {
    "package_name": "zwave-ad",
    "resource_name": "zw",
    "resource_type": "ad",
    "instance_id": "1",
    "version": "1.2.7",
    "resource_full_name": "Z-Wave adapter",
    "description": "Connects Z-Wave devices.",
    "author": "dev@futurehome.no",
    "doc_url": "",
    "adapter_info": {
      "technology": "zw",
      "network_management_type": "inclusion_exclusion",
      "fw_version": "v0.2.52",
      "hw_dependency": null,
      "services": [
        {
          "name": "zwave-ad",
          "address": "rt:ad/rn:zw/ad:1",
          "enabled": true,
          "interfaces": [
            {
              "intf_t": "in",
              "msg_t": "cmd.network.get_all_nodes",
              "val_t": "null",
              "ver": "1"
            }
          ]
        }
      ]
    },
    "is_instance_configurable": false,
    "config_required": false
  },
  "tags": null,
  "props": null,
  "ver": "1",
  "src": "-",
  "ctime": "2019-05-27T17:01:17.15+05:00",
  "uid": "b30cebdb-5f68-4fc1-8767-8a9367cb5fb9"
}
```

* Example of a discovery report for an application:

```json
{
  "type": "evt.discovery.report",
  "serv": "system",
  "val_t": "object",
  "val": {
    "package_name": "vinculum",
    "resource_name": "vinculum",
    "resource_type": "app",
    "instance_id": "1",
    "version": "3.0.36",
    "resource_full_name": "Vinculum",
    "description": "Device database and abstraction layer.",
    "author": "dev@futurehome.no",
    "doc_url": "",
    "app_info": {
      "services": [
        {
          "name": "vinculum",
          "address": "rt:app/rn:vinculum/ad:1",
          "enabled": true,
          "interfaces": [
            {
              "intf_t": "out",
              "msg_t": "evt.pd7.notify",
              "val_t": "object",
              "ver": "1"
            }
          ]
        }
      ]
    },
    "is_instance_configurable": false,
    "config_required": false
  },
  "tags": null,
  "props": null,
  "ver": "1",
  "src": "-",
  "ctime": "2019-05-27T17:01:17.15+05:00",
  "uid": "b30cebdb-5f68-4fc1-8767-8a9367cb5fb9"
}
```
