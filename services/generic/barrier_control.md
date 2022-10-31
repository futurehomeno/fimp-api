# Barrier Control service

The service represent devices like garage doors, barriers, window protection shades, and similar.

## Service name

`barrier_ctrl`

## Interfaces

| Type | Interface                | Value type | Properties   | Description                                                                                                                                                                |
|------|--------------------------|------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.notiftype.get_report | null       |              | Requests notification types the device is using while opening/closing door.                                                                                                |
| in   | cmd.notiftype.set        | bool_map   |              | Sets notification type the device is is using while opening/closing door. Configurable notification types are defined in [`sup_notiftypes`](#service-properties) property. |
| out  | evt.notiftype.report     | bool_map   |              | Returns notification types the device is using while opening/closing door.                                                                                                 |
| -    |                          |            |              |                                                                                                                                                                            |
| in   | cmd.op.stop              | null       |              | Commence emergency stop of any operation.                                                                                                                                  |
| -    |                          |            |              |                                                                                                                                                                            |
| in   | cmd.state.get_report     | null       |              | Requests the current state of the device.                                                                                                                                  |
| out  | evt.state.report         | string     | `stopped_at` | Reports the current state of the device, one of values defined in [`sup_states`](#service-properties) property.                                                            |
| -    |                          |            |              |                                                                                                                                                                            |
| in   | cmd.tstate.set           | string     |              | Sets the target state of the device to the one of values defined in [`sup_tstates`](#service-properties) property.                                                         |

## Interface properties

| Name         | Required | Example | Description                                                                                                                    |
|--------------|----------|---------|--------------------------------------------------------------------------------------------------------------------------------|
| `stopped_at` | No       | `"30"`  | Position as percentage value at which the barrier stopped on emergency halt, where `1` is near closed while `99` is near open. |

## Service properties

| Name             | Type      | Example                                    | Description                                                                                        |
|------------------|-----------|--------------------------------------------|----------------------------------------------------------------------------------------------------|
| `sup_notiftypes` | str_array | `["audio", "visual"]`                      | List of supported notification types. Possible values are: `audio`, `visual`.                      |
| `sup_states`     | str_array | `["open", "closed", "closing", "opening"]` | List of supported states. Possible values are:  `closed`, `closing`, `stopped`, `opening`, `open`. |
| `sup_tstates`    | str_array | `["open", "closed"]`                       | List of supported target states. Possible values are: `closed`, `open`.                            |

## Examples

* Example of a configuration command of the notification types:

```json
{
  "serv": "barrier_ctrl",
  "type": "cmd.notiftype.set",
  "val_t": "bool_map",
  "val": {
    "audio": false,
    "visual": true
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:barrier_ctrl/ad:50_0"
}
```

* Example of a command to open the barrier:

```json
{
  "serv": "barrier_ctrl",
  "type": "cmd.tstate.set",
  "val_t": "string",
  "val": "open",
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:barrier_ctrl/ad:50_0"
}
```

* Example of a reporting stating the barrier was stopped at 30% position:

```json
{
  "serv": "barrier_ctrl",
  "type": "evt.state.report",
  "val_t": "string",
  "val": "stopped",
  "props": {
    "stopped_at": "30"
  },
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:barrier_ctrl/ad:50_0"
}
```