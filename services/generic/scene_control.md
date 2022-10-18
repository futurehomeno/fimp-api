### Scene controller service

The service represents a device which can be used to control scenes. Normally it's remote controller.

#### Service names

`scene_ctrl`

#### Interfaces

Type | Interface            | Value type | Description
-----|----------------------|------------|-------------------
in   | cmd.scene.get_report | null       | The command is a request for current scene.
in   | cmd.scene.set        | string     | Set scene
out  | evt.scene.report     | string     | Event is generated whenever scene button is pressed on controller.

#### Service props

Name         | Value example | Description
-------------|---------------|-------------
`sup_scenes` | 1, a, movies  | List of supported scenes