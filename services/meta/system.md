# System related device service

## Service names

`dev_sys`

## Interfaces

Type | Interface                   | Value type | Description
-----|---------------------------- |------------|------------
in   | cmd.config.get_report       | str_array  | Requests service to respond with config report. If array is empty - report all parameters.
in   | cmd.config.set              | str_map    | Sets configuration. Value is a key-value pairs.
in   | cmd.thing.reboot            | string     | Requests device to run either complete reboot or reboot specific component.
out  | evt.config.report           | str_map    | Reports configurations in form of key-value pairs.
-|||
in   | cmd.group.add_members       | object     | Adds members to the group. Object has the same format as members_report
in   | cmd.group.delete_members    | object     | Object has the same format as report.
in   | cmd.group.get_members       | string     | Value is a group name.
out  | evt.group.members_report    | object     | Object structure `{"group":"group1", "members":["node1", "node2"]}`
-|||
in   | cmd.node_block.set          | str_map    | Value: `{"period_hours": "1"}`, device will be blocked from now + 1h
in   | cmd.node_block.get          | str_map    | Value example `{"expire_at":"2020-11-09T10:28:34Z", "isBlocked" : "true"}`.  Time is in local timezone.
out  | evt.node_block.report"      | str_map    | Value example `{"expire_at":"2020-11-09T10:28:34Z"}`. Time is in local timezone.
-|||
in   | cmd.wuptimer.get            | null       |
in   | cmd.wuptimer.set            | str_map    | Value example `{"interval":"3600"}`. Interval is in seconds. Min and Max are device specific values. Please refeer to device datasheet.
out  | evt.wuptimer.config_report  | str_map    | Value example `{"current": 4200, "default": 86400, "interval": 60, "maximum": 86400, "minimum": 1800}`
-|||
in   | cmd.node_reinterview        | str_map    | Value example `{"max_age":"1"}`. The maximum age of the NodeInfo frame, given in 2^n minutes. If the cache entry does not exist or if it is older than the value given in this field,  the ZIP will attempt to get a Fresh NodeInfo frame before responding to the Node Info Cached Get command. A value of 15 means infinite, i.e. No Cache Refresh.
-|||
in   | cmd.channel.get             | null    | Requests the current Zigbee channel.
out  | evt.channel.report          | int     | Reports the current Zigbee channel. The value is 0 if the network has not been established yet.

## Notes

- Z-Wave configuration values should be in form <value>;size, for instance 12;2
- Z-Wave association member should be in form <node_id>\_<endpoint_id>, for instance 10_0
