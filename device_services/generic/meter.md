# Meter Services

Meters report readings of imported/consumed or exported/produced values of their respective type.
An electricity meter service can represent a stand-alone AMS meter, like a HAN sensor or a main electricity meter, or just a metering functionality of another device.

## Service names

| Service name    | Example units                                 | Description        |
|-----------------|-----------------------------------------------|--------------------|
| `meter_elec`    | W, kWh, V, A, kVAh, Hz, power_factor, pulse_c | Electricity meter. |
| `meter_gas`     | cub_m, cub_f, pulse_c                         | Gas meter.         |
| `meter_water`   | cub_m, cub_f, gallon, pulse_c                 | Water meter.       |
| `meter_heating` | kWh                                           | Heating meter.     |
| `meter_cooling` | kWh                                           | Cooling meter.     |

## Interfaces

| Type | Interface                   | Value type | Properties                                            | Storage | Description                                                                                                                                                                 |
|------|-----------------------------|------------|-------------------------------------------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.meter.get_report        | string     |                                                       |         | Value is an import/consumption `unit` defined in [`sup_units`](#service-properties) property. May not be supported by all meters. Empty value requests all supported units. |
| out  | evt.meter.report            | float      | `unit`, `prv_data`, `delta_t`, `direction`, `virtual` | `unit`  | Returns an import/consumption meter report for `unit` specified in properties.                                                                                              |
| in   | cmd.meter.reset             | null       |                                                       |         | Resets all historical readings.                                                                                                                                             |
| -    |                             |            |                                                       |         |                                                                                                                                                                             |
| in   | cmd.meter_export.get_report | string     |                                                       |         | Value is a export/production `unit` defined in <br/>[`sup_export_units`](#service-properties) property.                                                                     |
| out  | evt.meter_export.report     | float      | `unit`, `prv_data`, `delta_t`, `direction`            | `unit`  | Returns a export/production meter report for `unit` specified in properties.                                                                                                |
| -    |                             |            |                                                       |         |                                                                                                                                                                             |
| in   | cmd.meter_ext.get_report    | null       |                                                       |         | Requests an extended electricity report.                                                                                                                                    |
| out  | evt.meter_ext.report        | float_map  |                                                       |         | Returns an extended electricity report. See [`extended_report`](#definitions) definition for more information.                                                              |

> For backward compatibility the service reports imported/consumed values using `evt.meter.report` interface and exported/produced values using `evt.meter.export_report`.

## Interface properties

| Name        | Example    | Required | Description                                                                                                          |
|-------------|------------|----------|----------------------------------------------------------------------------------------------------------------------|
| `unit`      | `"kWh"`    | Yes      | One of the units defined in `sup_units` property. See list of [well-defined units](#service-names) for each service. |
| `delta_t`   | `"60"`     | No       | Elapsed time in seconds between the current reading and the previous one if the device supports this feature.        |
| `prv_data`  | `"123.5"`  | No       | Contains the previous meter reading for the same unit if the device supports this feature.                           |
| `direction` | `"export"` | No       | Either `import` for `evt.meter.report` or `export` for `evt.meter.export_report`.                                    |
| `virtual`   | `"true"`   | No       | Field is present and equals `true` if the measurement was calculated by a virtual service.                           |

## Service properties

| Name                | Type      | Value example                                                  | Description                                                        |
|---------------------|-----------|----------------------------------------------------------------|--------------------------------------------------------------------|
| `sup_units`         | str_array | `["W", "kWh", "A", "V"]`                                       | List of supported import/consumption units.                        |
| `sup_export_units`  | str_array | `["W", "kWh", "A", "V"]`                                       | List of supported export/production units.                         |
| `sup_extended_vals` | str_array | `["e_import", "p_import", "u1", "u2", "u3", "i1", "i2", "i3"]` | List of values contained in the [`extended_report`](#definitions). |
| `is_virtual`        | bool      | `true`                                                         | Field is present and equals `true` if the service is virtual.      |

## Definitions

* `extended_report` is a float map with the following structure:

| Key                 | Unit | Description                   |
|---------------------|------|-------------------------------|
| `e_import`          | kWh  | Energy import                 |
| `e_export`          | kWh  | Energy export                 |
| `last_e_export`     | kWh  | Energy export that day        |
| `last_e_import`     | kWh  | Energy import that day        |
| `p_import`          | W    | Power import                  |
| `p_import_react`    | VAR  | Reactive power import         |
| `p_import_apparent` | VA   | Apparent power import         |
| `p_import_avg`      | W    | Average power import          |
| `p_import_min`      | W    | Minimum power import that day |
| `p_import_max`      | W    | Maximum power import that day |
| `p_export`          | W    | Power export                  |
| `p_export_react`    | VAR  | Reactive power export         |
| `p_export_min`      | W    | Minimum power export that day |
| `p_export_max`      | W    | Maximum power export that day |
| `p_factor`          |      | Power factor                  |
| `freq`              | Hz   | Frequency                     |
| `freq_min`          | Hz   | Minimum frequency             |
| `freq_max`          | Hz   | Maximum frequency             |
| `u1`                | V    | Voltage phase 1               |
| `u2`                | V    | Voltage phase 2               |
| `u3`                | V    | Voltage phase 3               |
| `i1`                | A    | Current phase 1               |
| `i2`                | A    | Current phase 2               |
| `i3`                | A    | Current phase 3               |
| `dc_p`              | W    | DC power                      |
| `dc_p_min`          | W    | Minimum DC power              |
| `dc_p_max`          | W    | Maximum DC power              |
| `dc_u`              | V    | DC voltage                    |
| `dc_u_min`          | V    | Minimum DC voltage            |
| `dc_u_max`          | V    | Maximum DC voltage            |
| `dc_i`              | A    | DC current                    |
| `dc_i_min`          | A    | Minimum DC current            |
| `dc_i_max`          | A    | Maximum DC current            |

> Every time it is being sent, the extended report must contain all supported extended values, as all previously stored data will be overwritten. If it is not possible to
> send all supported values at the same time, an arbitrary set of available values must be selected and reported consistently.

## Examples

* Example of an energy import report:

```json
{
  "serv": "meter_elec",
  "type": "evt.meter.report",
  "val_t": "float",
  "val": 255.488998413086,
  "storage": {
    "sub_value": "kWh"
  },
  "props": {
    "delta_t": "120",
    "prv_data": "255.488998",
    "direction": "import",
    "unit": "kWh"
  },
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:meter_elec/ad:7_0"
}
```

* Example of a power export report:

```json
{
  "serv": "meter_elec",
  "type": "evt.meter_export.report",
  "val_t": "float",
  "val": 0,
  "storage": {
    "sub_value": "W"
  },
  "props": {
    "delta_t": "120",
    "prv_data": "0",
    "direction": "export",
    "unit": "W"
  },
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:meter_elec/ad:7_0"
}
```

* Example of an extended report:

```json
{
  "serv": "meter_elec",
  "type": "evt.meter_ext.report",
  "val_t": "float_map",
  "val": {
    "e_export": 0,
    "e_import": 60467.02,
    "i1": 5.32,
    "i2": 0,
    "i3": 0,
    "p_export": 0,
    "p_import": 1215.17,
    "u1": 234.75,
    "u2": 234.75,
    "u3": 234.75
  },
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:meter_elec/ad:1_2"
}
```