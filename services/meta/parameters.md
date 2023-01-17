# Parameters Service

Parameters service allows configuration of a device.

## Service name

`parameters`

## Interfaces

| Type | Interface                 | Value type | Description                                                                                                  |
|------|---------------------------|------------|--------------------------------------------------------------------------------------------------------------|
| in   | cmd.sup_params.get_report | null       | Requests information about known parameters.                                                                 |
| out  | evt.sup_params.report     | object     | Reports known parameters of the device, contains array of [`sup_parameter`](#definitions) objects.           |
| in   | cmd.param.set             | object     | Sets parameter, see [`parameter_value`](#definitions).                                                       |
| in   | cmd.param.get_report      | str_array  | Requests report with currently set values for specified parameters.                                          |
| out  | evt.param.report          | object     | Reports current value for specified parameters, contains array of [`parameter_value`](#definitions) objects. |


## Service properties

| Name      | Type      | Example | Description                                                |
|-----------|-----------|---------|------------------------------------------------------------|
| sup_sizes | int_array | `[1,2]` | Optional. Defines supported sizes of the parameter values. |

## Definitions

* `sup_parameter` is an object of the following structure:

| Field         | Type   | Example                                                                  | Description                                                                    |
|---------------|--------|--------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| parameter_id  | string | `"1"`                                                                    | ID of the parameter.                                                           |
| name          | string | `"Sensitivity of the PR sensor"`                                         | Name of the parameter.                                                         |
| description   | string | `""`                                                                     | Description of the parameter.                                                  |
| widget_type   | string | `"select"`                                                               | Format of the parameter, one of [`widget_type`](#definitions).                 |
| value_type    | string | `"int"`                                                                  | Type of the value.                                                             |
| options       | object | `[{"label":"Option 1", "value": {"value_type": "int", "int_value": 1}}]` | Only for `select` and `multiselect`. Array of [`select_option`](#definitions). |
| min           | int    | `-1`                                                                     | Only for `input`. Minimum possible value of the parameter.                     |
| max           | int    | `20`                                                                     | Only for `input`. Maximum possible value of the parameter.                     |
| default_value | object | `{"value_type": "int", "int_value": 1}`                                  | Default value, see [`value`](#definitions).                                    |
| read_only     | bool   | `false`                                                                  | If true value cannot be set.                                                   |

* `widget_type` can be one of:
    * `input` - input a single value,
    * `select` - select one item from supported options,
    * `multiselect` - select multiple items from supported options.

* `value` is an object with the following structure:

| Field           | Type      | Example  | Description                                |
|-----------------|-----------|----------|--------------------------------------------|
| value_type      | string    | `"int"`  | Value type.                                |
| int_value       | int       | `1`      | Only if `value_type` is `int` value.       | 
| int_array_value | int_array | `[1, 3]` | Only if `value_type` is `int_array` value. | 

* `select_option` is an object of the following structure:

| Field | Type   | Example                                 | Description                         |
|-------|--------|-----------------------------------------|-------------------------------------|
| label | string | `"Option 1"`                            | Label of the option.                |
| value | object | `{"value_type": "int", "int_value": 1}` | Value, see [`value`](#definitions). |

* `parameter_value` is an object of the following structure:

| Field        | Type   | Example                                 | Description                                                                          |
|--------------|--------|-----------------------------------------|--------------------------------------------------------------------------------------|
| parameter_id | string | `"1"`                                   | Id of the parameter.                                                                 |
| value        | object | `{"value_type": "int", "int_value": 1}` | Value, see [`value`](#definitions).                                                  |
| size         | int    | `"1"`                                   | Required only if [`sup_sizes`](#service-properties) is set. Size of parameter value. |

## Examples

* Example of `evt.sup_params.report`:

```json 
{
  "serv": "parameters",
  "type": "evt.sup_params.report",
  "val_t": "object",
  "val": [
    {
      "parameter_id": "2",
      "name": "LED alarm event reporting",
      "description": "",
      "value_type": "int",
      "widget_type": "select",
      "options": [
        {
          "label": "Option 0",
          "value": {
            "value_type": "int",
            "int_value": 0
          }
        },
        {
          "label": "Option 1",
          "value": {
            "value_type": "int",
            "int_value": 1
          }
        },
        {
          "label": "Option 2",
          "value": {
            "value_type": "int",
            "int_value": 2
          }
        }
      ],
      "default_value": {
        "value": 1,
        "value_type": "int"
      },
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

* Example of `evt.param.report`:

```json
{
  "serv": "parameters",
  "type": "evt.param.report",
  "val_t": "object",
  "val": [
    {
      "parameter_id": "2",
      "value": {
        "int_value": 1,
        "value_type": "int"
      }
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