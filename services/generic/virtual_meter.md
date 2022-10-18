### Virtual meter service

This service enables a device to report accumulated consumption and/or pulses in case it does not have its own metering capabilities (eg. a relay with output binary switch service or thermostat accumulating momentary power measured in Watts into energy consumption measured in kWh). If a virtual meter service is present in a device, upon manual configuration providing a consumption per supported unit, a proper meter service will be added to the device. The service then will calculate cumulated consumption at every state change, mode change and at least once during a configured interval.

#### Service names

`virtual_meter_elec`

#### Interfaces

Type | Interface               | Value type | Props  | Description
-----|-------------------------|------------|--------|-------------
in   | cmd.config.set_interval | int        |        | Sets minimal reporting interval in minutes for accumulated consumption and pulses. Overwrites a default value of 30 minutes.
in   | cmd.config.get_interval | null       |        | Requests reporting interval in minutes for accumulated consumption and pulses.
out  | evt.config.interval_report  | int    |        | Reports reporting interval in minutes for accumulated consumption and pulses.
in   | cmd.meter.add           | float_map  | `unit` | Adds corresponding meter service (eg. meter_elec) to a selected device and the provided `unit` to report accumulated consumption. Map of floats shall provide consumption for every mode. Every `cmd.meter.add` command overwrites previous.
in   | cmd.meter.remove        | null       |        | Removes all added virtual meter services from a selected device. The device shall not be reporting accumulated consumption nor pulses anymore. If removal was successful `evt.meter.report` with empty float_map.
in   | cmd.meter.get_report    | null       |        | Requests the report of the currently set values for each mode.
out  | evt.meter.report        | float_map  | `unit` | Reports currently set values for each mode and the provided `unit`.

#### Interface props

Name         | Value example | Description
-------------|---------------|-------------
`unit`       | "W", "m3/h"   | Pulse's unit - consumption per unit of time. This is a **required** property.

#### Service props

Name                | Value example                                                   | Description
--------------------|-----------------------------------------------------------------|-------------
`sup_units`         | ["W"]                                                           | List of supported units.
`sup_modes`         | ["on", "off"] for relay, ["off", "heat", "cool"] for thermostat | List of supported modes.

#### Examples

Adding virtual meter service on a device working in a one of three available modes "off", "heat" or "fan":

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
   }
}
```

Virtual meter service measurement reporting consumed energy value equal 123.5 kWh:

```json
{
   "type": "evt.meter.report",
   "serv": "meter_elec",
   "val_t": "float",
   "val": { 123.5 },
   "props": {"unit": "kWh", "virtual" : "true"}
}
```