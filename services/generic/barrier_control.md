### Barrier control service

The service represent devices like garage door openers, barriers, window protection shades, etc.

#### Service names

`barrier_ctrl`

#### Interfaces

Type | Interface                | Value type | Description
-----|--------------------------|------------|------------
in   | cmd.notiftype.get_report | null       |
in   | cmd.notiftype.set        | bool_map   | Configuration of notification type device is is using while opening/closing door.
out  | evt.notiftype.report     | bool_map   |
-|||
in   | cmd.op.stop              | null       | Emergency stop of any operation.
-|||
in   | cmd.state.get_report     | null       | Get current state
out  | evt.state.report         | string     | Current state
-|||
in   | cmd.tstate.set           | string     | Setting target state

#### Interface props

Name        | Value example | Description
------------|---------------|-------------
`stopped_at`| 30            | Stopped at exact position (percentage value).

#### Service props

Name             | Value example                  | Description
-----------------|--------------------------------|-------------
`sup_notiftypes` | audio, visual                  | supported notification-types, like siren, flashlight
`sup_states`     | open, closed, closing, opening | supported states
`sup_tstates`    | open, closed                    | supported target states