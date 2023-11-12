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
in   | cmd.doorman.integration       | str_map    | Start lock integration | {"name":"Jon", "slot_number":"0", "code_type":"pin", "code":"123456"}
in   | cmd.doorman_param.set         | str_map    |                        | {"parameter_id":"5", "value":"5"}
in   | cmd.doorman_param.get_report  | null       |                        |
out  | evt.doorman_param.report      | str_map    | Response to get_report | List of all available [parameters](#configuration-parameters) in format {"ID":"_value_"}
in   | cmd.doorman_user.set          | str_map    | Set pin or tag         | {"name":"Jon", "slot_number":"1", "code_type":"pin", "code":"123456"}
in   | cmd.doorman_user.get_all      | null       | Get all user slots     |
out  | evt.doorman_user.report       | object     | Response to get_all    | See below
in   | cmd.doorman_user.clear        | str_map    |                        | {"slot_number":"1"}
out  | evt.doorman_activity.report   | str_map    | Triggered by an event from the device | Each of 4 types has a different format, see examples below |
in   | cmd.doorman.arm_confirm       | str_map    |                        | {"sequence_number":"0", "operating_parameter":"0"}
out  | evt.doorman_tag.report        | str_map    | tag_id is 8-byte long  | {"type":"unrecognized_tag", "tag_id": "123456AB"}

### Interface props

Name                | Value                                                    | Description
--------------------|----------------------------------------------------------|-------------
`slot_number`       |  0-9 for PIN codes, 10-19 for RFID tags, 20 for 24h code | ID assigned to each user.
`code_type`         | "pin", "tag", "tag+pin", "24h", "s4+pin", "s8+pin"       | List of supported code types Valid length for specified slots
`card_uid_data`     |                                                          | The Hex format of the TAG UID used in evt.doorman_activity.report event_type=3
`arming_parameter`  |  0 - unlock, 1 - unlock with relock, 2 - lock, 255 - no action | Used in evt.doorman_activity_report event_type=2 to correspond with `operating_parameter` from cmd.doorman.arm_config
`user_status`       | "added", "removed"                                       | Determines whether a user was successfully added or removed from the system in evt.doorman_activity_report event_type=1
`secure_mode`       | "true", "false"                                          | Determines whether the device is in the secure mode in evt.doorman_activity_report event_type=0
`alarm_type`        | <0-255>                                                  | Enum value indicating the alarm type in evt.doorman_activity_report event_type=0
`alarm_level`       | <0-255>                                                  | Enum value parameter for the alarm type from evt.doorman_activity_report event_type=0

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

### Message Examples

Topic example: 

`pt:j1/mt:cmd/rt:dev/rn:zigbee/ad:1/sv:doorman/ad:2_1`

*Note: number `2` at the end of the topic is the device address. Change it to the actual address when sending the commands.*

- cmd.doorman.integration

    Sent automatically from the hub upon reception of `evt.doorman.session_report`

    ```jsx
    {
    "serv": "doorman",
    "type": "cmd.doorman.integration",
    "val_t": "str_map",
    "val": {"slot_number":"0", "code_type":"pin",
    "code":"123456"},
    "props": null,
    "tags": null,
    "src": "thingsplex-ui",
    "ver": "1"
    }
    ```

- cmd.doorman_param.set

    Sets Doorman's parameters. For the valid `parameter_id` values and what they mean, check with corresponding version of Doorman cluster implementation. Some examplary parameters are:

  	DoormanSilentMode              = 0x01
	DoormanAutoRelock              = 0x02
	DoormanLanguage                = 0x05
	DoormanSystemArmHoldTime       = 0x10
	DoormanHomeAwayAlarmMode       = 0x11
	DoormanPartAlarmSystem         = 0x12
	DoormanUserCodeBlockingEnable  = 0x13

    ```jsx
    {
      "serv": "doorman",
      "type": "cmd.doorman.set_param",
      "val_t": "str_map",
      "val": {"parameter_id":"5", "value":"5"},
      "props": null,
      "tags": null,
      "src": "thingsplex-ui",
      "ver": "1"
    }
    ```

    [Configuration parameters](https://www.notion.so/3de70e7b58d1489482f2115a2e486866)

- cmd.doorman_param.get_report

    Returns the values of all the parameters in an `evt.doorman_param.report` message.

    ```jsx
    {
      "serv": "doorman",
      "type": "cmd.doorman_param.get_report",
      "val_t": "null",
      "val": null,
      "props": null,
      "tags": null,
      "src": "thingsplex-ui",
      "ver": "1"
    }
    ```

- cmd.doorman_user.set

    Creates a new user and assigns a pin code to them. An `evt.doorman_user.report` message will be returned.

    ```jsx
    {
      "serv": "doorman",
      "type": "cmd.doorman_user.set"
      "val_t": "str_map",
      "val": {
        "name": "Jon"
        "slot_number": "1",
        "code": "111111",
        "code_type":"pin"
      },
      "props": null,
      "tags": null,
      "src": "thingsplex-ui",
      "ver": "1"
    }
    ```

- cmd.doorman_user.clear

    Creates a new user and assigns a pin code to them. An `evt.doorman_user.report` message will be returned.

    ```jsx
    {
      "serv": "doorman",
      "type": "cmd.doorman_user.clear"
      "val_t": "str_map",
      "val": {
        "slot_number": "1",
      },
      "props": null,
      "tags": null,
      "src": "thingsplex-ui",
      "ver": "1"
    }
    ```

- cmd.doorman_user.get_all

    Get a list of all configured slots in an `evt.doorman_user.report` message.

    ```jsx
    {
      "serv": "doorman",
      "type": "cmd.doorman_user.get_all",
      "val_t": "null",
      "val": null,
      "src": "thingsplex-ui",
      "ver": "1"
    }
    ```

- evt.doorman_user.report

    Get a list of all configured slots

    ```jsx
    {
      "serv": "doorman",
      "type": "evt.doorman_user.report",
      "val_t": "object",
      "val": {
        "slots": [
          {
            "id": 3,
            "name": "Jon",
            "created_at": "2020-04-22T16:05:03.48677828+02:00"
          }
        ]
      },
      "src": "thingsplex-ui",
      "ver": "1"
    }
    ```

- evt.open.report

    Sent by the adapter when the door opens/closes.

    ```jsx
    {
      "type": "evt.open.report",
      "serv": "door_lock",
      "val_t": "bool",
      "val": false,
      "tags": null,
      "props": null,
      "ver": "1",
      "corid": "",
      "ctime": "2020-05-06T11:55:21.02+02:00",
      "uid": "8ed699b1-86bc-47ae-9c88-03ecc4b5c132"
    }
    ```

- evt.alarm.report

    Sent by the adapter upon certain events

    ```jsx
    {
      "type": "evt.alarm.report",
      "serv": "alarm_lock",
      "val_t": "str_map",
      "val": {
        "event": "manual_lock",
        "status": "active"
      },
      "tags": null,
      "props": null,
      "ver": "1",
      "corid": "",
      "ctime": "2020-04-24T17:12:50.686+02:00",
      "uid": "aeae3ebd-9db9-4cad-a9db-23ee493f5f83"
    }
    ```

    Event types:

    ```jsx
    serviceName: "alarm_lock"
    eventTypes: {
        "jammed",
        "manual_unlock",
        "manual_lock",
        "rf_unlock",
        "rf_lock",
        "keypad_unlock",
        "keypad_lock",
        "tag_unlock",
        "tag_lock",
        "auto_locked",
        "lock_failed",
        "door_opened",
        "door_closed"
    }

    serviceName: "alarm_burglar"
    eventTypes: {
        "tamper_invalid_code",
        "tamper_removed_cover",
        "tamper_force_open"
    }

    serviceName: "alarm_power"
    eventTypes: {
        "replace_soon"
    }
    ```

- evt.doorman_activity.report 

    Sent by the lock when an alarm event happens (event_type=0)

    ```jsx
    {
      "type": "evt.doorman_activity.report",
      "serv": "doorman",
      "val_t": "str_map",
      "val": {
        "event_type": "0",
        "error_code": "0",
	"status": "53"
        "alarm_type": "21",
        "alarm_level": "1",
	"secure_mode": "true", // sent only when secure mode has changed
      },
      "tags": null,
      "props": null,
      "ver": "1",
      "corid": "",
      "ctime": "2020-04-24T17:12:50.659+02:00",
      "uid": "58a915ee-afdf-4769-b819-123d5979154b"
    }
    ```

    Sent by the lock when a user event happens (event_type=1)

    ```jsx
    {
      "type": "evt.doorman_activity.report",
      "serv": "doorman",
      "val_t": "str_map",
      "val": {
        "event_type": "1",
        "error_code": "0",
	"slot_number": "0"
        "status": "53",
        "user_status": "added", //or "removed"
      },
      "tags": null,
      "props": null,
      "ver": "1",
      "corid": "",
      "ctime": "2020-04-24T17:12:50.659+02:00",
      "uid": "58a915ee-afdf-4769-b819-123d5979154b"
    }
    ```

    Sent by the lock when an arm event happens (event_type=2)

    ```jsx
    {
      "type": "evt.doorman_activity.report",
      "serv": "doorman",
      "val_t": "str_map",
      "val": {
        "event_type": "2",
        "error_code": "0",
	"slot_number": "0"
        "status": "53",
        "arming_parameter": "0",
      },
      "tags": null,
      "props": null,
      "ver": "1",
      "corid": "",
      "ctime": "2020-04-24T17:12:50.659+02:00",
      "uid": "58a915ee-afdf-4769-b819-123d5979154b"
    }
    ```

    Sent by the lock when an unlock event happens (event_type=3)

    ```jsx
    {
      "type": "evt.doorman_activity.report",
      "serv": "doorman",
      "val_t": "str_map",
      "val": {
        "event_type": "3",
        "error_code": "0",
	"slot_number": "0"
        "status": "53",
        "card_uid_data": "AACDEF12", // 8 bytes string
      },
      "tags": null,
      "props": null,
      "ver": "1",
      "corid": "",
      "ctime": "2020-04-24T17:12:50.659+02:00",
      "uid": "58a915ee-afdf-4769-b819-123d5979154b"
    }
    ```
