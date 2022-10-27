# Basic Service

A generic service allowing to interact with an actuator of a device. 
If a device supports an actuator that is not supported by the adapter, then the basic service might be used to provide a partial functionality of this unsupported actuator.

> Please note that basic service is required by Z-Wave specification and serves as a fallback service for devices that are not yet supported by the adapter in order to maintain
> a rudimentary forward-compatibility. As such this service should not be implemented outside of Z-Wave. Other adapters should use only dedicated services instead.

## Service name

`basic`

## Interfaces

| Type | Interface          | Value type | Description                                  |
|------|--------------------|------------|----------------------------------------------|
| in   | cmd.lvl.get_report | null       | Requests report of the set level.            |
| in   | cmd.lvl.set        | int        | Sets the level using a numeric value.        |
| out  | evt.lvl.report     | int        | Reports the set level using a numeric value. |

## Examples

* Example of a report request command:

```json
{
  "serv": "basic",
  "type": "cmd.lvl.get_report",
  "val_t": "null",
  "val": null,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:basic/ad:11_0"
}
```

* Example of a level report:

```json
{
  "serv": "basic",
  "type": "evt.lvl.report",
  "val_t": "int",
  "val": 0,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "3cd089e1-a453-4410-9ce5-b3aa61ae443f",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:basic/ad:11_0"
}
```

