# OTA Service
This service is used to manage over-the-air (OTA) upgrades of end devices.

## Service name

`ota`

## Interfaces

Type | Interface                   | Value type | Description                                                                                                      |
-----|-----------------------------|------------|------------------------------------------------------------------------------------------------------------------|
out  | evt.ota_progress.report     | int_map    | Shows update transfer progress and estimated time left, see [`ota_progress`](#definitions).                      |
out  | evt.ota_start.report        | null       | Sent on upgrade start.                                                                                           |
out  | evt.ota_end.report          | object     | Sent on upgrade end with upgrade status, see [`ota_end`](#definitions).                                          |
in   | cmd.ota_status.get_report   | null       | Requests update progress information.                                                                            |
out  | evt.ota_status.report       | object     | Shows update phase, see [`ota_status`](#definitions).                                                            |
in   | cmd.ota_update.install      | string     | Z-Wave only. Starts an update of the device. Value should be the full path to the update                         | 

## Definitions

* `ota_progress` is an object of the following structure:
  
| Field          | Type   | Example         | Description                                                 |
|----------------|--------|-----------------|-------------------------------------------------------------|      
| progress       | int    | `10`            | Progress percentage of the update transfer.                 |
| remaining_min  | int    | `3`             | Remaining time until the end of the transfer (minutes).     | 
| remaining_sec  | int    | `35`            | Remaining time until the end of the transfer (seconds).     |

* `ota_status` is an object with the following structure:

| Field          | Type   | Example         | Description                                                                                                     |
|----------------|--------|-----------------|-----------------------------------------------------------------------------------------------------------------|
| state          | string | `"IN PROGRESS"` | One of the `state` values, see [`state`](#definitions) for definitions.                                         |
| substate       | string | `"TRANSFERING"` | One of the `substate` values, see [`state`](#definitions) for definitions.                                      |
| last_update    | int    | `132351314`     | Optional. Unix timestamp of the last started update process.                                                    |


* `state`: Current state of the update process, can be one of: `"NOT STARTED"`, `"IN PROGRESS"`, `"FINISHED"`.
* `substate`: Gives more detailed information about the current update phase. Available values depend on the value in `state`:
  * for `"IN PROGRESS"`: `"STARTED"`, `"TRANSFERING"`, `"REDISCOVERY"`, `"DEVICE REBOOTING"`, `"NEEDS USER ACTION TO START"`.
  * for `"FINISHED"`: `"SUCCESS"`, `"LOW BATTERY"`, `"NOT UPGRADABLE"`, `"INVALID FILE"`, `"ERROR"`.

* `ota_end` is an object with the following structure:

| Field          | Type   | Example          | Description                                                           |
|----------------|--------|------------------|-----------------------------------------------------------------------|
| success        | bool   | `true`           | Shows whether the update was successful or not.                       |
| error          | string | `"invalid_file"` | In case of a failed update describes fail reason, otherwise empty.    |

## Examples

```json
{
   "type": "evt.ota_progress.report",
   "serv": "ota",
   "val_t": "int_map",
   "val": {
      "progress": 10,
      "remaining_min": 40,
      "remaining_sec": 3
   }
}
```

```json
{
   "type": "evt.ota_end.report",
   "serv": "ota",
   "val_t": "object",
   "val": {
      "success": true,
      "error": ""
   }
}
```

```json
{
   "type": "evt.ota_status.report",
   "serv": "ota",
   "val_t": "object",
   "val": {
      "state": "IN PROGRESS",
      "substate": "TRANSFERING",
      "last_update": 12625242636
   }
}
```
