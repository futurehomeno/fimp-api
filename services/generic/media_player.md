### Media player service

#### Service name

`media_player`

#### Interfaces

Type        | Interface                         | Value type        | Description
------------|---------------------------        |-------------------|-------
in          | cmd.playback.set                  | string            | play, pause, toggle_play_pause, next_track, previous_track
in          | cmd.playback.get_report           | null              |
out         | evt.playback.report               | string            |
-|||
in          | cmd.playbackmode.set              | bool_map          | {"repeat": false, "repeat_one": false, "crossfade": false, "shuffle": false}
in          | cmd.playbackmode.get_report       | null              |
out         | evt.playbackmode.report           | bool_map          |
-|||
in          | cmd.volume.set                    | int               | 0-100
in          | cmd.volume.get_report             | null              |
out         | evt.volume.report                 | int               | 0-100
-|||
in          | cmd.mute.set                      | bool              |
in          | cmd.mute.get_report               | null              |
out         | evt.mute.report                   | bool              |
-|||
in          | cmd.metadata.get_report           | null              |
out         | evt.metadata.report               | str_map           | {"album": "", "track": "", "artist": "", "image_url": ""}

### Service props

Name           | Value example                                                      | Description
---------------|--------------------------------------------------------------------|-------
`sup_modes`    | repeat, repeat_one, shuffle, crossfade                             | supported modes.
`sup_playback` | play, pause, toggle_play_pause, next_track, previous_track         | supported playbacks.
`sup_metadata` | album, track, artist, image_url                                    | supported metadata.