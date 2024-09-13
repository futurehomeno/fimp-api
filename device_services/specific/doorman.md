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
out  | evt.doorman_activity.report   | str_map    | Modes settings         | {"secure_mode": "true", "auto_lock": "true", "three_min_lock": "false"}
in   | cmd.doorman.arm_confirm       | str_map    | Sets arming setting    | {"operating_parameter":"0"}
out  | evt.doorman_tag.report        | str_map    | tag_id is 8-byte long  | {"type":"unrecognized_tag", "tag_id": "12345678AABBCCDD"}

### Interface props

Name                | Value                                                    | Description
--------------------|----------------------------------------------------------|-------------
`slot_number`       | 0-9 for PIN codes, 10-19 for RFID tags, 20 for 24h code | ID assigned to each user.
`code_type`         | "pin", "tag", "tag+pin", "24h", "s4+pin", "s8+pin"       | List of supported code types Valid length for specified slots
`card_uid_data`     |                                                          | The Hex format of the TAG UID used in evt.doorman_activity.report event_type=3
`arming_parameter`  | 0 - disarming, 1 - arming                                | Determines disarming/arming setting on the device
`secure_mode`       | "true", "false"                                          | Determines whether the device is in the secure mode in evt.doorman_activity_report. Sent only when changed.
`auto_lock`         | "true", "false"                                          | Determines whether the device is in the auto mode in evt.doorman_activity_report. Sent only when changed.
`secure_mode`       | "true", "false"                                          | Determines whether the device is in the 3 min lock mode in evt.doorman_activity_report. Sent only when changed.

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

- cmd.doorman.integration

    Sent automatically from the hub upon reception of `evt.doorman.session_report`

    ```jsx
    {
    "serv": "doorman",
    "type": "cmd.doorman.integration",
    "val_t": "str_map",
    "val": {"slot_number":"0", "code_type":"pin", "code":"123456", "name": "Jon"},
    "props": null,
    "tags": null,
    "src": "thingsplex-ui",
    "ver": "1"
    }
    ```

- cmd.doorman_param.set

    Sets configuration parameter from the [list](#configuration-parameters). For the valid `parameter_id` values and what they mean, check with corresponding version of Doorman cluster implementation

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

- evt.doorman_activity.report sent by the device upon secure mode change

    ```jsx
    {
      "type": "evt.doorman_activity.report",
      "serv": "doorman",
      "val_t": "str_map",
      "val": {
        "secure_mode": "true",
      },
      "tags": null,
      "props": null,
      "ver": "1",
      "corid": "",
      "ctime": "2020-04-24T17:12:50.659+02:00",
      "uid": "58a915ee-afdf-4769-b819-123d5979154b"
    }
    ```
