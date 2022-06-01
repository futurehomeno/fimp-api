# Thing Management (Pairing)

The following APIs should be common across all adapters, but the example code will use zwave-ad. Notes have been added for specific differences for the most common adapters.

## Adding a thing to FH system - SmartStart (Z-Wave only)

Smart Start inclusion is a process of adding devices with pre-configuration step using it's DSK printed on a back of a device.
With this functionality, you simply mount your device and power it on.
The devices are then automatically recognized and added to the network because they already come with a configuration set beforehand.

There are two types of adding devices using SmartStart:
1. Scanning it's DSK using mobile phone camera.
2. Manually writing a DSK code into a Node Provisioning List of a Smarthub.

What is a Node Provisioning List?
NPL is a list which contains all the DSK's for devices that can be added using SmartStart or by a classic inclusion with Security S2 capability without additional classic inclusion security bootstraping key exchange step.
NPL is a Z-Wave abstraction which is used mostly for SmartStart functionality but also for simplifying S2 capable nodes inclusion.
NPL comes with a possibility to add, remove or edit it's entries.

### Adding a Z-Wave device to Node Provisioning List with QR Code

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

    {
        "serv": "zwave-ad",
        "type": "cmd.npl.qr",
        "val_t": "str",
        "val": "92011287329843274893247893247324",
        "props": null,
        "tags": null,
        "ctime": "1970-01-01T00:00:00+0000",
        "uid": "123456789"
    }

### Adding or editing a Z-Wave device to Node Provisioning List manually

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

    {
        "serv": "zwave-ad",
        "type": "cmd.npl.upsert",
        "val_t": "str",
        "val": "67656-08786-98576-65768-67656-08786-98576-65768",
        "props": {
            "inclusion_setting": "pending"/"passive"/"ignored",
            "bootstraping_mode": "s2_only"/"smart_start"/"smart_start_lr",
            "network_status": {
                "node_id": 10,
                "status": "not_in_network"/"failing"
            }
            "generic_device_class": "0x10",
            "specific_device_class": "0x15",
            "installer_icon_type": "0x10",
            "manufacturer_id": "0x0012",
            "product_type": "0x0013",
            "product_id": "0x0014",
            "application_version": "0x15",
            "application_subversion": "0x16",
            "inclusion_request_interval": "512",
            "uuid_representation": "6",
            "uuid": "58D5E212-165B-4CA0-909B-C86B9CEE0111",
            "supported_protocols": "1",
            "name": "FH Smart Start Plug",
            "location": "Living Room",
            "joining_info_type": "3",
        },
        "tags": null,
        "ctime": "1970-01-01T00:00:00+0000",
        "uid": "123456789"
    }

### Removing a Z-Wave device from Node Provisioning List

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

    {
        "serv": "zwave-ad",
        "type": "cmd.npl.entry_delete",
        "val_t": "str",
        "val": "67656-08786-98576-65768-67656-08786-98576-65768",
        "props": null,
        "tags": null,
        "ctime": "1970-01-01T00:00:00+0000",
        "uid": "123456789"
    }

### Report for Node Provisioning List Entry
Below report can occur in four situations:
1. After adding entry (status="added").
2. After deleting entry (status="deleted" or status="deleted_only_from_npl").
3. After editing entry (status="edited", network_status: {"status": "not_in_network"}).
4. After powering up a device (status="edited", network_status: {"status": "included"}).
5. After inclusion in wrong network (status="included_bad_network").

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

    {
        "serv": "zwave-ad",
        "type": "evt.npl.entry_report",
        "val_t": "object",
        "val": {
            "status": "added"/"edited"/"deleted"/"deleted_only_from_npl"/"included_bad_network",
            "dsk": "67656-08786-98576-65768-67656-08786-98576-65768"
        },
        "props": {
            "inclusion_setting": "pending"/"passive"/"ignored",
            "bootstraping_mode": "s2_only"/"smart_start"/"smart_start_lr",
            "network_status": {
                "node_id": 10,
                "status": "not_in_network"/"failing/"included"
            }
            "generic_device_class": "0x10",
            "specific_device_class": "0x15",
            "installer_icon_type": "0x10",
            "manufacturer_id": "0x0012",
            "product_type": "0x0013",
            "product_id": "0x0014",
            "application_version": "0x15",
            "application_subversion": "0x16",
            "inclusion_request_interval": "512",
            "uuid_representation": "6",
            "uuid": "58D5E212-165B-4CA0-909B-C86B9CEE0111",
            "supported_protocols": "1",
            "name": "FH Smart Start Plug",
            "location": "Living Room",
            "joining_info_type": "3",
        },
        "tags": null,
        "ctime": "1970-01-01T00:00:00+0000",
        "uid": "123456789"
    }

### Getting all entries for a Node Provisioning List

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

    {
        "serv": "zwave-ad",
        "type": "cmd.npl.get_list",
        "val_t": "null",
        "val": null,
        "props": null,
        "tags": null,
        "ctime": "1970-01-01T00:00:00+0000",
        "uid": "123456789"
    }

### Report after getting all entries for a Node Provisioning List

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

    {
        "serv": "zwave-ad",
        "type": "evt.npl.list",
        "val_t": "str_array",
        "val": [
            "67656-08786-98576-65768-67656-08786-98576-65768",
            "67621-02386-98426-64568-12446-24561-98576-65768"
        ]
        "props": [
            {
                "inclusion_setting": "pending"/"passive"/"ignored",
                "bootstraping_mode": "s2_only"/"smart_start"/"smart_start_lr",
                "network_status": {
                    "node_id": 10,
                    "status": "not_in_network"/"failing"
                }
                "generic_device_class": "0x10",
                "specific_device_class": "0x15",
                "installer_icon_type": "0x10",
                "manufacturer_id": "0x0012",
                "product_type": "0x0013",
                "product_id": "0x0014",
                "application_version": "0x15",
                "application_subversion": "0x16",
                "inclusion_request_interval": "512",
                "uuid_representation": "6",
                "uuid": "58D5E212-165B-4CA0-909B-C86B9CEE0111",
                "supported_protocols": "1",
                "name": "FH Smart Start Plug",
                "location": "Living Room",
                "joining_info_type": "3",
            },
            {
                "inclusion_setting": "pending"/"passive"/"ignored",
                "bootstraping_mode": "s2_only"/"smart_start"/"smart_start_lr",
                "network_status": {
                    "node_id": 11,
                    "status": "not_in_network"/"failing"
                }
                "generic_device_class": "0x11",
                "specific_device_class": "0x11",
                "installer_icon_type": "0x14",
                "manufacturer_id": "0x4235",
                "product_type": "0x1235",
                "product_id": "0x5453",
                "application_version": "0x15",
                "application_subversion": "0x16",
                "inclusion_request_interval": "512",
                "uuid_representation": "6",
                "uuid": "58D5E212-165B-4CA0-909B-C86B9CEE0111",
                "supported_protocols": "1",
                "name": "Fibaro Wall Plug",
                "location": "Hallway",
                "joining_info_type": "3",
            },
        ]
        "tags": null,
        "ctime": "1970-01-01T00:00:00+0000",
        "uid": "123456789"
    }

## Adding a thing to FH system - classic inclusion

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
