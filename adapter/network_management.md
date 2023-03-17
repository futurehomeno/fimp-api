# Network Management

The following document describes the interaction flows and FIMP specification used in management of adapter network, specifically to get connection status or update the network.

## Behaviors and Flows

### Reporting Network Status

* At any time, upon receiving `cmd.network.get_node` command, an adapter must respond with an appropriate `evt.network.node_report` report containing status of a requested thing.
* At any time, upon receiving `cmd.network.get_all_nodes` command, an adapter must respond with `evt.network.all_nodes_report` report containing status of all things.
* On its own, an adapter must publish `evt.network.node_report` whenever the status of a thing changes.
* On its own, an adapter should publish `evt.network.all_nodes_report` at least once per day.

### Resetting Network

* Upon receiving `cmd.network.reset` command, the adapter should start resetting the network.
* For each removed thing it should emit `evt.thing.exclusion_report` as specified in [thing management](/adapter/thing_management.md#interfaces) document.
* Once the process is finished, the adapter should emit `evt.network.reset_done`.

## FIMP Specification

### Topics

Every adapter should have unique resource name and use the following topics in accordance with [topic format](/fimp/topic_format.md):

`pt:j1/mt:cmd/rt:ad/rn:{RESOURCE_NAME}/ad:1`

`pt:j1/mt:evt/rt:ad/rn:{RESOURCE_NAME}/ad:1`

### Service name

Every adapter should define its own service name.

### Interfaces

| Type | Interface                    | Value type | Description                                                                                                       |
|------|------------------------------|------------|-------------------------------------------------------------------------------------------------------------------|
| in   | cmd.network.get_node         | string     | Requests state of a thing with the provided address.                                                              |                         
| out  | evt.network.node_report      | object     | Reports state of a single thing, see [`node_report`](#definitions) object.                                        |
| in   | cmd.network.get_all_nodes    | null       | Requests state of all things.                                                                                     |                         
| out  | evt.network.all_nodes_report | object     | Reports state of all things, an array of [`node_report`](#definitions) objects.                                   |
| in   | cmd.network.update           | string     | Requests update of the network topology, see [`network_update_mode`](#definitions) definition for allowed values. | 
| in   | cmd.network.node_update      | string¹    | Requests an interview and discovery of its capabilities for the provided address of a thing.                      |
| in   | cmd.network.reset            | null       | Requests forceful removal of all things and resets the network.                                                   |
| out  | evt.network.reset_done       | null       | Reports that network reset has been completed.                                                                    |
| in   | cmd.ping.send                | string     | Requests execution of a ping for the provided address of a thing.                                                 |
| out  | evt.ping.report              | object     | Reports ping results, see [`ping_report`](#definitions) definition.                                               |

> ¹ For backwards compatibility Zigbee and Z-Wave adapters must also accept integer value.

### Definitions

* `node_report` is an object with the following structure:

| Field            | Type      | Example                  | Description                                                                                                                         |
|------------------|-----------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| address          | string    | `"4"`                    | Unique address of a thing, equal to `address` field in [inclusion_report](/adapter/thing_management.md#definitions) for this thing. |
| hash             | string    | `"zw_398_3_12"`          | Equal to `product_hash` field in [inclusion_report](/adapter/thing_management.md#definitions) for this thing.                       |
| alias            | string    | `"Fibaro Double Switch"` | Equal to `product_name` field in [inclusion_report](/adapter/thing_management.md#definitions) for this thing.                       |
| power_source     | string    | `"ac"`                   | Equal to `power_source` field in [inclusion_report](/adapter/thing_management.md#definitions) for this thing.                       |
| wakeup_interval  | string    | `"3600"`                 | Equal to `wakeup_interval` field in [inclusion_report](/adapter/thing_management.md#definitions) for this thing.                    |
| comm_tech        | string    | `"zw"`                   | Equal to `comm_tech` field in [inclusion_report](/adapter/thing_management.md#definitions) for this thing.                          |
| status           | string    | `"UP"`                   | Reachability status of a thing, either `UP` for online devices or `DOWN` for an offline device.                                     |
| operationability | str_array | `["sleep", "update"]`    | Operationability status of a thing, an array with zero, one or more non-exclusive statuses, see [`operationability`](#definitions). |
| conn_quality     | string    | `"high"`                 | Network connection quality rating, one of `low`, `medium`, `high`, or `undefined` if unknown or not applicable.                     |
| conn_type        | string    | `"direct"`               | Either `direct` or `indirect`, if communication is going through hops or third party cloud services/proxies.                        |

* `operationability` is one of the following values:

| `operationability` | Description                                                                                                                                       |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `sleep`            | Indicates that a sleeping device is currently sleeping and will process any incoming commands with a delay upon the next wakeup period.           |
| `discovery`        | Indicates that a device is being discovered by the adapter and some of its functionalities might not be yet available or visible.                 |
| `update`           | Indicates that a device is being updated with a new firmware which may lead to reduced responsiveness or temporary unavailability during reboots. |

* `network_update_mode` is one of the following values: `full`, `topology`.

* `ping_report` is an object with the following structure:

| Field   | Type   | Example                                          | Description                                                                                                                                                   |
|---------|--------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| address | string | `"4"`                                            | Unique address of a thing.                                                                                                                                    |
| status  | string | `"SUCCESS"`                                      | Either `SUCCESS` for a successful ping or `FAILED` if response was not received within configured timeout.                                                    |
| delay   | int    | `321`                                            | Number of milliseconds between sending a ping and receiving a response or acknowledgement.                                                                    |
| nodes   | object | `[{"address":"4","type":"rssi","value":"-87"}]"` | An optional array of node connection quality, where the first element represents the hub while the last one the thing. See [`routing_quality`](#definitions). |

* `routing_quality` is an object with the following structure:

| Field   | Type   | Example  | Description                                                     |
|---------|--------|----------|-----------------------------------------------------------------|
| address | string | `"4"`    | Unique address of a thing.                                      |
| type    | string | `"rssi"` | Type of connection quality measurement, either `rssi` or `lqi`. |
| value   | string | `"-87"`  | Value of connection quality.                                    |

### Examples

* Example of a command requesting status of a thing with address 31:

```json
{
  "serv": "zigbee",
  "type": "cmd.network.get_node",
  "val_t": "string",
  "val": "31",
  "props": null,
  "tags": null,
  "ver": "1",
  "ctime": "2018-11-22T23:14:40+0100",
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zigbee/ad:1"
}
```

* Example of a report containing status of a single thing:

```json
{
  "serv": "zwave-ad",
  "type": "evt.thing.node_report",
  "val_t": "object",
  "val": {
    "address": "63",
    "hash": "zw_271_1794_4096",
    "alias": "Sensor",
    "power_source": "battery",
    "wakeup_interval": "3600",
    "comm_tech": "zw",
    "status": "UP",
    "operationability": [
      "sleep"
    ],
    "conn_quality": "medium",
    "conn_type": "indirect"
  },
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2018-11-22T23:14:40+0100",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:evt/rt:ad/rn:zw/ad:1"
}
```

* Example of a command requesting status of all things:

```json
{
  "serv": "zigbee",
  "type": "cmd.network.get_all_nodes",
  "val_t": "null",
  "val": null,
  "props": null,
  "tags": null,
  "ver": "1",
  "ctime": "2018-11-22T23:14:40+0100",
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zigbee/ad:1"
}
```

* Example of a report containing status of all things:

```json
{
  "serv": "zwave-ad",
  "type": "evt.thing.node_report",
  "val_t": "object",
  "val": [
    {
      "address": "63",
      "hash": "zw_271_1794_4096",
      "alias": "Sensor",
      "power_source": "battery",
      "wakeup_interval": "3600",
      "comm_tech": "zw",
      "status": "UP",
      "operationability": [
        "sleep"
      ],
      "conn_quality": "medium",
      "conn_type": "indirect"
    },
    {
      "address": "46",
      "hash": "zw_398_3_12",
      "alias": "Sensor",
      "power_source": "ac",
      "wakeup_int": "-1",
      "comm_tech": "zw",
      "status": "DOWN",
      "operationability": [],
      "conn_quality": "high",
      "conn_type": "direct"
    }
  ],
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2018-11-22T23:14:40+0100",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:evt/rt:ad/rn:zw/ad:1"
}
```

* Example of a command requesting update of the network topology:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.network.update",
  "val_t": "string",
  "val": "topology",
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of a command requesting rediscovery of the thing with address 12:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.network.node_update",
  "val_t": "string",
  "val": "12",
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2018-11-22T23:14:40+0100",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of a command requesting reset of the entire network:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.network.reset",
  "val_t": "null",
  "val": null,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2018-11-22T23:14:40+0100",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of a report confirming reset of the entire network:

```json
{
  "serv": "zwave-ad",
  "type": "evt.network.reset_done",
  "val_t": "null",
  "val": null,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2018-11-22T23:14:40+0100",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:evt/rt:ad/rn:zw/ad:1"
}
```

* Example of a command requesting ping for thing at address 4:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.ping.send",
  "val_t": "string",
  "val": "4",
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2018-11-22T23:14:40+0100",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of a report containing ping report for thing 4 connected indirectly through single hop at address 2:

```json
{
  "serv": "zwave-ad",
  "type": "evt.ping.report",
  "val_t": "object",
  "val": {
    "address": "4",
    "status": "SUCCESS",
    "delay": 341,
    "nodes": [
      {
        "address": "2",
        "type": "rssi",
        "value": "-57"
      },
      {
        "address": "4",
        "type": "rssi",
        "value": "-87"
      }
    ]
  },
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2018-11-22T23:14:40+0100",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:evt/rt:ad/rn:zw/ad:1"
}
```