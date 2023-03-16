# Logging

The following document describes a recommended common interface for configuration of logging by the application or adapter.

## Service name

And application or adapter may bundle all logging related interfaces under dedicated `log` service. However, it may also attach them to a specific service.

## Interfaces

| Type | Interface            | Value type | Description                                                                                      |
|------|----------------------|------------|--------------------------------------------------------------------------------------------------|
| in   | cmd.log.set_level    | string     | Sets the logging level, see [logging_level](#definitions) for possible values.                   |
| in   | cmd.log.get_level    | null       | Requests the currently set logging level, see [logging_level](#definitions) for possible values. |
| out  | evt.log.level_report | string     | Reports the currently set logging level, see [logging_level](#definitions) for possible values.  |

## Definitions

* `logging_level` is one of the following values: `trace`, `debug`, `info`, `warning`, `error`, `fatal`.

## Examples

* Example of a command setting a logging level to `debug`.

```json
{
  "serv": "energy_guard",
  "type": "cmd.log.set_level",
  "val_t": "string",
  "val": "debug",
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2022-11-22T23:14:40+0100",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:app/rn:energy_guard/ad:1"
}
```