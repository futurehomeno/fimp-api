# Numeric Sensor Services

Numeric sensor services represent a device or device functionality capable of numeric measurements.
The most popular sensors measure temperature, air humidity, or light intensity.

## Service names

| Service name         | Units                    | Description                     |
|----------------------|--------------------------|---------------------------------|
| `sensor_accelx`      | m/s2                     | Acceleration, X-axis            |
| `sensor_accely`      | m/s2                     | Acceleration, Y-axis            |
| `sensor_accelz`      | m/s2                     | Acceleration, Z-axis            |
| `sensor_airflow`     | m3/h, ft3/m              | Air flow sensor                 |
| `sensor_anglepos`    | %, degN, degS            | Angle Position sensor           |
| `sensor_atmo`        | kPa, ha, mbar            | Atmospheric pressure sensor.    |
| `sensor_baro`        | kPa, ha, mbar            | Barometric  pressure sensor.    |
| `sensor_co2`         | ppm                      | CO2-level sensor                |
| `sensor_co`          | mol/m3                   | Carbon Monoxide level sensor    |
| `sensor_current`     | A, mA                    | Current sensor                  |
| `sensor_dew`         | C, F                     | Dew point sensor                |
| `sensor_direct`      | deg                      | Direction sensor                |
| `sensor_distance`    | m, cm, ft                | Distance sensor                 |
| `sensor_elresist`    | ohm/m                    | Electrical resistivity sensor   |
| `sensor_freq`        | Hz, kHz                  | Frequency sensor                |
| `sensor_gp`          | %, NOM                   | General purpose sensor          |
| `sensor_gust`        | kph                      | Gust sensor                     |
| `sensor_humid`       | %, g/m3                  | Relative humidity sensor        |
| `sensor_lumin`       | Lux, %                   | Luminance sensor                |
| `sensor_moist`       | %, kOhm, m3/m3, aw       | Moisture sensor                 |
| `sensor_noise`       | dB                       | Noise sensor                    |
| `sensor_power`       | W, Btu/h                 | Power sensor. **Deprecated.**   |
| `sensor_rain`        | mm/h, in/h               | Rain rate sensor                |
| `sensor_rotation`    | rpm, Hz                  | Rotation sensor                 |
| `sensor_seismicint`  | EMCRO, LEIDO, MERC, SHDO | Seismic intensity sensor        |
| `sensor_seismicmag`  | MB, ML, MW, MS           | Seismic magnitude sensor        |
| `sensor_solarrad`    | w/m2                     | Solar radiation                 |
| `sensor_tank`        | l, gal, m3               | Tank capacity sensor            |
| `sensor_temp`        | C, F                     | Temperature sensor              |
| `sensor_tidelvl`     | m, ft                    | Tide level sensor               |
| `sensor_uv`          | index                    | Ultraviolet sensor              |
| `sensor_veloc`       | m/s, mph                 | Velocity sensor                 |
| `sensor_voltage`     | V, mV                    | Voltage sensor. **Deprecated.** |
| `sensor_watflow`     | l/h                      | Water flow sensor               |
| `sensor_watpressure` | kPa                      | Water pressure sensor           |
| `sensor_wattemp`     | C, F                     | Water temperature sensor        |
| `sensor_weight`      | kg, lbs                  | Weight sensor                   |
| `sensor_wind`        | kph                      | Wind sensor                     |

> Please note that `sensor_power` and `sensor_voltage` services are deprecated. 
> A [`meter_elec`](/device_services/generic/meter.md) service should be used instead for reporting electricity measurements.

## Interfaces

| Type | Interface             | Value type | Properties | Storage     | Aggregation | Description                                                               |
|------|-----------------------|------------|------------|-------------|-------------|---------------------------------------------------------------------------|
| in   | cmd.sensor.get_report | string     |            |             |             | Value is the desired unit. Use empty value to get report in default unit. |
| out  | evt.sensor.report     | float      | `unit`     | `aggregate` | `unit`      |                                                                           |

## Interface properties

| Name   | Example | Required | Description                                       |
|--------|---------|----------|---------------------------------------------------|
| `unit` | `"C"`   | Yes      | One of the units defined in `sup_units` property. |

## Service properties

| Name        | Type      | Example | Description                                                                                 |
|-------------|-----------|---------|---------------------------------------------------------------------------------------------|
| `sup_units` | str_array | ["C"]   | List of supported units. See list of [well-defined units](#service-names) for each service. |

## Examples

* Example of a temperature sensor report:

```json
{
  "serv": "sensor_temp",
  "type": "evt.sensor.report",
  "val_t": "float",
  "val": 22,
  "storage": {
    "strategy": "aggregate",
    "sub_value": "C"
  },
  "props": {
    "unit": "C"
  },
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "5c0df678-144b-4184-b024-f0cd6f6aa382",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:sensor_temp/ad:18_2"
}
```