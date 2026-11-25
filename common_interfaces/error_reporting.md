# Error Reporting

The following document describes the common interface for error reporting.

## When an error must be reported

* A command that fails must be answered with exactly one `evt.error.report`.
  A report that looks like success must not be sent instead. A state report showing the real state of the device may be sent before the error report.
* A command with a value outside the advertised range or not in the supported list must be rejected with an error report (`out_of_range` or `not_supported`), for example a value above `max_current`, outside `min` and `max`, or not listed in `sup_modes` or `sup_setpoints`.
  Such a value must not be changed silently, for example clamped, capped or rounded, and then applied, with these exceptions:
  * a level in the [output level switch](/device_services/generic/output_level_switch.md) service outside `min_lvl` and `max_lvl` is limited to that range, and the report carries the level that was set,
  * a value may be rounded to the step the service supports, for example a setpoint to the nearest half degree, and the report carries the stored value.
* A failure found after the command was accepted, for example when a device or a cloud service rejects it later, must still be reported. The report carries the `corid` of that command, see [correlation](#correlation).
* A fault not tied to a command, for example a device fault or a lost connection, must not be reported with `evt.error.report`. It is reported through the own reports of the service, such as state, alarm or connectivity reports.

## Topics

An error report is published:
* on the topic given in the `resp_to` property of the command, when the command has one,
* otherwise on the event topic that mirrors the command topic: the same address with `mt:evt` in place of `mt:cmd`.
  For example, a command received on `pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:out_bin_switch/ad:12_0` is answered on `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:out_bin_switch/ad:12_0`.

## Service name

Interface for error reporting does not have its own dedicated service and always belongs to a particular service where the error occurred.
An error report carries the service of the command it answers.

Every service that accepts commands must list `evt.error.report` among its interfaces, for a device service in its [inclusion report](/adapter/thing_management.md#definitions).

## Interfaces

| Type | Interface        | Value type | Properties                                           | Description                                                                    |
|------|------------------|------------|------------------------------------------------------|--------------------------------------------------------------------------------|
| out  | evt.error.report | string     | `msg`, `src`, `cmd_topic`, `cmd_service`, `cmd_type` | Reports an error, the value is an error code, see [error codes](#error-codes). |

## Error codes

| Code             | Meaning                                                               | Example situation                                                                   |
|------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| `bad_request`    | The command is malformed or its value has a wrong type.               | `cmd.max_current.set` is received with `val_t` equal to `string`.                   |
| `out_of_range`   | A numeric value is outside the advertised range.                      | `cmd.max_current.set` with `40` while `sup_max_current` is `32`.                    |
| `not_supported`  | A value is not in the supported list, or the action is not supported. | `cmd.mode.set` to a thermostat with a mode not listed in `sup_modes`.               |
| `not_found`      | The addressed thing, node or object does not exist.                   | `cmd.thing.get_inclusion_report` for an address that has no thing.                  |
| `busy`           | Another operation is running and the command cannot be handled now.   | A second command arrives while a previous operation on the device is still running. |
| `unauthorized`   | The implementation lacks a valid login or the rights for the action.  | The login to the cloud service of the device has expired.                           |
| `device_refused` | The device or its cloud service received the command and rejected it. | A chargepoint rejects `cmd.charge.start` because no car is connected.               |
| `unavailable`    | The device or the cloud service cannot be reached or did not answer.  | The device is offline or the request to its cloud service timed out.                |
| `rate_limited`   | Refused for now because of too many requests; may be retried later.  | The cloud service of the device answers HTTP 429 Too Many Requests.                 |
| `internal`       | Any other failure inside the implementation.                          | An unexpected error while processing the command.                                   |

An implementation may define additional codes for conditions specific to it. Such codes must utilize `snake_case`.
A consumer must treat a code it does not know as `internal`.

> Please note that older implementations may still send a free-form text in the value instead of an error code, and error reports without `corid`.
> A consumer must tolerate both and should read such a text as the message.

## Interface properties

| Name          | Example                                                   | Required | Description                                                                                                                                                                                                                                                                |
|---------------|-----------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `msg`         | `"Maximum current must be between 6 and 32 A."`           | Yes      | Describes the error. For every code except `internal` it is one plain human-readable sentence; for `internal` it may carry technical detail of the failure. It must not contain URLs, keys, tokens, passwords, identifiers of accounts or devices, or raw response bodies. |
| `src`         | `"60"`                                                    | No       | An arbitrary string defining a source, an origin or a general context for the error.                                                                                                                                                                                       |
| `cmd_topic`   | `"pt:j1/mt:cmd/rt:dev/rn:easee/ad:1/sv:chargepoint/ad:1"` | Yes      | Topic of the command the report answers.                                                                                                                                                                                                                                   |
| `cmd_service` | `"chargepoint"`                                           | Yes      | Service of the command the report answers.                                                                                                                                                                                                                                 |
| `cmd_type`    | `"cmd.max_current.set"`                                   | Yes      | Type or interface name of the command the report answers.                                                                                                                                                                                                                  |

## Correlation

An error report always answers a command and must carry the `corid` message property equal to the `uid` of that command, also when the failure is found after the command was accepted.
There is no error report without a `corid`.
See [message properties](/fimp/message_format.md#message-properties) for more details.

## Storage

An error report on a device service (resource type `dev`) must carry the `skip` storage strategy, so it is not stored as a last known value.
See [storage policy](/fimp/message_format.md#skipping) for more details.

```json
{
  "storage": {
    "strategy": "skip"
  }
}
```

## Examples

* Example of an error report answering a command `cmd.max_current.set` with the value `40` and `uid` equal to `d8da6560-cb1e-4a83-80dd-1a85c1349d27`, sent to a chargepoint which advertises `sup_max_current` equal to `32`:

```json
{
  "serv": "chargepoint",
  "type": "evt.error.report",
  "val_t": "string",
  "val": "out_of_range",
  "storage": {
    "strategy": "skip"
  },
  "props": {
    "msg": "Maximum current must be between 6 and 32 A.",
    "cmd_topic": "pt:j1/mt:cmd/rt:dev/rn:easee/ad:1/sv:chargepoint/ad:1",
    "cmd_service": "chargepoint",
    "cmd_type": "cmd.max_current.set"
  },
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2026-11-25T10:15:02.4+01:00",
  "corid": "d8da6560-cb1e-4a83-80dd-1a85c1349d27",
  "uid": "d1b18e32-7a17-4c87-af70-7af1dfac7ec3",
  "topic": "pt:j1/mt:evt/rt:dev/rn:easee/ad:1/sv:chargepoint/ad:1"
}
```

* Example of an error report on an adapter level answering a command `cmd.thing.get_inclusion_report` with `uid` equal to `373bcccf-5065-4ea4-b1f8-3df073852188` and `resp_to` equal to `pt:j1/mt:rsp/rt:app/rn:tpflow/ad:1`, requested for an address that has no thing:

```json
{
  "serv": "zwave-ad",
  "type": "evt.error.report",
  "val_t": "string",
  "val": "not_found",
  "props": {
    "msg": "Thing was not found.",
    "src": "60",
    "cmd_topic": "pt:j1/mt:cmd/rt:ad/rn:zw/ad:1",
    "cmd_service": "zwave-ad",
    "cmd_type": "cmd.thing.get_inclusion_report"
  },
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2026-11-25T10:16:40.1+01:00",
  "corid": "373bcccf-5065-4ea4-b1f8-3df073852188",
  "uid": "1a9be716-16bc-4c83-b740-88470266b508",
  "topic": "pt:j1/mt:rsp/rt:app/rn:tpflow/ad:1"
}
```

* Example of an error report for a late failure: a command `cmd.charge.start` with `uid` equal to `9bc04f66-7bdc-4f80-88ee-b563b0b957e2` was accepted and sent to the cloud service of the chargepoint, which rejected it later:

```json
{
  "serv": "chargepoint",
  "type": "evt.error.report",
  "val_t": "string",
  "val": "device_refused",
  "storage": {
    "strategy": "skip"
  },
  "props": {
    "msg": "The chargepoint refused to start charging.",
    "cmd_topic": "pt:j1/mt:cmd/rt:dev/rn:easee/ad:1/sv:chargepoint/ad:1",
    "cmd_service": "chargepoint",
    "cmd_type": "cmd.charge.start"
  },
  "tags": null,
  "src": "-",
  "ver": "1",
  "ctime": "2026-11-25T10:20:11.8+01:00",
  "corid": "9bc04f66-7bdc-4f80-88ee-b563b0b957e2",
  "uid": "b7531603-83ae-401c-888c-834448563015",
  "topic": "pt:j1/mt:evt/rt:dev/rn:easee/ad:1/sv:chargepoint/ad:1"
}
```
