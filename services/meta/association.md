### Association Service
This service allows creating a direct association between a source device (e.g. switch) and a set of destination devices (e.g. lamps). The `group` needs to be specified for zwave-ad while it's implicitly set for zigbee-ad.

This service intends to replace `group` commands in `dev_sys` service.

A controllable device (like a lamp) would have a list of `in_services` that would indicate the services it supports. A controller (like a button) would have a list of `out_services` instead.

#### Service Name

`association`

#### Interfaces

Type | Interface                  | Value type | Description
-----|-----------------------     |------------|------------
in   | cmd.association.add        | object     | Add members to the group
in   | cmd.association.delete     | object     | Remove association for a single member
in   | cmd.association.delete_all | string     | Remove associations for all group members
in   | cmd.association.get_report | string     | Get all members of a group
out  | evt.association.report     | object     | Response for `get_report`

#### Service Props

Name             | Supported Values           | Description
-----------------|----------------------------|-------------
`in_services`   | `["out_bin_switch", "out_lvl_switch", "color"]` | List of services that can be controlled, e.g. on a lamp
`out_services`   | `["out_bin_switch", "out_lvl_switch", "color"]` | List of services the device can control, e.g. on a button

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
    "group": "group_1",
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
    "group": "group_1",
    "members":["2_1"]
  },
  "props": null,
  "tags": null
}

{
  "serv": "association",
  "type": "cmd.association.delete_all",
  "val_t": "str",
  "val": "group_1",
  "props": null,
  "tags": null
}

{
  "serv": "association",
  "type": "cmd.association.get_report",
  "val_t": "str",
  "val": "group_1",
  "props": null,
  "tags": null
}

{
  "serv": "association",
  "type": "evt.association.report",
  "val_t": "object",
  "val": {
    "group": "group_1",
    "member": ["2_1", "3_1"],
  },
  "props": null,
  "tags": null
}
```