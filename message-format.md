# FIMP message format 

## FIMP topic format format

### Device service topic

pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:sensor_presence/ad:16_0

pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:out_bin_switch/ad:15_0

### Technology adapter topic

pt:j1/mt:evt/rt:app/rn:cloud-bridge/ad:1

pt:j1/mt:cmd/rt:app/rn:cloud-bridge/ad:1

### Application topic 

pt:j1/mt:evt/rt:ad/rn:zigbee/ad:1

pt:j1/mt:cmd/rt:ad/rn:zigbee/ad:1

### Cloud API topic 

pt:j1/mt:evt/rt:cloud/rn:auth-api/ad:1

pt:j1/mt:cmd/rt:cloud/rn:auth-api/ad:1

### FIMP JSON format. 
 
Fields:

Property | Type                |Required | Desc               
---------|---------------------|---------|----------------------------------------------------------------
type     | String              | Yes     | Interface type, defines message format.
serv     | String              | Yes     | Service name the interface is part of.
val_t    | String              | Yes     | Data format of `val` field. See below.
val      | dynamic             | Yes     | "payload" - it can be either simple type or complex object.
tags     | List<String>        | No      | List of tags.
props    | Map<String, String> | Yes     | Map of properties.
ctime    | String              | Yes     | Message creation time, e.g. `"2019-05-31 17:36:31 +0200"`
ver      | String              | Yes     | Version of the message format, default: `"1"`.
uid      | String              | Yes     | Unique message identifier.
corid    | String              | No      | Message correlation id. Used for request - response matching.
src      | String              | No      | Source or of the message, should be set only for commands.
resp_to  | String              | No*     | Response topic where requester will expect to receive response.

* Required for Prime Fimp messages.

List of supported `val` types: 

* string
* int
* float 
* bool
* null
* str_array
* int_array
* float_array
* int_map
* str_map
* float_map
* bool_map
* object - A complex object which can't be mapped to primitive types. The structure of an object is defined by interface type and is unique for every interface type. 
* base64

Message example: 

```json
{
   "type": "evt.sensor.report",
   "serv": "temp_sensor",
   "val_t": "float",
   "val": 21.5,
   "tags": ["tag1", "alarm"],
   "props": {
     "prop1": "4",
     "prop2": "6"
   },
   "ctime": "2016-12-21T13:34:14.085581515+01:00",
   "ver": "1.0",
   "uid": "fb033c27-e7b5-4834-97ec-632ccb987e9e",
   "corid": "uid_of_request",
   "src": "vinculum",
   "resp_to": "/pt:j1/mt:rsp/rn:smarthome-app/ad:1"
}
```
