# Energy Storage Service

An energy-storage service represents the battery bank of a hybrid inverter or a standalone home battery. State of charge is exposed through the dedicated `cmd.soc` / `evt.soc` pair; all other electrical measurements travel through the `meter_elec` extended-report interface so clients that already consume meter data need no extra schema.

Field keys follow the [`meter_elec`](./meter.md#electricity-measurements) convention viewed from the storage unit's perspective: `i_import` / `p_import` while charging, `i_export` / `p_export` while discharging.

## Service name

| Service name     | Description                                      |
|------------------|--------------------------------------------------|
| `energy_storage` | Battery bank.                                    |

## Interfaces

| Type | Interface                    | Value type   | Description                                                                       |
|------|------------------------------|--------------|-----------------------------------------------------------------------------------|
| in   | `cmd.soc.get_report`         | `null`       | Request the state-of-charge report.                                               |
| out  | `evt.soc.report`             | `int`        | State of charge in percent (0..100).                                              |
| in   | `cmd.meter_ext.get_report`   | `str_array`  | Request selected extended values. Empty or null value requests all supported.     |
| out  | `evt.meter_ext.report`       | `str_array`  | Current measurements.                                                             |
| out  | `evt.storage.report`         | `float_map`  | Electrical snapshot. Fields: `u`, `i_import`, `i_export`, `p_import`, `p_export`. |
| out  | `evt.error.report`           | `string`     | Reports processing errors.                                                        |
| in	 | `cmd.storage.set_type`       | `string`     | Set battery chemistry. Allowed: LiFePo4, AGM. Affetcs SoC calculation.
| in	 | `cmd.storage.get_type`       | `null`       | Request current battery type.
| out	 | `evt.storage.type_report`    | `string` 	   | Current battery type.

## Service properties

| Name                    | Type        | Value example                                           | Description                                                            |
|-------------------------|-------------|---------------------------------------------------------|------------------------------------------------------------------------|
| `sup_extended_vals`     | `str_array` | `["u","i_import","i_export","p_import","p_export"]`     | List of supported `evt.storage.report` keys.                           |
| `nominal_voltage`       | `float`     | `48`                                                    | Rated battery-bank voltage, V. Omitted if not known.                   |
| `max_charge_current`    | `float`     | `60`                                                    | Maximum allowed charging current, A. Omitted if not known.             |
| `max_discharge_current` | `float`     | `60`                                                    | Maximum allowed discharging current, A. Omitted if not known.          |
| `capacity_kwh`          | `float`     | `10.24`                                                 | Usable bank capacity, kWh. Omitted if not known.                       |

Adapters MUST NOT set a rating property to 0 — omit it instead, so that clients can distinguish "unknown" from "zero".



## Example — `evt.storage.report`

```json
{
  "serv": "energy_storage",
  "type": "evt.storage.report",
  "val_t": "float_map",
  "val": {
    "u": 26.5,
    "i_import": 0,
    "i_export": 10,
    "p_import": 0,
    "p_export": 265
  },
  "src": "ess",
  "ver": "1"
}
```

## Example — `evt.soc.report`

```json
{
  "serv": "energy_storage",
  "type": "evt.soc.report",
  "val_t": "int",
  "val": 100,
  "src": "ess",
  "ver": "1"
}
```
