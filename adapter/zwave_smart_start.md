# Z-Wave SmartStart

SmartStart inclusion is a process of adding a device with a pre-configuration step using a DSK (Device Specific Key) printed on the back of the device.
This key is then scanned and added to the adapter NPL (Node Provisioning List) which is then used to automatically add the device to the network.
When a device is powered up, if it supports SmartStart and is already in the NPL, it will automatically be detected and added to the network by the adapter.
Additionally, an entry in the NPL will used to simplify classic inclusion of S2 capable devices, allowing to skip security keys exchange.

## Behaviors and Flows

### Smart Start Inclusion

* Client sends a `cmd.npl.qr` with a valid QR code value or a complete `cmd.npl.entry_upsert` command. These add an NPL entry to the list.
* When the device is turned on the pairing process will start automatically.

## Removing entry from NPL

* Client sends `cmd.npl.entry_delete` with the DSK of the entry which is to be deleted.

## FIMP Specification

### Topics

`pt:j1/mt:cmd/rt:ad/rn:zw/ad:1`

`pt:j1/mt:evt/rt:ad/rn:zw/ad:1`

### Service name

`zwave-ad`

### Interfaces

| Type | Interface                  | Value type | Description                                                                           |
|------|----------------------------|------------|---------------------------------------------------------------------------------------|
| in   | cmd.npl.qr                 | string     | Add an NPL entry from a QR code.                                                      |
| in   | cmd.npl.entry_upsert       | object     | Insert or update an NPL entry. See [`NPL_entry`](#definitions) for more information.  |
| in   | cmd.npl.entry_delete       | string     | Remove a device with the specific [`DSK`](#definitions) from the NPL list.            |
| in   | cmd.npl.all_entries_remove | null       | Remove all entries from the NPL list.                                                 |
| in   | cmd.npl.entry_get          | string     | Request a report of an NPL entry with the specific [`DSK`](#definitions).              |
| in   | cmd.npl.all_entries_get    | null       | Request a report of all NPL entries.                                                  |
| out  | evt.npl.entry_report       | object     | Report of a specific NPL entry. See [`NPL_entry`](#definitions) for more information. |                              
| out  | evt.npl.list               | object     | Report of all NPL list entries. Value is an array of [`NPL_entry`](#definitions).     |

### Definitions

* `DSK` - Device Specific Key, unique for each device. Example value: `"67656-08786-98576-65768-67656-08786-98576-65768"`.

* `inclusion_setting` can be one of the following:

| Value       | Description                                                                                                                                                              |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `"pending"` | Device will be added to network right after powering it up.                                                                                                              |
| `"passive"` | Controller has decided to not perform inclusion right after powering up a device. When get for all entries is executed this state is changed automatically to 'pending'. | 
| `"ignored"` | Controller has decided to not perform inclusion right after powering up a device. This state can be changed only manually.                                               |

* `bootstrapping_mode` can be one of the following:

| Value              | Description                                                                                    |
|--------------------|------------------------------------------------------------------------------------------------|
| `"s2_only"`        | Device must manually be set to Learn Mode and follow S2 bootstraping instructions.             |
| `"smart_start"`    | Device will be included and S2 bootstrapped automatically using Z-Wave Smart Start.            |
| `"smart_start_lr"` | Device will be included and S2 bootstrapped automatically using Z-Wave Long Range Smart Start. |

* `joining_info_type` describes security level, possible values: `"s0"`, `"s2_unauth"`, `"s2_auth"`, `"s2_ac"`.

* `NPL_entry` is an object with the following structure:

| Field    | Type   | Description                                                                 |
|----------|--------|-----------------------------------------------------------------------------|
| dsk      | string | See [`DSK`](#definitions) for more information.                             |
| metadata | object | Device's information. See [`metadata`](#definitions) for object definition. |

* `metadata` is an object with the following structure:

| Field                      | Type      | Description                                                                                                                           |
|----------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------|
| product_type_info          | object    | Device class information. See [`product_type_info`](#definitions).                                                                    |
| product_id_info            | object    | Product id information. See [`product_id_info`](#definitions).                                                                        |
| inclusion_request_interval | int       | Interval defined in seconds for sending inclusion requests from slave device to the Z-Wave controller. Default is set to 512 seconds. |
| uuid16_info                | object    | UUID16 assigned to the device. See [`uuid16_info`](#definitions).                                                                     |
| supported_protocols        | int       | Defines supported Z-Wave protocol, `0` for default Z-Wave, `1` for Z-Wave Long Range.                                                 |
| name                       | string    | Name of the device. See note below.                                                                                                   |
| location                   | string    | Location assigned to the device. See note below.                                                                                      |                
| inclusion_setting          | string    | See [`inclusion_setting`](#definitions) for more information.                                                                         |
| joining_info_type          | str_array | Array of [`joining_info_type`](#definitions).                                                                                         |
| bootstrapping_mode         | string    | See [`bootstrapping_mode`](#definitions) for more information.                                                                        |     

> Following rules govern `name` and `location` restrictions:
>  - must be UTF-8 encoded
>  - must not contain any appended termination characters
>  - may contain the dot
>  - must not contain the underscore character “_”.
>  - each name sub-string (separated by the dot character “.”) must not end with the dash character “-”.
>
> Both are case-sensitive. The combined Name and Location strings must not be longer than 62 characters.

* `product_type_info` is an object with the following structure:

| Field                 | Type | Example | Description                            |
|-----------------------|------|---------|----------------------------------------|
| generic_device_class  | int  | `7`     | Generic device class.                  |
| specific_device_class | int  | `2`     | Specific device class.                 |
| installer_icon_type   | int  | `1567`  | Icon of the device from specification. |

* `product_id_info` is an object with the following structure:

| Field                  | Type | Example | Description                                                  |
|------------------------|------|---------|--------------------------------------------------------------|
| manufacturer_id        | int  | `271`   | Unique value given for every Z-Wave devices manufacturer.    |
| product_type           | int  | `1463`  | Represents a group of devices within a single manufacturer.  |
| product_id             | int  | `3562`  | Represents a specific device within specific `product_type`. |
| application_version    | int  | `1`     | Version of application installed on Z-Wave device.           |
| application_subversion | int  | `2`     | Subversion of application installed on Z-Wave device.        |

* `uuid16_info` is an object with the following structure:

| Field               | Type   | Example | Description                  |
|---------------------|--------|---------|------------------------------|
| uuid_representation | int    | `271`   | Format of the UUID16.        |
| uuid                | string | `1463`  | UUID assigned to the device. |

### Examples

* Example of a command adding a Z-Wave device to NPL via QR Code:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.npl.qr",
  "val_t": "string",
  "val": "900126418131374522186120921014625903142418367280825200100435401536022000271023060409601280",
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of a command adding or editing device in NPL manually:

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
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of a command removing a device from NPL:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.npl.entry_delete",
  "val_t": "string",
  "val": "67656-08786-98576-65768-67656-08786-98576-65768",
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of a command removing all NPL entries:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.npl.all_entries_remove",
  "val_t": "null",
  "val": null,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of a command requesting an NPL entry report for a given DSK:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.npl.entry_get",
  "val_t": "string",
  "val": "67656-08786-98576-65768-67656-08786-98576-65768",
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of a command requesting all NPL entries report:

```json
{
  "serv": "zwave-ad",
  "type": "cmd.npl.all_entries_get",
  "val_t": "null",
  "val": null,
  "props": null,
  "tags": null,
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1"
}
```

* Example of report of an NPL entry:

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
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:evt/rt:ad/rn:zw/ad:1"
}
```

* Example of report for all NPL entries:

```json
{
  "serv": "zwave-ad",
  "type": "evt.npl.list",
  "val_t": "object",
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
          "s2_unauth"
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
  "src": "-",
  "ver": "1",
  "uid": "1e965f4c-07ee-4e3e-8c03-e61e9aa9192a",
  "topic": "pt:j1/mt:evt/rt:ad/rn:zw/ad:1"
}
```