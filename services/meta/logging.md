### Logging interfaces

#### Service name

Command can belong to any service of any application or adapter.

#### Interfaces

Type | Interface             | Value type | Properties | Description
-----|-----------------------|------------|------------|--------------
in   | cmd.log.set_level     | string     |            |
in   | cmd.log.get_level     | null       |            |
out  | evt.log.level_report  | string     |            |

Supported log level : `trace`,`debug`,`info`,`warn`,`error`