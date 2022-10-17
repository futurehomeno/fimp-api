### OTA Service
This service is used to manage over-the-air (OTA) upgrades of end devices.

#### Service name

`ota`

#### Interfaces

Type | Interface               | Value type | Description
-----|-------------------------|------------|--------------
out  | evt.ota_progress.report | int_map    | Shows upgrade progress and estimated time left.
out  | evt.ota_end.report      | object     | Sent on upgrade end with upgrade status.

#### Examples

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
