### Water heater service

#### Service names

`water_heater`

#### Interfaces

Type | Interface               | Value type | Description
-----|-------------------------|------------|------------------
in   | cmd.mode.get_report     | null       |
in   | cmd.mode.set            | string     | Set water heater mode.
out  | evt.mode.report         | string     |
-|||
in   | cmd.setpoint.get_report | string     | value is a set-point type
in   | cmd.setpoint.set        | object     | val = {"type":"normal", "temp":81.5, "unit":"C"}
out  | evt.setpoint.report     | object     | val = {"type":"normal", "temp":81.5, "unit":"C"}
-|||
in   | cmd.state.get_report    | null       |
out  | evt.state.report        | string     | Reports operational state.

#### Service props

Name            | Value example                            | Description
----------------|------------------------------------------|-------------
`sup_modes`     | off, normal, boost, eco, vacation        | Supported modes.
`sup_setpoints` | normal, boost, vacation                  | Supported set-points.
`sup_states`    | idle, heat                               | Optional, supported states.
`sup_range`     | {"min":20.0, "max":85.0}                 | Optional, supported range of temperature control.
`sup_ranges`    | {"normal":{"min":20.0, "max":85.0}, ...} | Optional, supported ranges per mode, if set `sup_range` should be omitted.
`sup_step`      | 1.0                                      | Optional, supported step for temperature control.

Modes: off, normal, boost, eco, vacation.

Set-point types: normal, boost, vacation.