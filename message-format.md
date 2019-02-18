### FIMP message format 

#### FIMP topic format format .


##### Device service topic

pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:sensor_presence/ad:16_0

pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:out_bin_switch/ad:15_0

##### Technology adapter topic

pt:j1/mt:evt/rt:app/rn:cloud-bridge/ad:1

pt:j1/mt:cmd/rt:app/rn:cloud-bridge/ad:1

##### Application topic 

pt:j1/mt:evt/rt:ad/rn:zigbee/ad:1

pt:j1/mt:cmd/rt:ad/rn:zigbee/ad:1

##### Cloud API topic 

pt:j1/mt:evt/rt:cloud/rn:auth-api/ad:1

pt:j1/mt:cmd/rt:cloud/rn:auth-api/ad:1


##### FIMP json format . 
 

Fields :

* type - interface type , definese message format .
* serv - service name the interface is part of . 
* val_t - value type defines data format of *val* field.
* val - value , it can be either simple type of complex object.
* tags - list of tags , where each element is a string . (Optional)
* props - map of properties , where key and value are strings .(Optional)
* ctime - message creation time .
* ver - version of the message format .
* uid - message unique identifier .
* corid - message correlation id . Is used for request - response correlation . (Optional) 

List of supported value types : 

* string 
* int 
* float 
* bool 
* null
* str_array
* int_rray 
* float_array
* int_map
* str_map
* float_map
* bool_map
* object - is a complex object which can't be mapped to primitive types . The structure of an object is defined by interface type and is unique 
for every interface type . 
* base64

Message example: 

```javascript

{
 	"type":"evt.sensor.report",
 	"serv":"temp_sensor",
 	"valType":"float",
 	"val":21.5,
 	"tags":["tag1","alarm"],
 	"props":{"prop1":"4","prop2:"6"},
 	"ctime":"2016-12-21T13:34:14.085581515+01:00",
 	"ver":"1.0",
 	"corid":"uid_of_request",
 	"uid":"fb033c27-e7b5-4834-97ec-632ccb987e9e"
}
```

	










