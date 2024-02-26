# Chargepoint Service

Chargepoint service is used to represent EV chargers.

## Service name

`chargepoint`

## Interfaces

| Type | Interface                       | Value type | Properties                                                          | Description                                                                                                           |
|------|---------------------------------|------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| in   | cmd.charge.start                | null       | `charging_mode`                                                     | Starts/resumes charging an EV. Charger must be in `ready_to_charge` state.                                            |
| in   | cmd.charge.stop                 | null       |                                                                     | Stops/pauses charging an EV. Charger must be in `charging` state.                                                     |
| -    |                                 |            |                                                                     |                                                                                                                       |
| in   | cmd.state.get_report            | null       |                                                                     | Gets the `state` of the chargepoint.                                                                                  |
| out  | evt.state.report                | string     | `charging_mode`                                                     | Reports the `state` of the chargepoint, see [`sup_states`](#service-properties) for list of possible states.          |
| -    |                                 |            |                                                                     |                                                                                                                       |
| in   | cmd.cable_lock.set              | bool       |                                                                     | Locks and unlocks the cable/connector.                                                                                |
| in   | cmd.cable_lock.get_report       | null       |                                                                     | Gets the status of the cable/connector lock.                                                                          |
| out  | evt.cable_lock.report           | bool       | `cable_current`, `cable_plugged`                                    | Reports `true` if the cable/connector is **locked** and `false` otherwise.                                            |
| -    |                                 |            |                                                                     |                                                                                                                       |
| in   | cmd.current_session.set_current | int        |                                                                     | Sets the offered current for the ongoing session in `A`, must be an integer between `6` and `max_current` value.      |
| in   | cmd.current_session.get_report  | null       |                                                                     | Requests energy consumed during the current session and optionally additional characteristics.                        |
| out  | evt.current_session.report      | float      | `previous_session`, `started_at`,  `finished_at`, `offered_current` | Reports energy consumed during the current session in `kWh` and optionally additional characteristics.                |
| -    |                                 |            |                                                                     |                                                                                                                       |
| in   | cmd.max_current.set             | int        |                                                                     | Sets the maximum offered current in `A`, must be an integer between `6` and `sup_max_current` service property value. |
| in   | cmd.max_current.get_report      | null       |                                                                     | Requests the maximum offered energy.                                                                                  |
| out  | evt.max_current.report          | int        |                                                                     | Reports the maximum offered current in `A`, this is effectively a static load balancing value.                        |
| -    |                                 |            |                                                                     |                                                                                                                       |
| in   | cmd.phase_mode.set              | string     |                                                                     | Sets the phase mode for EVSEs installed in 3-phase configuration. See [the list](#definitions) of possible values.    |
| in   | cmd.phase_mode.get_report       | null       |                                                                     | Requests the phase mode.                                                                                              |
| out  | evt.phase_mode.report           | string     |                                                                     | Reports the phase mode.                                                                                               |

## Interface properties

| Name               | Example                       | Required | Description                                                                                                                                 |
|--------------------|-------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `charging_mode`    | `"slow"`                      | No       | One of charging modes defined in [`sup_charging_modes`](#service-properties) property.                                                      |
| `cable_current`    | `"16"`                        | No       | Maximum current in `A` supported by the cable. Reading may be available only when cable is plugged. Might not be supported by all chargers. |
| `cable_plugged`    | `"true"`                      | No       | Detects whether the cable is plugged on the EVSE side. Might not be supported by all chargers.                                              |
| `previous_session` | `"2.5"`                       | No       | Reports energy consumed during previous session in `kWh`.                                                                                   |
| `started_at`       | `"2022-09-01T08:00:00Z02:00"` | No       | Time of current session start in RFC3339 format.                                                                                            |
| `finished_at`      | `"2022-09-01T12:00:00Z02:00"` | No       | Time of current session end in RFC3339 format. Present only if the current session has finished.                                            |
| `offered_current`  | `"8"`                         | No       | Reports offered current in `A`, this is effectively a dynamic load balancing value.                                                         |

> Please note that `offered_current` property:
> * is equal to `max_current` in a newly started charging session,
> * is equal to any integer between `6` and `max_current` if the value was modified by `cmd.current_session.set_current` command.
> * is equal to `0` if the charging session is paused, but should return to previously set value when the session is resumed.

## Service properties

| Name                 | Type      | Example                                                       | Description                                                                                  |
|----------------------|-----------|---------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| `sup_states`         | str_array | `["disconnected", "charging", "ready_to_charge", "finished"]` | List of possible states of the chargepoint. See [the list](#definitions) of possible values. |
| `sup_charging_modes` | str_array | `["slow", "normal"]`                                          | Optionally supported charging modes.                                                         |
| `sup_max_current`    | int       | `32`                                                          | Maximum current limit in `A` as set by the installer.                                        |
| `sup_phase_modes`    | str_array | `["NL1L2L3", "NL1"]`                                          | Optionally supported phase modes. See [the list](#definitions) of possible values.           |
| `grid_type`          | string    | `"TN"`                                                        | Grid type of the charger. Possible values are `IT`, `TT` and `TN`.                           |
| `phases`             | int       | `1`                                                           | Number of phases of the charger. Possible values are `1` and `3`.                            |

## Definitions

* `state` is one of the following values:

| `state`             | OCPP status              | Description                                                                        |
|---------------------|--------------------------|------------------------------------------------------------------------------------|
| `disconnected`      | Available                | EV is not connected to the EVSE.                                                   |
| `requesting`        | Preparing                | EV is connected to the EVSE but is not yet ready to charge.                        |
| `ready_to_charge`   | Preparing, SuspendedEVSE | EV is ready to charge but session has not yet been started or charging is paused.  |
| `charging`          | Charging                 | EV is charging.                                                                    |
| `switching_phases`  | SuspendedEVSE            | Charging session is active but EVSE is not ready to charge due to phase switching. |
| `suspended_by_ev`   | SuspendedEV              | Charging session is active but EV is not ready to charge at the moment.            |
| `suspended_by_evse` | SuspendedEVSE            | Charging session is active but EVSE is not ready to charge at the moment.          |
| `finished`          | Finishing                | Charging session is finishing or has been finished and awaits EV to be unplugged.  |
| `reserved`          | Reserved                 | EVSE is reserved for a future charging session.                                    |
| `unavailable`       | Unavailable              | EVSE is not available for charging because of maintenance or firmware update.      |
| `error`             | Faulted                  | EVSE is in an error state.                                                         |
| `unknown`           | -                        | EVSE state is unknown.                                                             |

> Please note that `ready_to_charge` and `charging` are states required for charging control, while others have mostly informative value.

* `phase_mode` defines allowed phase balancing modes for EVSEs installed in 3-phase configuration, see table below for more details on modes:

| Phase mode | Grid to EVSE | EVSE to EV | Allowed for grid types |
|------------|--------------|------------|------------------------|
| `NL1L2L3`  | N L1 L2 L3   | N L1 L2 L3 | `TN`                   |
| `NL1`      | N L1         | N L1       | `TN`                   |
| `NL2`      | N L2         | N L1       | `TN`                   |
| `NL3`      | N L3         | N L1       | `TN`                   |
| `L1L2L3`   | L1 L2 L3     | N L1 L2    | `IT`, `TT`             |
| `L1L2`     | L1 L2        | N L1       | `IT`, `TT`             |
| `L2L3`     | L2 L3        | N L1       | `IT`, `TT`             |
| `L3L1`     | L1 L3        | N L1       | `IT`, `TT`             |

> Based on an EVSE capabilities and its configuration a chargepoint service may support only a subset of the above modes.
> For example a EVSE connected to a `TN` grid and capable of charging from all 3 phases at once or 1st phase only,
> should list `NL1L2L3` and `NL1` as supported phase modes.

## Examples

* Example of a command to start charging an EV using a `slow` charging mode:

```json
{
  "serv": "chargepoint",
  "type": "cmd.charge.start",
  "val_t": "null",
  "val": null,
  "props": {
    "charging_mode": "slow"
  },
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:easee/ad:1/sv:chargepoint/ad:1"
}
```

* Example of a state report of a charger during charging using a `slow` charging mode:

```json
{
  "serv": "chargepoint",
  "type": "evt.state.report",
  "val_t": "string",
  "val": "charging",
  "props": {
    "charging_mode": "slow"
  },
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:easee/ad:1/sv:chargepoint/ad:1"
}
```
