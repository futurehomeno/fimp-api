### Color control service

The service has to be used to control color components of a lightning device.

#### Service names

`color_ctrl`

#### Interfaces

Type | Interface                  | Value type |  Description
-----|----------------------------|------------|-------------------
in   | cmd.color.get_report       | null       | The command is a request for a map of color component values
in   | cmd.color.set              | int_map    | value is a map of color components. val= {"red":200, "green":100, "blue":45}
out  | evt.color.report           | int_map    | Map of color components, where value is component intensity.
-|||
in   | cmd.color.start_transition | object     | Example value: val= {"component": "red", "transition": "up", "duration": 127}
in   | cmd.color.stop_transition  | str        | Stop fading/enhancing single color component. val = "red"

#### Service props

Name             | Value example                                                              | Description
-----------------|----------------------------------------------------------------------------|-------------
`sup_components` | ["red", "green", "blue"]                                                   | List of supported color components
`sup_durations`  | [{"min": 1, "max": 127, "step": 1}, {"min": 180, "max": 7620, "step": 60}] | Supported duration steps for transition change (optional). Min and max always reflects seconds.

Supported color components:
- Zwave: red, green, blue, warm_w, cold_w, amber, cyan, purple
- Zigbee: red, green, blue, temp

#### Notes

- temp - is color temperature in Mired (micro reciprocal degree). It is related to Kelvins as:
  `temp_kelvins = 1,000,000 / temp_mireds`
  Supported `temp` values: 1-65279 mired. Actual color temperature supported by end devices is 2700K-6500K.

- warm_w - is warm white light source intensity. Value range 0-255.

- cold_w - is cold white light source intensity. Value range 0-255.

- Mix of warm white intensity and cold white intensity forms color temperature.

- Duration property within cmd.color.start_transition command is optional and means seconds.

- In the Z-Wave protocol, color component transition duration can only be set between 1 - 127 seconds or 1 - 127 minutes. In order to fully support the Z-Wave protocol, sup_durations property can contain an array of ranges with a specific step.
