# Technology Specific Service

This service is used to handle specific protocol capabilities that were not covered generically by any other FIMP service.

## Service name

`technology_specific`

## Interfaces

| Type | Interface               | Value type | Storage            | Description                                                                                                                    |
|------|-------------------------|------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------|
| out  | evt.notification.report | object     | `category:subject` | Reports notifications that are sent by the device. See [`notification_report`](#definitions) for details.                      |
| out  | evt.sensor.report       | object     | `type:unit`        | Reports multilevel sensor readings including unknown sensor and unknown unit. See [`sensor_report`](#definitions) for details. |
| out  | evt.meter.report        | object     | `type:unit`        | Reports meter readings with unknown meter type or/and unit. See [`meter_report`](#definitions) for details.                    |
| out  | evt.meter_export.report | object     | `type:unit`        | Reports export meter readings with unknown meter type or/and unit. See [`meter_report`](#definitions) for details.                    |
| in   | cmd.meter.reset         | null       |                    | Resets all historical readings for all meters of this device.                                                                  |

## Definitions

* `notification_report` is an object with the following structure:

| Field    | Type   | Example                  | Description                                   |
|----------|--------|--------------------------|-----------------------------------------------|
| domain   | string | `"zwave"`                | Domain for the notification.                  |
| type     | string | `"state"`                | Either `event` or `state`.                    |
| category | string | `"home_security"`        | Category of the notification.                 |
| subject  | string | `"motion_sensor_status"` | Actual subject or type of the event or state. |
| value    | string | `"motion_detected"`      | Value of the event or state.                  |

* `sensor_report` is an object with the following structure:

| Field  | Type   | Example   | Description                  |
|--------|--------|-----------|------------------------------|
| domain | string | `"zwave"` | Domain for the notification. |
| type   | string | `"7"`     | Type of the sensor.          |
| unit   | string | `"10"`    | Unit of the reported value.  |
| value  | float  | `20.5`    | Reported value.              |

* `meter_report` is an object with the following structure:

| Field     | Type   | Example    | Description                  |
|-----------|--------|------------|------------------------------|
| domain    | string | `"zwave"`  | Domain for the notification. |
| type      | string | `"11"`     | Type of the sensor.          |
| unit      | string | `"10"`     | Unit of the reported value.  |
| value     | float  | `20.5`     | Reported value.              |

## Examples

* Example of motion detection state reported by motion sensor within the home security category:

```json
{
  "serv": "technology_specific",
  "type": "evt.notification.report",
  "val_t": "object",
  "val": {
    "domain": "zwave",
    "type": "state",
    "category": "home_security",
    "subject": "motion_sensor_status",
    "value": "motion_detected"
  },
  "storage": {
       "sub_value": "home_security:motion_sensor_status"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:technology_specific/ad:17_0"
}
```

* Example of idle state reported by motion sensor within the home security category:

```json
{
  "serv": "technology_specific",
  "type": "evt.notification.report",
  "val_t": "object",
  "val": {
    "domain": "zwave",
    "type": "state",
    "category": "home_security",
    "subject": "motion_sensor_status",
    "value": "state_idle"
  },
  "storage": {
       "sub_value": "home_security:motion_sensor_status"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:technology_specific/ad:17_0"
}
```

* Example of a stateless event notification of glass breakage within the home security category:

```json
{
  "serv": "technology_specific",
  "type": "evt.notification.report",
  "val_t": "str_map",
  "val": {
    "domain": "zwave",
    "type": "event",
    "category": "home_security",
    "value": "glass_breakage"
  },
  "storage": {
       "sub_value": "home_security:glass_breakage"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:technology_specific/ad:17_0"
}
```

* Unknown notification:

```json
{
  "serv": "technology_specific",
  "type": "evt.notification.report",
  "val_t": "object",
  "val": {
    "domain": "zwave",
    "type": "state",
    "category": "31",
    "subject": "30",
    "value": "30"
  },
  "storage": {
       "sub_value": "31:30"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:technology_specific/ad:17_0"
}
```

* Sensor report with unknown sensor type and unit:

```json
{
  "serv": "technology_specific",
  "type": "evt.sensor.report",
  "val_t": "object",
  "val": {
    "domain": "zwave",
    "type": "7",
    "unit": "10",
    "value": 20
  },
  "storage": {
      "sub_value": "7:10"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:technology_specific/ad:17_0"
}
```

* Meter report with unknown meter type and unit:

```json
{
  "serv": "technology_specific",
  "type": "evt.meter.report",
  "val_t": "object",
  "val": {
    "domain": "zwave",
    "type": "11",
    "unit": "10",
    "value": 20
  },
  "storage": {
      "sub_value": "11:10"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:technology_specific/ad:17_0"
}
```

* Export meter report with unknown meter type and unit:

```json
{
  "serv": "technology_specific",
  "type": "evt.meter_export.report",
  "val_t": "object",
  "val": {
    "domain": "zwave",
    "type": "11",
    "unit": "10",
    "value": 20
  },
  "storage": {
      "sub_value": "11:10"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:technology_specific/ad:17_0"
}
```