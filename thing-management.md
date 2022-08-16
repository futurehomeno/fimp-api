# Thing Management (Pairing)

The following APIs should be common across all adapters, but the example code will use zwave-ad for simplicity. Notes have been added for specific differences for the most common adapters.

## Adding a thing to FH system - SmartStart (Z-Wave only)

SmartStart inclusion is a process of adding a device with a pre-configuration step using a DSK printed on the back of the device. With this functionality, you simply set up your device and power it on. The device is then automatically recognized and added to the network because it already comes with a configuration set by default.

There are two ways of adding a device to the NPL:

1. Scanning the DSK using a mobile phone camera (QR).
2. Manually entering the DSK into the Node Provisioning List.

### What is the Node Provisioning List?

NPL is a list which contains all the DSKs for devices that will be added using SmartStart (if those are SmartStart capable) or by classic inclusion with Security S2 without the additional classic inclusion security bootstrapping key exchange step. It is a Z-Wave abstraction which is used mostly for SmartStart functionality but also for simplifying inclusion of S2 capable nodes. It comes with the possibility to add, edit or remove its entries.

### Additional documentation for SmartStart and NPL

All documents are located in z-wave/smartstart directory.

1. Node Provisioning Information Type Registry: Most of properties used in FIMP model are taken from this document. Example: 3.1.2.8 SmartStart Inclusion Setting Information Type is basically translated to "inclusion_setting" in FIMP protocol.
2. Node Provisioning QR Code Format: Document for any kind of front end application which would want to implement QR Code scanning capability.
3. Z-Wave Network Protocol Command Class Specification: Adnotation 4.5.12.5 shows diagrams for use cases of SmartStart and NPL.

### NPL Data Model

All of the properties are optional with three exceptions: 'inclusion_setting', 'bootstraping_mode' and 'network_status'.

#### `inclusion_setting`

Can be one of the following:

- `pending`: Device will be added to network right after powering it up. 
- `passive`: Controller has decided to not perform inclusion right after powering up a device. When get for all entries is executed this state is changed automatically to 'pending'.
- `ignored`: Controller has decided to not perform inclusion right after powering up a device. This state can be changed only manually.

#### `bootstrapping_mode`

Can be one of the following:

- `s2_only`: Device must manually be set to Learn Mode and follow S2 bootstraping instructions.
- `smart_start`: Device will be included and S2 bootstrapped automatically using Z-Wave Smart Start.
- `smart_start_lr`: Device will be included and S2 bootstrapped automatically using Z-Wave Long Range Smart Start.

#### `network_status`

Object containing nodeId and status.

> `status` can be:
- `not_in_network`: A device is not currently included in the network.
- `added`: A device is included in the network and is functional.
- `failed`: A device is included in the network but is now marked as failing (e.g. communication fails or it has not woken up for longer than expected)
> `nodeId`: Unique identifier assigned to a device by a Smarthub.

#### `generic_device_class`

Z-Wave generic device class (represented by a number).

#### `specific_device_class`

Z-Wave specific device class. Pair of generic_device_class and specific_device_class represents specific device type.

#### `installer_icon_type`

Z-Wave specification has a list of icons with integer values corresponding with each of them.

#### `manufacturer_id`

Unique integer value given for every manufacturer who sells Z-Wave devices. 

#### `product_type`

Manufacturer - defined integer value which should represent a group of devices within a single manufacturer.

#### `product_id`

Manufacturer - defined integer value which right along with manufacturer_id and product_type creates a unique set of number representing one single Z-Wave device model.

#### `application_version`

Version of application installed on Z-Wave device.

#### `application_subversion`

Subversion of application installed on Z-Wave device.

#### `inclusion_request_interval`

Interval defined by seconds for sending inclusion requests from slave device to Z-Wave controller. Default is set to 512 seconds.

#### `uuid_representation`

Described in Node Provisioning Information Type Registry 3.1.2.4.

#### `uuid`

Described in Node Provisioning Information Type Registry 3.1.2.4.

#### `supported_protocols`

Can be one of the following:

- 0: Z-Wave is supported
- 1: Z-Wave Long Range is supported

#### `name`

The name of the device being upserted in the NPL.
The Name:
- must be UTF-8 encoded
- must not contain any appended termination characters
- may contain the dot
- must not contain the underscore character “_”.
- Each name sub-string (separated by the dot character “.”) must not end with the dash character “-”.

Device name is case sensitive.
The combined Name and Location strings must not be longer than 62 characters.


#### `location`

Location assigned to a device.
The Location:
- must be UTF-8 encoded
- must not contain any appended termination characters
- may contain the dot
- must not contain the underscore character “_”.
- Each location sub-string (separated by the dot character “.”) must not end with the dash character “-”.

Device location is case sensitive.
The combined Name and Location strings must not be longer than 62 characters.

#### `joining_info_type`

Array of strings which represents joining mode.
Possible values: ["s0", "s2_unauth", "s2_auth", "s2_ac"]

### NPL Report Data Model

#### `dsk`

The DSK of the device that has been acted upon.

### Adding a Z-Wave device to NPL with QR Code

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

```json
{
    "serv": "zwave-ad",
    "type": "cmd.npl.qr",
    "val_t": "string",
    "val": "900126418131374522186120921014625903142418367280825200100435401536022000271023060409601280",
    "props": null,
    "tags": null,
    "ctime": "1970-01-01T00:00:00+0000",
    "uid": "123456789"
}
```

### Adding or editing a Z-Wave device to NPL manually

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

```json
{
    "serv": "zwave-ad",
    "type": "cmd.npl.entry_upsert",
    "val_t": "object",
    "val": {
        "dsk": "67656-08786-98576-65768-67656-08786-98576-65768",
        "metadata": {
            "product_type_info": {
                "generic_device_class": 7,
                "specific_device_class": 1,
                "installer_icon_type": 1792
            },
            "product_id_info": {
                "manufacturer_id": 271,
                "product_type": 1536,
                "product_id": 4096,
                "application_version": 1,
                "application_subversion": 2
            },
            "inclusion_request_interval": 512,
            "uuid16_info": {
                "uuid_representation": 6,
                "uuid": "58D5E212-165B-4CA0-909B-C86B9CEE0111"
            },
            "supported_protocols": 0,
            "name": "FH Smart Start Plug",
            "location": "Living Room",
            "inclusion_setting": "pending",
            "joining_info_type": [
                "s0",
                "s2_unauth",
                "s2_auth",
                "s2_ac"
            ],
            "bootstrapping_mode": "s2_only"
        }
    },
    "props": null,
    "tags": null,
    "ctime": "1970-01-01T00:00:00+0000",
    "uid": "123456789"
}
```

### Removing a Z-Wave device from NPL

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

```json
{
    "serv": "zwave-ad",
    "type": "cmd.npl.entry_delete",
    "val_t": "string",
    "val": "67656-08786-98576-65768-67656-08786-98576-65768",
    "props": null,
    "tags": null,
    "ctime": "1970-01-01T00:00:00+0000",
    "uid": "123456789"
}
```

### Remove all NPL entries.

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

```json
{
    "serv": "zwave-ad",
    "type": "cmd.npl.all_entries_remove",
    "val_t": "null",
    "val": null,
    "props": null,
    "tags": null,
    "ctime": "1970-01-01T00:00:00+0000",
    "uid": "123456789"
}
```

### Get NPL entry report for given DSK.

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

```json
{
    "serv": "zwave-ad",
    "type": "cmd.npl.entry_get",
    "val_t": "string",
    "val": "67656-08786-98576-65768-67656-08786-98576-65768",
    "props": null,
    "tags": null,
    "ctime": "1970-01-01T00:00:00+0000",
    "uid": "123456789"
}
```

### Get NPL all entries report.

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

```json
{
    "serv": "zwave-ad",
    "type": "cmd.npl.all_entries_get",
    "val_t": "null",
    "val": null,
    "props": null,
    "tags": null,
    "ctime": "1970-01-01T00:00:00+0000",
    "uid": "123456789"
}
```

### Report for NPL Entry

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

```json
{
    "serv": "zwave-ad",
    "type": "evt.npl.entry_report",
    "val_t": "object",
    "val": {
        "dsk": "67656-08786-98576-65768-67656-08786-98576-65768",
        "metadata": {
            "product_type_info": {
                "generic_device_class": 7,
                "specific_device_class": 1,
                "installer_icon_type": 1792
            },
            "product_id_info": {
                "manufacturer_id": 271,
                "product_type": 1536,
                "product_id": 4096,
                "application_version": 1,
                "application_subversion": 2
            },
            "inclusion_request_interval": 512,
            "uuid16_info": {
                "uuid_representation": 6,
                "uuid": "58D5E212-165B-4CA0-909B-C86B9CEE0111"
            },
            "supported_protocols": 0,
            "name": "FH Smart Start Plug",
            "location": "Living Room",
            "inclusion_setting": "pending",
            "joining_info_type": [
                "s0",
                "s2_unauth",
                "s2_auth",
                "s2_ac"
            ],
            "bootstrapping_mode": "s2_only",
            "network_status_info": {
                "node_id": 10,
                "status": "not_in_network"
            }
        }
    },
    "props": null,
    "tags": null,
    "ctime": "1970-01-01T00:00:00+0000",
    "uid": "123456789"
}
```

### Report after getting all entries for a NPL

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

```json
{
    "serv": "zwave-ad",
    "type": "evt.npl.list",
    "val_t": "str_array",
    "val": [
        {
            "dsk": "67656-08786-98576-65768-67656-08786-98576-65768",
            "metadata": {
                "product_type_info": {
                    "generic_device_class": 7,
                    "specific_device_class": 1,
                    "installer_icon_type": 1792
                },
                "product_id_info": {
                    "manufacturer_id": 271,
                    "product_type": 1536,
                    "product_id": 4096,
                    "application_version": 1,
                    "application_subversion": 2
                },
                "inclusion_request_interval": 512,
                "uuid16_info": {
                    "uuid_representation": 6,
                    "uuid": "58D5E212-165B-4CA0-909B-C86B9CEE0111"
                },
                "supported_protocols": 0,
                "name": "FH Smart Start Plug",
                "location": "Living Room",
                "inclusion_setting": "pending",
                "joining_info_type": [
                    "s0",
                    "s2_unauth",
                    "s2_auth",
                    "s2_ac"
                ],
                "bootstrapping_mode": "s2_only",
                "network_status_info": {
                    "node_id": 10,
                    "status": "not_in_network"
                }
            }
        },
        {
            "dsk": "67621-02386-98426-64568-12446-24561-98576-65768",
            "metadata": {
                "product_type_info": {
                    "generic_device_class": 7,
                    "specific_device_class": 1,
                    "installer_icon_type": 1792
                },
                "product_id_info": {
                    "manufacturer_id": 271,
                    "product_type": 1536,
                    "product_id": 4096,
                    "application_version": 1,
                    "application_subversion": 2
                },
                "inclusion_request_interval": 512,
                "uuid16_info": {
                    "uuid_representation": 6,
                    "uuid": "58D5E212-165B-4CA0-909B-C86B9CEE0111"
                },
                "supported_protocols": 0,
                "name": "Fibaro Wall Plug",
                "location": "Bedroom",
                "inclusion_setting": "pending",
                "joining_info_type": [
                    "s0",
                    "s2_unauth",
                ],
                "bootstrapping_mode": "smart_start",
                "network_status_info": {
                    "node_id": 11,
                    "status": "not_in_network"
                }
            }
        }
    ],
    "props": null,
    "tags": null,
    "ctime": "1970-01-01T00:00:00+0000",
    "uid": "123456789"
}
```

## Adding a thing to FH system - classic inclusion

Inclusion process generally consists of 2 steps:

1. An application sends inclusion command to adapter. This indicates the beginning of the adding process.
2. Adapter generates inclusion_report event right after a thing was added. This indicates the end of the adding process.

ZigBee allows you to add multiple devices in one go, thus the generation of an inclusion report does not end the pairing process. Instead, the user has to manually stop the process or wait for it to time out.

### Starting inclusion

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

```json
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
```

### Stopping inclusion

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

```json
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
```

### Sample inclusion report

Topic: `pt:j1/mt:evt/rt:ad/rn:zw/ad:1`

Message (report):

```json
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
```

### Getting inclusion report

An adapter should always respond with an inclusion report on `get_inclusion_report` command. In the following example, we ask for the inclusion report for the device with node-id of 22 on the zwave adapter.

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

```json
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
```

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

```json
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
```

### Stopping exclusion

Topic: `pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

Message (command):

```json
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
```

### Sample exclusion report

Topic: `pt:j1/mt:evt/rt:ad/rn:zw/ad:1`

Message (report):

```json
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
```

### Delete specific thing

The following example will delete the device with address id 1 from the network.

Topic: `pt:j1/mt:cmd/rt:ad/rn:zigbee/ad:1`

Message (command):

```json
{
    "serv": "zigbee",
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
```
