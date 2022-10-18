### Inverter services

An inverter device is normally composed of one or several inverter services. Detailed diagram - [Inverter and battery charge controller](static/inverter.png)

#### Service name

`inverter_grid_conn` - represents inverter connection to grid.

#### Interfaces

Type | Interface                | Value type | Properties | Description
-----|--------------------------|------------|------------|--------------
out  | evt.meter_ext.report     | float_map  |            | [Extended meter report](#extended-report-object) with up to 17 data points.
in   | cmd.meter_ext.get_report | null       |            | Request extended report.


#### Service name

`inverter_consumer_conn` - represents inverter connection to consumer.

#### Interfaces

Type | Interface                | Value type | Properties | Description
-----|--------------------------|------------|------------|--------------
out  | evt.meter_ext.report     | float_map  |            | [Extended meter report](#extended-report-object) with up to 17 data points.
in   | cmd.meter_ext.get_report | null       |            | Request extended report.


#### Service name

`inverter_solar_conn` - represents inverter connection to solar panel.

#### Interfaces

Type | Interface                | Value type | Properties | Description
-----|--------------------------|------------|------------|--------------
out  | evt.meter_ext.report     | float_map  |            | [Extended meter report](#extended-report-object) with up to 17 data points.
in   | cmd.meter_ext.get_report | null       |            | Request extended report.
