# Alarm Services

Alarm services are used to represent devices or functionalities responsible for detecting an undesired state and raising an alarm.
Typical examples are SDCO (Smoke and Carbon Monoxide Detector), leak detector or burglar alarm.

## Service names

| Service name        | Event types                                                                                                                                                                                                                                                                              |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `alarm_appliance`   | program_started, program_inprogress, program_completed, replace_filter, set_temp_error, supplying_water, water_supply_err, boiling, boiling_err, washing, washing_err, rinsing, rinsing_err, draining, draining_err, spinning, spinning_err, drying, drying_err, fan_err, compressor_err |
| `alarm_burglar`     | intrusion, tamper_removed_cover, tamper_invalid_code, tamper_force_open, alarm_burglar, glass_breakage                                                                                                                                                                                   |
| `alarm_emergency`   | police, fire, medical                                                                                                                                                                                                                                                                    |
| `alarm_fire`        | smoke, smoke_test                                                                                                                                                                                                                                                                        |
| `alarm_gas`         | CO, CO2, combust_gas_detected, toxic_gas_detected, test, replace                                                                                                                                                                                                                         |
| `alarm_health`      | leaving_bed, sitting_on_bed, lying_on_bed, posture_change, sitting_on_bed_edge, alarm_health, volatile_organic_compound                                                                                                                                                                  |
| `alarm_heat`        | overheat, temp_rise, underheat, window_open                                                                                                                                                                                                                                              |
| `alarm_lock`        | manual_lock, manual_unlock, rf_lock, rf_unlock, keypad_lock, keypad_unlock, tag_lock, tag_unlock, manual_not_locked, rf_not_locked, auto_locked, jammed, door_opened, door_closed, lock_failed                                                                                           |
| `alarm_power`       | on, ac_on, ac_off, surge, voltage_drop, over_current, over_voltage, replace_soon, replace_now, charging, charged, charge_soon, charge_now                                                                                                                                                |
| `alarm_siren`       | inactive, siren_active                                                                                                                                                                                                                                                                   |
| `alarm_system`      | hw_failure, sw_failure, hw_failure_with_code, sw_failure_with_code                                                                                                                                                                                                                       |
| `alarm_time`        | wakeup, timer_ended, time_remaining                                                                                                                                                                                                                                                      |
| `alarm_water_valve` | valve_op, master_valve_op, valve_short_circuit, current_alarm, alarm_water_valve, master_valve_current_alarm                                                                                                                                                                             |
| `alarm_water`       | leak, level_drop, replace_filter                                                                                                                                                                                                                                                         |
| `alarm_weather`     | inactive, moisture                                                                                                                                                                                                                                                                       |

## Interfaces

| Type | Interface            | Value type | Storage | Description                                                                                                                                            |
|------|----------------------|------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.alarm.get_report | str_map    |         | Requests [`event`](#service-names) status. See [`event_request`](#definitions) definition for more details. May not be fully supported by all devices. |
| out  | evt.alarm.report     | str_map    | `event` | Reports [`event`](#service-names) status. See [`event_report`](#definitions) definition for more details.                                              |
| in   | cmd.alarm.clear      | string     |         | Clears [`event`](#service-names) provided in the value.                                                                                                |

## Service properties

| Name         | Type      | Example                 | Description                                                                                           |
|--------------|-----------|-------------------------|-------------------------------------------------------------------------------------------------------|
| `sup_events` | str_array | ["smoke", "smoke_test"] | List of supported `event` values. See list of [well-defined events](#service-names) for each service. |

## Definitions

* `event_request` is a string map with the following structure:

| Field  | Type   | Example                  | Description                                                                                   |
|--------|--------|--------------------------|-----------------------------------------------------------------------------------------------|
| event  | string | `"tamper_removed_cover"` | One of the supported `event` values declared in [`sup_events`](#service-properties) property. |

* `event_report` is a string map with the following structure:

| Field  | Type   | Example                  | Description                                                                                   |
|--------|--------|--------------------------|-----------------------------------------------------------------------------------------------|
| event  | string | `"tamper_removed_cover"` | One of the supported `event` values declared in [`sup_events`](#service-properties) property. |
| status | string | `"activ"`                | Either `activ` for activated or `deactiv` for deactivated alarm.                              |

## Examples

* Example of a raised burglar alarm.

```json
{
  "serv": "alarm_burglar",
  "type": "evt.alarm.report",
  "val_t": "str_map",
  "val": {
    "event": "tamper_removed_cover",
    "status": "activ"
  },
  "storage": {
    "sub_value": "tamper_removed_cover"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:alarm_burglar/ad:31_0"
}
```