### Siren service

#### Service names

`siren_ctrl`

#### Interfaces

Type | Interface           | Value type | Description
-----|---------------------|------------|------------
in   | cmd.mode.get_report | null       |
in   | cmd.mode.set        | string     | Control siren using selected tone
out  | evt.mode.report     | string     |

Topic example: `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:siren_ctrl/ad:15_0`

#### Service props

Name             | Value example       | Description
-----------------|---------------------|-------------
`sup_modes`      | on, off, fire, leak | List of supported tones