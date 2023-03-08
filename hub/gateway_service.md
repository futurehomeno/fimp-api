# Gateway Service

The gateway service represents a hub as a whole and provides a way to interact with it on the highest level.
A special topic `pt:j1/mt:cmd/rt:ad/rn:gateway/ad:1` must be used to issue commands to the gateway.

## FIMP Specification

### Topics

`pt:j1/mt:cmd/rt:ad/rn:gateway/ad:1`

`pt:j1/mt:evt/rt:ad/rn:gateway/ad:1`

### Service name

`gateway`

### Interfaces

| Type | Interface                 | Value type | Description                                                                                      |
|------|---------------------------|------------|--------------------------------------------------------------------------------------------------|
| in   | cmd.gateway.identify      | null       | Identifies the hub visually, a light will turn on for 600ms then turn off for 200ms three times. |
| in   | cmd.gateway.reboot        | null       | Reboots the gateway.                                                                             |
| in   | cmd.gateway.shutdown      | null       | Powers down the gateway.                                                                         |
| in   | cmd.gateway.factory_reset | null       | Instructs the gateway to perform a factory reset.                                                |
| out  | evt.gateway.factory_reset | null       | Reports that the factory reset started.                                                          |

> All applications running on the hub are required to listen for the `evt.gateway.factory_reset` event and perform a factory reset of their own data.

### Examples

* Example of a factory reset command:

```json
{
  "serv": "gateway",
  "type": "cmd.gateway.factory_reset",
  "val_t": "null",
  "val": null,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:gateway/ad:1"
}
```