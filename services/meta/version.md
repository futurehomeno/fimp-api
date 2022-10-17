### Version service

Version service is exposing device hardware and software versions.

#### Service names

`version`

#### Interfaces

Type | Interface                     | Value type | Properties              | Description
-----|-------------------------------|------------|-------------------------|-------------
in   | cmd.version.get_report |  null     |  | get device software versions report
out  | evt.version.report   |  int_map  |  |[Extended version report](#extended-version-object)

#### Extended version report

All numbers are in decimal representation.

Name            | Value type   | Description
----------------|--------------|--------------
`firmware`      | string       | Firmware main version
`hardware`      | string       | Hardware version
`sdk_library`   | string       | SDK Library type (manufacturer internal)
`protocol`      | string       | Protocol version (Z-Wave)