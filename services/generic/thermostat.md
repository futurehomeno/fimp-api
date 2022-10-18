### Thermostat service

#### Service names

`thermostat`

#### Interfaces

Type | Interface               | Value type | Description
-----|-------------------------|------------|------------------
in   | cmd.mode.get_report     | null       |
in   | cmd.mode.set            | string     | Set thermostat mode.
out  | evt.mode.report         | string     |
-|||
in   | cmd.setpoint.get_report | string     | value is a set-point type
in   | cmd.setpoint.set        | str_map    | val = {"type":"heat", "temp":"21.5", "unit":"C"}
out  | evt.setpoint.report     | str_map    | val = {"type":"heat", "temp":"21.5", "unit":"C"}
-|||
in   | cmd.state.get_report    | null       |
out  | evt.state.report        | string     | Reports operational state.

#### Service props

Name            | Value example                                                                  | Description
----------------|--------------------------------------------------------------------------------|-------------
`sup_modes`     | off, heat, cool                                                                | Supported modes.
`sup_setpoints` | heat, cool                                                                     | Supported set-points.
`sup_states`    | idle, heat, cool, idle, heat, cool, fan_only, pending_heat, pending_cool, vent |

Modes: off, heat, cool, auto, aux_heat, resume, fan, furnace, dry_air, moist_air, auto_changeover, energy_heat, energy_cool, away.

Set-point types: heat, cool, furnace, dry_air, moist_air, auto_changeover, energy_heat, energy_cool, special_heat.

#### Interface storage

Name        | Value example | Description
------------|---------------|-------------
`sub_value` | "heat"        | With usage of sub_value, Vinculum will know that it has to store separate temperature for every mode of given thermostat temperature.

#### Examples
```json
{
    "val_t": "str_map",
    "val": {"type": "heat", "temp": 22.0,"unit": "C" },
    "storage": {
       "sub_value": "heat"
    }
}
{
    "val_t": "str_map",
    "val": {"type": "cool", "temp": 20.0,"unit": "C" },
    "storage": {
       "sub_value": "cool"
    }
}
```