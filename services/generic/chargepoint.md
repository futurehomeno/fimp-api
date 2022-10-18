### Chargepoint service

Used for EV chargers.

#### Service names

`chargepoint`

#### Interfaces

Type | Interface                    | Value type | Properties      | Description
-----|------------------------------|----------|-----------------|------------
in   | cmd.charge.start             | null     | `charging_mode` | Start charging (allow cars to charge) OCPP: Remote Start Transaction.
in   | cmd.charge.stop              | null     |                 | Stop charging (stop cars from charging) OCPP: Remote Stop Transaction.
-|||
in   | cmd.state.get_report         | null     |                 | Get the state of the chargepoint, see sup_states.
out  | evt.state.report             | string   |                 | State report of the chargepoint.
-|||
in   | cmd.cable_lock.set           | bool     |                 | Lock & unlock the cable/connector.
in   | cmd.cable_lock.get_report    | null     |                 | Get the status of the cable_lock.
out  | evt.cable_lock.report        | bool     |                 | Cable lock report of the chargepoint (true = locked, false = unlocked).
-|||
in   | cmd.current_session.get_report | null     |                 | Command for getting energy (kWh) for the current session.
out  | evt.current_session.report   | float    |                 |
-|||
out  | evt.error.report             | string   |                 |

#### Service props

Name                  | Value example                                                                                               | Description
----------------------|-------------------------------------------------------------------------------------------------------------|-------------
`sup_states`          | ["disconnected", “requesting”, “charging”, “ready_to_charge”, "finished", "reserved", "unavailable", "error", "unknown"] | State of the `chargepoint`.
`sup_charging_modes`  | ["slow", “normal”]                                                                                          | Optional, supported charging modes. Required, if the device supports energy management.

#### Interface props

Name                  | Value example                                                                                               | Description
----------------------|-------------------------------------------------------------------------------------------------------------|-------------
`charging_mode`       | "slow"                                                                                                      | Optional, current charging mode.