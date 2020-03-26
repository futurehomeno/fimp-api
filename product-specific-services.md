# Product Specific Services
The following services are designed for specific products.

## Doorman service
Yale Doorman custom service definition.

### Service names

`doorman`

### Interfaces

Type | Interface                     | Value Type | Description            | Example
-----|-------------------------------|------------|------------------------| --------
out  | evt.doorman_session.report    | null       | Integration required   | 
in   | cmd.doorman.integration       | str_map    | Start lock integration | {"slot_number":"0", "code_type":"pin", "code":"123456"}
in   | cmd.doorman_param.set         | str_map    |                        | {"parameter_id":"5", "value":"5"}
in   | cmd.doorman_param.get_report | null       |                        | 
out  | evt.doorman_param.report      | str_map    | Response to get_params | 
in   | cmd.doorman_user.set          | str_map    | Set pin or tag         | {“slot_number”:”0”, ”code”:”123456”}
in   | cmd.doorman_user.clear        | str_map    |                        | {“slot_number”:”0”}
out  | evt.doorman_activity.report   | str_map    | Sent after an activity | {“event_type”:”id”, “status”:”0”, “error_code”:”0”, “user_status”:”added”, “slot_number”:”0”, “alarm_type”:”0”, “alarm_level”:”0”, “arming_parameter”:”0”, “sequence_number”:”0”, ”card_uid_data”:”12345678”}
in   | cmd.doorman.arm_confirm       | str_map    |                        | {“sequence_number”:”0”, “operating_parameter”:”0”}
out  | evt.op.ack                    | string     | Command sent to lock. Applies to `cmd.doorman_param.set` | Value can be "ack" or "nack"

More details and examples can be found on [Notion](https://www.notion.so/Assa-Abloy-Yale-doorman-v2-Zigbee-c94f3164a74f4035bf2d47d29ec9c9c0).

### Interface props

Name              | Value                                              | Description
------------------|----------------------------------------------------|-------------
`slot_number`     | 0-19                                               | 0-9 (for PIN codes), 10-19 (for RFID tags) 
`code_type`       | "pin", "tag", "tag+pin", "24h", "s4+pin", "s8+pin" | List of supported code types Valid length for specified slots
`pin_code_length` | 6 (For slot number 0-19), 4 - For slot number 20   | Valid length for specified slots
`card_uid_data`   |                                                    | The Hex format of the TAG UID
`user_status`     | “added”, “removed”                                 | Determines whether a user was successfully added or removed from the system.

### Configuration parameters

Name                 | ID | Value
---------------------|----|-------
Silent mode on/off   | 1 | 1: Silent mode ON 2: Volume 1 (low) 3: Volume 2 (high)
Auto Relock on/off   | 2 | 0: OFF 255: ON
Language             | 5 | 1: English, 4: Danish, 5: Norwegian, 6: Swedish
System Arm hold time (long pressed time) | 16 | Selectable between 1,000~20,000ms with 100ms steps
Home/Away Alarm Mode | 17 | 0: OFF, 1: Home Alarm Mode, 2: Away Alarm Mode
Part of Alarm System | 18 | 0: OFF (Lock is not in Alarm system), 1: ON (default - Lock is in Alarm system)
User Code Blocking Enable | 19 | 0: Disabled (User can open lock by user code or integrated system), 1: Enabled, User can open only with TAG or TAG + PIN. User code, and remote open does not work.
