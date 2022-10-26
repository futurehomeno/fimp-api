# Contact Sensor Service

Contact sensor service is a binary sensor used by devices such as magnetic contact sensors usually installed in windows or doors.

## Service name

`sensor_contact`

## Interfaces

| Type | Interface           | Value type | Description                                       |
|------|---------------------|------------|---------------------------------------------------|
| in   | cmd.open.get_report | null       | Requests the contact state report.                |
| out  | evt.open.report     | bool       | Reports `true` if **open** and `false` otherwise. |


## Examples

* Example of a report when something is open:

```json
{
  "serv": "sensor_contact",
  "type": "evt.open.report",
  "val_t": "bool",
  "val": true,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:sensor_contact/ad:1_1"
}
```