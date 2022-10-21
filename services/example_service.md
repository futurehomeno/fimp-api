# Example Service

This section should contain a short description of the service and its purpose. This example showcases a service which contain: 
* example of a service property
* example of an interface with an interface property
* example of an interface with a specific storage requirement
* definition of an object
* definition of an enum

> Please note that:
> * columns **Properties** and **Storage** in the **Interfaces** table are optional and should not be added if not needed
> * sections **Interface properties**, **Service properties**, **Definitions**, and **Adapter guidelines** are optional and should not be added if not needed

## Service name

`example_service`

## Interfaces

| Type | Interface               | Value type | Properties   | Storage      | Description                                                                           |
|------|-------------------------|------------|--------------|--------------|---------------------------------------------------------------------------------------|
| in   | cmd.domain_a.get_report | null       |              |              | Requests a report of something from domain A.                                         |
| in   | cmd.domain_a.set        | object     |              |              | Sets something in domain A, see definition of [`object_a`](#definitions) object.      |
| out  | evt.domain_a.report     | object     |              |              | Reports something from domain A, see definition of [`object_a`](#definitions) object. |
| -    |                         |            |              |              |                                                                                       |
| in   | cmd.domain_b.get_report | string     |              |              | Requests a report of something from domain B.                                         |
| out  | evt.domain_b.report     | float      | `property_a` | `property_a` | Reports something from domain B.                                                      |

## Interface properties

| Name         | Example   | Description                                                                                                     |
|--------------|-----------|-----------------------------------------------------------------------------------------------------------------|
| `property_a` | `"val_1"` | This is an example value, one of possible values defined in [`sup_vals`](#service-properties) service property. |

> Note that all interface properties included in the FIMP message must be strings as per the message schema.

## Service properties

| Name       | Type      | Example              | Description                                                                                      |
|------------|-----------|----------------------|--------------------------------------------------------------------------------------------------|
| `sup_vals` | str_array | `["val_1", "val_2"]` | Description of the service property, may contain one or more values of [`enum_a`](#definitions). |

> Note that each service property included in the device inclusion report can have a different type.

## Definitions

* `attribute_a` is an object with the following structure:

| Field   | Type   | Example     | Description                                                       |
|---------|--------|-------------|-------------------------------------------------------------------|
| field_a | float  | `123.45`    | Description of the field.                                         |
| field_b | string | `"value_2"` | Description of the field, one of [`enum_a`](#definitions) values. |

* `enum_a` is one of the following values: `val_1`, `val_2`, `val_3`.

## Examples

* Example of a report of something from domain A:

```json
{
  "serv": "example",
  "type": "evt.domain_a.report",
  "val_t": "object",
  "val": {
    "field_a": 123.45,
    "field_b": "value_2"
  },
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "3cd089e1-a453-4410-9ce5-b3aa61ae443f",
  "topic": "pt:j1/mt:evt/rt:dev/rn:example_adapter/ad:1/sv:example_service/ad:1"
}
```

* Example of a report of something from domain B:

```json
{
  "serv": "example_service",
  "type": "evt.domain_b.report",
  "val_t": "float",
  "val": 123.45,
  "props": {
    "property_a": "val_2"
  },
  "storage": {
    "sub_value": "val_2"
  },
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "3cd089e1-a453-4410-9ce5-b3aa61ae443f",
  "topic": "pt:j1/mt:evt/rt:dev/rn:example_adapter/ad:1/sv:example_service/ad:1"
}
```

## Adapter guidelines

This section should contain optional guidelines for the adapter implementation.