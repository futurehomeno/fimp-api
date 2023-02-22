# Topic Format

All messages sent over MQTT adhering to the FIMP protocol must be published on topics that follow the format described in this document.
A topic is divided into multiple segments which allow to distinguish between different types of messages, resources and services.
The segments are separated by a forward slash `/` which allow for selective subscriptions in accordance with the MQTT protocol

## Topic segments

Following is the list of all topic segments and their description:

| Segment | Name             | Examples         | Description                                                                                       |
|---------|------------------|------------------|---------------------------------------------------------------------------------------------------|
| `pt`    | Parser type      | `j1`             | Possible values are: `j1` (JSON v1), `j1c1` (JSON v1 Compression Type 1 gzip).                    |
| `mt`    | Message type     | `evt`            | Possible values are: `cmd` (command), `evt` (event), `rsp` (response).                            |
| `rt`    | Resource type    | `dev`            | Possible values are defined in [resource types](#resource-types) section.                         |
| `rn`    | Resource name    | `zw`             | An arbitrary name of the application or component, preferably snake_case.                         |
| `ad`    | Resource address | `1`              | An arbitrary string defining address of the resource, resources on the hub will normally use `1`. |
| `sv`    | Service name     | `out_bin_switch` | Name of the device service.                                                                       |
| `ad`    | Service address  | `1_1`            | An arbitrary string defining address of the device service.                                       |

> While service address can be any arbitrary string, by Zigbee/Z-Wave convention service addresses contain node ID/UID, underscore and channel/endpoint.

## Resource types

Each valid topic consists of various number of segments depending on the represented resource type. The following is the list of all resource types:

| Resource Type | Name        | Segments | Description                                                                    |
|---------------|-------------|----------|--------------------------------------------------------------------------------|
| `dev`         | Device      | 7        | Represents a specific device connected through a technology adapter.           |
| `loc`         | Location    | 7        | Represents a virtual device simulated on the location level by an application. |
| `ad`          | Adapter     | 5        | Represents a technology adapter, such as Z-Wave or Zigbee.                     |
| `app`         | Application | 5        | Represents an application running on the hub.                                  |
| `cloud`       | Cloud       | 5        | Represents a system component running in the cloud backend.                    |
| `discovery`   | Discovery   | 3        | Represents the entire gateway, used in service discovery mechanism.            |

## Topic examples

| Topic                                                           | Resource    | Description                                                                                                                   |
|-----------------------------------------------------------------|-------------|-------------------------------------------------------------------------------------------------------------------------------|
| `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:sensor_presence/ad:16_0`     | Device      | Topic on which events of `sensor_presence` device service at address `16_0` are published by `zw` technology adapter.         |
| `pt:j1/mt:cmd/rt:dev/rn:zigbee/ad:1/sv:out_bin_switch/ad:2_1`   | Device      | Topic on which commands for `out_bin_switch` device service at address `2_1` are listened for by `zigbee` technology adapter. |
| `pt:j1/mt:evt/rt:loc/rn:room/ad:3/sv:thermostat/ad:1`           | Location    | Topic on which events of virtual `thermostat` service for a room with ID `3` are published.                                   |
| `pt:j1/mt:cmd/rt:loc/rn:room/ad:5/sv:thermostat/ad:1`           | Location    | Topic on which commands for virtual `thermostat` service for a room with ID `5` are listened for.                             |
| `pt:j1/mt:evt/rt:ad/rn:zw/ad:1`                                 | Adapter     | Topic on which events of `zw` technology adapter are published.                                                               |
| `pt:j1/mt:cmd/rt:ad/rn:zigbee/ad:1`                             | Adapter     | Topic on which commands for `zw` technology adapter are listened for.                                                         |
| `pt:j1/mt:evt/rt:ad/rn:gateway/ad:1`                            | Adapter     | Special topic on which events of the entire gateway are published.                                                            |
| `pt:j1/mt:cmd/rt:ad/rn:gateway/ad:1`                            | Adapter     | Special topic on which commands for the entire gateway are listened for.                                                      |
| `pt:j1/mt:evt/rt:app/rn:tpflow/ad:1`                            | Application | Topic on which events of `tpflow` application are published.                                                                  |
| `pt:j1/mt:cmd/rt:app/rn:tpflow/ad:1`                            | Application | Topic on which commands for `tpflow` application are listened for.                                                            |
| `pt:j1/mt:rsp/rt:app/rn:tpflow/ad:1`                            | Application | Topic on which a `tpflow` application listens for a response.                                                                 |
| `pt:j1/mt:evt/rt:cloud/rn:backend-service/ad:metrics-collector` | Cloud       | Topic on which a backend service `metrics-collector` publishes its events.                                                    |
| `pt:j1/mt:cmd/rt:cloud/rn:backend-service/ad:metrics-collector` | Cloud       | Topic on which a backend service `metrics-collector` listens for a command.                                                   |
| `pt:j1/mt:rsp/rt:cloud/rn:backend-service/ad:metrics-collector` | Cloud       | Topic on which a backend service `metrics-collector` listens for a response.                                                  |
| `pt:j1/mt:rsp/rt:cloud/rn:remote-client/ad:smarthome-app`       | Cloud       | Topic on which a remote client `smarthome-app` listens for a response.                                                        |
| `pt:j1/mt:evt/rt:discovery`                                     | Discovery   | Special topic on which all resources publish their service discovery reports.                                                 |
| `pt:j1/mt:cmd/rt:discovery`                                     | Discovery   | Special topic on which all service discovery reports can be requested.                                                        |


> Both resource name and address in the response type topics are arbitrary and can be set to any value.
> It is recommended to use resource name of the application or component issuing a command.
> Wherever needed it is possible to use pseudo-random hashes as resource address to emulate synchronous request-response behavior like `pt:j1/mt:rsp/rt:app/rn:tpflow/ad:0d082607`.
> For more details see [`resp_to`](/message-format.md#message-properties) message property in message format section.
