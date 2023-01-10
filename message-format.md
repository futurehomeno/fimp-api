# Message Format

Messages sent over MQTT adhering to the FIMP protocol are JSON messages which meet schema requirements outlined in this document.

## Example message

Following is the example of a FIMP message containing energy consumption report from an electricity meter. More examples can be found in particular [services](services/services.md)
specifications.

```json
{
  "serv": "meter_elec",
  "type": "evt.meter.report",
  "val_t": "float",
  "val": 255.488998413086,
  "storage": {
    "sub_value": "kWh"
  },
  "props": {
    "delta_t": "120",
    "prv_data": "255.488998",
    "direction": "import",
    "unit": "kWh"
  },
  "tags": [],
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "ctime": "2022-12-02T10:08:27.5+01:00",
  "src": "zwave-ad",
  "ver": "1",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:meter_elec/ad:7_0"
}
```

## Message Properties

Following is the list of message properties in accordance to FIMP version 1.

| Property  | Type         | Example                                   | Required | Description                                                                                                                                                                                                                          |
|-----------|--------------|-------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `serv`    | String       | `"out_bin_switch"`                        | Yes      | The name of the service the interface is part of. Service names should utilize `snake_case`.                                                                                                                                         |
| `type`    | String       | `"evt.binary.report"`                     | Yes      | The name of the interface represented by the message. See the [Interface Format](#interface-format) section for more details.                                                                                                        |
| `val_t`   | String       | `"bool"`                                  | Yes      | Type of the value stored in `val` property. See the list of [Value Types](#value-types) section for more details.                                                                                                                    |
| `val`     | Any          | `3.33`                                    | Yes      | Payload of the message of which type is defined in `val_t` property.                                                                                                                                                                 |
| `storage` | Object       | `{"sub_value": "kWh"}`                    | No       | Defines optional storage aggregation key for multi-value reports. Applies only to device reports. Parser must accept missing key or `null` value as an empty `object`.                                                               |
| `props`   | String Map   | `{"unit":"W"}`                            | No       | An optional map of properties. Please note that all properties including numeric ones must be encoded as strings. Parser must accept missing key or `null` value as an empty `map`.                                                  |
| `tags`    | String Array | `{"test"}`                                | No       | An optional list of tags. Parser must accept missing key or `null` value as an empty `array`.                                                                                                                                        |
| `resp_to` | String       | `"pt:j1/mt:rsp/rt:app/rn:angry-dog/ad:1"` | No       | A topic where a response to the request will be expected. Does not apply to most of the broadcast type of events, especially asynchronous device events for which adapter will ignore this property. Parser must accept missing key. |
| `corid`   | String       | `"e0749aaa-05b8-4983-89e1-f225b539cc40"`  | No       | Response correlation identifier that is equal to the `uid` property of the request, used for request-response matching. Parser must accept missing key.                                                                              |
| `uid`     | String       | `"9bb1be75-35d7-4069-ac00-b974315f7ec3"`  | Yes      | A unique message identifier in form of UUID. It is recommended to use Version 4.                                                                                                                                                     |
| `ctime`   | String       | `"2022-12-02T10:08:27.5+01:00"`           | Yes      | Message creation time in RFC3339 format. For compatibility reasons a message parser must treat a missing key as the current timestamp. See [time format](#time-format) section for disambiguation.                                   |
| `src`     | String       | `"smarthome-app"`                         | Yes      | Name of the message publisher identifying a HUB, mobile or cloud application or service. For compatibility reasons a message parser must tolerate a missing key.                                                                     |
| `ver`     | String       | `"1"`                                     | Yes      | Version of the message format. The current version is `1`.                                                                                                                                                                           |
| `topic`   | String       | `"pt:j1/mt:evt/rt:app/rn:vinculum/ad:1"`  | No       | The MQTT topic on which the message was originally received, required only when message is processed outside of MQTT context, for example in a Kafka stream.                                                                         |

## Value Types

Since message `val` property can be of any type, `val_t` defines what type it is. Following is the list of supported value types:

| `val_t`     | Example `val`                                            | Comments                                                                                                                    |
|-------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| string      | `"Hello world!"`                                         |                                                                                                                             |
| int         | `3`                                                      |                                                                                                                             |
| float       | `3.1415`                                                 | As JSON lacks distinction between integers and floats, both `3.00` and `3` are valid payloads for this type.                |
| bool        | `true`                                                   |                                                                                                                             |
| null        | `null`                                                   |                                                                                                                             |
| str_array   | `["Hello", "world"]`                                     |                                                                                                                             |
| int_array   | `[0, 1, 1, 2, 3, 5, 8, 13]`                              |                                                                                                                             |
| float_array | `[3.14, 3, 2.71, 2.00]`                                  |                                                                                                                             |
| int_map     | `{"answer": 42}`                                         |                                                                                                                             |
| str_map     | `{"ip": "192.168.1.1"}`                                  |                                                                                                                             |
| float_map   | `{"pi": 3.14}`                                           |                                                                                                                             |
| bool_map    | `{"enabled": true}`                                      |                                                                                                                             |
| object      | `{"nested": {"objects": "supported"}}`                   | Used for complex objects which cannot be mapped to primitive types. Structure is defined uniquely per service or interface. |
| bin         | `"U28gbG9uZywgYW5kIHRoYW5rcyBmb3IgYWxsIHRoZSBmaXNoLg=="` | Used for `base64` encoded binary payloads.                                                                                  |

## Time Format

Time must be formatted in accordance to the RFC3339 format. A message parser must be able to read all the following timestamps as valid.
When producing messages it is recommended to only use the first one.

| Format                                   | Recommended |
|------------------------------------------|-------------|
| `"2006-01-02T15:04:05.999999999Z07:00"`  | Yes         | 
| `"2006-01-02T15:04:05.999999999Z0700"`   | No          | 
| `"2006-01-02 15:04:05.999999999 Z0700"`  | No          | 
| `"2006-01-02 15:04:05.999999999 Z07:00"` | No          | 

## Interface Format

Each interface consist of three segments separated by a dot in accordance to this schema `{type}.{attribute}.{action}`:

| Segment     | Example      | Description                                                                                                                                                                         |
|-------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *type*      | `cmd`        | Defines the **type** of the interface, either `cmd` for consumed incoming commands or `evt` for produced outgoing events.                                                           |
| *attribute* | `lvl`        | Defines the **attribute** or a **domain** of the service. A service might have multiple attributes, while each attribute might have multiple interfaces. Must utilize `snake_case`. |
| *action*    | `get_report` | Defines the **action** invoked by the command or reported **data** in the case of an event. Must utilize `snake_case`.                                                              |

Typically, getter, setter and report interfaces are bundled by the common `attribute`. For example in case of [`out_lvl_switch`](/services/generic/output_level_switch.md) service:

* `cmd.lvl.get_report` is used to perform *action* of getting the report of the current `lvl` *attribute* value.
* `cmd.lvl.set` is used to perform *action* of setting the `lvl` *attribute* value.
* `evt.lvl.report` is used to *report* the current `lvl` *attribute* value.

> All messages sent by a device which have interface *type* segment equal to `evt` while *action* segment is equal or ends with `report` suffix, will be recorded as a last known
> value in the Vinculum database under its *attribute* key. For example, a message with interface `evt.lvl.report` will have its value recorded under the `lvl` attribute.
> Therefore, in case of device services it is forbidden to use multiple reporting interfaces for the same attribute, unless a `storage` property is properly defined in the message.
