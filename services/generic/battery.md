### Battery service

#### Service names

`battery`

#### Interfaces

Type | Interface          | Value type | Properties | Description
-----|--------------------|------------|----------- |------------------
in   | cmd.lvl.get_report | null       |            | Get battery level over level report.
out  | evt.lvl.report     | int        | state      |
-|||
out  | evt.alarm.report   | str_map    |            | val = {"event": "low_battery", "status": "activ"}
-|||
in   | cmd.health.get_report| null     |            | Request battery health report
out  | evt.health.report  | int        |            | Battery health in %
in   | cmd.sensor.get_report | string  |            | Request battery temperature report in celsius.
out  | evt.sensor.report  | float      | unit       | Battery temperature in celsius.
-|||
in   | cmd.battery.get_report | null |              | Get full battery report
out  | evt.battery.report | object |                | Battery full report


Battery report object example :

```javascript

{
   "lvl": 90 ,
   "health" : 70,
   "state" : "charging",
   "temp_sensor" : 40,
}

```



#### Interface props

Name    | Value example | Description
--------|---------------|-------------
`state` | "charging"    | available states: charging, charged, replace, emtpy , idle