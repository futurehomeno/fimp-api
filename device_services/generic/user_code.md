# User Code Service

User code service is used by door locks, keypads and other security panels to enter and manage pin codes and RFIDs.

> Please note that this service is subject to minor backwards-incompatible changes in the future required to better align Zigbee and Z-Wave implementations.

## Service name

`user_code`

| Type | Interface                  | Value type | Storage     | Aggregation | Description                                                                                                                                 |
|------|----------------------------|------------|-------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.usercode.clear         | str_map    |             |             | Clears a single user slot. See [`clear_request`](#definitions) definition for more information.                                             |
| in   | cmd.usercode.clear_all     | null       |             |             | Clears all slots.                                                                                                                           |
| in   | cmd.usercode.get           | str_map    |             |             | Requests listing of all users.                                                                                                              |
| in   | cmd.usercode.set           | str_map    |             |             | Creates a new user. See [`user`](#definitions) string map definition for more information.                                                  |
| out  | evt.usercode.users_report  | object     | `skip`      |             | Lists all users as a mapping of [`slot`](#definitions) object array to identification types. See [example](#user-listing) for more details. |
| out  | evt.usercode.config_report | str_map    | `skip`      |             | Confirms the success of a set or a clear command. See [`config_report`](#definitions) definition for more details.                          |
| out  | evt.usercode.access_report | str_map    | `aggregate` | `event`     | Notifies about access attempt. See [`access_report`](#definitions) definition for more details.                                             |

> Please note that for backwards compatibility `evt.usercode.users_report` is sent with static `"users"` storage sub-value. Consult the [example](#user-listing) for more details.

## Service properties

| Name              | Type      | Example                 | Description                                                                         |
|-------------------|-----------|-------------------------|-------------------------------------------------------------------------------------|
| `sup_usercodes`   | str_array | ["pin", "rfid"]         | List of supported user code types. Possible values are: `pin`, `rfid`.              |
| `sup_userstatus`  | str_array | ["enabled", "disabled"] | List of supported user status types. Possible values are: `enabled` and `disabled`. |
| `sup_usertypes`   | str_array | ["normal", "master"]    | List of supported user types. Possible values are: `normal` and `master`.           |
| `sup_users`       | int       | `10`                    | Number of supported user slots.                                                     |
| `min_code_length` | int       | `4`                     | Minimum length of a user code.                                                      |
| `max_code_length` | int       | `4`                     | Maximum length of a user code.                                                      |

## Definitions

* `user` is a string map with the following structure:

| Field       | Example       | Description                                                                                          |
|-------------|---------------|------------------------------------------------------------------------------------------------------|
| id_type     | `"pin"`       | One of the identification types declared in [`sup_usercodes`](#service-properties) property.         |
| slot        | `"3"`         | Slot used for the user, must be within range defined in [`sup_users`](#service-properties) property. |
| alias       | `"Jon"`       | User alias or a display name.                                                                        |
| code        | `"1234"`      | User authentication code such as PIN.                                                                |
| user_id     | `"987654321"` | An optional custom user identification.                                                              |
| user_status | `"enabled"`   | An option user status declared in [`sup_userstatus`](#service-properties) property.                  |
| user_type   | `"normal"`    | An option user type declared in [`sup_usertypes`](#service-properties) property.                     |

* `slot` is an object with the following structure:

| Field      | Type   | Example                                 | Description                                       |
|------------|--------|-----------------------------------------|---------------------------------------------------|
| slot       | int    | `3`                                     | Slot used for the user.                           |
| alias      | string | `"Jon"`                                 | User alias or display name.                       |
| userId     | string | `"987654321"`                           | An optional custom user identification.           |
| created_at | string | `"2022-11-30T15:42:54.593324971+01:00"` | An optional user creation time in RFC3339 format. |

* `clear_request` is a string map with the following structure:

| Field       | Example       | Description                                                                                          |
|-------------|---------------|------------------------------------------------------------------------------------------------------|
| id_type     | `"pin"`       | One of the identification types declared in [`sup_usercodes`](#service-properties) property.         |
| slot        | `"3"`         | Slot used for the user, must be within range defined in [`sup_users`](#service-properties) property. |

* `config_report` is a string map with the following structure:

| Field          | Example        | Description                                                                                            |
|----------------|----------------|--------------------------------------------------------------------------------------------------------|
| event          | `"code_added"` | One of the following values: `code_added`, `code_deleted`.                                             |
| slot           | `"3"`          | Slot used for the user, must be within range defined in [`sup_users`](#service-properties) property.   |
| alias          | `"Jon"`        | User alias or a display name.                                                                          |
| identification | `"pin"`        | One of the supported identification types declared in [`sup_usercodes`](#service-properties) property. |

* `access_report` is a string map with the following structure:

| Field          | Example      | Description                                                                                            |
|----------------|--------------|--------------------------------------------------------------------------------------------------------|
| event          | `"unlocked"` | One of the following values: `locked`, `unlocked`, `unauthorized`.                                     |
| permission     | `"granted"`  | One of the following values: `granted`, `denied`.                                                      |
| identification | `"pin"`      | One of the supported identification types declared in [`sup_usercodes`](#service-properties) property. |
| alias          | `"Jon"`      | User alias or a display name if it is known.                                                           |

## Examples

### User creation

* Example of a command adding a new user `Jon` with code `1234` to a slot `3` of `pin` authorization method:

```json
    {
  "serv": "user_code",
  "type": "cmd.usercode.set",
  "val_t": "str_map",
  "val": {
    "id_type": "pin",
    "slot": "3",
    "alias": "Jon",
    "code": "1234",
    "user_id": "987654321",
    "user_status": "enabled",
    "user_type": "normal"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:user_code/ad:110_0"
}
```

* Example of a response confirming the success of the command:

```json
{
  "serv": "user_code",
  "type": "evt.usercode.config_report",
  "val_t": "str_map",
  "val": {
    "event": "code_added",
    "slot": "3",
    "alias": "Jon",
    "identification": "pin"
  },
  "storage": {
    "strategy": "skip"
  },
  "props": {},
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "8630619b-a5f3-438e-8868-acd66a7b81de",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:user_code/ad:110_0"
}
```

### User deletion

* Example of a command deleting a user from a slot `3` for `pin` authorization method:

```json
{
  "serv": "user_code",
  "type": "cmd.usercode.clear",
  "val_t": "str_map",
  "val": {
    "id_type": "pin",
    "slot": "3"
  },
  "props": {},
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "fa7fe4c1-a0bf-4bd5-a5ea-27c4f8be03da",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:user_code/ad:110_0"
}
```

* Example of a response confirming the success of the command:

```json
{
  "serv": "user_code",
  "type": "evt.usercode.config_report",
  "val_t": "str_map",
  "val": {
    "event": "code_deleted",
    "slot": "3",
    "alias": "Jon",
    "identification": "pin"
  },
  "storage": {
    "strategy": "skip"
  },
  "props": {},
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "b25dc2dc-a693-4184-8f3c-9476eb557bc5",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:user_code/ad:110_0"
}
```

### User listing

* Example of a command listing all users:

```json
{
  "serv": "user_code",
  "type": "cmd.usercode.get",
  "val_t": "str_map",
  "val": {},
  "props": {},
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "e0d1ef19-b65d-4c29-b173-2b1b0141fa13",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:user_code/ad:110_0"
}
```

* Example of a response listing all users:

```json
{
  "serv": "user_code",
  "type": "evt.usercode.users_report",
  "val_t": "object",
  "val": {
    "pin": [
      {
        "slot": 3,
        "alias": "Jon",
        "userId": "987654321",
        "created_at": "2022-11-30T15:42:54.593324971+01:00"
      }
    ]
  },
  "storage": {
    "strategy": "skip"
  },
  "props": {},
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "961d2024-0d85-43ae-82e8-dd93085aaf78",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:user_code/ad:110_0"
}
```

### Access reports

* Example of an access report event when door is unlocked by using a valid PIN:

```json
{
  "serv": "user_code",
  "type": "evt.usercode.access_report",
  "val_t": "str_map",
  "val": {
    "event": "unlocked",
    "alias": "Jon",
    "identification": "pin",
    "permission": "granted"
  },
  "storage": {
    "strategy": "aggregate",
    "sub_value": "unlocked"
  },
  "props": {},
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "961d2024-0d85-43ae-82e8-dd93085aaf78",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:user_code/ad:110_0"
}
```

* Example of an access report event when door is locked by using a valid PIN:

```json
{
  "serv": "user_code",
  "type": "evt.usercode.access_report",
  "val_t": "str_map",
  "val": {
    "event": "locked",
    "alias": "Jon",
    "identification": "pin",
    "permission": "granted"
  },
  "storage": {
    "strategy": "aggregate",
    "sub_value": "locked"
  },
  "props": {},
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "961d2024-0d85-43ae-82e8-dd93085aaf78",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:user_code/ad:110_0"
}
```

* Example of an access report event when door is unsuccessfully accessed using invalid PIN:

```json
{
  "serv": "user_code",
  "type": "evt.usercode.access_report",
  "val_t": "str_map",
  "val": {
    "event": "unauthorized",
    "identification": "pin",
    "permission": "denied"
  },
  "storage": {
    "strategy": "aggregate",
    "sub_value": "unauthorized"
  },
  "props": {},
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "961d2024-0d85-43ae-82e8-dd93085aaf78",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:user_code/ad:110_0"
}
```