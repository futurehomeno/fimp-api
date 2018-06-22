## Andgry Dog API 
AngryDog - is device and system monitoring service for edge gateways . 

Whenever monitoring service fails to contact a device, it generates the message : 

**Topic**:pt:j1/mt:evt/rt:app/rn:angry_dog/ad:1

**Service**:angry_dog

**Interface**:evt.alarm.dev_mon_report

**Payload**:

```json 
{
  "type": "evt.alarm.dev_mon_report",
  "serv": "angry_dog",
  "val_t": "str_map",
  "val": {
    "event": "contact_lost",
    "device_id": "23",
    "device_address":"zw:45",
    "device_name":"",
    "location_desc": "kitchen",
    "location_id": "",
    "description":"",
    "power_source":"ac"
  },
  "tags": null,
  "props": {},
  "ver": "",
  "corid": "",
  "ctime": "2018-05-23T16:23:35+0200",
  "uid": ""
}
```
***Supported events***: contact_lost, contact_established,low_battery
