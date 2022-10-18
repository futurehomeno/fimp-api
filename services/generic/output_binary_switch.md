### Output binary switch service

Output binary switch service for wall-plugs, relays, simple sirens, etc.

#### Service names

`out_bin_switch`

#### Interfaces

Type | Interface             | Value type | Description
-----|-----------------------|------------|------------
in   | cmd.binary.get_report | null       |
in   | cmd.binary.set        | bool       |
out  | evt.binary.report     | bool       | Reports true when switch is ON and false when switch is OFF