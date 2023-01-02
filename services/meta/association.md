# Association Service
This service allows creating a direct association between a source device (e.g. switch) and a set of destination devices (e.g. lamps). All devices taking part in the association process need to be included and controllable. The `group` needs to be specified for zwave-ad while it's implicitly set for zigbee-ad.

This service intends to replace `group` commands in `dev_sys` service.

## Service Name

`association`

## Interfaces

Type | Interface                  | Value type | Properties     | Description                                                                                                                                                                              |
-----|----------------------------|------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
in   | cmd.association.add        | object     |                | Add members to a specific association group. See [`association_members`](#definitions) for value definition.                                                                                        |
in   | cmd.association.delete     | object     |                | Remove a single memeber from an association group. See [`association_members`](#definitions) for value definition.                                                                       |
in   | cmd.association.delete_all | int        |                | Remove all memebers from an association group.                                                                                                                                           |
in   | cmd.association.get_report | int        |                | Request report of a specific association group.                                                                                                                                          |
out  | evt.association.report     | object     | `max_supports` | Reports members of a specific association. Property `max_supports` defines how many devices can be added to this group. See [`association_members`](#definitions) for value definition.  |
in   | cmd.groups_info.get_report | null       |                | Z-Wave only. Request detailed information about supported association groups.                                                                                                            |
out  | evt.groups_info.report     | object     |                | Z-Wave only. Returns a list of supported associations groups with descriptions. See [`association_info_object`](#definitions).                                                           |

## Service Props

Name             | Supported Values                                | Description                                                             |
-----------------|-------------------------------------------------|-------------------------------------------------------------------------|
`in_services`    | `["out_bin_switch", "out_lvl_switch", "color"]` | Zigbee only. List of services that can be controlled, e.g. on a lamp.   |
`out_services`   | `["out_bin_switch", "out_lvl_switch", "color"]` | Zigbee only. List of services the device can control, e.g. on a button. |

> A controllable device (like a lamp) would have a list of `in_services` that would indicate the services it supports. A controller (like a button) would have a list of `out_services` instead.

## Definitions
* `association_members` is an object describing association group members:
 
| Field        | Type      | Example           | Description                                    |
|--------------|-----------|-------------------|------------------------------------------------|
| `group`      | int       | `1, 3, 5`         | Id of the supported group.                     |
| `members`    | str_array | `["2_0", "15_1"]` | List of group members.                         |

> The `group` field is completely ignored for zigbee. The field can be null, empty or removed completely for commands and will be missing for events. Zigbee-ad internally creates a group with an ID that's equal to the device ID.

* `association_info` is an object describing a specific association group:

| Field        | Type   | Example                                   | Description                                                       |
|--------------|--------|-------------------------------------------|-------------------------------------------------------------------|
| `group_num`  | int    | `1, 3, 5`                                 | Id of the supported group.                                        |
| `trigger`    | string | `"Sensor - Temperature", "Control Key 2"` | General description of the trigger type.                          |
| `name`       | string | `"Lifeline", "Dimmer (S1)"`               | Name of the group, specified by the device manufacturer.          |
| `commands`   | object | `[{"class": 128, "command": 3}]`          | Array of [`commands`](#definitions).                              |

* `commands` is an int_map describing specific commands sent by an association:
 
| Field        | Type | Example         | Description                                           |
|--------------|------|-----------------|-------------------------------------------------------|
| `class`      | int  | `104, 128, 130` | Command class.                                        |
| `command`    | int  | `1, 3, 4`       | Id of the specific command in that command class.     |

* `trigger` describes the event which will trigger sending an association command. This can be one of the following:
  * `Lifeline` - special, used only fro receiving reports from the device.
  * `Control` - triggered by pressing a physical button, e.g. `"Control Key 3"`.
  * `Sensor` - triggered by a sensor report, e.g. `"Sensor - Humidity"`.
  * `Notification` - triggered by an alarm, e.g. `"Notification - Smoke"`.
  * `Meter` - triggered by a meter report, e.g. `"Meter - Electric"`.
   
## Examples

```json
{
  "serv": "association",
  "type": "cmd.association.add",
  "val_t": "object",
  "val": {
    "group": 1,
    "members": ["2_1"]
  },
  "props": null,
  "tags": null
}

{
  "serv": "association",
  "type": "cmd.association.delete",
  "val_t": "object",
  "val": {
    "group": 1,
    "members":["2_1"]
  },
  "props": null,
  "tags": null
}

{
  "serv": "association",
  "type": "cmd.association.delete_all",
  "val_t": "int",
  "val": 2,
  "props": null,
  "tags": null
}

{
  "serv": "association",
  "type": "cmd.association.get_report",
  "val_t": "int",
  "val": 2,
  "props": null,
  "tags": null
}

{
  "serv": "association",
  "type": "evt.association.report",
  "val_t": "object",
  "val": {
    "group": 3,
    "member": ["2_1", "3_1"],
  },
  "props": null,
  "tags": null
}

{
  "serv": "association",
  "type": "evt.groups_info.report",
  "val_t": "object",
  "val": [
    {
      "commands": [
        {
          "class": 128,
          "command": 3
        },
        {
          "class": 113,
          "command": 5
        },
        {
          "class": 49,
          "command": 5
        },
        {
          "class": 90,
          "command": 1
        }
      ],
      "group_num": 1,
      "name": "Lifeline",
      "trigger": "Lifeline"
    },
    {
      "commands": [
        {
          "class": 32,
          "command": 1
        }
      ],
      "group_num": 2,
      "name": "Basic set",
      "trigger": "Notification - Smoke"
    },
    {
      "commands": [
        {
          "class": 43,
          "command": 1
        }
      ],
      "group_num": 3,
      "name": "Scene set",
      "trigger": "Control Key 1"
    }
  ],
  "props": {},
  "tags": null,
}
```