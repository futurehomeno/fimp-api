# Inverter Service

An inverter device is exposed as a single FIMP service named `inverter`. The service describes the whole hybrid / string / micro inverter on one topic and publishes grouped `float_map` reports per subsystem (grid, PV string(s), load).

Field keys reuse the meter_elec convention documented under
[`meter_elec` → Electricity measurements](./meter.md#electricity-measurements):
`u` (voltage, V), `i` (current, A), `i_import` / `i_export` (directional
current, A), `p_import` / `p_export` (directional power, W), `freq`
(frequency, Hz), and the DC-side counterparts `dc_u`, `dc_i`, `dc_p`.

## Service name

| Service name | Description                                        |
|--------------|----------------------------------------------------|
| `inverter`   | Whole-inverter service covering grid, PV and load. |

## Service properties

| Name             | Type | Value example | Description                                                                                                   |
|------------------|------|---------------|---------------------------------------------------------------------------------------------------------------|
| `sup_pv_strings` | int  | `2`           | Number of PV MPPT inputs exposed. The service publishes `evt.pv_1.report` … `evt.pv_<sup_pv_strings>.report`. |

## Interfaces

| Type | Interface                  | Value type  | Description                                                        |
|------|----------------------------|-------------|--------------------------------------------------------------------|
| in   | `cmd.grid.get_report`      | `null`      | Request the grid report.                                           |
| out  | `evt.grid.report`          | `float_map` | Grid-side measurements. Fields: `u`, `freq`, `p_import`.           |
| in   | `cmd.pv_<n>.get_report`    | `null`      | Request the PV string #n report. `n` ∈ [1, `sup_pv_strings`].      |
| out  | `evt.pv_<n>.report`        | `float_map` | PV string #n DC-side measurements. Fields: `dc_u`, `dc_i`, `dc_p`. |
| in   | `cmd.load.get_report`      | `null`      | Request the load report.                                           |
| out  | `evt.load.report`          | `float_map` | Load-side (inverter output) measurements. Fields: `u`, `p_import`. |
| out  | `evt.error.report`         | `string`    | Reports processing errors.                                         |

## Example — grid report

```json
{
  "serv": "inverter",
  "type": "evt.grid.report",
  "val_t": "float_map",
  "val": {
    "u": 230.1,
    "freq": 49.9,
    "p_import": 0
  },
  "src": "ess",
  "ver": "1"
}
```

## Example — PV string #1 report

```json
{
  "serv": "inverter",
  "type": "evt.pv_1.report",
  "val_t": "float_map",
  "val": {
    "dc_u": 137.2,
    "dc_i": 1.57,
    "dc_p": 215
  },
  "src": "ess",
  "ver": "1"
}
```

## Adapter guidelines

* `sup_pv_strings` MUST be set on the service specification so clients can discover how many PV reports to subscribe to.
* Quantities not supported by the underlying hardware (e.g. PV current on some PIP inverters) SHOULD be reported as `0` rather than omitted.
