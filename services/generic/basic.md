### Basic service

A generic service and the most simple way to interact with a device. The actual meaning of "basic" varies from device to device.

#### Service names

`basic`

#### Interfaces

Type | Interface          | Value type | Description
-----|--------------------|------------|------------
in   | cmd.lvl.get_report | null       |
in   | cmd.lvl.set        | int        | Sets level using numeric value
out  | evt.lvl.report     | int        | Reports level using numeric value