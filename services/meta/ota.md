### OTA Service
This service is used to manage over-the-air (OTA) upgrades of end devices.

#### Service name

`ota`

#### Interfaces

Type | Interface               | Value type | Description                                                                                                      |
-----|-------------------------|------------|------------------------------------------------------------------------------------------------------------------|
in   | cmd.status.get_report   | null       | Requests update progress information.                                                                            |
out  | evt.status.report       | object     | Shows update progress and estimated time left. See [`ota_report_object`](#definitions) for detailed information. |
in   | cmd.update.install      | string     | Starts an update of the device. Value should be the full path to the update file.                                | 

## Definitions

* `ota_report_object` is an object with the following structure:

| Field          | Type   | Example         | Description                                                                                                     |
|----------------|--------|-----------------|-----------------------------------------------------------------------------------------------------------------|
| state          | string | `"IN PROGRESS"` | One of the `state` values.                                                                                      |
| substate       | string | `"TRANSFERING"` | One of the `substate` values.                                                                                   |       
| progress       | int    | `10`            | Optional, only available in substate `TRANSFERING`. Progress percentage of the update transfer.                 |
| remaining_min  | int    | `3`             | Optional, only available in substate `TRANSFERING`. Remaining time until the end of the transfer (minutes).     | 
| remaining_sec  | int    | `35`            | Optional, only available in substate `TRANSFERING`. Remaining time until the end of the transfer (seconds).     |
| last_update    | int    | `132351314`     | Optional. Unix timestamp of the last started update process.                                                    |        


* `state`: Current state of the update process, can be one of: `"NOT STARTED"`, `"IN PROGRESS"`, `"FINISHED"`.
* `substate`: Gives more detailed information about the current update phase. Available values depend on the value in `state`:
  * for `"IN PROGRESS"`: `"STARTED"`, `"TRANSFERING"`, `"REDISCOVERY"`, `"DEVICE REBOOTING"`, `"NEEDS USER ACTION TO START"`.
  * for `"FINISHED"`: `"SUCCESS"`, `"LOW BATTERY"`, `"NOT UPGRADABLE"`, `"INVALID FILE"`, `"ERROR"`.
#### Examples

```json
{
   "type": "evt.status.report",
   "serv": "ota",
   "val_t": "object",
   "val": {
      "progress": 10,
      "remaining_min": 40,
      "remaining_sec": 3,
      "state": "IN PROGRESS",
      "substate": "TRANSFERING",
      "last_update": 12625242636
   }
}
```
