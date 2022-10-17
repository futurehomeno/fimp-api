### User code service

Is used by door locks, keypads, security panels to enter and manage pin codes and rfids.

Detailed specification is avaliable on zwave-ad repo under docs folder.

#### Service names

`user_code`

Type | Interface                      | Value type | Description
-----|--------------------------------|------------|------------------
in   | cmd.usercode.clear             | str_map    | Clear a single slot. On success, a config report is sent with val: `{"event": "code_deleted"}`
in   | cmd.usercode.clear_all         | null       | Clear all slots
in   | cmd.usercode.get               | null       | Get all users. Response comes as `evt.usercode.users_report`
in   | cmd.usercode.set               | str_map    | Set a new user. On success, a config report is sent with val: `{"event": "code_added"}`
out  | evt.usercode.config_report     | str_map    | Confirms the success of a `set` or `clear` command
out  | evt.usercode.users_report      | str_map    | A response to `get` command

#### Service props

Name             | Values                     | Description
-----------------|----------------------------|-------------
`sup_usercodes`  | ["pin", "rfid"]            | List of supported user code types
`sup_userstatus` | ["enabled", "disabled"]    | List of supported user status types
`sup_usertypes`  | ["master", "unrestricted"] | List of supported user types

#### Examples

```json
{
  "serv": "user_code",
  "type": "cmd.usercode.set",
  "val_t": "str_map",
  "val": {
    "slot": "25",
    "id_type": "pin",
    "user_id": "1",
    "user_status": "enabled",
    "code": "2334",
    "alias": "Jonny"
  },
  "ver": "1",
  "props": null,
  "tags": null
}
{
  "serv": "user_code",
  "type": "cmd.usercode.clear",
  "val_t": "str_map",
  "val": {
    "id_type": "pin",
    "slot": "1"
  },
  "ver": "1",
  "props": null,
  "tags": null
}
{
  "serv": "user_code",
  "type": "evt.usercode.users_report",
  "val_t": "object",
  "val": {
    "pin": [
      {
        "slot": 1,
        "alias": "Jonny",
        "created_at": "2020-12-30T15:42:54.593324971+01:00"
      },
     ]
  },
  "ver": "1",
  "props": null,
  "tags": null
}

```