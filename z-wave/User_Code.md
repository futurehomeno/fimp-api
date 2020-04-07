# User Code CC
### Administration
## Get Slot 1 user details
Topic: `pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:user_code/ad:9_0` 
```
{
 "ctime": "2019-04-30T10:42:45+0200",
 "props": {},
 "serv": "user_code",
 "tags": [],
 "type": "cmd.usercode.get",
 "val_t": "str_map",
 "val": {
  "slot":"1"
  }
}
```

Output:
```
{
  "ctime": "2019-09-04T09:42:32+0200",
  "props": {},
  "serv": "user_code",
  "tags": [],
  "type": "evt.usercode.config_report",
  "val": {
    "alias": "James LeBron",
    "slot": "7",
    "user_id": "1",
    "user_status": "enabled"
  },
  "val_t": "str_map"
}
```


## Setting code 1235 on Slot 1
Topic: `pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:user_code/ad:6_0` 
```
{
  "ctime": "2019-04-30T10:42:45+0200",
  "props": {},
  "serv": "user_code",
  "tags": [],
  "type": "cmd.usercode.set",
  "val_t": "str_map",
  "val": {
    "slot": "7",
    "user_id": "1",
    "id_type": "pin",
    "user_status": "enabled",
    "code": "1235",
    "alias": "LeBron James"
  }
}
 ```
Output as confirmation:
Topic : `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:user_code/ad:6_0`
Service : `user_code`
Interface : `evt.usercode.access_report`
 ```
{
  "ctime": "2019-09-04T10:00:05+0200",
  "props": {},
  "serv": "user_code",
  "tags": [],
  "type": "evt.usercode.access_report",
  "val": {
    "alias": "James LeBron",
    "event": "code_added",
    "identification": "pin",
    "slot": "7",
    "user_id": "1"
  },
  "val_t": "str_map"
}
 ```

## Clearing Slot 1
Topic: `pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:user_code/ad:6_0` 
```
{
  "ctime": "2019-04-30T10:42:45+0200",
  "props": {},
  "serv": "user_code",
  "tags": [],
  "type": "cmd.usercode.clear",
  "val_t": "str_map",
  "val": {
    "slot":"8"
  }
}
```

Output as confirmation:
Topic : `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:user_code/ad:6_0`
Service : `user_code`
Interface : `evt.usercode.access_report`
```
{
  "ctime": "2019-09-04T10:00:58+0200",
  "props": {},
  "serv": "user_code",
  "tags": [],
  "type": "evt.usercode.access_report",
  "val": {
    "alias": "James LeBron",
    "event": "code_deleted",
    "identification": "pin",
    "slot": "8",
    "user_id": "GUID-000-1234-QUERTY"
  },
  "val_t": "str_map"
}
```

## Clearing all codes
Topic: `pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:user_code/ad:6_0` 
```
{
  "ctime": "2019-04-30T10:42:45+0200",
  "props": {},
  "serv": "user_code",
  "tags": [],
  "type": "cmd.usercode.clearall",
  "val_t": "null"
}
```

Output as confirmation:
Topic : `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:user_code/ad:6_0`
Service : `user_code`
Interface : `evt.usercode.access_report`
```
{
  "ctime": "2019-09-04T09:52:15+0200",
  "props": {},
  "serv": "user_code",
  "tags": [],
  "type": "evt.usercode.access_report",
  "val": {
    "event": "code_all_deleted",
    "identification": "pin"
  },
  "val_t": "str_map"
}
```

## Events
User Code service supports events caused by user interaciton (using the indetification interface).

Topic : `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:user_code/ad:6_0`
Service : `user_code`
Interface : `evt.usercode.access_report`

### Access Granted 
Door is unlocked by using valid PIN
```
{
  "ctime": "2019-09-04T09:12:02+0200",
  "props": {},
  "serv": "user_code",
  "tags": [],
  "type": "evt.usercode.access_report",
  "val": {
    "alias": "James LeBron",
    "event": "unlocked",
    "identification": "pin",
    "permission": "granted",
    "id_type": "permanent"
  },
  "val_t": "str_map"
}
```

### Access Denied 
Access was denied by using invalid PIN code
```
{
  "ctime": "2019-09-04T09:12:02+0200",
  "props": {},
  "serv": "user_code",
  "tags": [],
  "type": "evt.usercode.access_report",
  "val": {
    "event": "unauthorized",
    "identification": "pin",
    "permission": "denied"
  },
  "val_t": "str_map"
}
```

### Doors locked
Door is locked by using valid PIN (not using autolock feature)
```
{
  "ctime": "2019-09-04T09:12:02+0200",
  "props": {},
  "serv": "user_code",
  "tags": [],
  "type": "evt.usercode.access_report",
  "val": {
    "alias": "James LeBron",
    "event": "locked",
    "identification": "pin",
    "permission":"granted",
    "id_type": "permanent"
  },
  "val_t": "str_map"
}
```

# Schedule Entry Lock
The Schedule Entry Lock Type Commands are for controlling the schedules of an Entry Lock
using schedule based user code Ids. 

## Prerequisites
Doorlock device must support following commands classes:

 - COMMAND_CLASS_SCHEDULE_ENTRY_LOCK_V3 
 - COMMAND_CLASS_TIME 
 - COMMAND_CLASS_TIME_PARAMETERS
 - USER_CODE

Operational rules/workflow:

 - Device MUST have time corrctly set to a local timezone.
 - Device MUST have added users (using user_code service) before assiging schedules
 - Application MUST clear both, user and schedule upon deleting.
 - Deleted schedule will enable full-time access for user which schedule was assigned to

## Schedule Entry Lock Set Command
This command sets or erases a schedule slot for a identified user who already has valid user access
code (ser_code service). The year day schedule represents two days, any time apart, where the specified user ID’s code is
valid. When setting the schedule slot, the start parameters of the time fence needs to occur prior to
the stop parameters and the year day schedule is automatically enabled for the identified user.

Note: Each user can only use one type of scheduling at a time.

FIMP command which set user 1 from user_code service to slot 1 with access granted from 21.1.2020 17:01 to 1.12.2023 23:59:

Use following topic while posting the message:

```pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:schedule_entry/ad:8_0```

```json
{
  "serv": "schedule_entry",
  "type": "cmd.schedule_entry.set",
  "val": {
    "slot": 1,
    "user_id": 1,
    "year_start": 20,
    "month_start": 1,
    "day_start": 21,
    "hour_start": 17,
    "minute_start": 1,
    "year_end": 23,
    "month_end": 12,
    "day_end": 1,
    "hour_end": 23,
    "minute_end": 59
  },
  "val_t": "int_map",
  "props": null,
  "tags": null,
  "src": "tplex-ui",
  "ver": "1",
  "uid": "64799021-ed78-4e37-9c08-80e06508bb25"
}
```
Parameters explained:

 - Schedule Slot ID (8 bits) - A value from 1 to Number of Slots Year Day Supported.    
 - Start/Stop Year (8 bits) - A value from 0 to 99 that represents the 2 year in the century.
 - Start/Stop Month (8 bits) - A value from 1 to 12 that represents the month in a year.
 - Start/Stop Day (8 bits) - A value from 1 to 31 that represents the date of the month.
 - Start/Stop Hour (8 bits) - A value from 0 to 23 representing the starting hour.
 - Start/Stop Minute (8 bits) -A value from 0 to 59 representing the starting minute.

## Schedule Entry Lock Get Command
This command gets a year/day schedule slot for an identified user and specified schedule slot ID.

Use following topic while posting the message:

```pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:schedule_entry/ad:8_0```

```json
{
  "serv": "schedule_entry",
  "type": "cmd.schedule_entry.get_report",
  "val": {
    "slot": 1,
    "user_id": 1
  },
  "val_t": "object",
  "props": null,
  "tags": null,
  "src": "tplex-ui",
  "ver": "1",
  "uid": "64799021-ed78-4e37-9c08-80e06508bb25"
}

If slot is found and it is valid reposne will be posted on following topic:

```json
{
  "ctime": "2020-04-01T13:50:55+0200",
  "props": {},
  "serv": "schedule_entry",
  "tags": [],
  "type": "evt.schedule_entry.report",
  "val": {
    "slot": 1,
    "user_id": 0
  },
  "val_t": "object"
}
```


If slot is erased/empty the fields will look like this:

```json
{
  "ctime": "2020-04-01T13:50:55+0200",
  "props": {},
  "serv": "schedule_entry",
  "tags": [],
  "type": "evt.schedule_entry.report",
  "val": {
    "slot": 1,
    "user_id": 0
  },
  "val_t": "object"
}
```

## Schedule Entry Lock Clear Command
This command will erase schedule slot for an identified user and specified schedule slot ID.

Use following topic while posting the message:

```pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:schedule_entry/ad:8_0```

```json
{
  "serv": "schedule_entry",
  "type": "cmd.schedule_entry.clear",
  "val": {
    "slot": 1,
    "user_id": 1
  },
  "val_t": "int_map",
  "props": null,
  "tags": null,
  "src": "tplex-ui",
  "ver": "1",
  "uid": "64799021-ed78-4e37-9c08-80e06508bb25"
}

To verify that slot was clear please issue get_report command.