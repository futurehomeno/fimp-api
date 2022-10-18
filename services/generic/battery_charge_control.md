### Battery charge controller service

#### Service name

`battery_charge_ctrl` - represents battery charge controller.

#### Interfaces

Type | Interface                | Value type | Properties | Description
-----|--------------------------|------------|------------|--------------
out  | evt.meter_ext.report     | float_map  |            | [Extended meter report](#extended-report-object) with up to 17 data points.
in   | cmd.meter_ext.get_report | null       |            | Request extended report.
in   | cmd.mode.get_report      | null       |            |
-|||
in   | cmd.mode.set             | string     |            | Set charge mode.
out  | evt.mode.report          | string     |            | Charge mode report.


#### Service props

Name            | Value example                                                                  | Description
----------------|--------------------------------------------------------------------------------|-------------
`sup_modes`     | idle, charging, discharging                                                    | Supported modes.
