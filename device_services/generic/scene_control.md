# Scene Control Service

The service represents a device which can be used to control scenes, such as a remote controller.

## Service name

`scene_ctrl`

## Interfaces

| Type | Interface            | Value type | Description                                                                                                           |
|------|----------------------|------------|-----------------------------------------------------------------------------------------------------------------------|
| in   | cmd.scene.get_report | null       | Requests the currently active scene.                                                                                  |
| in   | cmd.scene.set        | string     | Sets the scene to the one provided in the value.                                                                      |
| out  | evt.scene.report     | string     | Event is generated whenever scene button is pressed on the controller.                                                |
| out  | evt.lvl.report       | int        | Reports the level value. See the [`min_lvl`](#Service_properties) and [`max_lvl`](#Service_properties) for reference. |

> Devices designed only as scene controllers may support only `evt.scene.report` interface and send report whenever a physical button is pressed.
> Devices designed only as scene activators may support only `cmd.scene.set` interface and can be used to activate a scene by sending a command.

## Service properties

| Name         | Type      | Example                                            | Description                                                   |
|--------------|-----------|----------------------------------------------------|--------------------------------------------------------- -----|
| `min_lvl`    | int       | `0`                                                | A minimum reportable level value for evt.lvl.report interface.|
| `max_lvl`    | int       | `254`                                              | A maximum reportable level value for evt.lvl.report interface.|
| `sup_scenes` | str_array | `["1.key_pressed_1_time", "2.key_pressed_1_time"]` | List of supported scenes.                                     |

> A device may define its own free-form scene names. However, when applicable, it is recommended to use *KEY_NUMBER.KEY_EVENT* naming convention. 
> Possible values for *KEY_EVENT* are: `key_pressed_1_time`, `key_pressed_2_times`, `key_pressed_3_times`, `key_released`, `key_held_down`.

## Examples

* Example of an event sent when button 1 is pressed on the controller:

```json
    {
      "serv": "scene_ctrl",
      "type": "evt.scene.report",
      "val_t": "string",
      "val": "1.key_pressed_1_time",
      "props": {},
      "tags": [],
      "src": "-",
      "ver": "1",
      "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
      "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:scene_ctrl/ad:17_0"
    }
```

* Example of an event sent when dimmer was rotated on the controller:

```json
    {
      "serv": "scene_ctrl",
      "type": "evt.lvl.report",
      "val_t": "int",
      "val": 127,
      "props": {},
      "tags": [],
      "src": "-",
      "ver": "1",
      "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
      "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:scene_ctrl/ad:17_0"
    }
```
