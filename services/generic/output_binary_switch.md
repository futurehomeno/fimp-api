# Output Binary Switch Service

Output binary switch service acts as an on/off switch for wall-plugs, relays, simple sirens and other similar devices.

## Service name

`out_bin_switch`

## Interfaces

| Type | Interface             | Value type | Description                                                                      |
|------|-----------------------|------------|----------------------------------------------------------------------------------|
| in   | cmd.binary.get_report | null       | Requests report of the binary state.                                             |
| in   | cmd.binary.set        | bool       | Sets the binary state.                                                           |
| out  | evt.binary.report     | bool       | Reports `true` when the switch is **on** and `false` when the switch is **off**. |