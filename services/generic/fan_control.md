# Fan Control Service

The service is used to control a fan operational modes, speed and receive state updates.

> Please note that some fan devices might be supported in a limited way using [`thermostat`](/services/generic/thermostat.md) service.

## Service name

`fan_ctrl`

## Interfaces

| Type | Interface           | Value type | Description                                                                                |
|------|---------------------|------------|--------------------------------------------------------------------------------------------|
| in   | cmd.mode.get_report | null       | Requests the current fan mode.                                                             |
| in   | cmd.mode.set        | string     | Sets the fan mode to one of values defined in [`sup_modes`](#service-properties) property. |
| out  | evt.mode.report     | string     | Current fan mode                                                                           |

## Service properties

| Name         | Type      | Example           | Description                                                                             |
|--------------|-----------|-------------------|-----------------------------------------------------------------------------------------|
| `sup_modes`  | str_array | `["low", "high"]` | List of supported modes. Possible values are: `quiet`, `low`, `medium`, `high`, `auto`. |

## Examples

* Example of a command to set fan mode to `low`:

```json
    {
      "serv": "fan_ctrl",
      "type": "cmd.mode.set",
      "val_t": "string",
      "val": "low",
      "props": {},
      "tags": [],
      "src": "-",
      "ver": "1",
      "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
      "topic": "pt:j1/mt:cmd/rt:dev/rn:sensibo/ad:1/sv:fan_ctrl/ad:1"
    }
```