### Indicator service

The service represents indicator device e.g. a simple visual indicator like an LED element, text based indicator like small LCD screen, etc. Some indicators can be composed of several components, for instance multiple LED segments or multiple LCD displays in one device, where one can display temperature another can display humidity, etc. Indicator components are set independently by using different keys in message payload (`val`).

#### Service names

`indicator_ctrl`

#### Interfaces

Type | Interface                          | Value type | Properties | Description
-----|------------------------------------|------------|------------|------------
in   | cmd.indicator.set_visual_element   | int_map    | duration   | Requests visual element (led or some other light source) to display information. Key is a name of indicator component and value is actual value to set.
in   | cmd.indicator.set_text             | str_map    | duration   | Requests text indicator to display text. Key is name of indicator component and value is text to be displayed by the component.
in   | cmd.indicator.identify             | null       |            | Requests device to identify itself by switching a visual indicator on and off several times.

#### Interface props

Name                  | Value example                                                            | Description
----------------------|--------------------------------------------------------------------------|-------------
duration              | "10"                                                                     | Defines how long the indicator should display the information in seconds.
