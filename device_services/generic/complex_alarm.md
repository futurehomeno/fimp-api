# Complex Alarm System Service

The service represents an alarm system or sub-system with its own internal logic.
It is used primarily in certain SDCO detectors.

## Service name

`complex_alarm_system`

## Interfaces

| Type | Interface         | Value type | Description                                                                         |
|------|-------------------|------------|-------------------------------------------------------------------------------------|
| in   | cmd.alarm.silence | string     | Silence sirens without deactivating raised alarms. Value should be an empty string. |

## Examples

* Example of a command to silence the siren.

```json
{
  "type": "cmd.alarm.silence",
  "serv": "complex_alarm_system",
  "val_t": "string",
  "val": "",
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:complex_alarm_system/ad:31_0"
}
```