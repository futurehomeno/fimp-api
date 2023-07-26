# Power Regulator Service

Power regulator service acts as a controller responsible for turning the relay on and off for a given part of the duty cycle.

## Service name

`power_regulator`

## Interfaces

| Type | Interface             | Value type | Description                     |
|------|-----------------------|------------|---------------------------------|
| in   | cmd.cycle.set         | int        | Sets the cycle value.           |                                                                               
| in   | cmd.cycle.get_report  | null       | Requests the cycle value.       |
| out  | evt.cycle.report      | int        | Reports the cycle value.        |
| -    |                       |            |                                 |
| in   | cmd.period.set        | int        | Sets the duty period value.     |                                                                               
| in   | cmd.period.get_report | null       | Requests the duty period value. |
| out  | evt.period.report     | int        | Reports the duty period value.  |

## Service properties

| Name          | Type   | Example                            | Description                                                                                |
|---------------|--------|------------------------------------|--------------------------------------------------------------------------------------------|
| `max_lvl`     | int    | `100`                              | A maximum supported level value.                                                           |
| `min_lvl`     | int    | `5`                                | A minimum supported level value.                                                           |
| `lvl_step`    | int    | `5`                                | A step of level.                                                                           |
| `sup_periods` | object | `[{"min":60,"max":1800,"step":1}]` | Supported duty period settings in form of array of [`period_range`](#definitions) objects. |

## Definitions

* `period_range` is an object with the following structure:

| Field | Type | Example | Description                                                  |
|-------|------|---------|--------------------------------------------------------------|
| min   | int  | `60`    | From what minimum value a duty period can be set in seconds. |
| max   | int  | `1800`  | To what maximum value a duty period can be set in seconds.   |
| step  | int  | `1`     | Step value for the range in seconds.                         |

> Multiple ranges can be defined in the `sup_periods` property to accommodate different duty period capabilities of the device.
> An enumeration list of cycles can be defined by ranges with equal min and max values.
> Ranges can also be used to define different precision, e.g. a second precision in range up to a minute and a minute precision in range up to an hour.

## Examples

* Example of the command to set the duty cycle to 75%:

```json
{
  "serv": "power_regulator",
  "type": "cmd.cycle.set",
  "val_t": "int",
  "val": 75,
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "49b60210-5374-11ed-b6d0-33d4305f427b",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zigbee/ad:1/sv:power_regulator/ad:124_0"
}
```

* Example of the duty cycle report.

```json
{
  "serv": "power_regulator",
  "type": "evt.cycle.report",
  "val_t": "int",
  "val": 75,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:power_regulator/ad:124_0"
}
```

* Example of the command to set the duty period to 1800 seconds:

```json
{
  "serv": "power_regulator",
  "type": "cmd.period.set",
  "val_t": "int",
  "val": 1800,
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "49b60210-5374-11ed-b6d0-33d4305f427b",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zigbee/ad:1/sv:power_regulator/ad:124_0"
}
```

* Example of the duty period report.

```json
{
  "serv": "power_regulator",
  "type": "evt.period.report",
  "val_t": "int",
  "val": 1800,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:power_regulator/ad:124_0"
}
```
