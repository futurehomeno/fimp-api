### Technology specific service

This service is used to handle specific protocol capabilities that were not covered generically by any other FIMP service.

#### Service name

`technology_specific`

#### Interfaces

Type | Interface               | Value type | Description
-----|-------------------------|------------|--------------
out  | evt.notification.report | object     | Notification reports that are sent by devices.
out  | evt.sensor.report       | object     | Multilevel sensor reports with unknown sensor type or/and unknown unit.
out  | evt.meter.report        | object     | Meter reports with unknown meter type or/and unit.
in   | cmd.meter.reset         | null       | Resets all historical readings for all meters of this device.

#### Interface storage

Name        | Value example                 | Description
------------|-------------------------------|-------------
`sub_value` | "home_security:sensor_status" | With usage of sub_value, Vinculum will know that it has to store separate value for every pair of choosen properties for given notification.


#### Examples

Motion Detection occurs for state Motion Sensor Status:

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
  }
}
```

Motion Sensor Status state has been changed to State Idle:

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
  }
}
```

Stateles (event) notification occurs:

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
  }
}
```

Unknown notification occurs:

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
  }
}
```

Sensor report with unknown sensor type and unit:

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
  }
}
```

Meter report with unknown meter type and unit:

```json
{
  "serv": "technology_specific",
  "type": "evt.meter.report",
  "val_t": "object",
  "val": {
    "domain": "zwave",
    "type": "11",
    "unit": "10",
    "rate_type": "import",
    "value": 20
  },
  "storage": {
      "sub_value": "11:10:import"
  }
}
```