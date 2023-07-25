# Color Control Service

The service can be used to control color components of a lighting device, such as LED strips or bulbs.

## Service name

`color_ctrl`

## Interfaces

| Type | Interface                  | Value type | Description                                                                                                                                                      |
|------|----------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.color.get_report       | null       | Requests a map of color component values.                                                                                                                        |
| in   | cmd.color.set              | int_map    | Sets values for all color components using a map in which key is a [`color_component`](#definitions) listed in [`sup_components`](#service-properties) property. |
| out  | evt.color.report           | int_map    | Returns map of color components, where value is the component intensity.                                                                                         |
| -    |                            |            |                                                                                                                                                                  |
| in   | cmd.color.start_transition | object     | Starts a single color component transition, see the [`transition`](#definitions) object definition for more details.                                             |
| in   | cmd.color.stop_transition  | str        | Stops transition of the single color component referenced in the value.                                                                                          |

## Service properties

| Name             | Type      | Example                                                                      | Description                                                                                                          |
|------------------|-----------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| `sup_components` | str_array | `["red", "green", "blue"]`                                                   | List of supported color components, see definition of [`color_component`](#definitions) for list of possible values. |
| `sup_durations`  | object    | `[{"min": 1, "max": 127, "step": 1}, {"min": 180, "max": 7620, "step": 60}]` | Supported duration steps for transition change as an array of [`transition_range`](#definitions) objects.            |

> In the Z-Wave protocol, color component transition duration can only be set between 1-127 seconds or 1-127 minutes. In order to fully support the Z-Wave protocol,
> `sup_durations` property can contain an array of ranges with a specific step.

## Definitions

* `color_component` represents a single color component, see the table below for well-defined color components:

| Color component | Z-Wave | Zigbee | Range   | Description                                                                                                  |
|-----------------|--------|--------|---------|--------------------------------------------------------------------------------------------------------------|
| `red`           | Yes    | Yes    | 0-255   | Defines intensity of red color.                                                                              |
| `green`         | Yes    | Yes    | 0-255   | Defines intensity of green color.                                                                            |
| `blue`          | Yes    | Yes    | 0-255   | Defines intensity of blue color.                                                                             |
| `warm_w`        | Yes    | No     | 0-255   | Is intensity of warm white light source. Mix of warm white and cold white intensity forms color temperature. |
| `cold_w`        | Yes    | No     | 0-255   | Is intensity of cold white light source. Mix of warm white and cold white intensity forms color temperature. |
| `temp`          | No     | Yes    | 1-65279 | Is the color temperature in Kelvins. Values supported by end devices are 2700K-6500K.                        |
| `amber`         | Yes    | No     | 0-255   | Defines intensity of amber color.                                                                            |
| `cyan`          | Yes    | No     | 0-255   | Defines intensity of cyan color.                                                                             |
| `purple`        | Yes    | No     | 0-255   | Defines intensity of purple color.                                                                           |

* `transition` is an object representing a single color transition change with the following structure:

| Field      | Type   | Example | Description                                                                                                             |
|------------|--------|---------|-------------------------------------------------------------------------------------------------------------------------|
| component  | string | `"red"` | One of the supported `color_component` values. See [`sup_components`](#service-properties) property for allowed values. |
| transition | string | `"up"`  | Direction of the transition, either `up` or `down`.                                                                     |
| duration   | int    | `127`   | Optional duration of the transition in seconds. See [`sup_durations`](#service-properties) property for allowed values. |

* `transition_range` is an object with the following structure:

| Field | Type | Example | Description                        |
|-------|------|---------|------------------------------------|
| min   | int  | `1`     | Minimum settable value in seconds. |
| max   | int  | `127`   | Maximum settable value in seconds. | 
| step  | int  | `1`     | Step size.                         |

## Examples

* Example of a command setting a color to red:

```json
    {
  "serv": "color_ctrl",
  "type": "cmd.color.set",
  "val_t": "int_map",
  "val": {
    "red": 255,
    "green": 0,
    "blue": 0
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:color_ctrl/ad:19_0"
}
```

* Example of a command to start a red color transition taking 30 seconds:

```json
    {
  "serv": "color_ctrl",
  "type": "cmd.color.start_transition",
  "val_t": "object",
  "val": {
    "component": "red",
    "transition": "up",
    "duration": 30
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:color_ctrl/ad:19_0"
}
```
