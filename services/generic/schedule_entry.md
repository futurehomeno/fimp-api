# Schedule Entry Service

This service handles a schedule slot for a user who already has valid user access code defined in [user_code](/services/generic/user_code.md) service.
A schedule entry for a user defines time when he can access the device using his authorization method.
If no schedule entries are defined for a user he can access the device at any time.
This service relies on `time` and `time_parameters` services to be present in the device.

> Please note that this service is subject to backwards-incompatible changes required to properly support different types of schedules.

## Service name

`schedule_entry`

## Interfaces

| Type | Interface                     | Value type | Storage        | Description                                                                                                                        |
|------|-------------------------------|------------|----------------|------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.schedule_entry.get_report | int_map    |                | Gets the schedule entry report for the specified slot. See [`schedule_slot`](#definitions) definition for more information.        |
| in   | cmd.schedule_entry.set        | int_map    |                | Sets the schedule entry for the specified slot. See [`year_day_schedule`](#definitions) definition for more information.           |
| in   | cmd.schedule_entry.clear      | int_map    |                | Clears the schedule entry for the specified slot. See [`schedule_slot`](#definitions) definition for more information.             |
| out  | evt.schedule_entry.report     | int_map    | `user_id:slot` | Reports the schedule entry report for the specified slot. See [`year_day_schedule`](#definitions) definition for more information. |

## Service properties

| Name    | Type      | Example | Description                             |
|---------|-----------|---------|-----------------------------------------|
| `slots` | int       | `2`     | Number of slots for schedules per user. |

## Definitions

* `year_day_schedule` is an int map with the following structure:

| Field        | Example | Description                                                                                                      |
|--------------|---------|------------------------------------------------------------------------------------------------------------------|
| slot         | 1       | Number of the schedule slot of the user. Must be between 1 and value in [`slots`](#service-properties) property. |
| user_id      | 1       | Number of the user slot as defined in the [`user_code`](/services/generic/user_code.md) service.                 |
| year_start   | 20      | Value from 0 to 99 that represents the year in the century. Value should be skipped if slot is empty.            |
| month_start  | 1       | Value from 1 to 12 that represents the month in a year. Value should be skipped if slot is empty.                |
| day_start    | 1       | Value from 1 to 31 that represents the date of the month. Value should be skipped if slot is empty.              |
| hour_start   | 7       | Value from 0 to 23 representing the starting hour. Value should be skipped if slot is empty.                     |
| minute_start | 30      | Value from 0 to 59 representing the starting minute. Value should be skipped if slot is empty.                   |
| year_end     | 25      | Value from 0 to 99 that represents the year in the century. Value should be skipped if slot is empty.            |
| month_end    | 12      | Value from 1 to 12 that represents the month in a year. Value should be skipped if slot is empty.                |
| day_end      | 31      | Value from 1 to 31 that represents the date of the month. Value should be skipped if slot is empty.              |
| hour_end     | 18      | Value from 0 to 23 representing the starting hour. Value should be skipped if slot is empty.                     |
| minute_end   | 30      | Value from 0 to 59 representing the starting minute. Value should be skipped if slot is empty.                   |

> Please note that all start values must be lower than all end value.

* `schdule_slot` is an int map with the following structure:

| Field        | Example | Description                                                                                                      |
|--------------|---------|------------------------------------------------------------------------------------------------------------------|
| slot         | 1       | Number of the schedule slot of the user. Must be between 1 and value in [`slots`](#service-properties) property. |
| user_id      | 1       | Number of the user slot as defined in the [`user_code`](/services/generic/user_code.md) service.                 |

## Examples

* Example of a command setting a schedule entry for user `1` at slot `1` between `2020-01-01 7:30` to `2025-12-31 18:30`:

```json
{
  "serv": "schedule_entry",
  "type": "cmd.schedule_entry.set",
  "val_t": "int_map",
  "val": {
    "slot": 1,
    "user_id": 1,
    "year_start": 20,
    "month_start": 1,
    "day_start": 1,
    "hour_start": 7,
    "minute_start": 30,
    "year_end": 25,
    "month_end": 12,
    "day_end": 31,
    "hour_end": 18,
    "minute_end": 30
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:schedule_entry/ad:110_0"
}
```

* Example of a command clearing a schedule entry for user `1` at slot `1`:

```json
{
  "serv": "schedule_entry",
  "type": "cmd.schedule_entry.clear",
  "val_t": "int_map",
  "val": {
    "slot": 1,
    "user_id": 1
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:schedule_entry/ad:110_0"
}
```

* Example of a command getting a schedule entry for user `1` at slot `1`:

```json
{
  "serv": "schedule_entry",
  "type": "cmd.schedule_entry.get_report",
  "val_t": "int_map",
  "val": {
    "slot": 1,
    "user_id": 1
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:schedule_entry/ad:110_0"
}
```

* Example of a message reporting the schedule entry for the specified slot:

```json
{
  "serv": "schedule_entry",
  "type": "cmd.schedule_entry.report",
  "val_t": "int_map",
  "val": {
    "slot": 1,
    "user_id": 1,
    "year_start": 20,
    "month_start": 1,
    "day_start": 1,
    "hour_start": 7,
    "minute_start": 30,
    "year_end": 25,
    "month_end": 12,
    "day_end": 31,
    "hour_end": 18,
    "minute_end": 30
  },
  "storage": {
    "sub_value": "1:1"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:schedule_entry/ad:110_0"
}
```