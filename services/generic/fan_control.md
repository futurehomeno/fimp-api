### Fan control service

The service has to be used to control a fan operational modes, speed and receive state updates.

#### Service names

`fan_ctrl`

#### Interfaces

Type | Interface              | Value type |  Description
-----|------------------------|------------|-------------------
in   | cmd.lvl.get_report     | null       | The command is a request for current fan speed level.
in   | cmd.lvl.set            | int        | Fan speed, value 0 - 100 %
out  | evt.lvl.report         | null       | Current fan speed level.
-|||
in   | cmd.mode.get_report    | null       | The command is a request for current fan mode report.
in   | cmd.mode.set           | string     | Fan mode. Supported values: auto_low, auto_high, auto_mid, low, high, mid,  humid_circulation, up_down,  left_right, quiet
out  | evt.mode.report        | string     | Current fan mode
-|||
in   | cmd.modelvl.get_report | string     | The command is a request for fan speed level for particular mode. If mode is set to "", the device should report levels for all modes.
in   | cmd.modelvl.set        | int_map    | val = {"mid":90, "auto_low":10}
out  | evt.modelvl.report     | int_map    | val = {"mid":90, "auto_low":10}
-|||
in   | cmd.state.get_report   | null       | The command is a request for current fan state report
out  | evt.state.report       | string     | Report operational state. Supported values: idle, low, high, mid

#### Service props

Name         | Value example      | Description
-------------|--------------------|-------------
`sup_modes`  | auto_low, auto_mid | List of supported modes
`sup_states` | idle, low, high    |