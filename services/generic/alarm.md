### Alarm services

#### Service names

Service name        | Event                                   | Description
--------------------|-----------------------------------------|------------
`alarm_appliance`   | program_started, program_inprogress, program_completed, replace_filter, set_temp_error, supplying_water, water_supply_err, boiling, boiling_err, washing, washing_err, rinsing, rinsing_err, draining, draining_err, spinning, spinning_err, drying, drying_err, fan_err, compressor_err |
`alarm_burglar`     | intrusion, tamper_removed_cover, tamper_invalid_code, tamper_force_open, alarm_burglar, glass_breakage |
`alarm_emergency`   | police, fire, medical                   |
`alarm_fire`        | smoke, smoke_test                       |
`alarm_gas`         | CO, CO2, combust_gas_detected, toxic_gas_detected, test, replace |
`alarm_health`      | leaving_bed, sitting_on_bed, lying_on_bed, posture_change, sitting_on_bed_edge, alarm_health, volatile_organic_compound |
`alarm_heat`        | overheat, temp_rise, underheat          |
`alarm_lock`        | manual_lock, manual_unlock, rf_lock, rf_unlock, keypad_lock, keypad_unlock, tag_lock, tag_unlock, manual_not_locked, rf_not_locked, auto_locked, jammed, door_opened, door_closed, lock_failed | TODO: move to doorlock service
`alarm_power`       | on, ac_on, ac_off, surge, voltage_drop, over_current, over_voltage, replace_soon, replace_now, charging, charged, charge_soon, charge_now | TODO: move to power_supply service
`alarm_siren`       | inactive, siren_active                  |
`alarm_system`      | hw_failure, sw_failure, hw_failure_with_code, sw_failure_with_code |
`alarm_time`        | wakeup, timer_ended, time_remaining     |
`alarm_water_valve` | valve_op, master_valve_op, valve_short_circuit, current_alarm, alarm_water_valve, master_valve_current_alarm |
`alarm_water`       | leak, level_drop, replace_filter        |
`alarm_weather`     | inactive, moisture                      |

#### Interfaces

Type | Interface            | Value type | Description
-----|----------------------|------------|--------------------
in   | cmd.alarm.get_report | str_map    | val = {"event": "tamper_removed_cover"}
out  | evt.alarm.report     | str_map    | val = {"event": "tamper_removed_cover", "status": "activ"}
in   | cmd.alarm.clear      | string     | val = event that should be cleared – device should send a new report after.

Supported statuses: activ, deactiv. IMPORTANT: These are shorthands for "activated" and "deactivated", not typos.

Interface cmd.alarm.get_report is used in Z-wave to clear last event for given event.

Example message: [evt.sensor.report](json-v1/messages/examples/evt.alarm.report.json)

#### Service props

Name         | Value example           | Description
-------------|-------------------------|-------------
`sup_events` | ["smoke", "smoke_test"] | supported events.
