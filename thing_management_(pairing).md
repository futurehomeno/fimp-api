# Thing Management (Pairing)

The following APIs should be common across all adapters, but the example code will use zwave-ad. Notes have been added for specific differences for the most common adapters.

## Adding a thing to FH system

Inclusion process generally consists of 2 steps:

1. An application sends inclusion command to adapter. This indicates the beginning of the adding process.
2. Adapter generates inclusion_report event right after a thing was added. This indicates the end of the adding process.

ZigBee allows you to add multiple devices in one go, thus the generation of an inclusion report does not end the pairing process. Instead, the user has to manually stop the process or wait for it to time out.

### Starting inclusion

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

    {
        "serv": "zwave-ad",
        "type": "cmd.thing.inclusion",
        "val_t": "bool",
        "val": true,
        "props": null,
        "tags": null,
        "ctime": "1970-01-01T00:00:00+0000",
        "uid": "123456789"
    }

### Stopping inclusion

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

    {
        "serv": "zwave-ad",
        "type": "cmd.thing.inclusion",
        "val_t": "bool",
        "val": false,
        "props": null,
        "tags": null,
        "ctime": "1970-01-01T00:00:00+0000",
        "uid": "123456789"
    }

### Sample inclusion report

Topic: `pt:j1/mt:evt/rt:ad/rn:zw/ad:1`

Message (report):

    {
        "serv": "zwave-ad",
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
                    "zw_supported_cc": []
                }
            },
            "services": [
                {
                    "address": "/rt:dev/rn:zw/ad:1/sv:basic/ad:21_0",
                    "groups": ["ch_0"],
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
                    "groups": ["ch_0"],
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
                    "address": "/rt:dev/rn:zw/ad:1/sv:dev_sys/ad:21_0",
                    "groups": ["ch_0"],
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
        "ctime": "1970-01-01T00:00:00+0000",
        "uid": "123456789",
        "props": {},
        "tags": []
    }

### Getting inclusion report

An adapter should always respond with an inclusion report on `get_inclusion_report` command. In the following example, we ask for the inclusion report for the device with node-id of 22 on the zwave adapter.

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

    {
        "serv": "zwave-ad",
        "type": "cmd.thing.get_inclusion_report",
        "val_t": "string",
        "val": "22",
        "props": null,
        "tags": null,
        "ctime": "1970-01-01T00:00:00+0000",
        "uid": "123456789"
    }

## Removing a thing from FH system

There are two main ways of excluding a device:

Exclusion process type 1 (zwave): The process consist of 2 steps:

1. An application sends exclusion command to adapter, adapter goes into exclusion mode, after that user can exclude device from network by triggering exclusion sequence on the device.
2. Adapter generates exclusion_report event right after a thing was removed from system.

Exclusion process type 2 (zigbee): The process consist of 2 steps:

1. User finds device in UI which he wants to delete and clicks "Delete" button, UI sends special delete command with device address to adapter and adapter removes the device from network.
2. Adapter generates exclusion_report event right after a thing was deleted from system.

### Starting exclusion

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

    {
        "serv": "zwave-ad",
        "type": "cmd.thing.exclusion",
        "val_t": "bool",
        "val": true,
        "props": null,
        "tags": null,
        "ctime": "1970-01-01T00:00:00+0000",
        "uid": "123456789"
    }

### Stopping exclusion

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

    {
        "serv": "zwave-ad",
        "type": "cmd.thing.exclusion",
        "val_t": "bool",
        "val": false,
        "props": null,
        "tags": null,
        "ctime": "1970-01-01T00:00:00+0000",
        "uid": "123456789"
    }

### Sample exclusion report

Topic: `pt:j1/mt:evt/rt:ad/rn:zw/ad:1`

Message (report):

    {
        "props": {},
        "serv": "zwave-ad",
        "tags": [],
        "type": "evt.thing.exclusion_report",
        "val": {
            "address": "24"
        },
        "val_t": "object",
        "ctime": "1970-01-01T00:00:00+0000",
        "uid": "123456789"
    }

### Delete specific thing

The following example will delete the device with address id 1 from the network.

Topic: `pt:j1/mt:cmd/rt:ad/rn:zigbee/ad:1`

Message (command):

    {
        "serv": "zigbee-ad",
        "type": "cmd.thing.delete",
        "val_t": "str_map",
        "val": {
            "address": "1",
            "stop": ""
        },
        "props": null,
        "tags": null,
        "ctime": "1970-01-01T00:00:00+0000",
        "uid": "123456789"
    }
