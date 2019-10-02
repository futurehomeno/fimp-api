# Technology adapter API

## Adding a thing to FH system

Inclusion process consists of 2 steps:

1. An application sends inclusion command to adapter.

2. Adapter generates inclusion_report event right after a thing was added.

### Inclusion command

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message:

```json
{
    "serv": "zwave-ad",
    "type": "cmd.thing.inclusion",
    "val_t": "bool",
    "val": true,
    "props": null,
    "tags": null,
    "ctime": "2017-08-23T12:07:00+0200",
    "uid": "124235254"
}
```
### Inclusion report

Topic: `pt:j1/mt:evt/rt:ad/rn:zw/ad:1`

Message:

```json
{
    "ctime": "2017-07-25T17:53:12+0200",
    "props": {},
    "serv": "zwave-ad",
    "tags": [],
    "type": "evt.thing.inclusion_report",
    "val": {
        "address": "21",
        "category": "UNKNOWN ",
        "comm_tech": "zw",
        "device_type":"dimmer",
        "device_id": "",
        "hw_ver": "1",
        "is_sensor": "0",
        "manufacturer_id": "134",
        "power_source": "0",
        "product_hash": "zw_134_3_116",
        "product_id": "3_116",
        "prop_set": {
            "nif_0": {
                "zw_generic_dev_class": "16",
                "zw_installer_icon": "1792",
                "zw_node_type": "0",
                "zw_plus_version": "1",
                "zw_role_type": "5",
                "zw_specific_dev_class": "1",
                "zw_supported_cc": [

                ]
            }
        },
        "services": [
            {
                "address": "/rt:dev/rn:zw/ad:1/sv:basic/ad:21_0",
                "groups": [
                    "ch_0"
                ],
                "interfaces": [
                    {
                        "intf_t": "out",
                        "msg_t": "evt.lvl.report",
                        "val_t": "int",
                        "ver": "1"
                    },
                    {
                        "intf_t": "in",
                        "msg_t": "cmd.lvl.set",
                        "val_t": "int",
                        "ver": "1"
                    },
                    {
                        "intf_t": "in",
                        "msg_t": "cmd.lvl.get_report",
                        "val_t": "null",
                        "ver": "1"
                    }
                ],
                "location": "",
                "name": "basic",
                "prop_set_ref": "nif_0",
                "props": {
                    "is_secure": false,
                    "is_unsecure": true
                }
            },
            {
                "address": "/rt:dev/rn:zw/ad:1/sv:out_bin_switch/ad:21_0",
                "groups": [
                    "ch_0"
                ],
                "interfaces": [
                    {
                        "intf_t": "out",
                        "msg_t": "evt.binary.report",
                        "val_t": "bool",
                        "ver": "1"
                    },
                    {
                        "intf_t": "in",
                        "msg_t": "cmd.binary.set",
                        "val_t": "bool",
                        "ver": "1"
                    },
                    {
                        "intf_t": "in",
                        "msg_t": "cmd.binary.get_report",
                        "val_t": "null",
                        "ver": "1"
                    }
                ],
                "location": "",
                "name": "out_bin_switch",
                "prop_set_ref": "nif_0",
                "props": {
                    "is_secure": false,
                    "is_unsecure": true
                }
            },
            {
                "address": "/rt:dev/rn:zw/ad:1/sv:meter_elec/ad:21_0",
                "groups": [
                    "ch_0"
                ],
                "interfaces": [
                    {
                        "intf_t": "out",
                        "msg_t": "evt.meter.report",
                        "val_t": "float",
                        "ver": "1"
                    },
                    {
                        "intf_t": "in",
                        "msg_t": "cmd.meter.reset",
                        "val_t": "null",
                        "ver": "1"
                    },
                    {
                        "intf_t": "in",
                        "msg_t": "cmd.meter.get_report",
                        "val_t": "string",
                        "ver": "1"
                    }
                ],
                "location": "",
                "name": "meter_elec",
                "prop_set_ref": "nif_0",
                "props": {
                    "is_secure": false,
                    "is_unsecure": true,
                    "sup_units": [
                        "kWh",
                        "W",
                        "V",
                        "A"
                    ]
                }
            },
            {
                "address": "/rt:dev/rn:zw/ad:1/sv:alarm_heat/ad:21_0",
                "groups": [
                    "ch_0"
                ],
                "interfaces": [
                    {
                        "intf_t": "out",
                        "msg_t": "evt.alarm.report",
                        "val_t": "str_map",
                        "ver": "1"
                    },
                    {
                        "intf_t": "in",
                        "msg_t": "cmd.alarm.get_report",
                        "val_t": "string",
                        "ver": "1"
                    }
                ],
                "location": "",
                "name": "alarm_heat",
                "prop_set_ref": "nif_0",
                "props": {
                    "is_secure": false,
                    "is_unsecure": true,
                    "sup_events": [
                        "overheat"
                    ]
                }
            },
            {
                "address": "/rt:dev/rn:zw/ad:1/sv:alarm_power/ad:21_0",
                "groups": [
                    "ch_0"
                ],
                "interfaces": [
                    {
                        "intf_t": "out",
                        "msg_t": "evt.alarm.report",
                        "val_t": "str_map",
                        "ver": "1"
                    },
                    {
                        "intf_t": "in",
                        "msg_t": "cmd.alarm.get_report",
                        "val_t": "string",
                        "ver": "1"
                    }
                ],
                "location": "",
                "name": "alarm_power",
                "prop_set_ref": "nif_0",
                "props": {
                    "is_secure": false,
                    "is_unsecure": true,
                    "sup_events": [
                        "over_current"
                    ]
                }
            },
            {
                "address": "/rt:dev/rn:zw/ad:1/sv:dev_sys/ad:21_0",
                "groups": [
                    "ch_0"
                ],
                "interfaces": [
                    {
                        "intf_t": "out",
                        "msg_t": "evt.config.report",
                        "val_t": "str_map",
                        "ver": "1"
                    },
                    {
                        "intf_t": "in",
                        "msg_t": "cmd.config.set",
                        "val_t": "str_map",
                        "ver": "1"
                    },
                    {
                        "intf_t": "in",
                        "msg_t": "cmd.config.get_report",
                        "val_t": "str_array",
                        "ver": "1"
                    },
                    {
                        "intf_t": "out",
                        "msg_t": "evt.group.members_report",
                        "val_t": "object",
                        "ver": "1"
                    },
                    {
                        "intf_t": "in",
                        "msg_t": "cmd.group.add_members",
                        "val_t": "object",
                        "ver": "1"
                    },
                    {
                        "intf_t": "in",
                        "msg_t": "cmd.group.delete_members",
                        "val_t": "object",
                        "ver": "1"
                    },
                    {
                        "intf_t": "in",
                        "msg_t": "cmd.group.get_members",
                        "val_t": "string",
                        "ver": "1"
                    }
                ],
                "location": "",
                "name": "dev_sys",
                "prop_set_ref": "nif_0",
                "props": {
                    "is_secure": false,
                    "is_unsecure": true
                }
            }
        ],
        "sw_ver": "257",
        "tech_specific_props": {
            "zw_lib_type": "3",
            "zw_product_id": "116",
            "zw_product_type": "3",
            "zw_protocol_ver": "1062",
            "zw_sleep_capable": "0"
        },
        "wakeup_interval": "-1"
    },
    "val_t": "object",
    "ctime":"2017-08-23T12:07:00+0200",
    "uid":"124235254"
}
```

In addition, an addapter should always respond with inclusion report on `get_inclusion_report` command:

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message:

```json
{
    "serv": "zwave-ad",
    "type": "cmd.thing.get_inclusion_report",
    "val_t": "string",
    "val": "22",
    "props": null,
    "tags": null
}
```

## Removing a thing from FH system

Exclusion process type 1 (zwave). The process consist of 2 steps:

1. An application sends exclusion command to adapter, adapter goes into exclusion mode, after that user can exclude device from network by triggering exclusion sequence on the device.

2. Adapter generates exclusion_report event right after a thing was removed from system.

Exclusion process type 2 (zigbee). The process consist of 2 steps:

1. User finds device in UI which he wants to delete and clicks "Delete" button, UI sends special delete command with device address to adapter and adapter removes the device from network.

2. Adapter generates exclusion_report event right after a thing was deleted from system.

### Exclusion command

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message:

```json
{
    "serv": "zwave-ad",
    "type": "cmd.thing.exclusion",
    "val_t": "bool",
    "val": false,
    "props": null,
    "tags": null,
    "ctime":"2017-08-23T12:07:00+0200",
    "uid":"124235254"
}
```

### Exclusion report

Topic: `pt:j1/mt:evt/rt:ad/rn:zw/ad:1`

Message:

```json
{
    "ctime": "2017-07-25T18:07:49+0200",
    "props": {},
    "serv": "zwave-ad",
    "tags": [],
    "type": "evt.thing.exclusion_report",
    "val": {
        "address": "24"
    },
    "val_t": "object",
    "ctime":"2017-08-23T12:07:00+0200",
    "uid":"124235254"
}
```

### Delete device from network command:

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message:

```json
{
    "serv": "zwave-ad",
    "type": "cmd.thing.delete",
    "val_t": "str_map",
    "val": {
        "address": "71",
        "stop": ""
    },
    "props": null,
    "tags": null,
    "ctime":"2017-08-23T12:07:00+0200",
    "uid":"124235254"
}
```

## Error reporting.

Topic: `pt:j1/mt:evt/rt:ad/rn:zw/ad:1` or service address: `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:dev_sys/ad:95_0`

Message:

```json
{
    "serv": "zigbee",
    "type": "evt.error.report",
    "val": "TX_ERROR",
    "val_t": "string",
    "props": {
        "msg": "TRANSMIT_COMPLETE_NOROUTE",
        "src": "nodeId=64_0"
    },
    "tags": [],
    "ctime": "2018-11-22T23:14:40+0100",
    "uid":"76533455876765"
 }
```

val - is error code, src - origin of the error.

## Requesting list of devices from adapter.

An adapter has to support api for requesting a list of devices and respond with the list.

### Command

Topic: `pt:j1/mt:cmd/rt:ad/rn:zigbee/ad:1`

Message:

```json
{
    "serv": "zigbee",
    "type": "cmd.network.get_all_nodes",
    "val_t": "null",
    "val": null,
    "props": null,
    "tags": null,
    "ctime": "2018-11-22T23:14:40+0100",
    "uid":"76533455876765"
}
```

### Report event

Topic: `pt:j1/mt:evt/rt:ad/rn:zigbee/ad:1`

Message:

```json
{
    "ctime": "2018-11-23T16:53:11+0100",
    "props": {},
    "serv": "zigbee",
    "tags": [],
    "type": "evt.network.all_nodes_report",
    "val": [
        {
            "address": "46",
            "alias":"Sensor 1 ",
            "hash": "zw_398_3_12",
            "power_source": "battery",
            "status": "DOWN",
            "wakeup_int": "4200"
        },
        {
            "address": "63",
            "alias":"Sensor 2 ",
            "hash": "zw_271_1794_4096",
            "power_source": "battery",
            "status": "UP",
            "wakeup_int": "3600"
        },
        {
            "address": "80",
            "alias":"Dimmer ",
            "hash": "zw_134_3_96",
            "power_source": "ac",
            "status": "UP",
            "wakeup_int": "-1"
        }
    ],
    "val_t": "object"
}
```

address - is technology specific device address

alias (optional) - device or product name or alias

hash (optional) - product unique identifier

power_source - power source descriptor, ac,battery

status (optional) - device status

wakeup_int (optional) - device wakeup interval, applicable only if device is battery powered.

## Certification Test

Supported by zigbee-ad. When `cmd.cert_test.start` is received, the transiever starts sending `cmd.binary.set` to the device which node id and endpoint are provided in the payload every 50ms. When `cmd.cert_test.stop` is received the test is stopped.

__Topic__

`pt:j1/mt:cmd/rt:ad/rn:zigbee/ad:1`

__Message__

`val` has the format `<node_id>_<endpoint_id>`. It only matters in the start command.

```json
{
    "type": "cmd.cert_test.start",
    "val_t": "string",
    "val": "1_1",
    "props": null,
    "tags": null,
    "src": "thingsplex-ui",
    "ver": "1"
}
```

```json
{
    "type": "cmd.cert_test.stop",
    "val_t": "string",
    "val": "1_1",
    "props": null,
    "tags": null,
    "src": "thingsplex-ui",
    "ver": "1"
}
```
