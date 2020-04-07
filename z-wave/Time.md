# Time and Time Parameters CC
The Time Command Class, version1 is used to read date and time from a supporting node in a Z-Wave network. Users can get time and date repors separately.

*NOTE: Time report contains RTC failure field. True (1) indicates that RTC chip in failure. This might be a HW fault (batterz or oscilator/crytal). Time might be inaccurate in this case.*

## Time
```json
pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:time/ad:6_0
{
  "serv": "time",
  "type": "cmd.time.get_report",
  "val_t": "null",
  "val": null,
  "props": null,
  "tags": null,
  "src": "tplex-ui",
  "ver": "1",
  "uid": "8285a97d-5629-429a-9d67-87d17e648d3a"
}
```
Response

```json
pt:j1/mt:evt/rt:ad/rn:zw/ad:6
{
  "ctime": "2020-04-02T11:23:29+0200",
  "props": {},
  "serv": "time",
  "tags": [],
  "type": "evt.time.report",
  "val": {
    "hour": 11,
    "minute": 23,
    "rtc_fail": 0,
    "second": 29
  },
  "val_t": "object"
}
```

## Date
Get current date
```json
{
  "serv": "time",
  "type": "cmd.date.get_report",
  "val_t": "null",
  "val": null,
  "props": null,
  "tags": null,
  "src": "tplex-ui",
  "ver": "1",
  "uid": "8285a97d-5629-429a-9d67-87d17e648d3a"
}
```
response

```json
{
  "ctime": "2020-04-02T14:01:26+0200",
  "props": {},
  "serv": "time",
  "tags": [],
  "type": "evt.date.report",
  "val": {
    "day": 2,
    "month": 4,
    "year": 2020
  },
  "val_t": "object"
}```


# Time parameters
## Get currently set parameters
```json
{
  "serv": "time_parameters",
  "type": "cmd.time_parameters.get",
  "val_t": "null",
  "val": null,
  "props": null,
  "tags": null,
  "src": "tplex-ui",
  "ver": "1",
  "uid": "8285a97d-5629-429a-9d67-87d17e648d3a"
}
```
Response
```json
{
  "ctime": "2020-04-02T14:01:26+0200",
  "props": {},
  "serv": "time",
  "tags": [],
  "type": "evt.date.report",
  "val": {
    "day": 2,
    "month": 4,
    "year": 2020
  },
  "val_t": "object"
}```


##Setting the parameters
 - Year (8 bits) - A value from 0 to 99 that represents the 2 year in the century.
 - Month (8 bits) - A value from 1 to 12 that represents the month in a year.
 - Day (8 bits) - A value from 1 to 31 that represents the date of the month.
 - Hour (8 bits) - A value from 0 to 23 representing the starting hour.
 - Minute (8 bits) -A value from 0 to 59 representing the starting minute.
 - Seconds (8 bits) -A value from 0 to 59 representing the starting second.

Please be advised that message will be delivered with a delay of minimium one second and max 8 in a big networks.

```json
{
  "serv": "time_parameters",
  "type": "cmd.time_parameters.set",
  "val_t": "null",
  "val": {
    "year": 20,
    "month": 1,
    "day": 21,
    "hour": 17,
    "minute": 1,
    "second": 23
  },
  "val_t": "int_map",
  "props": null,
  "tags": null,
  "src": "tplex-ui",
  "ver": "1",
  "uid": "8285a97d-5629-429a-9d67-87d17e648d3a"
}
```