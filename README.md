# FIMP service catalog 

### Service cocept.
FIMP protocol is based on everything-is-a-service concept . 

![Service concept](static/service_concept.png) 

### List of technology independent services.

## Basic service 
Service name : **basic**

Description  : Meaning of **basic** service can vary from device to device . It's generic and most simple way to interact with a device . 

Type  | Interface                | Value type | Description 
------|--------------------------|------------|------------
out   | evt.level.report         | int        | Reports level using numeric value 
in    | cmd.level.set            | int        | Sets level using numeric value 
in    | cmd.level.get_report     | null       | 

***

## Device/Thing system service 
Service name : **dev_sys**

Type  | Interface                | Value type | Description 
------|--------------------------|------------|------------
out   | evt.config.report        | str_map    | Reports configurations in form of key-value pairs . 
in    | cmd.config.set           | str_map    | Sets configuration . Value is a key-value pairs.
in    | cmd.config.get_report    | str_array  | Requests service to respond with config report . 
out   | evt.group.members_report | object     | Object structure {"group":"group1","members":["node1","node2"]} 
in    | cmd.group.add_members    | object     | Adds members to the group. Object has the same format as members_report
in    | cmd.group.delete_members | object     | Object has the same format as report. 
in    | cmd.group.get_members    | string     | Value is a group name . 

***

## Output binary switch service 

Service name : **out_bin_switch** 

Description  : The service is provided by wallplugs , relays , simple sirens , etc . 

Type  | Interface                | Value type | Description 
------|--------------------------|------------|------------ 
out   | evt.binary.report        | bool       | Reports true when switch is ON and false whenr switch is OFF 
in    | cmd.binary.set           | bool       | 
in    | cmd.binary.get_report    | null       | 

***

## Meter service 
Service name : Refer to the table below.

Description  : The service is used by meters to report consumption . 

Type  | Interface                | Value type | Properties                | Description 
------|--------------------------|------------|---------------------------|------------- 
out   | evt.meter.report         | float      | unit , prv_data , delta_t | prv_data - previous meter reading , delta_t - time delta 
in    | evt.meter.reset          | null       |                           | Resets all historical readings . 
in    | evt.meter.get_report     | string     |                           | Value - is a unit . May not be supported by all meter .

Supported meter types and their units : 

Service name       | Units                               | Description 
 ------------------|-------------------------------------|------------
 meter_elec        | kWh,kVAh,W,pulse_c,V,A,power_factor | Electric meter 
 meter_gas         | cub_m,cub_f,pulse_c                 | Gas meter 
 meter_water       | cub_m,cub_f,galon,pulse_c           | Water meter 

***

## Sensor service 
Service name : Refer to the table below . 
  
Description :  

 Type  | Interface                | Value type | Properties                | Description 
-------|--------------------------|------------|---------------------------|------------- 
out    | evt.sensor.report        | float      | unit                      | 
in     | cmd.sensor.get_report    | string     |                           | Value is desired unit. Use empty value to get report in default unit .   

 Supported sensor type and their units :

 Service name       | Units                 | Description 
 -------------------|-----------------------|------------
 sensor_temp        | C, F                  | Temperature sensor
 sensor_gp          | % , NOM               | General purpose sensor  
 sensor_lumin       | Lux , %               | Luminance sensor
 sensor_power       | W,Btu/h               | Power sensor . Btu/h - British thermal unit per hour
 sensor_humid       | %,g/m3                | Relative humidity sensor
 sensor_veloc       | m/s,mph               | Velocity sensor
 sensor_direct      | deg                   | Direction sensor
 sensor_atmo        | kPa,ha                | Atmospheric pressure sensor . ha - inches of Mercury
 sensor_baro        | kPa,ha                | Barometric  pressure sensor . ha - inches of Mercury
 sensor_solarrad    | w/m2                  | Solar radiation
 sensor_dew         | C, F                  | Dew point sensor
 sensor_rain        | mm/h,in/h             | Rain rate sensor
 sensor_tidelvl     | m, ft                 | Tide level sensor
 sensor_weight      | kg, lbs               | Weight sensor
 sensor_voltage     | V, mV                 | Voltage sensor
 sensor_current     | A, mA                 | Current sensor
 sensor_co2         | ppm                   | CO2-level sensor
 sensor_co          | mol/m3                | Carbon Monoxide level sensor
 sensor_airflow     | m3/h,ft3/m            | Air flow sensor
 sensor_tank        | l,gal,m3              | Tank capacity sensor
 sensor_distance    | m,cm,ft               | Distance sensor
 sensor_anglepos    | %,degN,degS           | Angle Position sensor
 sensor_rotation    | rpm,Hz                | Rotation sensor
 sensor_seismicint  | EMCRO,LEIDO,MERC,SHDO | Seismic intensity sensor
 sensor_seismicmag  | MB,ML,MW,MS           | Seismic magnitude sensor
 sensor_uv          | index                 | Ultraviolet sensor
 sensor_elresist    | ohm/m                 | Electrical resistivity sensor
 sensor_moist       | %,kOhm,m3/m3,aw       | Moisture sensor
 sensor_freq        | Hz,kHz                | Frequency sensor
 sensor_accelx      | m/s2                  | Acceleration, X-axis
 sensor_accely      | m/s2                  | Acceleration, Y-axis
 sensor_accelz      | m/s2                  | Acceleration, Z-axis
 sensor_accelz      | m/s2                  | Acceleration, Z-axis
 sensor_watflow     | l/h                   | Water flow sensor
 sensor_watpressure | kPa                   | Water pressure sensor

Example message : [evt.sensor.report](json-v1/messages/examples/evt.sensor.report)

***

