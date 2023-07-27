# Thermostat Service

Thermostat service is used to control the temperature in a room or a building and represents devices like thermostats, heaters or air conditioning.

## Service name

`thermostat`

## Interfaces

| Type | Interface               | Value type | Storage     | Aggregation | Description                                                                                                                                          |
|------|-------------------------|------------|-------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.mode.get_report     | null       |             |             | Requests the thermostat `mode`.                                                                                                                      |
| in   | cmd.mode.set            | string     |             |             | Sets the thermostat `mode`. Must be one of the values declared in [`sup_modes`](#service-properties) property.                                       |
| out  | evt.mode.report         | string     |             |             | Reports the thermostat `mode`.                                                                                                                       |
| -    |                         |            |             |             |                                                                                                                                                      |
| in   | cmd.setpoint.get_report | string     |             |             | Gets the value for the provided `setpoint` in value. Must be one of the setpoints declared in [`sup_setpoints`](#service-properties) property.       |
| in   | cmd.setpoint.set        | str_map    |             |             | Sets the value of a setpoint. See the [`setpoint_map`](#definitions) definition for reference.                                                       |
| out  | evt.setpoint.report     | str_map    | `aggregate` | `setpoint`  | Reports the value of a setpoint. See the [`setpoint_map`](#definitions) definition for reference.                                                    |
| -    |                         |            |             |             |                                                                                                                                                      |
| in   | cmd.state.get_report    | null       |             |             | Requests the operational `state` of the device.                                                                                                      |
| out  | evt.state.report        | string     |             |             | Reports the operational `state` of the device, one of the values declared in [`sup_states`](#service-properties) property.                           |
| -    |                         |            |             |             |                                                                                                                                                      |
| in   | cmd.sensing.set         | string     |             |             | Sets the `sensing` type of the device, one of the valuesdeclared in `sup_sensing`.                                                                   |
| in   | cmd.sensing.get_report  | null       |             |             | Requests the `sensing` type of the device.                                                                                                           |
| out  | evt.sensing.report      | string     |             |             | Reports the `sensing` type of the device, one of the values declared in [`sup_sensing`](#service-properties) property.                               |
| -    |                         |            |             |             |                                                                                                                                                      |
| in   | cmd.window.get_report   | null       |             |             | Requests the state of the window.                                                                                                                    |
| out  | evt.window.report       | bool       |             |             | Reports the state of the window. `true` if it is open and `false' if it is closed.                                                                  |

## Service properties

| Name               | Type      | Example                            | Description                                                                                                                                                        |
|--------------------|-----------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `sup_modes`        | str_array | `["off", "heat", "cool", "auto"]`                | List of supported modes, see the definition of [`mode`](#definitions) for well-defined examples.                                                                   |
| `sup_setpoints`    | str_array | `["heat", "cool"]`                               | List of supported setpoints for which a value can be set. Usually a sub-set of `sup_modes`. See the definition of [`setpoint`](#definitions) for more information. |
| `sup_temperatures` | object    | `{"heat": {"min": 10, "max": 30}}`               | List of supported temperature ranges of each setpoint, see [`range`](#definitions) object definition.                                                              |
| `sup_states`       | str_array | `["idle", "heat", "cool"]`                       | List of supported states, see the definition of [`state`](#definitions) for well-defined examples.                                                                 |
| `sup_sensing`      | str_array | `["internal", "floor", "both", "floor_limit"]`   | List of supported sensing types.                                                                                                                                   |

> A device may define their own modes and setpoints outside the well-defined lists contained in the definitions section.
> However, it is recommended to use the well-defined values whenever possible.

## Definitions

* `setpoint_map` is a string map with the following structure:

| Field | Type   | Example  | Description                                                                           |
|-------|--------|----------|---------------------------------------------------------------------------------------|
| type  | string | `"heat"` | One of the `setpoints` values declared in [`sup_setpoints`](#service-properties) property. |
| temp  | string | `"21.5"` | Setpoint value in the provided unit.                                                  |
| unit  | string | `"C"`    | Setpoint unit.                                                                        |

* `mode` is a mode of operation of the device, well-defined modes include: `off`, `heat`, `cool`, `aux_heat`, `energy_heat`, `energy_cool`, `fan`, `fan_only`, `auto`,
  `auto_changeover`, `dry`, `dry_air`, `moist_air`, `resume`, `furnace`, `manufacturer_specific`.

* `setpoint` represents a specific setpoint configuration used by the device in a specific mode of operation; a mode may use **none, one or more** setpoints, e.g.:
  mode `auto` utilizes both `heat` and `cool` setpoints to keep the temperature between set values.

* `range` is an object with the following structure:

| Field | Type  | Example | Description             |
|-------|-------|---------|-------------------------|
| min   | float | `10.0`  | Minimum settable value. |
| max   | float | `30.0`  | Maximum settable value. | 

* `state` is an operational state of the device, well-defined states include: `idle`, `heat`, `cool`, `fan`.

## Examples

* Example of a command requesting a value for `heat` setpoint:

```json
{
  "serv": "thermostat",
  "type": "cmd.setpoint.get_report",
  "val_t": "string",
  "val": "heat",
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "49b60210-5374-11ed-b6d0-33d4305f427b",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zigbee/ad:1/sv:thermostat/ad:2_1"
}
```

* Example of a `heat` setpoint report:

```json
{
  "serv": "thermostat",
  "type": "evt.setpoint.report",
  "val_t": "str_map",
  "val": {
    "type": "heat",
    "temp": "21.5",
    "unit": "C"
  },
  "storage": {
    "strategy": "aggregate",
    "sub_value": "heat"
  },
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:thermostat/ad:2_1"
}
```

* Example of a cmd setting `sensing` type:
  
```json
{
  "serv": "thermostat",
  "type": "cmd.sensing.set",
  "val_t": "string",
  "val": "floor",
  "storage": {
    "strategy": "aggregate",
    "sub_value": "heat"
  },
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:thermostat/ad:2_1"
}
```
