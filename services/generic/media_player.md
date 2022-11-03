# Media Player Service

Media player service is used to control playback on a media player device.

## Service name

`media_player`

## Interfaces

| Type | Interface                   | Value type | Description                                                                                                                     |
|------|-----------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------|
| in   | cmd.playback.set            | string     | Executes one of playback actions defined in [`sup_playback`](#service-properties) property.                                     |
| in   | cmd.playback.get_report     | null       | Request current playback action.                                                                                                |
| out  | evt.playback.report         | string     | Reports current playback action.                                                                                                |
| -    |                             |            |                                                                                                                                 |
| in   | cmd.playbackmode.set        | bool_map   | Allows to configure playback modes. Configurable playback modes are defined in [`sup_modes`](#service-properties) property.     |
| in   | cmd.playbackmode.get_report | null       | Requests playback mode configuration.                                                                                           |
| out  | evt.playbackmode.report     | bool_map   | Reports configured playback modes.                                                                                              |
| -    |                             |            |                                                                                                                                 |
| in   | cmd.volume.set              | int        | Sets playback volume within 0-100 range.                                                                                        |
| in   | cmd.volume.get_report       | null       | Requests playback volume.                                                                                                       |
| out  | evt.volume.report           | int        | Reports playback volume.                                                                                                        |
| -    |                             |            |                                                                                                                                 |
| in   | cmd.mute.set                | bool       | Allows to mute/unmute the playback.                                                                                             |
| in   | cmd.mute.get_report         | null       | Requests report on whether playback is muted.                                                                                   |
| out  | evt.mute.report             | bool       | Returns `true` for **muted** playback, otherwise `false`.                                                                       |
| -    |                             |            |                                                                                                                                 |
| in   | cmd.metadata.get_report     | null       | Requests metadata of the currently played track.                                                                                |
| out  | evt.metadata.report         | str_map    | Returns metadata of the currently played track. Report contains keys defined in [`sup_metadata`](#service-properties) property. |

## Service properties

| Name           | Type      | Example                 | Description                                                                                                            |
|----------------|-----------|-------------------------|------------------------------------------------------------------------------------------------------------------------|
| `sup_playback` | str_array | `["play", "pause"]`     | Supported playback actions. Possible value are: `play`, `pause`, `toggle_play_pause`, `next_track`, `previous_track` . |
| `sup_modes`    | str_array | `["repeat", "shuffle"]` | Supported playback modes. Possible values are: `repeat`, `repeat_one`, `shuffle`, `crossfade`.                         |
| `sup_metadata` | str_array | `["album", "track"]`    | Supported metadata. Possible values are: `album`, `track`, `artist`, `image_url`.                                      |

## Examples

* Example of a `next_track` playback command:

```json
{
  "serv": "media_player",
  "type": "cmd.playback.set",
  "val_t": "string",
  "val": "next_track",
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:sonos/ad:1/sv:media_player/ad:1"
}
```

* Example of a playback mode configuration command:

```json
{
  "serv": "media_player",
  "type": "cmd.playbackmode.set",
  "val_t": "bool_map",
  "val": {
    "repeat": true,
    "shuffle": false,
    "crossfade": true
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:cmd/rt:dev/rn:sonos/ad:1/sv:media_player/ad:1"
}
```

* Example of a metadata report:

```json
{
  "serv": "media_player",
  "type": "evt.metadata.report",
  "val_t": "str_map",
  "val": {
    "album": "The Dark Side of the Moon",
    "track": "Money",
    "artist": "Pink Floyd",
    "image_url": "https://upload.wikimedia.org/wikipedia/en/3/3b/Dark_Side_of_the_Moon.png"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "eb99fe48-3276-4a21-acd4-a6cbfb3a800d",
  "topic": "pt:j1/mt:evt/rt:dev/rn:sonos/ad:1/sv:media_player/ad:1"
}
```