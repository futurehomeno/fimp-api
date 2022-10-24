### Door lock service

#### Service names

`door_lock`

#### Interfaces

Type | Interface                     | Value type | Properties                      | Description
-----|-------------------------------|------------|---------------------------------|------------------
in   | cmd.lock.get_report           | null       |                                 |
in   | cmd.lock.set                  | bool       | mode_op                         | Use true to secure a lock and false to unsecure.
in   | cmd.lock.set_with_code        | str_map    |                                 | Used to lock/unlock locks required PIN/RFID, {“op”:”lock”, ”code_type”:”pin”, "code":”12345” }.
out  | evt.lock.report               | bool_map   | timeout_m, timeout_s, lock_type | value = {"is_secured":true, "door_is_closed":true, "bolt_is_locked":true, "latch_is_closed":true}.
-|||
in   | cmd.open.get_report           | null       |                                 |
out  | evt.open.report               | bool       | true = open                     | Used to report if the door is open or closed.
-|||
in   | cmd.auto_lock.set             | bool       | true = auto-lock enabled        | Enable/disable auto-lock feature.
in   | cmd.auto_lock.get_report      | null       |                                 |
out  | evt.auto_lock.report          | bool       | true = auto-lock enabled        |
-|||
in   | cmd.volume.set                | int        | `min_volume`-`max_volume`       |
in   | cmd.volume.get_report         | null       |                                 |
out  | evt.volume.report             | int        | `min_volume`-`max_volume`       |
-|||
in   | cmd.lock.set_configuration    | object     |                                 | Used to set configuration for door lock. Properties described within Notes section.
in   | cmd.lock.get_configuration    | null       |                                 | Used to get current configuration for door lock.     
out  | evt.lock.configuration_report | object     |                                 | Used to report current configuration for door lock.

#### Interface props

Name        | Value example | Description
------------|---------------|-------------
`mode_op`   | "in", "tmout" | Optional. Used to describe advanced unsecure operation mode.
`lock_type` | "key"         | How lock was activated, it can take values: "key", "pin", "rfid".
`timeout_s` | "6"           | Remaining time in seconds before the lock will be automatically locked again. 
`timeout_m` | "5"           | Remaining time in minutes before the lock will be automatically locked again. 

#### Service props

Name                        | Value example                                                         | Description
----------------------------|-----------------------------------------------------------------------|-------------
`sup_components`            | ["is_secured", "door_is_closed", "bolt_is_locked", "latch_is_closed"] | List of supported lock configuration components.
`sup_op_types`              | ["timed", "constant"]                                                 | List of supported operation types.
`sup_modes`                 | ["unsecured", "secured"]                                              | List of supported modes.
`min_volume`                | 0                                                                     | Minimum volume level.
`max_volume`                | 2                                                                     | Maximum volume level.
`supports_auto_relock`      | true                                                                  | Defines if device supports auto-relock capability.
`supports_hold_and_release` | false                                                                 | Defines if device supports hold and release capability.
`supports_block_to_block`   | true                                                                  | Defines if device supports block_to_block capability.
`supports_twist_assist`     | false                                                                 | Defines if device supports twist assist capability.
`min_lock_timeout_seconds`  | 0                                                                     | Defines minimum value of lock going to a secured state after receiving cmd.lock.set with one of timed modes as a value. This properties value represents seconds.
`max_lock_timeout_seconds`  | 59                                                                    | Defines maximum value of lock going to a secured state after receiving cmd.lock.set with one of timed modes as a value. This properties value represents seconds.
`min_lock_timeout_minutes`  | 0                                                                     | Defines minimum value of lock going to a secured state after receiving cmd.lock.set with one of timed modes as a value. This properties value represents minutes.
`max_lock_timeout_minutes`  | 253                                                                   | Defines maximum value of lock going to a secured state after receiving cmd.lock.set with one of timed modes as a value. This properties value represents minutes.
`min_hold_and_release_time` | 1                                                                     | Defines minimum value of hold and release functionality in seconds.
`max_hold_and_release_time` | 65535                                                                 | Defines maximum value of hold and release functionality in seconds.
`min_auto_relock_time`      | 0                                                                     | Defines minimum value of lock going automatically to a secured state in seconds.
`max_auto_relock_time`      | 65535                                                                 | Defines maximum value of lock going automatically to a secured state in seconds.
`sup_out_handles`           | [1, 4]                                                                | Defines which outside handles are available to operate.
`sup_in_handles`            | [1, 2, 3, 4]                                                          | Defines which inside handles are available to operate.
`sup_handles`               | false                                                                 | Defines whether door lock gives an information about how many handles it has. False means, we must ommit "outside_handles_mode" and "inside_handles_mode" when sending "cmd.lock.set_configuration".


#### Example

```json
{
  "serv": "door_lock",
  "type": "cmd.lock.set_configuration",
  "val_t": "object",
  "val": {
    "operation_type": "timed",
    "outside_handles_mode": {
      "1": {
        "can_open": true
      },
      "1": {
        "can_open": true
      },
      "3": {
        "can_open": true
      },
      "4" {
        "can_open": true
      }
    },
    "inside_handles_mode": {
      "1": {
        "can_open": true
      },
      "1": {
        "can_open": true
      },
      "3": {
        "can_open": true
      },
      "4" {
        "can_open": true
      }
    },
    "lock_timeout_minutes": 2,
    "lock_timeout_seconds": 1,
    "auto_relock_time": 60,
    "hold_and_release_time": 55,
    "block_to_block": true,
    "twist_assist": false
  },
  "ver": "1",
  "props": null,
  "tags": null
}

```

#### Notes

Messages cmd.lock.set_configuration and evt.lock.configuration_report will look exactly the same according to value body.

Explanation of cmd.lock.set_configuration interface value properties.

- operation_type - One of sup_operation_types property within the service. At the moment supported values are: 'timed' and 'constant'.

- outside_handles_mode - Defines whether any of four outside handles can be opened locally, 1 means cannot open locally, 0 means can open locally. This field might be ommited, then all door handles can be opened locally.

- inside_handles_mode - Defines whether any of four inside handles can be opened locally, 1 means cannot open locally, 0 means can open locally. This field might be ommited, then all door handles can be opened locally.

- lock_timeout_minutes - This field is used to specify the time that a device must wait before returning to the secured mode when receiving timed operation modes. Values in range 0...253 must indicate the actual number of minutes. This field must be in range 0...253 if the operation_type field is set to 'timed'. This field might be ommited when operation_type field is set to 'constant'.

- lock_timeout_seconds - This field is used to specify the time that a device must wait before returning to the secured mode when receiving timed operation modes. Values in range 0...59 must indicate the actual number of seconds. This field must be in range 0...59 if the operation_type field is set to 'timed'. This field might be ommited when operation_type field is set to 'constant'.

- auto_relock_time - This field is used to specify the time setting in seconds for auto-relock functionality. The value 0 must indicate that the auto-relock functionality is disabled and the door lock must not return to secured mode automatically (unless using Timed Operation). Values in range 1...65535 must indicate that the auto-relock functionality is enabled and a device must return to secured mode after the time in seconds indicated by this field. This field will be ignored (so also can be ommited by client) if a device does not support a capability of auto-relock (service property 'supports_auto_relock').

- hold_and_release_time - This field is used to specify the time setting in seconds for letting the latch retracted after a device mode has been changed to unsecured. The value 0 must indicate that the hold and release functionality is disabled and a device must not keep the latch retracted when the door lock mode becomes unsecured. Values in range 1...65535 must indicate that the hold and release functionality is enabled and the door lock latch must keep open according to the time in seconds indicated by this field. This field will be ignored (so also can be ommited by client) if a device does not support a capability of hold and release (service property 'supports_hold_and_release').

- block_to_block - The value true must indicate that the block_to_block functionality is enabled and a device must activate its motors until blocked to try to reach the mode indicated by a cmd.lock.set, even if it detects to be already in a specified mode. The value false must indicate that the block_to_block functionality is disabled and a device may ignore cmd.lock.set message if it detects to be already in the specified mode. This field will be ignored (so also can be ommited by client) if a device does not support a capability of block_to_block (service property 'supports_block_to_block').

- twist_assist - The value true must indicate that the twist assist functionality is enabled and value false indicates that it's disabled. This field will be ignored (so also can be ommited by client) if a device does not support a capability of twist assist (service property 'supports_twist_assist').

Possible values for sup_modes service property for Z-Wave protocol.

- `unsecured`, `unsecured_with_timeout`, `unsecured_for_inside_door_handles`, `unsecured_for_inside_door_handles_with_timeout`, `unsecured_for_outside_door_handles`, `unsecured_for_outside_door_handles_with_timeout`, `secured`

Possible values for sup_components service property for Z-Wave protocol.

- `door_is_closed`, `door_is_open`, `bolt_is_locked`, `bolt_is_unlocked`, `latch_is_closed`, `latch_is_open`

Possible values for operation_type property for Z-Wave protocol.

- `constant`, `timed`.

Timed operation components (modes) must not be selectable by the end user if the door lock is not configured in timed operation.
