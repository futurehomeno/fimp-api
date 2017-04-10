# FIMP service catalog 

## List of technology independent service.

### Basic service 
Service name : **basic**

Description  : Meaning of **basic** service can vary from device to device . It's generic and most simple way to interact with a device . 

Type  | Interface                | Value type | Description 
------|--------------------------|------------|------------
out   | evt.level.report         | int        | A level report using numeric value 
in    | cmd.level.set            | int        | Set level using numeric value 
in    | cmd.level.get_report     | null       | 

***

### Device system service 
Service name : **dev_sys**

Type  | Interface                | Value type | Description 
------|--------------------------|------------|------------
out   | evt.config.report        | str_map    | Settings are in form of key - value pairs . 
in    | cmd.config.set           | str_map    | 
in    | cmd.config.get_report    | str_array  | Command requests service to respond with config report . 
out   | evt.group.members_report | object     | Object structure {"group":"group1","members":["node1","node2"]} 
in    | cmd.group.add_members    | object     | Command adds members to a group. Object has the same format as members_report
in    | cmd.group.delete_members | object     | Object has the same format as report. 
in    | cmd.group.get_members    | string     | Value is a group name . 

***

### Output binary switch service 


Service name : **out_bin_switch** 

Description  : The service is normally provided by wallplugs , relays , simple sirens , etc . 

Type  | Interface                | Value type | Description 
------|--------------------------|------------|------------ 
out   | evt.binary.report        | bool       | Reports true when switch is on and false whenr switch is off 
in    | cmd.binary.set           | bool       | 
in    | cmd.binary.get_report    | null       | 

***

### Electric meter service 
Service name : **meter_elec** 

Description  : The service is used by electricity meters to report consumption . 

Type  | Interface                | Value type | Properties                | Description 
------|--------------------------|------------|---------------------------|------------- 
out   | evt.meter.report         | float      | unit , prv_data , delta_t | prv_data - previous meter reading , delta_t - time delta 
in    | evt.meter.reset          | null       |                           | Resets all historical readings . 
in    | evt.meter.get_report     | string     |                           | Value - is a unit . May not be supported by all meter .

Supported units : kWh , kVAh , W , pulse_c , V , A , power_factor  

### Gas meter service 
Service name : **meter_gas** 

Description  : The service is used by gas meters to report consumption . Has the same interfaces as Electric meter service. 

Supported units : 

### Water meter service 
Service name : **meter_water** 

Description  : The service is used by water meters to report consumption . Has the same interfaces as Electric meter service.

***

### Sensor service 
Service name : **sensor_temp** , **sensor_gp** , **sensor_lumin** , **sensor_power** , **sensor_humid** , **sensor_veloc** , **sensor_winddir** , **sensor_atmo** , **sensor_baro** , **sensor_solarrad** , **sensor_dew** , **sensor_rain** , **sensor_tidelvl** , **sensor_weight** , **sensor_voltage** , **sensor_current** , **sensor_co2** , **sensor_airflow** , **sensor_tank** , **sensor_distance** , **sensor_anglepos** , **sensor_rotation** , **sensor_seismicint** , **sensor_uv** , **sensor_elresist** , 
  
Description :  

 Type  | Interface                | Value type | Properties                | Description 
-------|--------------------------|------------|---------------------------|------------- 
out    | evt.sensor.report        | float      | unit                      | 
in     | cmd.sensor.get_report    | string     |                           | Value is desired unit. Default is empty .  

 Service name       | Units | Description 
 -------------------|-------|------------
 sensor_temp        | C, F  | Temperature 
 sensor_gp          |       | General purpose  
