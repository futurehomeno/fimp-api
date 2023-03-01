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