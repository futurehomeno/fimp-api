# System related device service

System service is provides a set of optional interfaces for device management.

## Service names

`dev_sys`

## Interfaces

| Type | Interface                  | Value type | Description                                                                                                                                                                           |
|------|----------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.thing.reboot           | bool       | Requests device to reboot. If value is `true` the reboot should omit graceful shutdown procedure if device supports it.                                                               |                                
| -    |                            |            |                                                                                                                                                                                       |
| in   | cmd.config.get_report      | str_array  | **Deprecated** Use `parameters` service instead. Requests service to respond with config report. If array is empty it should report all parameters.                                   |
| in   | cmd.config.set             | str_map    | **Deprecated** Use `parameters` service instead. Sets configuration. Value is a map of key-value pairs. Configuration values should be in form `<value>;<size>`, for instance `12;2`. |
| out  | evt.config.report          | str_map    | **Deprecated** Use `parameters` service instead. Reports configurations in form of key-value pairs.                                                                                   |
| -    |                            |            |                                                                                                                                                                                       |
| in   | cmd.group.add_members      | object     | **Deprecated** Use `association` service instead. Adds members to the group. Object has the same format as members report.                                                            |
| in   | cmd.group.delete_members   | object     | **Deprecated** Use `association` service instead. Removes members from the group. Object has the same format as members report.                                                       |
| in   | cmd.group.get_members      | string     | **Deprecated** Use `association` service instead. Requests report with members for a provided group.                                                                                  |
| out  | evt.group.members_report   | object     | **Deprecated** Use `association` service instead. Reports members of a group, e.g.: `{"group":"3", "members":["10_0", "11_2"]}`.                                                      |
| -    |                            |            |                                                                                                                                                                                       |
| in   | cmd.node_block.set         | str_map    | Blocks device from now for the provided number of hours, e.g.: `{"period_hours": "1"}`.                                                                                               |
| in   | cmd.node_block.get         | null       | Requests node block status.                                                                                                                                                           |
| out  | evt.node_block.report      | str_map    | Reports node block status, e.g.: `{"expire_at":"2020-11-09T10:28:34Z", "isBlocked" : "true"}`.                                                                                        |
| -    |                            |            |                                                                                                                                                                                       |
| in   | cmd.wuptimer.get           | null       | Requests wake-up timer setting.                                                                                                                                                       |
| in   | cmd.wuptimer.set           | str_map    | Sets up wake-up timer setting, e.g. `{"interval":"3600"}`. Interval is in seconds. Minimum and maximum values are device specific.                                                    |
| out  | evt.wuptimer.config_report | str_map    | Reports the current wake-up timer configuration, e.g.: `{"current": 4200, "default": 86400, "interval": 60, "maximum": 86400, "minimum": 1800}`.                                      |
| -    |                            |            |                                                                                                                                                                                       |
| in   | cmd.channel.get            | null       | Requests the current Zigbee channel.                                                                                                                                                  |
| out  | evt.channel.report         | int        | Reports the current Zigbee channel. The value is 0 if the network has not been established yet.                                                                                       |

