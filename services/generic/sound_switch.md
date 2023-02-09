# Sound Switch Service

Sound Switch service allows to control the sound tones on the remote device.

## Service name

`sound_switch`

## Interfaces

| Type | Interface             | Value type | Description                                                                           |
| ---- | --------------------- | ---------- | ------------------------------------------------------------------------------------- |
| in   | cmd.config.get_report | null       | Requests the current configuration of the device.                                     |
| in   | cmd.config.set        | int_map    | Configures default tone and volume, see [`config_map`](#definitions) for more info.   |
| out  | evt.config.report     | int_map    | Reports default tone and volume, see [`config_map`](#definitions) for more info.      |
| in   | cmd.play.get_report   | null       | Requests current tone being played.                                                   |
| in   | cmd.play.set          | int_map    | Plays specific tone, see [`play_map`](#definitions) for more info.                    |
| in   | cmd.play.stop         | null       | Stops playing current tone.                                                           |
| out  | evt.play.report       | int_map    | Reports the current mode of the device, see [`play_map`](#definitions) for more info. |

## Service properties

| Name                        | Type   | Description                                                                        |
| --------------------------- | ------ | ---------------------------------------------------------------------------------- |
| `sup_tones`                 | object | Array of objects, see definition of [`supported_tone`](#definitions).              |   
| `supports_play_with_volume` | bool   | If true then the device will support setting volume in [`play_map`](#definitions). |

## Definitions

* `config_map` is an int_map of the following structure:

| Field             | Example         | Description                                                                                                       |
| ----------------- | --------------- | ----------------------------------------------------------------------------------------------------------------- |
| `default_tone_id` | `1`, `5`, `25`  | Tone must be one of [`sup_tones`](#service-properties). It will be used in case an unsupported tone is requested. |
| `volume`          | `0`, `35`, `70` | Volume should be a value between 0-100 where 0 mutes the device.                                                  |

* `play_map` is an int_map of the following structure:

| Field     | Example         | Description                                                                                                                                                          |
| --------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tone_id` | `1`, `5`, `25`  | Optional, if missing default tone will be played. Tone must be one of [`sup_tones`](#service-properties).                                                            |
| `volume`  | `0`, `35`, `70` | Optional, some devices do not support this. See [`supports_play_with_volume`](#service-properties). Volume should be a value between 0-100 where 0 mutes the device. |

* `supported_tone` is an object of the following structure:

| Field      | Type   | Example                     | Description                                    |
| ---------- | ------ | --------------------------- | ---------------------------------------------- |
| `tone_id`  | int    | `1`, `5`, `25`              | Id of the tone. Must be a value between 1-254. |
| `duration` | int    | `5`, `13`, `10`             | Duration of the sound described in seconds.    |
| `name`     | string | `"06 Chimes"`, `"17 Alarm"` | Name of the tone.                              |

## Examples

* Example of a configuration report:

```json
{
  "serv": "sound_switch",
  "type": "evt.config.report",
  "val_t": "int_map",
  "val": {"default_tone_id": 1, "volume":45},
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:sound_switch/ad:15_0"
}
```

* Example of `sup_tones`:

```json
"sup_tones": [
  {
    "duration": 5,
    "name": "01 Ding Dong",
    "tone_id": 1
  },
  {
    "duration": 9,
    "name": "02 Ding Dong Tubular",
    "tone_id": 2
  },
  {
    "duration": 10,
    "name": "03 Traditional Apartment Buzzer",
    "tone_id": 3
  },
  {
    "duration": 1,
    "name": "04 Electric Apartment Buzzer",
    "tone_id": 4
  }
]
```


