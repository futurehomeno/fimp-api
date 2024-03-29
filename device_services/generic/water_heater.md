# Water Heater Service

Water heater service represents a water heater device such as a water boiler or a water tank.

## Service name

`water_heater`

## Interfaces

| Type | Interface               | Value type | Storage     | Aggregation | Description                                                                                                                                    |
|------|-------------------------|------------|-------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.mode.get_report     | null       |             |             | Requests the water heater `mode`.                                                                                                              |
| in   | cmd.mode.set            | string     |             |             | Sets the water heater `mode`. Must be one of the values declared in [`sup_modes`](#service-properties) property.                               |
| out  | evt.mode.report         | string     |             |             | Reports the water heater `mode`.                                                                                                               |
| -    |                         |            |             |             |                                                                                                                                                |
| in   | cmd.setpoint.get_report | string     |             |             | Gets the value for the provided `setpoint` in value. Must be one of the setpoints declared in [`sup_setpoints`](#service-properties) property. |
| in   | cmd.setpoint.set        | object     |             |             | Sets the value of a setpoint. See the [`setpoint_object`](#definitions) definition for reference.                                              |
| out  | evt.setpoint.report     | object     | `aggregate` | `setpoint`  | Reports the value of a setpoint. See the [`setpoint_object`](#definitions) definition for reference.                                           |
| -    |                         |            |             |             |                                                                                                                                                |
| in   | cmd.state.get_report    | null       |             |             | Requests the operational `state` of the device.                                                                                                |
| out  | evt.state.report        | string     |             |             | Reports the operational `state` of the device, one of the values declared in [`sup_states`](#service-properties) property.                     |

## Service properties

| Name            | Type      | Example                               | Description                                                                                           |
|-----------------|-----------|---------------------------------------|-------------------------------------------------------------------------------------------------------|
| `sup_modes`     | str_array | `["off", "normal", "boost", "eco"]`   | List of supported modes, see the definition of [`mode`](#definitions) for well-defined examples.      |
| `sup_setpoints` | str_array | `["normal", "boost"]`                 | List of supported setpoints for which a value can be set.                                             |
| `sup_states`    | str_array | `["idle", "heat"]`                    | List of supported states, see the definition of [`state`](#definitions) for well-defined examples.    |
| `sup_range`     | object    | `{"min":20.0, "max":85.0}`            | Supported range of the temperature control, see [`range`](#definitions) object definition.            |
| `sup_ranges`    | object    | `{"normal":{"min":20.0, "max":85.0}}` | Supported ranges of the temperature control, a map of [`range`](#definitions) objects per `setpoint`. |
| `sup_step`      | float     | `1.0`                                 | Supported step for the temperature control.                                                           |

> A device may define their own modes and setpoints outside the well-defined lists contained in the definitions section.
> However, it is recommended to use the well-defined values whenever possible.

## Definitions

* `setpoint_object` is an object with the following structure:

| Field | Type   | Example    | Description                                                                           |
|-------|--------|------------|---------------------------------------------------------------------------------------|
| type  | string | `"normal"` | One of the `mode` values declared in [`sup_setpoints`](#service-properties) property. |
| temp  | float  | `65`       | Setpoint value in the provided unit.                                                  |
| unit  | string | `"C"`      | Setpoint unit.                                                                        |

* `range` is an object with the following structure:

| Field | Type  | Example | Description             |
|-------|-------|---------|-------------------------|
| min   | float | `20.0`  | Minimum settable value. |
| max   | float | `85.0`  | Maximum settable value. | 

* `mode` is a mode of operation of the device, well-defined modes include: `off`, `normal`, `boost`, `eco`.

* `setpoint` represents a specific setpoint configuration.

* `state` is an operational state of the device, well-defined states include: `idle`, `heat`.

## Examples

* Example of a command requesting a value for `boost` setpoint:

```json
{
  "serv": "water_heater",
  "type": "cmd.setpoint.get_report",
  "val_t": "string",
  "val": "boost",
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "49b60210-5374-11ed-b6d0-33d4305f427b",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:hoiax/ad:1/sv:water_heater/ad:1"
}
```

* Example of a `boost` setpoint report:

```json
{
  "serv": "water_heater",
  "type": "evt.setpoint.report",
  "val_t": "object",
  "val": {
    "type": "boost",
    "temp": 85.0,
    "unit": "C"
  },
  "storage": {
    "strategy": "aggregate",
    "sub_value": "boost"
  },
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:hoiax/ad:1/sv:water_heater/ad:1"
}
```