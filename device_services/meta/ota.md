# OTA Service

This service is used to manage over-the-air (OTA) updates of end devices.

## Service name

`ota`

## Interfaces

| Type | Interface               | Value type | Description                                                                                                |
|------|-------------------------|------------|------------------------------------------------------------------------------------------------------------|
| in   | cmd.ota_update.start    | string     | Starts an update of the device. Value should be the full path to the firmware image file.                  |
| out  | evt.ota_start.report    | null       | Reports on the start of the update process.                                                                |
| out  | evt.ota_progress.report | int_map    | Reports on the progress of the image transfer and estimated time left, see [`ota_progress`](#definitions). |
| out  | evt.ota_end.report      | object     | Reports on the end of the update process, see [`ota_end`](#definitions) definition for more details.       |

## Definitions

* `ota_progress` is an object of the following structure:

| Field         | Type | Example | Description                                             |
|---------------|------|---------|---------------------------------------------------------|
| progress      | int  | `10`    | Progress percentage of the firmware image transfer.     |
| remaining_min | int  | `3`     | Remaining time until the end of the transfer (minutes). |
| remaining_sec | int  | `35`    | Remaining time until the end of the transfer (seconds). |

* `ota_end` is an object with the following structure:

| Field   | Type   | Example           | Description                                                                                                                          |
|---------|--------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| success | bool   | `false`           | Shows whether the update was successful or not.                                                                                      |
| error   | string | `"invalid_image"` | If success is false it states the reason for update failure, see [`error`](#definitions) definition for list of all possible values. |

* `error` represents a cause of the failed update and is one of the following: `low_battery`, `invalid_image`, `not_upgradable`, `needs_user_action`, `other`.

## Examples

* Example of a report sent when the update process starts:

```json
{
  "type": "evt.ota_start.report",
  "serv": "ota",
  "val_t": "null",
  "val": null,
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:ota/ad:1_2"
}
```

* Example of message sent during the transfer of the image phase of the OTA update process:

```json
{
  "type": "evt.ota_progress.report",
  "serv": "ota",
  "val_t": "int_map",
  "val": {
    "progress": 10,
    "remaining_min": 40,
    "remaining_sec": 3
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:ota/ad:1_2"
}
```

* Example of a report sent when the update process is completed successfully:

```json
{
  "type": "evt.ota_end.report",
  "serv": "ota",
  "val_t": "object",
  "val": {
    "success": true
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:ota/ad:1_2"
}
```

* Example of a report sent when the update process fails due to device low battery level:

```json
{
  "type": "evt.ota_end.report",
  "serv": "ota",
  "val_t": "object",
  "val": {
    "success": false,
    "error": "low_battery"
  },
  "props": {},
  "tags": [],
  "src": "-",
  "ver": "1",
  "uid": "e604e951-7afb-4f96-981b-62e905757686",
  "topic": "pt:j1/mt:evt/rt:dev/rn:zigbee/ad:1/sv:ota/ad:1_2"
}
```