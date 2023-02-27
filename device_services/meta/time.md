### Time service

Service used to read time and date information.

#### Service names

`time`

#### Interface

Type | Interface           | Value type | Description
-----|---------------------|------------|------------
in   | cmd.time.get_report | null       | Get current time (from Z-wave node)
in   | cmd.date.get_report | null       | Get current date
out  | evt.date.report     | int_map    | Date report
out  | evt.date.report     | int_map    | Time report

### Time parameters service

The Time Parameters service is used to set date and time. Time zone offset and daylight savings may be set in the Time Parameters service if necessary. The data formats is ISO-8601 compliant.

Examples can be found in [Time.md](../../z-wave/Time.md) in the z-wave folder.

Note: In the case where the clock is updated via an external source such as SAT, internet, Rugby/Frankfurt source, omit this service.

#### Service names

`time_parameters`

#### Interface

Type | Interface                      | Value type | Description
-----|--------------------------------|------------|------------
in   | cmd.time_parameters.get_report | null       | Get current time parameters
in   | cmd.time_parameters.set        | int_map    | Sets current time parameters
out  | evt.time_parameters.report     | int_map    | Time parameters report

Examples can be found in [Time.md](../../z-wave/Time.md) in the z-wave folder.