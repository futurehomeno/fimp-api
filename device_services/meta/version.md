# Version service

Version service is exposing device hardware and software versions.

## Service name

`version`

## Interfaces

| Type | Interface              | Value type | Description                               |
|------|------------------------|------------|-------------------------------------------|
| in   | cmd.version.get_report | null       | Requests device software versions report. |
| out  | evt.version.report     | str_map    | Sends [version_report](#definitions).     |

## Definitions

* `version_report` is a string map with the following structure:

| Name          | Example | Description                                |
|---------------|---------|--------------------------------------------|
| `firmware`    | `"4.2"` | Firmware main version.                     |
| `hardware`    | `"255"` | Hardware version.                          |
| `sdk_library` | `"3"`   | Manufacturer internal SDK library version. |
| `protocol`    | `"6.4"` | Protocol version, e.g. Z-Wave.             |

## Examples

* Example of a version report:

```json
{
  "serv": "version",
  "type": "evt.version.report",
  "val_t": "str_map",
  "val": {
    "firmware": "4.2",
    "hardware": "255",
    "protocol": "6.4",
    "sdk_library": "3"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:version/ad:17_0"
}
```