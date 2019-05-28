### Application and adapter discovery protocol 

Every applicatoin or adapter which participates in service discover has to subscribe to well known discovery topic . 

**Well known discovery topic** : pt:j1/mt:cmd/rt:discovery

In order to discover application or adapter , interested application has to send discovery request message to well known address .
Whenever an application or adapter receives discovery request it has to respond with dicovery event . 

**Discovery response event topic** : pt:j1/mt:evt/rt:discovery 


Discovery request : 

```json

{
  "serv": "system",
  "type": "cmd.discovery.request",
  "val_t": "null",
  "val": null,
  "tags": null,
  "props": null,
  "ver": "1",
  "corid": "",
  "ctime": "2019-05-27T17:01:17.148+05:00",
  "uid": "8d7941e6-5a82-4f88-8403-63a0bd543e2a"
}

```

Discovery reply for application resource: 

```json 

{
  "type": "evt.discovery.report",
  "serv": "system",
  "val_t": "object",
  "val": {
    "resource_name": "smart-hvac",
    "resource_type": "app",
    "resource_full_name": "Smart HVAC controller",
    "description": "",
    "author": "dev@futurehome.no",
    "version": "1",
    "app_info": {
      "services": [
        {
          "name": "thermostat",
          "alias": "Set thermostat",
          "address": "rt:app/rn:smart-hvac/ad:1",
          "enabled": false,
           "interfaces": [
          {
            "intf_t": "in",
            "msg_t": "cmd.setpoint.set",
            "val_t": "str_map",
            "ver": "1"
          },
          {
            "intf_t": "in",
            "msg_t": "cmd.setpoint.get_report",
            "val_t": "string",
            "ver": "1"
          },
          {
            "intf_t": "out",
            "msg_t": "evt.setpoint.report",
            "val_t": "str_map",
            "ver": "1"
          },
          {
            "intf_t": "in",
            "msg_t": "cmd.mode.set",
            "val_t": "string",
            "ver": "1"
          },
          {
            "intf_t": "in",
            "msg_t": "cmd.mode.get_report",
            "val_t": "null",
            "ver": "1"
          },
          {
            "intf_t": "out",
            "msg_t": "evt.mode.report",
            "val_t": "string",
            "ver": "1"
          }
        ]
        }
      ]
    },
   "config_required": false,
    "configs": null,
    "props": null,
    "doc_url": "",
    "is_instance_configurable": false,
    "instance_id": "1"
  },
  "tags": null,
  "props": null,
  "ver": "1",
  "corid": "",
  "ctime": "2019-05-27T17:01:17.15+05:00",
  "uid": "b30cebdb-5f68-4fc1-8767-8a9367cb5fb9"
}

```


Discovery reply for adapter resource : 

```json 

{
  "type": "evt.discovery.report",
  "serv": "system",
  "val_t": "object",
  "val": {
    "resource_name": "canbus",
    "resource_type": "app",
    "resource_full_name": "Canbus adapter",
    "description": "",
    "author": "dev@futurehome.no",
    "version": "1",
    "adapter_info": {
      "fw_version": "v0.2.52",
      "technology": "canbus",
      "hw_dependency": {"serial_port":"/dev/ttyUSB1"},
      "network_management_type": "full_sync",
      "services": null
    },
    "config_required": false,
    "configs": null,
    "props": null,
    "doc_url": "",
    "is_instance_configurable": false,
    "instance_id": "1"
  },
  "tags": null,
  "props": null,
  "ver": "1",
  "corid": "",
  "ctime": "2019-05-27T17:01:17.15+05:00",
  "uid": "b30cebdb-5f68-4fc1-8767-8a9367cb5fb9"
}

```