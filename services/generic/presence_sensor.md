### Presence sensor service

Motion sensor or some other way of presence detection.

#### Service names

`sensor_presence`

#### Interfaces

Type | Interface               | Value type | Description
-----|-------------------------|------------|--------------------
in   | cmd.presence.get_report | null       |
out  | evt.presence.report     | bool       | true = presence