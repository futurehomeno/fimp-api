### Meter services

Meters report imported/consumed or exported/produced redings over the service.

#### Service names

Service name    | Units                                     | Description
----------------|-------------------------------------------|------------
`meter_elec`    | kWh, kVAh, W, pulse_c, V, A, power_factor | Electric meter
`meter_gas`     | cub_m, cub_f, pulse_c                     | Gas meter
`meter_water`   | cub_m, cub_f, gallon, pulse_c             | Water meter
`meter_heating` | kWh                                       | Heating meter
`meter_cooling` | kWh                                       | Cooling meter

#### Interfaces

Type | Interface                     | Value type | Properties              | Description
-----|-------------------------------|------------|-------------------------|-------------
in   | cmd.meter.get_report          | string     |                         | Value - is a unit. May not be supported by all meters.
in   | cmd.meter.get_export_report   | string     |                         | Value - is an export/production unit. May not be supported by all meters.
in   | cmd.meter.reset               | null       |                         | Resets all historical readings.
out  | evt.meter.report              | float      | unit, prv_data, delta_t | Returns import/consumption meter report.
out  | evt.meter.export_report       | float      | unit, prv_data, delta_t | Returns export/production meter report.
out  | evt.meter_ext.report          | float_map  |                         | [Extended meter report](#extended-report-object) with up to 17 data points
in   | cmd.meter_ext.get_report      | null       |                         | Request extended report

#### Interface props

Name         | Value example | Description
-------------|---------------|-------------
`delta_t`    |               | Elapsed time in seconds between the 'Meter Value' and the 'Previous Meter Value' measurements.
`prv_data`   |               | Previous meter reading.
`unit`       | "kWh"         | One of sup_units. For meter_unknown it will be a number.
`direction`  | "export"      | Defines whether reading is based on consumption (import) or production (export). Applicable for every meter except for meter_elec.
`virtual`    | "true"        | Field is present and equal "true" if the measurement was calculated by a virtual service, and "false" or not being present otherwise.

#### Important notes

For backward compatibility service "meter_elec" reports imported/consumed values using "evt.meter.report" interface and exported/produced values using "evt.meter.export_report" if applicable.

#### Interface storage

Name        | Value example | Description
------------|---------------|-------------
`sub_value` | "kWh"         | With usage of sub_value, Vinculum will know that it has to store separate meter reading for each unit.

#### Service props

Name                | Value example                                  | Description
--------------------|------------------------------------------------|-------------
`sup_units`         | ["W", "kWh", "A", "V"]                         | List of supported import/consumption units.
`sup_export_units`  | ["W", "kWh", "A", "V"]                         | List of supported export/production units.
`sup_extended_vals` | [See extended report](#extended-report-object) |

#### Extended report object

Name            | Unit    | Description
----------------|---------|--------------
`e_import`      | kWh     | Energy Import
`e_export`      | kWh     | Energy Export
`last_e_export` | kWh     | Energy Export that day
`last_e_import` | kWh     | Energy Import that day
`p_import`      | W       | Power Import
`p_import_react` | VAR    | Reactive Power Import
`p_import_apparent` | VA  | Apparent Power Import
`p_import_avg`  | W       | Power Import average
`p_import_min`  | W       | Power Import minimum that day
`p_import_max`  | W       | Power Import max that day
`p_export`      | W       | Power Export
`p_export_react` | VAR    | Reactive Power Export
`p_export_min`  | W       | Power Export minimum that day
`p_export_max`  | W       | Power Export max that day
`p_factor`      |         | Power Factor
`freq`          | Hz      | Frequency
`freq_min`      | Hz      | Frequency Min
`freq_max`      | Hz      | Frequency Max
`u1`            | V       | Voltage phase 1
`u2`            | V       | Voltage phase 2
`u3`            | V       | Voltage phase 3
`i1`            | A       | Current phase 1
`i2`            | A       | Current phase 2
`i3`            | A       | Current phase 3
`dc_p`          | W       | DC Power
`dc_p_min`      | W       | DC Power
`dc_p_max`      | W       | DC Power
`dc_u`          | V       | DC Voltage
`dc_u_min`      | V       | DC Min Voltage
`dc_u_max`      | V       | DC Max Voltage
`dc_i`          | A       | DC Current
`dc_i_min`      | A       | DC Min Current
`dc_i_max`      | A       | DC Max Current