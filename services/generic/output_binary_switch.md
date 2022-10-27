# Output Binary Switch Service

Output binary switch service acts as an on/off switch for wall-plugs, relays, simple sirens and other similar devices.

## Service name

`out_bin_switch`

## Interfaces

| Type | Interface             | Value type | Description                                                                      |
|------|-----------------------|------------|----------------------------------------------------------------------------------|
| in   | cmd.binary.get_report | null       | Requests report of the binary state.                                             |
| in   | cmd.binary.set        | bool       | Sets the binary state.                                                           |
| out  | evt.binary.report     | bool       | Reports `true` when the switch is **on** and `false` when the switch is **off**. |

## Examples

* Example of a report request command:

```json
{
  "serv": "out_bin_switch",
  "type": "cmd.binary.get_report",
  "val_t": "null",
  "val": null,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zigbee/ad:1/sv:out_bin_switch/ad:4_1"
}
```

* Example of a binary state report:

```json
{
  "serv": "out_bin_switch",
  "type": "evt.binary.report",
  "val_t": "bool",
  "val": false,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "90bfaa87-a9cf-4b8d-97a0-69faf543f6bb",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:out_bin_switch/ad:4_1"
}
```