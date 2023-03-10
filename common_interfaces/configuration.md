# Configuration

It is recommended that for every configuration parameter an application or adapter provides a respective:

* getter interface following the pattern `cmd.config.get_{PARAMETER}`,
* setter interface following the pattern `cmd.config.set_{PARAMETER}` if the parameter is not read-only,
* report interface following the pattern `evt.config.{PARAMETER}_report`.

An application or adapter may also provide a convenience getter and report interfaces for all configuration parameters returned at once in a single object.

## Service name

An application or adapter may bundle all configuration related interfaces under a dedicated `config` service.
However, it may also attach them to a specific service, especially if it hosts multiple services with their own dedicated configurations.

## Interfaces

| Type | Interface                     | Value type | Description                                              |
|------|-------------------------------|------------|----------------------------------------------------------|
| in   | cmd.config.set_{PARAMETER}    | any        | Sets {PARAMETER} to the provided value.                  |
| in   | cmd.config.get_{PARAMETER}    | null       | Requests the currently set value of {PARAMETER}.         |
| out  | evt.config.{PARAMETER}_report | any        | Reports the currently set value of {PARAMETER}.          |
| in   | cmd.config.get_report         | null       | Request all configuration parameters in a single object. |
| out  | evt.config.report             | object     | Reports all configuration parameters in a single object. |

## Examples

* Example of a command setting an option `delivery_area` to `NO1` value:

```json
{
  "serv": "energy_price",
  "type": "cmd.config.set_delivery_area",
  "val_t": "string",
  "val": "NO1",
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2022-11-22T23:14:40+0100",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:app/rn:energy_guard/ad:1"
}
```

* Example of a command requesting value of a parameter `delivery_area`:

```json
{
  "serv": "energy_price",
  "type": "cmd.config.get_delivery_area",
  "val_t": "null",
  "val": null,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2022-11-22T23:14:40+0100",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:app/rn:energy_guard/ad:1"
}
```

* Example of a report of value of a parameter `delivery_area`:

```json
{
  "serv": "energy_price",
  "type": "evt.config.delivery_area_report",
  "val_t": "string",
  "val": "NO5",
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2022-11-22T23:14:40+0100",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:evt/rt:app/rn:energy_guard/ad:1"
}
```
