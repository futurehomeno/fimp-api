# Association Service

This service allows creating a direct association between a source device (e.g. switch) and a set of destination devices (e.g. lamps).
All devices taking part in the association process need to be included and controllable.
This service replaces deprecated group functionalities in [system service](/device_services/meta/system.md).

## Service Name

`association`

## Interfaces

| Type | Interface                  | Value type | Properties     | Storage     | Aggregation | Description                                                                                                                                                                             |
|------|----------------------------|------------|----------------|-------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.association.add        | object     |                |             |             | Add members to a specific association group. See [`association_members`](#definitions) for value definition.                                                                            |
| in   | cmd.association.delete     | object     |                |             |             | Remove members from an association group. See [`association_members`](#definitions) for value definition.                                                                               |
| in   | cmd.association.delete_all | string     |                |             |             | Remove all members from an association group.                                                                                                                                           |
| in   | cmd.association.get_report | string     |                |             |             | Request report of a specific association group.                                                                                                                                         |
| out  | evt.association.report     | object     | `max_supports` | `aggregate` | `group`     | Reports members of a specific association. Property `max_supports` defines how many devices can be added to this group. See [`association_members`](#definitions) for value definition. |

## Service properties

| Name         | Example           | Description                                                                  |
|--------------|-------------------|------------------------------------------------------------------------------|
| `sup_groups` | `["1", "2", "3"]` | List of supported groups. If present, `group` field is required in messages. |

## Interface properties

| Name           | Example  | Description                                            |                      
|----------------|----------|--------------------------------------------------------|
| `max_supports` | `2`, `7` | Maximum number of members in the specific association. |

## Definitions

* `association_members` is an object describing association group members:

| Field     | Type      | Example           | Description                |
|-----------|-----------|-------------------|----------------------------|
| `group`   | string    | `"1"`, `"3"`      | Id of the supported group. |
| `members` | str_array | `["2_0", "15_1"]` | List of group members.     |

> The `group` field is completely ignored for Zigbee. The field can be null, empty or removed completely for commands and will be missing for events.
> Zigbee adapter internally creates a group with an ID that's equal to the device UDID.

## Examples

* Example of adding members to an association.

```json
{
  "serv": "association",
  "type": "cmd.association.add",
  "val_t": "object",
  "val": {
    "group": "1",
    "members": [
      "2_1"
    ]
  },
  "props": null,
  "tags": null
}
```

* Example of deleting members from an association.

```json
{
  "serv": "association",
  "type": "cmd.association.delete",
  "val_t": "object",
  "val": {
    "group": "1",
    "members": [
      "2_1"
    ]
  },
  "props": null,
  "tags": null
}
```

* Example of an association report request.

```json
{
  "serv": "association",
  "type": "cmd.association.get_report",
  "val_t": "string",
  "val": "2",
  "props": null,
  "tags": null
}
```

* Example of a report of association members.

```json
{
  "serv": "association",
  "type": "evt.association.report",
  "val_t": "object",
  "val": {
    "group": "3",
    "members": [
      "2_1",
      "3_1"
    ]
  },
  "storage": {
    "strategy": "aggregate",
    "sub_value": "3"
  },
  "props": null,
  "tags": null
}
```