# Presence Sensor Service

Presence sensor service is a binary sensor used by devices such as motion and presence sensors.

## Service name

`sensor_presence`

## Interfaces

| Type | Interface               | Value type | Description                                                       |
|------|-------------------------|------------|-------------------------------------------------------------------|
| in   | cmd.presence.get_report | null       | Requests the presence report.                                     |
| out  | evt.presence.report     | bool       | Reports `true` if presence is **detected** and `false` otherwise. |

## Examples

* Example of a report when presence is detected:

```json
{
  "serv": "sensor_presence",
  "type": "evt.presence.report",
  "val_t": "bool",
  "val": true,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:sensor_presence/ad:1_1"
}
```