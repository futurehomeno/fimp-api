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

| Field        | Type   | Example                              | Description                                                                   |
|--------------|--------|--------------------------------------|-------------------------------------------------------------------------------|
| parameter_id | string | `"1"`                                | Id of the parameter.                                                          |
| name         | string | `"Sensitivity of the PR sensor"`     | Name of the parameter.                                                        |
| description  | string | `""`                                 | Description of the parameter.                                                 |
| widget_type  | string | `"select"`                           | Format of the parameter, one of [`widget_type`](#definitions).                |
| value_type   | string | `"int"`                              | Type of the value.                                                            |
| options      | object | `[{"label":"Option 1", "value": 1}]` | Only for`select` and `multiselect`. Array of [`select_option`](#definitions). |
| min          | int    | `-1`                                 | Only for `input`. Minimum possible value of the parameter.                    |
| max          | int    | `20`                                 | Only for `input`. Maximum possible value of the parameter.                    |
| default      | int    | `1`                                  | Default value of the parameter.                                               |
| read_only    | bool   | `false`                              | If true - value cannot be set.                                                |

* `widget_type` can be one of:
  * `input` - input a number,
  * `select` - select one item from supported options,
  * `multiselect` - select multiple items from supported options.
  
* `select_option` is an object of the following structure:

| Field | Type   | Example      | Description          |
|-------|--------|--------------|----------------------|
| label | string | `"Option 1"` | Label of the option. |
| value | int    | `1`          | Value of the option. | 

* `parameter_value` is an object of the following structure:

| Field        | Type                  | Example | Description                                                                                              |
|--------------|-----------------------|---------|----------------------------------------------------------------------------------------------------------|
| parameter_id | string                | `"1"`   | Id of the parameter.                                                                                     |
| value_type   | string                | `"int"` | Type of the value. Can be either`"int"` (for `input` and `select`) or `"int_array"` (for `multiselect`). |
| value        | based on value_type   | `1`     | Value of the parameter.                                                                                  |

## Examples
