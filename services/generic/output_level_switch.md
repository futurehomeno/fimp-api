# Output Level Switch Service

Output level switch service acts as a level controller for devices such as dimmers, blinds or similar things which can be controlled with sliders.

## Service name

`out_lvl_switch`

## Interfaces

| Type | Interface          | Value type | Properties              | Description                                                                                                    |
|------|--------------------|------------|-------------------------|----------------------------------------------------------------------------------------------------------------|
| in   | cmd.binary.set     | bool       |                         | Setting `true` should result in setting the level to the last known non-zero value or fallback to the maximum. |
| out  | evt.binary.report  | bool       |                         | ***Deprecated***. The service should use `evt.lvl.report` instead.                                             |
| -    |                    |            |                         |                                                                                                                |
| in   | cmd.lvl.get_report | null       |                         | Requests the level value.                                                                                      |
| in   | cmd.lvl.set        | int        | `duration`              | Sets the level value.                                                                                          |
| in   | cmd.lvl.start      | string     | `start_lvl`, `duration` | Starts the level transition. Supported values are `up` and `down` and represent direction of the transition.   |
| in   | cmd.lvl.stop       | null       |                         | Stops a level change.                                                                                          |
| out  | evt.lvl.report     | int        |                         | Reports the level value.                                                                                       |

## Interface properties

| Name        | Example | Description                                                                                                                |
|-------------|---------|----------------------------------------------------------------------------------------------------------------------------|
| `duration`  | `"10"`  | Duration of the transition in seconds. Factory default is used if no value is provided.                                    |
| `start_lvl` | `"50"`  | Level from which to start the transition - between `min_lvl` and `max_lvl`. Current level is used if no value is provided. |

> Please note that above properties are not supported by all devices. The adapter should ignore the property if it is not supported by the device.

## Service properties

| Name      | Type   | Example    | Description                                                         |
|-----------|--------|------------|---------------------------------------------------------------------|
| `max_lvl` | int    | `99`       | A maximum supported level value.                                    |
| `min_lvl` | int    | `0`        | A minimum supported level value.                                    |
| `sw_type` | string | `"on_off"` | A type of level switch. Supported values are `on_off` or `up_down`. |

## Examples

* Example of the command to set the level to 75% within 10 second transition:

```json
{
  "serv": "out_lvl_switch",
  "type": "cmd.lvl.set",
  "val_t": "int",
  "val": 75,
  "props": {
    "duration": "10"
  },
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "49b60210-5374-11ed-b6d0-33d4305f427b",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:out_lvl_switch/ad:124_0"
}
```

* Example of the level report.

```json
{
  "serv": "out_lvl_switch",
  "type": "evt.lvl.report",
  "val_t": "int",
  "val": 75,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:out_lvl_switch/ad:124_0"
}
```

## Adapter guidelines

* After receiving `cmd.binary.set` command the adapter should respond with `evt.lvl.report` rather than `evt.binary.report`.