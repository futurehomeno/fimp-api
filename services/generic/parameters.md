# Parameters Service

Parameters service represents configuration of a device.

## Service name

`parameters`

## Interfaces

| Type | Interface                 | Value type | Description                                                                           |
|------|---------------------------|------------|---------------------------------------------------------------------------------------|
| in   | cmd.sup_params.get_report | null       | Requests information about known parameters.                                          |
| out  | evt.sup_params.report     | object     | Reports known parameters of the device, array of [`sup_parameter`](#definitions).     |
| in   | cmd.param.set             | object     | Sets parameter, see [`parameter_value`](#definitions).                                |
| in   | cmd.param.get_report      | string     | Request report of current value for specified parameter.                              |
| out  | evt.param.report          | object     | Reports current value for specified parameter, see [`parameter_value`](#definitions). |

## Definitions

* `sup_parameter` is an object of the following structure:

| Field         | Type   | Example                                 | Description                                                                    |
|---------------|--------|-----------------------------------------|--------------------------------------------------------------------------------|
| parameter_id  | string | `"1"`                                   | Id of the parameter.                                                           |
| name          | string | `"Sensitivity of the PR sensor"`        | Name of the parameter.                                                         |
| description   | string | `""`                                    | Description of the parameter.                                                  |
| widget_type   | string | `"select"`                              | Format of the parameter, one of [`widget_type`](#definitions).                 |
| value_type    | string | `"int"`                                 | Type of the value.                                                             |
| options       | object | `[{"label":"Option 1", "value": 1}]`    | Only for `select` and `multiselect`. Array of [`select_option`](#definitions). |
| min           | int    | `-1`                                    | Only for `input`. Minimum possible value of the parameter.                     |
| max           | int    | `20`                                    | Only for `input`. Maximum possible value of the parameter.                     |
| default_value | object | `{"value_type": "int", "int_value": 1}` | Value, see ['value`](#definitions).                                            |
| read_only     | bool   | `false`                                 | If true - value cannot be set.                                                 |

* `widget_type` can be one of:
  * `input` - input a number,
  * `select` - select one item from supported options,
  * `multiselect` - select multiple items from supported options.

* `value` is an object of the following structure:

| Field           | Type      | Example  | Description                                 |
|-----------------|-----------|----------|---------------------------------------------|
| value_type      | string    | `"int"`  | Value type.                                 |
| int_value       | int       | `1`      | Only if `value_type` is `int`. Value.       | 
| int_array_value | int_array | `[1, 3]` | Only if `value_type` is `int_array`. Value. | 

* `select_option` is an object of the following structure:

| Field | Type   | Example                                 | Description                         |
|-------|--------|-----------------------------------------|-------------------------------------|
| label | string | `"Option 1"`                            | Label of the option.                |
| value | object | `{"value_type": "int", "int_value": 1}` | Value, see ['value`](#definitions). |

* `parameter_value` is an object of the following structure:

| Field        | Type      | Example                                 | Description                         |
|--------------|-----------|-----------------------------------------|-------------------------------------|
| parameter_id | string    | `"1"`                                   | Id of the parameter.                |
| value        | object    | `{"value_type": "int", "int_value": 1}` | Value, see ['value`](#definitions). |

## Examples
