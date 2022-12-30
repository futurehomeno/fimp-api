### Association Service
This service allows creating a direct association between a source device (e.g. switch) and a set of destination devices (e.g. lamps). The `group` needs to be specified for zwave-ad while it's implicitly set for zigbee-ad.

This service intends to replace `group` commands in `dev_sys` service.

#### Service Name

`association`

#### Interfaces

Type | Interface                  | Value type | Properties     | Description                                                                                                                    |
-----|----------------------------|------------|----------------|--------------------------------------------------------------------------------------------------------------------------------|
in   | cmd.association.add        | object     |                | Add members to a specific association group.                                                                                   |
in   | cmd.association.delete     | object     |                | Remove a single memeber from an association group.                                                                             |
in   | cmd.association.delete_all | int        |                | Remove all memebers from an association group.                                                                                 |
in   | cmd.association.get_report | int        |                | Request report of a specific association group.                                                                                |
out  | evt.association.report     | object     | `max_supports` | Reports members of a specific association. Property `max_supports` defines how many devices can be added to this group.        |
in   | cmd.groups_info.get_report | null       |                | Z-Wave only. Request detailed information about supported association groups.                                                  |
out  | evt.groups_info.report     | object     |                | Z-Wave only. Returns a list of supported associations groups with descriptions. See [`association_info_object`](#definitions). |

### Definitions

* `association_info_object` is an object describing a specific association group

| Field        | Example                                   | Description                                                       |
|--------------|-------------------------------------------|-------------------------------------------------------------------|
| `group_num`  | `1, 3, 5`                                 | Id of the supported group.                                        |
| `trigger`    | `"Sensor - Temperature", "Control Key 2"` | General description of the trigger type.                          |
| `name`       | `"Lifeline", "Dimmer (S1)"`               | Name of the group, specified by the device manufacturer.          |
| `commands`   | `[{"class": 128, "command": 3}]`          | List of command class and command pairs sent by this association. |

* `trigger` describes the event which will trigger sending an association command. This can be one of the following:
  * `Lifeline` - special, used only fro receiving reports from the device.
  * `Control` - triggered by pressing a physical button, eg. `"Control Key 3"`.
  * `Sensor` - triggered by a sensor report, eg. `"Sensor - Humidity"`.
  * `Notification` - triggered by an alarm, eg. `"Notification - Smoke"`.
  * `Meter` - triggered by a meter report, eg. `"Meter - Electric"`.
   
#### Examples

_IMPORTANT_

- The `group` field is completely ignored for zigbee. The field can be null, empty or removed completely for commands and will be missing for events.
- Zigbee-ad internally creates a group with an ID that's equal to the device ID.

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