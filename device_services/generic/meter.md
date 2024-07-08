# Meter Services

Meters report readings of imported/consumed or exported/produced values of their respective type.
An electricity meter service can represent a stand-alone AMS meter, like a HAN sensor or a main electricity meter, or just a metering functionality of another device.

## Service names

| Service name    | Example units                                        | Description        |
|-----------------|------------------------------------------------------|--------------------|
| `meter_elec`    | W, kWh, V, A, VA, kVAh, VAr, kVArh, Hz, power_factor | Electricity meter. |
| `meter_gas`     | cub_m, cub_f, pulse_c                                | Gas meter.         |
| `meter_water`   | cub_m, cub_f, gallon, pulse_c                        | Water meter.       |
| `meter_heating` | kWh                                                  | Heating meter.     |
| `meter_cooling` | kWh                                                  | Cooling meter.     |

> For a complete list of supported electric units and extended values see [electricity measurements](#electricity-measurements) section.

## Interfaces

| Type | Interface                   | Value type | Properties                               | Storage     | Aggregation | Description                                                                                                                                                                         |
|------|-----------------------------|------------|------------------------------------------|-------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.meter.get_report        | string     |                                          |             |             | Value is an import/consumption `unit` defined in [`sup_units`](#service-properties) property. May not be supported by all meters. Empty or null value requests all supported units. |
| out  | evt.meter.report            | float      | `unit`, `prv_data`, `delta_t`, `virtual` | `aggregate` | `unit`      | Returns an import/consumption meter report for `unit` specified in properties.                                                                                                      |
| in   | cmd.meter.reset             | null       |                                          |             |             | Resets all historical readings.                                                                                                                                                     |
| -    |                             |            |                                          |             |             |                                                                                                                                                                                     |
| in   | cmd.meter_export.get_report | string     |                                          |             |             | Value is a export/production `unit` defined in [`sup_export_units`](#service-properties) property.                                                                                  |
| out  | evt.meter_export.report     | float      | `unit`, `prv_data`, `delta_t`            | `aggregate` | `unit`      | Returns a export/production meter report for `unit` specified in properties.                                                                                                        |
| -    |                             |            |                                          |             |             |                                                                                                                                                                                     |
| in   | cmd.meter_ext.get_report    | str_array  |                                          |             |             | Requests an extended electricity report for listed extended values. Empty or null value requests all supported extended values.                                                     |
| out  | evt.meter_ext.report        | float_map  |                                          | `split`     |             | Returns an extended electricity report. See [electricity measurements](#electricity-measurements) section for more information.                                                     |
| -    |                             |            |                                          |             |             |                                                                                                                                                                                     |
| out  | cmd.meter_log.start         | object     |                                          |             |             | Request thing to open a tunnel to metering device and adapter to start logging received data. see [`tunnel_request`](#definitions).                                                 |
| out  | cmd.meter_log.stop          | null       |                                          |             |             | Request thing to close the tunnel and adapter to conclude the log. Tunnel should be closed when not needed because of network load management.                                      |

> For backward compatibility the service reports imported/consumed values using `evt.meter.report` interface and exported/produced values using `evt.meter_export.report`.

## Definitions

* `tunnel request` is an object with following structure:

| Field         | Type   | Example                              | Description                                                                                            |
|---------------|--------|--------------------------------------|--------------------------------------------------------------------------------------------------------|
| `udid`        | int    | `1`                                  | Thing unique ID                                                                                        |
| `group`       | string | `1`                                  | Group unique ID [for Zigbee devices it will correspond to endpoint with tunneling cluster]             |
| `protocol`    | int    | `3`                                  | ID of protocol which will be tunneled from device to adapter see [`tunneling_protocols`](#definitions) |

* `tunneling_protocols`

| ID        | Description                    |
|-----------|--------------------------------|
| `0`       | DLMS/COSEM (IEC 62056)         |
| `1`       | IEC 61107                      |
| `2`       | ANSI C12                       |
| `3`       | M-BUS                          |
| `4`       | SML                            |
| `5`       | ClimateTalk                    |
| `6`       | GB-HRGP                        |
| `7`       | IP v4                          |
| `8`       | IP v6                          |
| `200-254` | Manufacturer defined protocols |


## Interface properties

| Name       | Example   | Required | Description                                                                                                          |
|------------|-----------|----------|----------------------------------------------------------------------------------------------------------------------|
| `unit`     | `"kWh"`   | Yes      | One of the units defined in `sup_units` property. See list of [well-defined units](#service-names) for each service. |
| `delta_t`  | `"60"`    | No       | Elapsed time in seconds between the current reading and the previous one if the device supports this feature.        |
| `prv_data` | `"123.5"` | No       | Contains the previous meter reading for the same unit if the device supports this feature.                           |
| `virtual`  | `"true"`  | No       | Field is present and equals `true` if the measurement was calculated by a virtual service.                           |

## Service properties

| Name                | Type      | Value example                                                  | Description                                                   |
|---------------------|-----------|----------------------------------------------------------------|---------------------------------------------------------------|
| `sup_units`         | str_array | `["W", "kWh", "A", "V"]`                                       | List of supported import/consumption units.                   |
| `sup_export_units`  | str_array | `["W", "kWh", "A", "V"]`                                       | List of supported export/production units.                    |
| `sup_extended_vals` | str_array | `["e_import", "p_import", "u1", "u2", "u3", "i1", "i2", "i3"]` | List of supported extended measurement values.                |
| `is_virtual`        | bool      | `true`                                                         | Field is present and equals `true` if the service is virtual. |

## Examples

* Example of an energy import report:

```json
{
  "serv": "meter_elec",
  "type": "evt.meter.report",
  "val_t": "float",
  "val": 255.488998413086,
  "storage": {
    "strategy": "aggregate",
    "sub_value": "kWh"
  },
  "props": {
    "delta_t": "120",
    "prv_data": "255.488998",
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
    "strategy": "aggregate",
    "sub_value": "W"
  },
  "props": {
    "delta_t": "120",
    "prv_data": "0",
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
  "storage": {
    "strategy": "split"
  },
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:meter_elec/ad:1_2"
}
```
* Open a tunnel to an AMS through Futurehome HAN NVE

```json
{
  "serv": "meter_elec",
  "type": "evt.meter_log.start",
  "val_t": "object",
  "val": {
    "udid": 1,
    "group": 1,
    "protocol": 3
  },
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:meter_elec/ad:1_2"
}
```

## Electricity measurements

Electricity measurements can be reported using different interfaces.
Some measurements are only available in `evt.meter_ext.report`, while others can be reported also either in `evt.meter.report` or `evt.meter_export.report`.
The following table lists all supported electricity measurements, interfaces which can be used to report them and their base units.

| Measurement                   | `evt.meter_ext.report` key | `evt.meter.report` unit | `evt.meter_export.report` unit | Unit  |
|-------------------------------|----------------------------|-------------------------|--------------------------------|-------|
| Power import total            | `p_import`                 | `W`                     |                                | W     |
| Power import phase 1          | `p1`                       |                         |                                | W     |
| Power import phase 2          | `p2`                       |                         |                                | W     |
| Power import phase 3          | `p3`                       |                         |                                | W     |
| Power export total            | `p_export`                 |                         | `W`                            | W     |
| Power export phase 1          | `p1_export`                |                         |                                | W     |
| Power export phase 2          | `p2_export`                |                         |                                | W     |
| Power export phase 3          | `p3_export`                |                         |                                | W     |
| Energy import total           | `e_import`                 | `kWh`                   |                                | kWh   |
| Energy import phase 1         | `e1_import`                |                         |                                | kWh   |
| Energy import phase 2         | `e2_import`                |                         |                                | kWh   |
| Energy import phase 3         | `e3_import`                |                         |                                | kWh   |
| Energy export total           | `e_export`                 |                         | `kWh`                          | kWh   |
| Energy export phase 1         | `e1_export`                |                         |                                | kWh   |
| Energy export phase 2         | `e2_export`                |                         |                                | kWh   |
| Energy export phase 3         | `e3_export`                |                         |                                | kWh   |
| Reactive energy import        | `e_import_react`           | `kVArh`                 |                                | kVArh |
| Apparent energy import        | `e_import_apparent`        | `kVAh`                  |                                | kVAh  |
| Reactive energy export        | `e_export_react`           |                         | `kVArh`                        | kVArh |
| Apparent energy export        | `e_export_apparent`        |                         | `kVAh`                         | kVAh  |
| Reactive power import total   | `p_import_react`           | `VAr`                   |                                | VAr   |
| Reactive power import phase 1 | `p1_import_react`          |                         |                                | VAr   |
| Reactive power import phase 2 | `p2_import_react`          |                         |                                | VAr   |
| Reactive power import phase 3 | `p3_import_react`          |                         |                                | VAr   |
| Reactive power export total   | `p_export_react`           |                         | `VAr`                          | VAr   |
| Reactive power export phase 1 | `p1_export_react`          |                         |                                | VAr   |
| Reactive power export phase 2 | `p2_export_react`          |                         |                                | VAr   |
| Reactive power export phase 3 | `p3_export_react`          |                         |                                | VAr   |
| Apparent power import total   | `p_import_apparent`        | `VA`                    |                                | VA    |
| Apparent power import phase 1 | `p1_import_apparent`       |                         |                                | VA    |
| Apparent power import phase 2 | `p2_import_apparent`       |                         |                                | VA    |
| Apparent power import phase 3 | `p3_import_apparent`       |                         |                                | VA    |
| Apparent power export total   | `p_export_apparent`        |                         | `VA`                           | VA    |
| Apparent power export phase 1 | `p1_export_apparent`       |                         |                                | VA    |
| Apparent power export phase 2 | `p2_export_apparent`       |                         |                                | VA    |
| Apparent power export phase 3 | `p3_export_apparent`       |                         |                                | VA    |
| Voltage                       | `u`                        | `V`                     |                                | V     |
| Voltage phase 1               | `u1`                       |                         |                                | V     |
| Voltage phase 2               | `u2`                       |                         |                                | V     |
| Voltage phase 3               | `u3`                       |                         |                                | V     |
| Voltage export                | `u_export`                 |                         | `V`                            | V     |
| Voltage export phase 1        | `u1_export`                |                         |                                | V     |
| Voltage export phase 2        | `u2_export`                |                         |                                | V     |
| Voltage export phase 3        | `u3_export`                |                         |                                | V     |
| Current                       | `i`                        | `A`                     |                                | A     |
| Current phase 1               | `i1`                       |                         |                                | A     |
| Current phase 2               | `i2`                       |                         |                                | A     |
| Current phase 3               | `i3`                       |                         |                                | A     |
| Current export                | `i_export`                 |                         | `A`                            | A     |
| Current export phase 1        | `i1_export`                |                         |                                | A     |
| Current export phase 2        | `i2_export`                |                         |                                | A     |
| Current export phase 3        | `i3_export`                |                         |                                | A     |
| Power factor                  | `p_factor`                 | `power_factor`          |                                |       |
| Power factor phase 1          | `p1_factor`                |                         |                                |       |
| Power factor phase 2          | `p2_factor`                |                         |                                |       |
| Power factor phase 3          | `p3_factor`                |                         |                                |       |
| Power factor export           | `p_factor_export`          |                         | `power_factor`                 |       |
| Power factor export phase 1   | `p1_factor_export`         |                         |                                |       |
| Power factor export phase 2   | `p2_factor_export`         |                         |                                |       |
| Power factor export phase 3   | `p3_factor_export`         |                         |                                |       |
| Frequency                     | `freq`                     | `Hz`                    | `Hz`                           |       |
| DC voltage                    | `dc_u`                     |                         |                                | V     |
| DC current                    | `dc_i`                     |                         |                                | A     |
| DC power                      | `dc_p`                     |                         |                                | W     |

## Adapter guidelines

Adapters implementing `meter_elec` service must follow the guidelines below:

* For maximum backwards compatibility **power import total** and **energy import total** measurements 
  *should* be reported using `evt.meter.report` interface using respectively `W` and `kWh` units.
* Adapter *may* include in `evt.meter_ext.report` report any measurement that is already reported using `evt.meter.report` or `evt.meter_export.report`, 
  including **power import total** and **energy import total**.
* If the same measurement is supported by two different interfaces, 
  each change of the measurement value *must* trigger two respective messages for both interfaces.
