# Virtual Meter Service

This service enables a device to report an accumulated consumption and/or pulses in case it does not have its own metering capabilities, e.g. relay with output binary switch
service or thermostat. For example a virtual electricity meter works by accumulating momentary power measured in Watts into lifetime energy consumption
measured in kWh. If a virtual meter service is present, upon manual configuration providing a consumption per supported unit, a proper meter service will be added to the device.
The service then will calculate cumulated consumption at every state change, mode change and at least once during a configured interval.

## Service names

| Service name         | Pulse Unit | Description                |
|----------------------|------------|----------------------------|
| `virtual_meter_elec` | W          | Virtual electricity meter. |

## Interfaces

| Type | Interface                  | Value type | Properties | Description                                                                                                                                                                                                                                    |
|------|----------------------------|------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.config.set_interval    | int        |            | Sets minimal reporting interval in minutes for accumulated consumption and pulses. Overwrites a default value of 30 minutes.                                                                                                                   |
| in   | cmd.config.get_interval    | null       |            | Requests reporting interval in minutes for accumulated consumption and pulses.                                                                                                                                                                 |
| out  | evt.config.interval_report | int        |            | Reports reporting interval in minutes for accumulated consumption and pulses.                                                                                                                                                                  |
| -    |                            |            |            |                                                                                                                                                                                                                                                |
| in   | cmd.meter.add              | float_map  | `unit`     | Adds corresponding meter service (eg. `meter_elec`) to a selected device and the provided `unit` to report accumulated consumption. Map of floats shall provide consumption for every mode. Every `cmd.meter.add` command overwrites previous. |
| in   | cmd.meter.remove           | null       |            | Removes all added virtual meter services from a selected device. The device shall not be reporting accumulated consumption nor pulses anymore. If removal was successful sends `evt.meter.report` with empty float map.                        |
| in   | cmd.meter.get_report       | null       |            | Requests the report of the currently set values for each mode.                                                                                                                                                                                 |
| out  | evt.meter.report           | float_map  | `unit`     | Reports currently set values for each mode and the provided `unit`.                                                                                                                                                                            |

## Interface properties

| Name   | Example | Required | Description                                                                       |
|--------|---------|----------|-----------------------------------------------------------------------------------|
| `unit` | `"W"`   | Yes      | Unit of a pulse or consumption per unit of time. This is a **required** property. |

## Service props

| Name        | Type      | Example                   | Description                    |
|-------------|-----------|---------------------------|--------------------------------|
| `sup_units` | str_array | `["W"]`                   | List of supported pulse units. |
| `sup_modes` | str_array | `["off", "heat", "cool"]` | List of supported modes.       |

## Examples

* Example of a command adding a virtual meter service to a device working in one of three available modes: "off", "heat" or "fan":

```json
{
  "type": "cmd.meter.add",
  "serv": "virtual_meter_elec",
  "val_t": "float_map",
  "val": {
    "off": 10,
    "heat": 1500,
    "fan": 250
  },
  "props": {
    "unit": "W"
  },
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zigbee/ad:1/sv:virtual_meter_elec/ad:1_2"
}
```

* Example of a virtual meter service measurement reporting consumed energy value equal 123.5 kWh:

```json
{
  "type": "evt.meter.report",
  "serv": "meter_elec",
  "val_t": "float",
  "val": 123.5,
  "props": {
    "unit": "kWh",
    "direction": "import",
    "virtual": "true"
  },
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:meter_elec/ad:1_2"
}
```