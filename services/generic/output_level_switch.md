### Output level switch service

Used for dimmers and things generally controlled with sliders.

#### Service names

`out_lvl_switch`

#### Interfaces

Type | Interface          | Value type | Properties              | Description
-----|--------------------|------------|-------------------------|------------
in   | cmd.binary.set     | bool       |                         | True should result in setting last known non-zero level or fallback to maximum.
out  | evt.binary.report  | bool       |                         | Deprecated. Service should use `evt.lvl.report` instead.
-|||
in   | cmd.lvl.get_report | null       |                         |
in   | cmd.lvl.set        | int        | `duration`              |
in   | cmd.lvl.start      | string     | `start_lvl`, `duration` | Supported values are `up` and `down`.
in   | cmd.lvl.stop       | null       |                         | Stop a level change.
out  | evt.lvl.report     | int        |                         |

#### Interface props

Name        | Value example | Description
------------|---------------|-------------
`duration`  | "10"          | Duration in seconds. Factory default is used if no value is provided.
`start_lvl` | "50"          | Level change direction. Supported values are integers from `min_lvl` to `max_lvl`.

#### Service props

Name      | Value example | Description
----------|---------------|-------------
`max_lvl` | 99            | A maximum supported value.
`min_lvl` | 0             | A minimum supported value.
`sw_type` | "on_off"      | A type of level switch. Supported values are `on_off` or `up_down`.