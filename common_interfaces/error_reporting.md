# Error Reporting

The following document describes a recommended common interface for error reporting.

## Topics

It is recommended that errors are reported on the topic most representative for the error source and context. 
For example, a technology adapter should report errors:
* concerning a particular device on the device event topic, e.g. `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:dev_sys/ad:95_0`,
* concerning the adapter itself on the adapter event topic, e.g. `pt:j1/mt:evt/rt:ad/rn:zw/ad:1`.

## Service name

Interface for error reporting does not have its own dedicated service and always belongs to a particular service where the error occurred.

## Interfaces

| Type | Interface        | Value type | Properties                                           | Description                                                                                                      |
|------|------------------|------------|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| out  | evt.error.report | string     | `msg`, `src`, `cmd_topic`, `cmd_service`, `cmd_type` | Reports an error, the value contains either an error code or free-form descriptive human-readable error message. |                         

> Please note that there are no conventions or standardization of error codes, but it may be introduced in the future. 
> All currently used errors codes are to be considered private and may be changed without a notice.

## Interface properties

| Name          | Example                                   | Required | Description                                                                                             |
|---------------|-------------------------------------------|----------|---------------------------------------------------------------------------------------------------------|
| `msg`         | `"Node at the address 60 was not found."` | No       | A free-form descriptive human-readable error message.                                                   |
| `src`         | `"60"`                                    | No       | An arbitrary string defining a source, an origin or a general context for the error.                    |
| `cmd_topic`   | `"pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"`         | No       | If error occurred during executing a received command it specifies its original topic.                  |
| `cmd_service` | `"zwave-ad"`                              | No       | If error occurred during executing a received command it specifies its original service.                |
| `cmd_type`    | `"cmd.network.get_node"`                  | No       | If error occurred during executing a received command it specifies its original type or interface name. |

## Examples

* Example of structured error message on an adapter level:

```json
{
  "serv": "zwave-ad",
  "type": "evt.error.report",
  "val_t": "string",
  "val": "ERR_NODE_NOT_FOUND",
  "props": {
    "msg": "Node at the address 60 was not found.",
    "src": "60",
    "cmd_topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1",
    "cmd_service": "zwave-ad",
    "cmd_type": "cmd.network.get_node"
  },
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2018-11-22T23:14:40+0100",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:evt/rt:ad/rn:zw/ad:1"
}
```

* Example of a free-form error message on an application level:

```json
{
  "serv": "energy_guard",
  "type": "evt.error.report",
  "val_t": "string",
  "val": "Failed to retrieve a current energy price schedule.",
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2022-11-22T23:14:40+0100",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:evt/rt:app/rn:energy_guard/ad:1"
}
```