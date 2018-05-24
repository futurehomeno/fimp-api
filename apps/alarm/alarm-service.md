## Alarm service API 

In case of alarm situation the service generated message : 

**Topic**:pt:j1/mt:evt/rt:app/rn:alarm_service/ad:1
**Service**:alarm_service
**Interface**:evt.alarm.ext_report
**Payload**:

```json 
{
  "type": "evt.alarm.ext_report",
  "serv": "alarm_service",
  "val_t": "",
  "val": {
    "device_desc": "",
    "device_id": "23",
    "event": "fire",
    "location_desc": "kitchen",
    "location_id": "",
    "status": "activ",
    "trans_nr": "819999999999"
  },
  "tags": null,
  "props": {},
  "ver": "",
  "corid": "",
  "ctime": "2018-05-23T16:23:35+0200",
  "uid": ""
}
```

After alarm situation was cleared the service sends deactivate event : 

**Topic**:pt:j1/mt:evt/rt:app/rn:alarm_service/ad:1
**Service**:alarm_service
**Interface**:evt.alarm.ext_report
**Payload**:

```json 
{
  "type": "evt.alarm.ext_report",
  "serv": "alarm_service",
  "val_t": "",
  "val": {
    "device_desc": "",
    "device_id": "23",
    "event": "fire",
    "location_desc": "kitchen",
    "location_id": "",
    "status": "deactiv",
    "trans_nr": "819999999999"
  },
  "tags": null,
  "props": {},
  "ver": "",
  "corid": "",
  "ctime": "2018-05-23T16:23:35+0200",
  "uid": ""
}
```