# Battery Service

Battery service represents a power unit within the device, usually found in battery-powered sensors, detectors, controllers, or similar devices.

## Service names

`battery`

## Interfaces

| Type | Interface          | Value type | Storage | Description                                                                                                                                                 |
|------|--------------------|------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.lvl.get_report | null       |         | Requests the battery level report.                                                                                                                          |
| out  | evt.lvl.report     | int        |         | Reports the battery level as percentage.                                                                                                                    |
| -    |                    |            |         |                                                                                                                                                             |
| out  | evt.alarm.report   | str_map    | `event` | Reports [`event`](#definitions) status. See [`event_report`](/device_services/generic/alarm.md#definitions) definition from alarm service for more details. |

## Service properties

| Name         | Type      | Example                                        | Description                                                                            |
|--------------|-----------|------------------------------------------------|----------------------------------------------------------------------------------------|
| `sup_events` | str_array | ["low_battery", "replace_soon", "replace_now"] | List of supported `event` values. See the list of [well-defined events](#definitions). |

## Definitions

* `event` represents a battery notification and is one of: `low_battery`, `replace_soon`, `replace_now`, `charging`, `charged`, `charge_soon`, `charge_now`.

## Examples

* Example of a battery level report:

```json
{
  "serv": "battery",
  "type": "evt.lvl.report",
  "val_t": "int",
  "val": 75,
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:battery/ad:12_1"
}
```

* Example of a low battery level alarm:

```json
{
  "serv": "battery",
  "type": "evt.alarm.report",
  "val_t": "str_map",
  "val": {
    "event": "low_battery",
    "status": "activ"
  },
  "storage": {
    "sub_value": "low_battery"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:battery/ad:12_1"
}
```