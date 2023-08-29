# Chargepoint Service

Chargepoint service is used to represent EV chargers.

## Service name

`chargepoint`

## Interfaces

| Type | Interface                       | Value type | Properties                                                 | Description                                                                                                        |
|------|---------------------------------|------------|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| in   | cmd.charge.start                | null       | `charging_mode`                                            | Starts/resumes charging an EV. Charger must be in `ready_to_charge` state.                                         |
| in   | cmd.charge.stop                 | null       |                                                            | Stops/pauses charging an EV. Charger must be in `charging` state.                                                  |
| -    |                                 |            |                                                            |                                                                                                                    |
| in   | cmd.state.get_report            | null       |                                                            | Gets the `state` of the chargepoint.                                                                               |
| out  | evt.state.report                | string     | `charging_mode`                                            | Reports the `state` of the chargepoint, see [`sup_states`](#service-properties) for list of possible states.       |
| -    |                                 |            |                                                            |                                                                                                                    |
| in   | cmd.cable_lock.set              | bool       |                                                            | Locks and unlocks the cable/connector.                                                                             |
| in   | cmd.cable_lock.get_report       | null       |                                                            | Gets the status of the cable/connector lock.                                                                       |
| out  | evt.cable_lock.report           | bool       |                                                            | Reports `true` if the cable/connector is **locked** and `false` otherwise.                                         |
| -    |                                 |            |                                                            |                                                                                                                    |
| in   | cmd.current_session.set_current | int        |                                                            | Sets the offered `current` for the ongoing session in `A`, must be an integer between `6` and `max_current` value. |
| in   | cmd.current_session.get_report  | null       |                                                            | Requests energy consumed during the current session and optionally additional characteristics.                     |
| out  | evt.current_session.report      | float      | `started_at`, `previous_session`, `current`, `max_current` | Reports energy consumed during the current session in `kWh` and optionally additional characteristics.             |

## Interface properties

| Name               | Example                       | Required | Description                                                                            |
|--------------------|-------------------------------|----------|----------------------------------------------------------------------------------------|
| `charging_mode`    | `"slow"`                      | No       | One of charging modes defined in [`sup_charging_modes`](#service-properties) property. |
| `started_at`       | `"2022-09-01T08:00:00Z02:00"` | No       | Time of current session start in RFC3339 format.                                       |
| `previous_session` | `"2.5"`                       | No       | Reports energy consumed during previous session in `kWh`.                              |
| `current`          | `"8"`                         | No       | Reports offered current in `A`.                                                        |
| `max_current`      | `"16"`                        | No       | Reports maximum allowed current in `A`.                                                |

> Please note that offered `current` property:
> * is equal to `max_current` property in a newly started charging session,
> * is equal to `0` if the charging session is paused,
> * is equal to any integer between `6` and `max_current` if the value was modified by `cmd.current_session.set_current` command.
> 
> Please note that setting `max_current` property lies outside the scope of this service. 
> The property servers only as an upper boundary for the `cmd.current_session.set_current` command.


## Service properties

| Name                 | Type      | Example                                                       | Description                                                                                  |
|----------------------|-----------|---------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| `sup_states`         | str_array | `["disconnected", "charging", "ready_to_charge", "finished"]` | List of possible states of the chargepoint. See [the list](#definitions) of possible values. |
| `sup_charging_modes` | str_array | `["slow", "normal"]`                                          | Optionally supported charging modes.                                                         |

## Definitions

* `state` is one of: `disconnected`, `requesting`, `charging`, `ready_to_charge`, `suspended_by_evse`, `suspended_by_ev`, `finished`, `reserved`, `unavailable`, `error`, `unknown`.

> Please note that `ready_to_charge` and `charging` are states required for charging control, while others have only informative value.

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
