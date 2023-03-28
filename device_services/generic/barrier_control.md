# Barrier Control service

The service represent devices like garage doors, barriers, window protection shades, and similar.

> Please note that blinds and similar devices might also be supported in a limited way using more generic 
> [`out_bin_switch`](/device_services/generic/output_binary_switch.md) and [`out_lvl_switch`](/device_services/generic/output_level_switch.md) services.

## Service name

`barrier_ctrl`

## Interfaces

| Type | Interface                | Value type | Properties | Description                                                                                                                                                                              |
|------|--------------------------|------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.notiftype.get_report | null       |            | Requests notification types the device supports when signalling opening/closing of the door.                                                                                             |
| in   | cmd.notiftype.set        | bool_map   |            | Sets notification type the device is using when signalling opening/closing of the door. Configurable notification types are defined in [`sup_notiftypes`](#service-properties) property. |
| out  | evt.notiftype.report     | bool_map   |            | Returns notification types the device is using while opening/closing door.                                                                                                               |
| -    |                          |            |            |                                                                                                                                                                                          |
| in   | cmd.op.stop              | null       |            | Stops any operation immediately.                                                                                                                                                         |
| -    |                          |            |            |                                                                                                                                                                                          |
| in   | cmd.state.get_report     | null       |            | Requests the current state of the device.                                                                                                                                                |
| out  | evt.state.report         | string     | `position` | Reports the current state of the device, one of values defined in [`sup_states`](#service-properties) property.                                                                          |
| -    |                          |            |            |                                                                                                                                                                                          |
| in   | cmd.tstate.set           | string     | `position` | Sets the target state of the device to the one of values defined in [`sup_tstates`](#service-properties) property.                                                                       |

## Interface properties

| Name       | Required | Example | Description                                                                    |
|------------|----------|---------|--------------------------------------------------------------------------------|
| `position` | No       | `"30"`  | Position as percentage value where `1` is near closed while `99` is near open. |

> Please note that property `position` is optional and depend directly on the device capabilities.
> * Property `position` in `cmd.tstate.set` will be ignored if the device does not support partial opening or closing indicated by `sup_tposition` service property.
> * Property `position` in `evt.state.report` might be present only on "stopped" state report or never if the device does not support live progress reporting.

## Service properties

| Name             | Type      | Example                                    | Description                                                                                       |
|------------------|-----------|--------------------------------------------|---------------------------------------------------------------------------------------------------|
| `sup_notiftypes` | str_array | `["audio", "visual"]`                      | List of supported notification types. Allowed values are: `audio`, `visual`.                      |
| `sup_states`     | str_array | `["open", "closed", "closing", "opening"]` | List of supported states. Allowed values are:  `closed`, `closing`, `stopped`, `opening`, `open`. |
| `sup_tstates`    | str_array | `["open", "closed"]`                       | List of supported target states. Allowed values are: `closed`, `open`.                            |
| `sup_tposition`  | bool      | `true`                                     | Indicates whether the `position` property is supported by `cmd.tstate.set` command.               |

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

* Example of a command to open the barrier partially to 50% position:

```json
{
  "serv": "barrier_ctrl",
  "type": "cmd.tstate.set",
  "val_t": "string",
  "val": "open",
  "props": {
    "position": "50"
  },
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
    "position": "30"
  },
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:barrier_ctrl/ad:50_0"
}
```