# Parameters Service

Parameters service allows for advanced configuration of a device. For a list of predefined parameters see [Predefined parameters](#predefined-parameters) section.

> Please note that this service is experimental and may be changed in the future.

## Service name

`parameters`

## Interfaces

| Type | Interface                 | Value type | Storage     | Aggregation    | Description                                                                                             |
|------|---------------------------|------------|-------------|----------------|---------------------------------------------------------------------------------------------------------|
| in   | cmd.sup_params.get_report | null       |             |                | Requests information about known parameters. Present if the device supports parameters discovery.       |
| out  | evt.sup_params.report     | object     |             |                | Reports known parameters of the device, contains an array of [`sup_parameter`](#definitions) objects.   |
| in   | cmd.param.set             | object     |             |                | Sets the parameter, see [`parameter_value`](#definitions).                                              |
| in   | cmd.param.get_report      | string     | `aggregate` | `parameter_id` | Requests report with currently set values for the specified parameter.                                  |
| out  | evt.param.report          | object     |             |                | Reports the current value for a specified parameter, contains [`parameter_value`](#definitions) object. |

> Some devices may not support parameter discovery while still supporting setting parameters manually if we know their ID and size.
> In such cases the service will not provide `cmd.sup_params.get_report` interface and require the user to provide the parameter ID and size manually.
> The list of supported parameters and their respective sizes can usually be found in the manual provided by the device producer.

## Service properties

| Name            | Type      | Example  | Description                                                                                                                                             |
|-----------------|-----------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| req_param_sizes | int_array | `[1, 2]` | Optional. Indicates that the device does not support parameter discovery and requires parameter size to be provided manually, when setting a parameter. |

## Definitions

* `sup_parameter` is an object with the following structure:

| Field         | Type   | Example                              | Description                                                                              |
|---------------|--------|--------------------------------------|------------------------------------------------------------------------------------------|
| parameter_id  | string | `"1"`                                | ID of the parameter.                                                                     |
| name          | string | `"Sensitivity of the PR sensor"`     | Optional name of the parameter.                                                          |
| description   | string | `""`                                 | Optional description of the parameter.                                                   |
| widget_type   | string | `"select"`                           | Format of the parameter, one of [`widget_type`](#definitions).                           |
| value_type    | string | `"int"`                              | Type of the value, one of [`value_type`](#definitions).                                  |
| options       | object | `[{"label":"Option 1", "value": 1}]` | Applies only to `select` and `multiselect`. Array of [`select_option`](#definitions).    |
| min           | int    | `-1`                                 | Applies only to `int` and `string` typed `input`. Minimum value/length of the parameter. |
| max           | int    | `20`                                 | Applies only to `int` and `string` typed `input`. Maximum value/length of the parameter. |
| default_value | any    | `1`                                  | Default value, the type is defined in `value_type` property.                             |
| read_only     | bool   | `false`                              | If true value cannot be set.                                                             |

* `widget_type` can be one of:
    * `input` - input a single value,
    * `select` - select one item from supported options,
    * `multiselect` - select multiple items from supported options.

* `value_type` can be one of `int`, `int_array`, `string`, `str_array`, `bool`.

* `select_option` is an object of the following structure:

| Field | Type   | Example      | Description                                                                                                                                                  |
|-------|--------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| label | string | `"Option 1"` | Optional label of the option.                                                                                                                                |
| value | any    | `1`          | Option value, the type is inferred from `value_type` property, e.g. for a multiselect property of the `int_array` type, the option value type must be `int`. |

* `parameter_value` is an object of the following structure:

| Field        | Type   | Example | Description                                                                                                                       |
|--------------|--------|---------|-----------------------------------------------------------------------------------------------------------------------------------|
| parameter_id | string | `"1"`   | ID of the parameter.                                                                                                              |
| value_type   | string | `"int"` | Type of the value, one of [`widget_type`](#definitions).                                                                          |
| value        | any    | `1`     | Value, the type is defined in `value_type` property.                                                                              |
| size         | int    | `2`     | Required only if [`req_param_sizes`](#service-properties) is set and parameter discovery is not available, and ignored otherwise. |

## Examples

* Example of message containing supported parameter specification:

```json 
{
  "serv": "parameters",
  "type": "evt.sup_params.report",
  "val_t": "object",
  "val": [
    {
      "parameter_id": "1",
      "name": "Example select parameter",
      "description": "Example long description of the parameter.",
      "value_type": "int",
      "widget_type": "select",
      "options": [
        {
          "label": "Example option 1",
          "value": 0
        },
        {
          "label": "Example option 2",
          "value": 1
        },
        {
          "label": "Example option 3",
          "value": 2
        }
      ],
      "default_value": 0,
      "read_only": false
    },
    {
      "parameter_id": "2",
      "name": "Example input parameter",
      "description": "Example long description of the parameter.",
      "value_type": "int",
      "widget_type": "input",
      "min": -5,
      "max": 5,
      "default_value": 0,
      "read_only": false
    }
  ],
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "961d2024-0d85-43ae-82e8-dd93085aaf78",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:parameters/ad:149_0"
}
```

* Example of message containing parameter value report:

```json
{
  "serv": "parameters",
  "type": "evt.param.report",
  "val_t": "object",
  "val": {
    "parameter_id": "2",
    "value_type": "int",
    "value": 3
  },
  "storage": {
    "strategy": "aggregate",
    "sub_value": "2"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "961d2024-0d85-43ae-82e8-dd93085aaf78",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:parameters/ad:149_0"
}
```

* Example of a command setting a parameter value when service does not support parameter discovery:

```json
{
  "serv": "parameters",
  "type": "cmd.param.set",
  "val_t": "object",
  "val": {
    "parameter_id": "3",
    "value_type": "int",
    "value": 53,
    "size": 4
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "961d2024-0d85-43ae-82e8-dd93085aaf78",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:parameters/ad:149_0"
}
```

## Predefined parameters

Parameters service is primarily intended to support vendor-specific configuration parameters that can vary for every device.
However, there are some predefined parameters which have a standardized meaning and are expected to have uniform implementation across devices which support them.

| Parameter ID          | Name                | Value Type | Requirements                              | Description                                                                                                                                                                                                                                      | 
|-----------------------|---------------------|------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `heat_control_mode`   | Heat control mode   | `string`   | `thermostat` or `power_regulator` service | Allows to switch heating control mode between thermostat and power <br/>regulator. Accepted values are `reg` for power regulator and `tht` for thermostat. Switch results in sending new inclusion report with requested device functionalities. |
| `cable_always_locked` | Cable always locked | `bool`     | `chargepoint` service                     | Allows to enforce charging cable to be always locked on the EVSE side to prevent theft.                                                                                                                                                          |
| `free_charging`       | Free charging       | `bool`     | `chargepoint` service                     | Determines whether chargepoint should automatically start charging an EV without an authorization or remote control trigger.                                                                                                                     |
| `led_brightness`      | LED brightness      | `int`      | `chargepoint` service                     | Allows to set the brightness of the LED ring on the chargepoint. Accepted values are defined by `min` and `max` properties of the parameter definition.                                                                                          |
