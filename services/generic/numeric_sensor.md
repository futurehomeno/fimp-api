### Numeric sensor services

#### Service names

Service name         | Units                    | Description
---------------------|--------------------------|------------
`sensor_accelx`      | m/s2                     | Acceleration, X-axis
`sensor_accely`      | m/s2                     | Acceleration, Y-axis
`sensor_accelz`      | m/s2                     | Acceleration, Z-axis
`sensor_airflow`     | m3/h, ft3/m              | Air flow sensor
`sensor_anglepos`    | %, degN, degS            | Angle Position sensor
`sensor_atmo`        | kPa, ha, mbar            | Atmospheric pressure sensor. ha - inches of Mercury
`sensor_baro`        | kPa, ha, mbar            | Barometric  pressure sensor. ha - inches of Mercury
`sensor_co2`         | ppm                      | CO2-level sensor
`sensor_co`          | mol/m3                   | Carbon Monoxide level sensor
`sensor_current`     | A, mA                    | Current sensor
`sensor_dew`         | C, F                     | Dew point sensor
`sensor_direct`      | deg                      | Direction sensor
`sensor_distance`    | m, cm, ft                | Distance sensor
`sensor_elresist`    | ohm/m                    | Electrical resistivity sensor
`sensor_freq`        | Hz, kHz                  | Frequency sensor
`sensor_gp`          | %, NOM                   | General purpose sensor
`sensor_gust`        | kph                      | Gust sensor
`sensor_humid`       | %, g/m3                  | Relative humidity sensor
`sensor_lumin`       | Lux, %                   | Luminance sensor
`sensor_moist`       | %, kOhm, m3/m3, aw       | Moisture sensor
`sensor_noise`       | dB                       | Noise sensor
`sensor_power`       | W, Btu/h                 | Power sensor. Btu/h - British thermal unit per hour
`sensor_rain`        | mm/h, in/h               | Rain rate sensor
`sensor_rotation`    | rpm, Hz                  | Rotation sensor
`sensor_seismicint`  | EMCRO, LEIDO, MERC, SHDO | Seismic intensity sensor
`sensor_seismicmag`  | MB, ML, MW, MS           | Seismic magnitude sensor
`sensor_solarrad`    | w/m2                     | Solar radiation
`sensor_tank`        | l, gal, m3               | Tank capacity sensor
`sensor_temp`        | C, F                     | Temperature sensor
`sensor_tidelvl`     | m, ft                    | Tide level sensor
`sensor_uv`          | index                    | Ultraviolet sensor
`sensor_veloc`       | m/s, mph                 | Velocity sensor
`sensor_voltage`     | V, mV                    | Voltage sensor
`sensor_watflow`     | l/h                      | Water flow sensor
`sensor_watpressure` | kPa                      | Water pressure sensor
`sensor_wattemp`     | C, F                     | Water temperature sensor
`sensor_weight`      | kg, lbs                  | Weight sensor
`sensor_wind`        | kph                      | Wind sensor

#### Interfaces

Type | Interface             | Value type | Properties | Description
-----|-----------------------|------------|------------|-------------
in   | cmd.sensor.get_report | string     |            | Value is desired unit. Use empty value to get report in default unit.
out  | evt.sensor.report     | float      | unit       |

Example message: [evt.sensor.report](json-v1/messages/examples/evt.sensor.report)

#### Service props

Name        | Value example | Description
------------|---------------|-------------
`sup_units` | ["C", "F"]    | list of supported units.