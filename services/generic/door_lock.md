# Door Lock Service

Door lock service is used to control door locks. It is used to lock and unlock doors, as well as to get the current state of the lock.

> Door lock device functionalities can be extended by [user code](/services/generic/user_code.md) and [schedule entry](/services/generic/schedule_entry.md) services.

## Service name

`door_lock`

## Interfaces

| Type | Interface                     | Value type | Properties                            | Description                                                                                                                                  |
|------|-------------------------------|------------|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.lock.get_report           | null       |                                       | Requests the lock status.                                                                                                                    |
| in   | cmd.lock.set                  | bool       | `mode_op`                             | **Secures** the lock if the provided value is `true` and unlocks it if the value is `false`.                                                 |
| out  | evt.lock.report               | bool_map   | `timeout_m`, `timeout_s`, `lock_type` | Returns the lock status as a boolean map of components defined in [`sup_components`](#service-properties) property.                          |
| -    |                               |            |                                       |                                                                                                                                              |
| in   | cmd.auto_lock.set             | bool       |                                       | Enables/disables the auto-lock feature.                                                                                                      |
| in   | cmd.auto_lock.get_report      | null       |                                       | Requests report on whether the auto-lock is enabled or disabled.                                                                             |
| out  | evt.auto_lock.report          | bool       |                                       | Reports `true` if the auto-lock is **enabled**, `false` otherwise.                                                                           |
| -    |                               |            |                                       |                                                                                                                                              |
| in   | cmd.volume.set                | int        |                                       | Sets the volume of the device. Value must be between [`min_volume`](#service-properties) and [`max_volume`](#service-properties) properties. |
| in   | cmd.volume.get_report         | null       |                                       | Requests the volume of the device.                                                                                                           |
| out  | evt.volume.report             | int        |                                       | Reports the volume of the device.                                                                                                            |
| -    |                               |            |                                       |                                                                                                                                              |
| in   | cmd.lock.set_configuration    | object     |                                       | Sets configuration for the door lock. See [`configuration`](#definitions) object reference for more details.                                 |
| in   | cmd.lock.get_configuration    | null       |                                       | Gets current configuration for the door lock.                                                                                                |
| out  | evt.lock.configuration_report | object     |                                       | Reports current configuration for the door lock.                                                                                             |

## Interface properties

| Name        | Example                    | Required | Description                                                                                                                                                                                                                                                                                                                              |
|-------------|----------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `mode_op`   | `"unsecured_with_timeout"` | No       | Optionally defines mode of an unlock operation. Possible values are an applicable sub-set of `sup_modes`](#service-properties): `unsecured_with_timeout`, `unsecured_for_inside_door_handles`, `unsecured_for_inside_door_handles_with_timeout`, `unsecured_for_outside_door_handles`,`unsecured_for_outside_door_handles_with_timeout`. |
| `lock_type` | `"key"`                    | No       | How lock was activated, it can take values such as `key`, `pin`, `rfid`.                                                                                                                                                                                                                                                                 |
| `timeout_s` | `"30"`                     | No       | Remaining time in seconds before the lock will be automatically secured again.                                                                                                                                                                                                                                                           |
| `timeout_m` | `"2"`                      | No       | Remaining time in minutes before the lock will be automatically secured again.                                                                                                                                                                                                                                                           |

## Service properties

| Name                        | Type      | Example                            | Description                                                                                                                                                                                                                                                                    |
|-----------------------------|-----------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `sup_components`            | str_array | `["is_secured", "door_is_closed"]` | List of supported lock configuration components. Possible values are: `is_secured`, `door_is_closed`, `bolt_is_locked`,  `latch_is_closed`.                                                                                                                                    |
| `sup_op_types`              | str_array | `["timed", "constant"]`            | List of supported operation types. Possible values are: `timed`, `constant`.                                                                                                                                                                                                   |
| `sup_modes`                 | str_array | `["unsecured", "secured"]`         | List of supported modes. Possible values are: `secured`, `unsecured`, `unsecured_with_timeout`, `unsecured_for_inside_door_handles`, `unsecured_for_inside_door_handles_with_timeout`, `unsecured_for_outside_door_handles`,`unsecured_for_outside_door_handles_with_timeout`. |
| `min_volume`                | int       | `0`                                | Minimum volume level.                                                                                                                                                                                                                                                          |
| `max_volume`                | int       | `2`                                | Maximum volume level.                                                                                                                                                                                                                                                          |
| `supports_auto_relock`      | bool      | `true`                             | Defines if device supports auto-relock capability.                                                                                                                                                                                                                             |
| `supports_hold_and_release` | bool      | `false`                            | Defines if device supports hold-and-release capability.                                                                                                                                                                                                                        |
| `supports_block_to_block`   | bool      | `true`                             | Defines if device supports block-to-block capability.                                                                                                                                                                                                                          |
| `supports_twist_assist`     | bool      | `false`                            | Defines if device supports twist assist capability.                                                                                                                                                                                                                            |
| `min_lock_timeout_seconds`  | int       | `0`                                | Defines minimum value of lock going to a secured state after receiving `cmd.lock.set` with one of timed modes as a value. This properties value represents seconds.                                                                                                            |
| `max_lock_timeout_seconds`  | int       | `59`                               | Defines maximum value of lock going to a secured state after receiving `cmd.lock.set` with one of timed modes as a value. This properties value represents seconds.                                                                                                            |
| `min_lock_timeout_minutes`  | int       | `0`                                | Defines minimum value of lock going to a secured state after receiving `cmd.lock.set` with one of timed modes as a value. This properties value represents minutes.                                                                                                            |
| `max_lock_timeout_minutes`  | int       | `253`                              | Defines maximum value of lock going to a secured state after receiving `cmd.lock.set` with one of timed modes as a value. This properties value represents minutes.                                                                                                            |
| `min_hold_and_release_time` | int       | `1`                                | Defines minimum value of hold and release functionality in seconds.                                                                                                                                                                                                            |
| `max_hold_and_release_time` | int       | `65535`                            | Defines maximum value of hold and release functionality in seconds.                                                                                                                                                                                                            |
| `min_auto_relock_time`      | int       | `0`                                | Defines minimum value of lock going automatically to a secured state in seconds.                                                                                                                                                                                               |
| `max_auto_relock_time`      | int       | `65535`                            | Defines maximum value of lock going automatically to a secured state in seconds.                                                                                                                                                                                               |
| `sup_out_handles`           | int_array | `[1, 4]`                           | Defines which outside handles are available to operate.                                                                                                                                                                                                                        |
| `sup_in_handles`            | int_array | `[1, 2, 3, 4]`                     | Defines which inside handles are available to operate.                                                                                                                                                                                                                         |
| `sup_handles`               | bool      | `true`                             | Defines whether door lock gives an information about how many handles it has, `false` means, we should omit `outside_handles_mode` and `inside_handles_mode` when sending `cmd.lock.set_configuration` command.                                                                |


## Definitions

* `configuration` is an object with the following structure:

| Field                 | Type   | Example                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------|--------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| operation_type        | string | `"timed"`                  | One of the values declared in [`sup_op_types`](#service-properties) property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| lock_timeout_minutes  | int    | `2`                        | The time in minutes that a device must wait before returning to the secured mode when receiving timed operation modes. This field must be in range 0-253 if the `operation_type` field is set to `timed`. This field should be skipped when operation_type field is set to `constant`.                                                                                                                                                                                                                                                                                                               |
| lock_timeout_seconds  | int    | `30`                       | The time in seconds that a device must wait before returning to the secured mode when receiving timed operation modes. This field must be in range 0-59 if the `operation_type` field is set to `timed`. This field should be skipped when operation_type field is set to `constant`.                                                                                                                                                                                                                                                                                                                |
| auto_relock_time      | int    | `60`                       | Specifies the time in seconds for auto-relock functionality. The value 0 must indicate that the auto-relock functionality is disabled and the door lock must not return to secured mode automatically, unless using timed operation. The value 0 indicates that the functionality is disabled. Values in 1-65535 range indicate that the auto-relock functionality is enabled and a device must return to secured mode after the time passes. This field will be ignored if a device does not support a capability of auto-relock defined in [`supports_auto_relock`](#service-properties) property. |
| hold_and_release_time | int    | `55`                       | Specifies the time in seconds for letting the latch be retracted after a device mode has been changed to unsecured. The value 0 indicates that the functionality is disabled. Value in range 1-65535 must indicates that the hold and release functionality is enabled and the door lock latch must keep open according to the time in seconds indicated by this field. This field will be ignored if a device does not support a capability of hold and release defined in [`supports_hold_and_release`](#service-properties) property.                                                             |
| block_to_block        | bool   | `true`                     | The value `true` must indicate that the block-to-block functionality is enabled and a device must activate its motors until blocked to try to reach the mode indicated by a `cmd.lock.set`, even if it detects to be already in a specified mode. The value `false` must indicate that the block-to-block functionality is disabled and a device may ignore `cmd.lock.set` message if it detects to be already in the specified mode. This field will be ignored if a device does not support a capability of block-to-block defined in [`supports_block_to_block`](#service-properties) property.   |
| twist_assist          | bool   | `true`                     | The value `true` must indicate that the twist assist functionality is enabled and value `false` indicates that it's disabled. This field will be ignored if a device does not support a capability of twist assist defined in [`supports_twist_assist`](#service-properties) property.                                                                                                                                                                                                                                                                                                               |
| outside_handles_mode  | object | `{"1":{"can_open":true}}`  | A map of [`handle_mode`](#definitions) objects per supported handles defined in [`sup_out_handles`](#service-properties) property. If handle is omitted in the map it is assumed it can be open. Field should be ignored if [`sup_out_handles`](#service-properties) property is empty.                                                                                                                                                                                                                                                                                                              |
| inside_handles_mode   | object | `{"1":{"can_open":false}}` | A map of [`handle_mode`](#definitions) objects per supported handles defined in [`sup_in_handles`](#service-properties) property. If handle is omitted in the map it is assumed it can be open. Field should be ignored if [`sup_in_handles`](#service-properties) property is empty.                                                                                                                                                                                                                                                                                                                |

* `handle_mode` is an object with the following structure:

| Field    | Type | Example | Description                                              |
|----------|------|---------|----------------------------------------------------------|
| can_open | bool | `true`  | Defines whether handle can be used to unsecure the lock. |


## Examples

* Example of a command unlocking the lock and leaving it unsecured for the time configured in lock timeout settings:

```json
{
  "serv": "door_lock",
  "type": "cmd.lock.set",
  "val_t": "bool",
  "val": false,
  "props": {
    "mode_op": "unsecured_with_timeout"
  },
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "49b60210-5374-11ed-b6d0-33d4305f427b",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:door_lock/ad:59_0"
}
```

* Example of a report of the lock state:

```json
{
  "serv": "door_lock",
  "type": "cmd.lock.report",
  "val_t": "bool_map",
  "val": {
    "is_secured": false, 
    "door_is_closed": false, 
    "bolt_is_locked": false, 
    "latch_is_closed": false
  },
  "props": {
    "timeout_m": "2",
    "timeout_s": "30"
  },
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "49b60210-5374-11ed-b6d0-33d4305f427b",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:door_lock/ad:59_0"
}
```

* Example of a configuration command:

```json
{
  "serv": "door_lock",
  "type": "cmd.lock.set_configuration",
  "val_t": "object",
  "val": {
    "operation_type": "timed",
    "lock_timeout_minutes": 2,
    "lock_timeout_seconds": 30,
    "outside_handles_mode": {
      "1": {
        "can_open": true
      },
      "4": {
        "can_open": false
      }
    },
    "inside_handles_mode": {
      "1": {
        "can_open": true
      },
      "2": {
        "can_open": false
      },
      "3": {
        "can_open": true
      },
      "4": {
        "can_open": true
      }
    },
    "auto_relock_time": 60,
    "hold_and_release_time": 55,
    "block_to_block": true,
    "twist_assist": false
  },
  "props": null,
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "49b60210-5374-11ed-b6d0-33d4305f427b",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:door_lock/ad:59_0"
}
```