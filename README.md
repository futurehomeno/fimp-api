# Futurehome IoT Messaging Protocol - FIMP

* [Service overview](#service-overview)
* [Component discovery mechanism](#component-discovery-mechanism)
* [Adding / removing things to FH system](#adding--removing-things-to-fh-system)
* [Services](#services)
   * [Basic service](#basic-service)
   * [System related device service](#system-related-device-service)
   * [Output binary switch service](#output-binary-switch-service)
   * [Output level switch service](#output-level-switch-service)
   * [Meter services](#meter-services)
   * [Numeric sensor services](#numeric-sensor-services)
   * [Contact sensor service](#contact-sensor-service)
   * [Presence sensor service](#presence-sensor-service)
   * [Alarm services](#alarm-services)
   * [Battery service](#battery-service)
   * [Thermostat service](#thermostat-service)
   * [Door lock service](#door-lock-service)
   * [User code service](#user-code-service)
   * [Color control service](#color-control-service)
   * [Scene controller service](#scene-controller-service)
   * [Fan control service](#fan-control-service)
   * [Siren service](#siren-service)
   * [Indicator service](#indicator-service)
   * [Barrier control service](#barrier-control-service)
   * [Complex alarm system service](#complex-alarm-system-service)
   * [Gateway service](#gateway-service)

## Service overview

In FIMP, the functionality of everything that's considered a device is represented by services. These say something about the capabilities of the device, e.g. the service `out_bin_sw` indicates that some part of the device can be turned on / off. Similarly `out_lvl_sw` indicates that some part of the device accepts a value between a given min and max. Note that the services are not specific as to what part of the device they represent. An `out_bin_sw` might turn on / off part of the device, or the device itself.

Each service is further represented by interfaces, where a service must have at least one interface. An interface consist of three parts separated by a period:

 1. The first part of the interface is the **type**. From the perspective of the receiver, it can be either `cmd` - representing an incoming message, or `evt` - representing an outgoing message.

 2. The second part of the interface is the **attribute** which says something about the values supported by the interface. E.g. the `binary` attribute specifies that this interface only support boolean values. A service can have multiple interfaces with different attributes.

 3. The third part of the interface represents the **action** to perform in the case of a `cmd` interface, or the data in the case of `evt`. Typically this takes the form of getters ans setters.

Bringing it all together: the interface `cmd.binary.set` allows you to send a **command** to the **binary attribute** saying you want to **set** (change) it. Similarly, `evt.binary.report` says that there was an **event** (message received) on the **binary attribute** where a **report** was received.

Additionally, each service it will have its own unique address (topic) over which it can send / receive messages, e.g. `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:out_bin_switch/ad:11_0`. The address can be broken down into the following components:

Type | Sample values                  | Description
-----|--------------------------------|------------
pt   | j1                             | parser type, typically j1, representing JSON v1.
mt   | evt, cmd, rsp                 | message type . cmd - command, evt - event, rsp - response to request
rt   | ad, app, dev                   | resource type, ad = adapter, dev = device.
rn   | zw, vinculum, zigbee, kind-owl | resource name, the actual name of the rt
sv   | out_bin_sw, out_lvl_sw, etc.   | service name
ad   |                                | the address of the preceding type.

Breaking down the example `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:out_bin_switch/ad:11_0`, this is the address specifying JSON v1 formatted events sent to a device using zwave with address 1, and the service `out_bin_sw` with address of 11_0. Note here that zwave actually has an address. This is normally set to 1, but in the case of the gateway having multiple instances of zwave, it can be another address.

Lastly, not that each interface within a service share the same address and that a service can never have more than one interface of the same type.

[FIMP message format](message-format.md)

[Topic examples](topics.md)

## Component discovery mechanism

The mechanism allows dynamically discover different system component like adapters and application.

[Component discovery flow and messages](component-discovery.md)

## Adding / removing things to FH system

Things can be added to FH ecosystem in 2 ways:

1. [Adding/removing a thing to FH system via adapter](thing-management.md)
2. [Connecting/disconnecting a system to FH system](system-management.md)

First method should be used to add a thing which isn't paired with underlying RF module, for instance: Z-Wave, Zigbee, Bluetooth

Second method should be used to connect a system which already has a number of connected devices, for instance: IKEA Trådfri, Phillips Hue, Sonos, etc.

Example: add z-wave device, remove z-wave device, add zigbee device, remove zigbee device.

## Services

### Basic service

A generic service and the most simple way to interact with a device. The actual meaning of "basic" varies from device to device.

#### Service names

`basic`

#### Interfaces

Type | Interface          | Value type | Description
-----|--------------------|------------|------------
in   | cmd.lvl.get_report | null       |
in   | cmd.lvl.set        | int        | Sets level using numeric value
out  | evt.lvl.report     | int        | Reports level using numeric value

***

### System related device service

#### Service names

`dev_sys`

#### Interfaces

Type | Interface                   | Value type | Description
-----|---------------------------- |------------|------------
in   | cmd.config.get_report       | str_array  | Requests service to respond with config report. If array is empty - report all parameters.
in   | cmd.config.get_supp_list    | null       | Requests service to respond with a list of supported configurations.
in   | cmd.config.set              | str_map    | Sets configuration. Value is a key-value pairs.
in   | cmd.config.supp_list_report | str_map    | List of supported configurations. Key - config name, value - short description.
in   | cmd.thing.reboot            | string     | Requests device to run either complete reboot or reboot specific component.
out  | evt.config.report           | str_map    | Reports configurations in form of key-value pairs.
-|||
in   | cmd.group.add_members       | object     | Adds members to the group. Object has the same format as members_report
in   | cmd.group.delete_members    | object     | Object has the same format as report.
in   | cmd.group.get_members       | string     | Value is a group name.
out  | evt.group.members_report    | object     | Object structure {"group":"group1", "members":["node1", "node2"]}

#### Notes

- z-wave configuration values should be in form <value>;size, for instance 12;2

- z-wave association member should be in form <node_id>\_<endpoint_id>, for instance 10_0

***

### Output binary switch service

Output binary switch service for wall-plugs, relays, simple sirens, etc.

#### Service names

`out_bin_switch`

#### Interfaces

Type | Interface             | Value type | Description
-----|-----------------------|------------|------------
in   | cmd.binary.get_report | null       |
in   | cmd.binary.set        | bool       |
out  | evt.binary.report     | bool       | Reports true when switch is ON and false when switch is OFF

***

### Output level switch service

Used for dimmers and things generally controlled with sliders.

#### Service names

`out_lvl_switch`

#### Interfaces

Type | Interface          | Value type | Properties              | Description
-----|--------------------|------------|-------------------------|------------
in   | cmd.binary.set     | bool       |                         | true is mapped to 255, false to 0
out  | evt.binary.report  | bool       |                         |
-|||
in   | cmd.lvl.get_report | null       |                         |
in   | cmd.lvl.set        | int        | `duration`              |
in   | cmd.lvl.start      | string     | `start_lvl`, `duration` |
in   | cmd.lvl.stop       | null       |                         | Stop a level change
out  | evt.lvl.report     | int        |                         |

#### Interface props

Name        | Value example | Description
------------|---------------|-------------
`duration`  | "10"          | duration in seconds. Factory default is used if no value is provided.
`start_lvl` | "up"          | level change direction. Supported values are `up`, `down` and `auto`.

#### Service props

Name      | Value example | Description
----------|---------------|-------------
`max_lvl` | 99            | maximum value.
`min_lvl` | 0             | minimum value.
`sw_type` | "on_off"      | type of level switch. Supported values are "on_off" or "up_down".

***

### Meter services

Meters report consumption over the service.

#### Service names

Service name  | Units                                     | Description
------------- |-------------------------------------------|------------
`meter_elec`  | kWh, kVAh, W, pulse_c, V, A, power_factor | Electric meter
`meter_gas`   | cub_m, cub_f, pulse_c                     | Gas meter
`meter_water` | cub_m, cub_f, gallon, pulse_c             | Water meter

#### Interfaces

Type | Interface                     | Value type | Properties              | Description
-----|-------------------------------|------------|-------------------------|-------------
in   | cmd.meter.get_report          | string     |                         | Value - is a unit. May not be supported by all meters.
in   | cmd.meter.reset               | null       |                         | Resets all historical readings.
out  | evt.meter.report              | float      | unit, prv_data, delta_t |
out  | evt.meter_ext.report          | float_map  |                         | [Extended meter report](#extended-report-object) with up to 17 data points
in   | cmd.meter_ext.get_report      | null       |                         | Request extended report

#### Interface props

Name       | Value example | Description
-----------|---------------|-------------
`delta_t`  |               | time delta
`prv_data` |               | previous meter reading
`unit`     |               |

#### Service props

Name                | Value example                                  | Description
--------------------|------------------------------------------------|-------------
`sup_units`         | ["W", "kWh", "A", "V"]                         | list of supported units.
`sup_extended_vals` | [See extended report](#extended-report-object) |

#### Extended report object

Name            | Unit    | Description
----------------|---------|--------------
`e_import`      | kWh     | Energy Import
`e_export`      | kWh     | Energy Export
`last_e_export` | kWh     | Energy Export that day
`last_e_import` | kWh     | Energy Import that day
`p_import`      | W       | Power Import
`p_import_react` | VA     | Reactive Power Import
`p_import_apparent` | VA  | Apparent Power Import
`p_import_avg`  | W       | Power Import average
`p_import_min`  | W       | Power Import minimum that day
`p_import_max`  | W       | Power Import max that day
`p_export`      | W       | Power Export
`p_export_react` | VA     | Reactive Power Export
`p_export_min`  | W       | Power Export minimum that day
`p_export_max`  | W       | Power Export max that day
`freq`          | Hz      | Frequency
`freq_min`      | Hz      | Frequency Min
`freq_max`      | Hz      | Frequency Max
`u1`            | V       | Voltage phase 1
`u2`            | V       | Voltage phase 2
`u3`            | V       | Voltage phase 3
`i1`            | A       | Current phase 1
`i2`            | A       | Current phase 2
`i3`            | A       | Current phase 3
`dc_p`          | W       | DC Power
`dc_p_min`      | W       | DC Power
`dc_p_max`      | W       | DC Power
`dc_u`          | V       | DC Voltage
`dc_u_min`      | V       | DC Min Voltage
`dc_u_max`      | V       | DC Max Voltage
`dc_i`          | A       | DC Current
`dc_i_min`      | A       | DC Min Current
`dc_i_max`      | A       | DC Max Current


***

### Numeric sensor services

#### Service names

Service name         | Units                    | Description
---------------------|--------------------------|------------
`sensor_accelx`      | m/s2                     | Acceleration, X-axis
`sensor_accely`      | m/s2                     | Acceleration, Y-axis
`sensor_accelz`      | m/s2                     | Acceleration, Z-axis
`sensor_airflow`     | m3/h, ft3/m              | Air flow sensor
`sensor_anglepos`    | %, degN, degS            | Angle Position sensor
`sensor_atmo`        | kPa, ha, mbar                  | Atmospheric pressure sensor. ha - inches of Mercury
`sensor_baro`        | kPa, ha, mbar                  | Barometric  pressure sensor. ha - inches of Mercury
`sensor_co2`         | ppm                      | CO2-level sensor
`sensor_co`          | mol/m3                   | Carbon Monoxide level sensor
`sensor_current`     | A, mA                    | Current sensor
`sensor_dew`         | C, F                     | Dew point sensor
`sensor_direct`      | deg                      | Direction sensor
`sensor_distance`    | m, cm, ft                | Distance sensor
`sensor_elresist`    | ohm/m                    | Electrical resistivity sensor
`sensor_freq`        | Hz, kHz                  | Frequency sensor
`sensor_gp`          | %, NOM                   | General purpose sensor
`sensor_gust`      | kph                  | Gust sensor
`sensor_humid`       | %, g/m3                  | Relative humidity sensor
`sensor_lumin`       | Lux, %                   | Luminance sensor
`sensor_moist`       | %, kOhm, m3/m3, aw       | Moisture sensor
`sensor_noise`       | dB                       | Noise sensor
`sensor_power`       | W, Btu/h                 | Power sensor. Btu/h - British thermal unit per hour
`sensor_rain`        | mm/h, in/h               | Rain rate sensor
`sensor_rotation`    | rpm, Hz                  | Rotation sensor
`sensor_seismicint`  | EMCRO, LEIDO, MERC, SHDO | Seismic intensity sensor
`sensor_seismicmag`  | MB, ML, MW, MS           | Seismic magnitude sensor
`sensor_solarrad`    | w/m2                     | Solar radiation
`sensor_tank`        | l, gal, m3               | Tank capacity sensor
`sensor_temp`        | C, F                     | Temperature sensor
`sensor_tidelvl`     | m, ft                    | Tide level sensor
`sensor_uv`          | index                    | Ultraviolet sensor
`sensor_veloc`       | m/s, mph                 | Velocity sensor
`sensor_voltage`     | V, mV                    | Voltage sensor
`sensor_watflow`     | l/h                      | Water flow sensor
`sensor_watpressure` | kPa                      | Water pressure sensor
`sensor_weight`      | kg, lbs                  | Weight sensor
`sensor_wind`      | kph                  | Wind sensor

#### Interfaces

Type | Interface             | Value type | Properties | Description
-----|-----------------------|------------|------------|-------------
in   | cmd.sensor.get_report | string     |            | Value is desired unit. Use empty value to get report in default unit.
out  | evt.sensor.report     | float      | unit       |

Example message: [evt.sensor.report](json-v1/messages/examples/evt.sensor.report)

#### Service props

Name        | Value example | Description
------------|---------------|-------------
`sup_units` | ["C", "F"]    | list of supported units.

***

### Contact sensor service

Binary contact sensor, normally magnetic contact.

#### Service names

`sensor_contact`

#### Interfaces

Type | Interface           | Value type | Description
-----|---------------------|------------|--------------------
in   | cmd.open.get_report | null       |
out  | evt.open.report     | bool       | true = open

***

### Presence sensor service

Motion sensor or some other way of presence detection.

#### Service names

`sensor_presence`

#### Interfaces

Type | Interface               | Value type | Description
-----|-------------------------|------------|--------------------
in   | cmd.presence.get_report | null       |
out  | evt.presence.report     | bool       | true = presence

***

### Alarm services

#### Service names

Service name        | Event                                   | Description
--------------------|-----------------------------------------|------------
`alarm_appliance`   | program_started, program_inprogress, program_completed, replace_filter, set_temp_error, supplying_water, water_supply_err, boiling, boiling_err, washing, washing_err, rinsing, rinsing_err, draining, draining_err, spinning, spinning_err, drying, drying_err, fan_err, compressor_err |
`alarm_burglar`     | intrusion, tamper_removed_cover, tamper_invalid_code, tamper_force_open, alarm_burglar, glass_breakage |
`alarm_emergency`   | police, fire, medical                   |
`alarm_fire`        | smoke, smoke_test                       |
`alarm_gas`         | CO, CO2, combust_gas_detected, toxic_gas_detected, test, replace |
`alarm_health`      | leaving_bed, sitting_on_bed, lying_on_bed, posture_change, sitting_on_bed_edge, alarm_health, volatile_organic_compound |
`alarm_heat`        | overheat, temp_rise, underheat          |
`alarm_lock`        | manual_lock, manual_unlock, rf_lock, rf_unlock, keypad_lock, keypad_unlock, tag_lock, tag_unlock, manual_not_locked, rf_not_locked, auto_locked, jammed, door_opened, door_closed, lock_failed | TODO: move to doorlock service
`alarm_power`       | on, ac_on, ac_off, surge, voltage_drop, over_current, over_voltage, replace_soon, replace_now, charging, charged, charge_soon, charge_now | TODO: move to power_supply service
`alarm_siren`       | inactive, siren_active                  |
`alarm_system`      | hw_failure, sw_failure, hw_failure_with_code, sw_failure_with_code |
`alarm_time`        | wakeup, timer_ended, time_remaining     |
`alarm_water_valve` | valve_op, master_valve_op, valve_short_circuit, current_alarm, alarm_water_valve, master_valve_current_alarm |
`alarm_water`       | leak, level_drop, replace_filter        |
`alarm_weather`     | inactive, moisture                      |

#### Interfaces

Type | Interface            | Value type | Description
-----|----------------------|------------|--------------------
in   | cmd.alarm.get_report | ?          |
out  | evt.alarm.report     | str_map    | val = {"event": "tamper_removed_cover", "status": "activ"}

Supported statuses: activ, deactiv. IMPORTANT: These are shorthands for "activated" and "deactivated", not typos.

Example message: [evt.sensor.report](json-v1/messages/examples/evt.alarm.report.json)

#### Service props

Name         | Value example           | Description
-------------|-------------------------|-------------
`sup_events` | ["smoke", "smoke_test"] | supported events.

***

### Battery service

#### Service names

`battery`

#### Interfaces

Type | Interface          | Value type | Properties | Description
-----|--------------------|------------|----------- |------------------
in   | cmd.lvl.get_report | null       |            | Get battery level over level report.
out  | evt.lvl.report     | int        | state      |
-|||
out  | evt.alarm.report   | str_map    |            | val = {"event": "low_battery", "status": "activ"}

#### Interface props

Name    | Value example | Description
--------|---------------|-------------
`state` | "charging"    | available states: charging, charged, replace, emtpy

### Thermostat service

#### Service names

`thermostat`

#### Interfaces

Type | Interface               | Value type | Description
-----|-------------------------|------------|------------------
in   | cmd.mode.get_report     | null       |
in   | cmd.mode.set            | string     |  Set thermostat mode:
out  | evt.mode.report         | string     |
-|||
in   | cmd.setpoint.get_report | string     | value is a set-point type
in   | cmd.setpoint.set        | str_map    | val = {"type":"heat", "temp":"21.5", "unit":"C"}
out  | evt.setpoint.report     | str_map    | val = {"type":"heat", "temp":"21.5", "unit":"C"}
-|||
in   | cmd.state.get_report    | null       |
out  | evt.state.report        | string     |  Reports operational state.

#### Service props

Name            | Value example                                                                  | Description
----------------|--------------------------------------------------------------------------------|-------------
`sup_modes`     | off, heat, cool                                                                | supported modes.
`sup_setpoints` | heat, cool                                                                     | supported set-points.
`sup_states`    | idle, heat, cool, idle, heat, cool, fan_only, pending_heat, pending_cool, vent |

Modes: off, heat, cool, auto, aux_heat, resume, fan, furnace, dry_air, moist_air, auto_changeover, energy_heat, energy_cool, away.

Set-point types: heat, cool, furnace, dry_air, moist_air, auto_changeover, energy_heat, energy_cool, special_heat,

### Door lock service

#### Service names

`door_lock`

#### Interfaces

Type | Interface               | Value type | Properties           | Description
-----|-------------------------|------------|----------------------|------------------
in   | cmd.lock.get_report     | null       |                      |
in   | cmd.lock.set            | bool       |                      | Use true to secure a lock and false to unsecure
in   | cmd.lock.set_with_code  | str_map    |                      | Used to lock/unlock locks required PIN/RFID, {“op”:”lock”, ”code_type”:”pin”, ”12345” }
out  | evt.lock.report         | bool_map   | timeout_s, lock_type | value = {"is_secured":true, "door_is_closed":true, "bolt_is_locked":true, "latch_is_closed":true}
-|||
in   | cmd.open.get_report     | null       |                      | 
out  | evt.open.report         | bool       | true = open          | Used to report if the door is open or closed



#### Interface props

Name        | Value example | Description
------------|---------------|-------------
`lock_type` | "key"         | how lock was activated, it can take values: "key", "pin", "rfid"
`timeout_s` |               |

#### Service props

Name             | Value example                                                         | Description
-----------------|-----------------------------------------------------------------------|-------------
`sup_components` | ["is_secured", "door_is_closed", "bolt_is_locked", "latch_is_closed"] | List of supported lock component components

### User code service

Is used by door locks, keypads, security panels to enter and manage pin codes and rfids.

Detailed specification is avaliable on zwave-ad repo under docs folder.

#### Service names

`user_code`

Type | Interface                      | Value type | Description
-----|--------------------------------|------------|------------------
in   | cmd.usercode.clear             | str_map    |
in   | cmd.usercode.clear_all         | null       |
in   | cmd.usercode.get               | str_map    |
in   | cmd.usercode.set               | str_map    |
out  | evt.usercode.access_report     | str_map    |

#### Service props

Name             | Value example              | Description
-----------------|----------------------------|-------------
`sup_usercodes`  | ["pin", "rfid"]            | List of supported user code types
`sup_userstatus` | ["enabled", "disabled"]    | List of supported user code types
`sup_usertypes`  | ["master", "unrestricted"] | List of supported user code types

### Color control service

The service has to be used to control color components of a lightning device.

#### Service names

`color_ctrl`

#### Interfaces

Type | Interface            | Value type |  Description
-----|----------------------|------------|-------------------
in   | cmd.color.get_report | null       | The command is a request for a map of color component values
in   | cmd.color.set        | int_map    | value is a map of color components. val= {"red":200, "green":100, "blue":45}
out  | evt.color.report     | int_map    | Map of color components, where value is component intensity.

#### Service props

Name             | Value example            | Description
-----------------|--------------------------|-------------
`sup_components` | ["red", "green", "blue"] | List of supported color components

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

### Fan control service

The service has to be used to control a fan operational modes, speed and receive state updates.

#### Service names

`fan_ctrl`

#### Interfaces

Type | Interface              | Value type |  Description
-----|------------------------|------------|-------------------
in   | cmd.lvl.get_report     | null       | The command is a request for current fan speed level.
in   | cmd.lvl.set            | int        | Fan speed, value 0 - 100 %
out  | evt.lvl.report         | null       | Current fan speed level.
-|||
in   | cmd.mode.get_report    | null       | The command is a request for current fan mode report.
in   | cmd.mode.set           | string     | Fan mode. Supported values: auto_low, auto_high, auto_mid, low, high, mid,  humid_circulation, up_down,  left_right, quiet
out  | evt.mode.report        | string     | Current fan mode
-|||
in   | cmd.modelvl.get_report | string     | The command is a request for fan speed level for particular mode. If mode is set to "", the device should report levels for all modes.
in   | cmd.modelvl.set        | int_map    | val = {"mid":90, "auto_low":10}
out  | evt.modelvl.report     | int_map    | val = {"mid":90, "auto_low":10}
-|||
in   | cmd.state.get_report   | null       | The command is a request for current fan state report
out  | evt.state.report       | string     | Report operational state. Supported values: idle, low, high, mid

#### Service props

Name         | Value example      | Description
-------------|--------------------|-------------
`sup_modes`  | auto_low, auto_mid | List of supported modes
`sup_states` | idle, low, high    |

### Siren service

#### Service names

`siren_ctrl`

#### Interfaces

Type | Interface           | Value type | Description
-----|---------------------|------------|------------
in   | cmd.mode.get_report | null       |
in   | cmd.mode.set        | string     | Control siren using selected tone
out  | evt.mode.report     | string     |

Topic example: `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:siren_ctrl/ad:15_0`

#### Service props

Name             | Value example       | Description
-----------------|---------------------|-------------
`sup_modes`      | on, off, fire, leak | List of supported tones

### Barrier control service

The service represent devices like garage door openers, barriers, window protection shades, etc.

#### Service names

`barrier_ctrl`

#### Interfaces

Type | Interface                | Value type | Description
-----|--------------------------|------------|------------
in   | cmd.notiftype.get_report | null       |
in   | cmd.notiftype.set        | bool_map   | Configuration of notification type device is is using while opening/closing door.
out  | evt.notiftype.report     | bool_map   |
-|||
in   | cmd.op.stop              | null       | Emergency stop of any operation.
-|||
in   | cmd.state.get_report     | null       | Get current state
out  | evt.state.report         | string     | Current state
-|||
in   | cmd.tstate.set           | string     | Setting target state

#### Service props

Name             | Value example                  | Description
-----------------|--------------------------------|-------------
`sup_notiftypes` | audio, visual                  | supported notification-types, like siren, flashlight
`sup_states`     | open, closed, closing, opening | supported states
`sup_tstates`    | open, closed                    | supported target states

### Complex alarm system service

The service represents alarm system or sub-system with internal logic. It can be either an app or complex alarm device.

#### Service names

`complex_alarm_system`

#### Interfaces

Type | Interface         | Value type | Description
-----|-------------------|------------|------------
in   | cmd.alarm.silence | string     | Silence sirens without ceasing alarm situation.

### Gateway service

The service represents gateway, hub or host computer. Adapter topic should be used to communicate with gateway service, *pt:j1/mt:evt/rt:ad/rn:gateway/ad:1* and *pt:j1/mt:evt/rt:ad/rn:gateway/ad:1*.


#### Service names

`gateway`

#### Interface

Type | Interface                 | Value type | Description
-----|---------------------------|------------|------------
in   | cmd.gateway.factory_reset | null       | Instructs gateway to perform factory reset
in   | cmd.gateway.reboot        | null       | Gateways reboot
in   | cmd.gateway.shutdown      | null       | Gateways shutdown
out  | evt.gateway.factory_reset | null       | Factory reset event

### Indicator service

The service represents indicator device e.g. a simple visual indicator like an LED element, text based indicator like small LCD screen, etc. Some indicators can be composed of several components, for instance multiple LED segments or multiple LCD displays in one device, where one can display temperature another can display humidity, etc. Indicator components are set independently by using different keys in message payload (`val`).

#### Service names

`indicator_ctrl`

#### Interfaces

Type | Interface                          | Value type | Properties | Description
-----|------------------------------------|------------|------------|------------
in   | cmd.indicator.set_visual_element   | int_map    | duration   | Requests visual element (led or some other light source) to display information. Key is a name of indicator component and value is actual value to set. Duration property defines how long the indicator should display the information
in   | cmd.indicator.set_text             | str_map    | duration   | Requests text indicator to display text. Key is name of indicator component and value is text to be displayed by the component. Duration property defines how long the indicator should display the information

### Product Specific Services

Documentation of product specific service can be found [here](product-specific-services.md).

### Time service

Service used to read time and date information.

#### Service names

`time`

#### Interface

Type | Interface           | Value type | Description
-----|---------------------|------------|------------
in   | cmd.time.get_report | null       | Get current time (from Z-wave node)
in   | cmd.date.get_report | null       | Get current date
out  | evt.date.report     | int_map    | Date report
out  | evt.date.report     | int_map    | Time report

### Time parameters service

The Time Parameters service is used to set date and time. Time zone offset and daylight savings may be set in the Time Parameters service if necessary. The data formats is ISO-8601 compliant.

Examples can be found in [Time.md](z-wave/Time.md) in the z-wave folder.

Note: In the case where the clock is updated via an external source such as SAT, internet, Rugby/Frankfurt source, omit this service.

#### Service names

`time_parameters`

#### Interface

Type | Interface                      | Value type | Description
-----|--------------------------------|------------|------------
in   | cmd.time_parameters.get_report | null       | Get current time parameters
in   | cmd.time_parameters.set        | int_map    | Sets current time parameters
out  | evt.time_parameters.report     | int_map    | Time parameters report

Examples can be found in [Time.md](z-wave/Time.md) in the z-wave folder.


### Schedule Entry Service

This service handles a schedule slot for an user who already has valid user access code [user_code](#user-code-service) service. The [year day schedule](z-wave/User_Code.md#schedule_entry_lock) represents two days, any time apart, where the specified user ID’s code is valid. When setting the schedule slot, the start parameters of the time fence needs to occur prior to the stop parameters and the year day schedule is automatically enabled for the identified user.

Note: Each user can only use one type of scheduling at a time.

Detailed specification is avaliable in [User_Code.md](z-wave/User_Code.md) in the z-wave folder.

#### Service names

`schedule_entry`

#### Interface

Type | Interface                     | Value type | Description
-----|-------------------------------|------------|------------
in   | cmd.schedule_entry.get_report | null       | Get schedule entry report for specified slot
in   | cmd.schedule_entry.set        | int_map    | Set schedule entry
in   | cmd.schedule_entry.clear      | int_map    | Clear schedule entry
out  | evt.schedule_entry.report     | int_map    | Schedule entry report
