# Siren Control Service

Siren control service allows you to control the siren on the device.

## Service name

`siren_ctrl`

## Interfaces

| Type | Interface           | Value type | Description                                                                                                          |
|------|---------------------|------------|----------------------------------------------------------------------------------------------------------------------|
| in   | cmd.mode.get_report | null       | Request the current mode of the device.                                                                              |
| in   | cmd.mode.set        | string     | Controls siren using the selected tone, must be one of modes defined in [`sup_modes`](#service-properties) property. |
| out  | evt.mode.report     | string     | Reports the current mode of the device.                                                                              |

## Service properties

| Name        | Type      | Example         | Description                                                                       |
|-------------|-----------|-----------------|-----------------------------------------------------------------------------------|
| `sup_modes` | str_array | `["on", "off"]` | List of supported tone modes. Well-defined values are: `on`, `off`, `fire`, `CO`. |

## Example

* Example of a mode report event:

```json
    {
  "serv": "siren_ctrl",
  "type": "evt.mode.report",
  "val_t": "string",
  "val": "fire",
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:siren_ctrl/ad:15_0"
}
```