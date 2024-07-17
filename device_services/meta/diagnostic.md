# Diagnostic Service

This service allows for the control of diagnostic functionalities of associated Things. A Thing can expose a diagnostic API that enables logging of device-specific data (e.g., logging communication between the Thing and the auxiliary devices it uses or controls).

## Service Name

`diagnostic`

## Interfaces

| Type | Interface                  | Value type | Properties        | Description                                                                                                                                                                                  |
|------|----------------------------|------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| out  | cmd.log.start              | null       | `tunnel_protocols` | Commands the Adapter to start logging device related data. If log should contain a data tunneled from auxiliary device protocol must be specified. see [`sup_protocols`](#service-properties) |
| out  | cmd.log.stop               | null       |                   | Commands the Adapter to stop logging device related data.                                                                                                                                    |

## Service properties

| Name           | Example           | Description                                                            |
|----------------|-------------------|------------------------------------------------------------------------|
| `sup_protocols` | `["iec_61107"]`   | List of supported communication protocols to be used for thing logging |

## Interface properties

| Name                  | Example   | Description                                                           |
|-----------------------|-----------|-----------------------------------------------------------------------|
| `tunnel_protocol`     | `"m-bus"` | Protocol to be used when recording a data tunneled directly from the  |

## Examples

* Example of starting logging the data tunneled from smart meter using `m-bus`

```json
{
  "serv": "diagnostic",
  "type": "cmd.log.start",
  "val_t": "null",
  "val": null,
  "props": {
    "tunnel_protocol": "m-bus"
  },
  "tags": null
}
```

* Example of deleting members from an association.

```json
{
  "serv": "diagnostic",
  "type": "cmd.log.stop",
  "val_t": "null",
  "val": null,
  "props": null,
  "tags": null
}
```


