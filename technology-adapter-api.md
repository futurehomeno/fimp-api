# Technology adapter API

The following APIs should be common across all adapters, but the example code will use zwave-ad. Notes have been added for specific differences for the most common adapters.

## Error reporting.

Topic: `pt:j1/mt:evt/rt:ad/rn:zw/ad:1` or service address: `pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:dev_sys/ad:95_0`

Message:

```json
{
    "serv": "zigbee",
    "type": "evt.error.report",
    "val": "TX_ERROR",
    "val_t": "string",
    "props": {
        "msg": "TRANSMIT_COMPLETE_NOROUTE",
        "src": "nodeId=64_0"
    },
    "tags": [],
    "ctime": "2018-11-22T23:14:40+0100",
    "uid":"76533455876765"
 }
```

val - is error code, src - origin of the error.

## Requesting list of devices from adapter

An adapter has to support an API for requesting a list of devices and respond with the list.

### Command

Topic: `pt:j1/mt:cmd/rt:ad/rn:zigbee/ad:1`

Message:

```json
{
    "serv": "zigbee",
    "type": "cmd.network.get_all_nodes",
    "val_t": "null",
    "val": null,
    "props": null,
    "tags": null,
    "ctime": "2018-11-22T23:14:40+0100",
    "uid":"76533455876765"
}
```

### Report event

Topic: `pt:j1/mt:evt/rt:ad/rn:zigbee/ad:1`

Message:

```json
{
    "ctime": "2018-11-23T16:53:11+0100",
    "props": {},
    "serv": "zigbee",
    "tags": [],
    "type": "evt.network.all_nodes_report",
    "val": [
        {
            "address": "46",
            "alias":"Sensor 1 ",
            "hash": "zw_398_3_12",
            "power_source": "battery",
            "status": "DOWN",
            "wakeup_int": "4200"
        },
        {
            "address": "63",
            "alias":"Sensor 2 ",
            "hash": "zw_271_1794_4096",
            "power_source": "battery",
            "status": "UP",
            "wakeup_int": "3600"
        },
        {
            "address": "80",
            "alias":"Dimmer ",
            "hash": "zw_134_3_96",
            "power_source": "ac",
            "status": "UP",
            "wakeup_int": "-1"
        }
    ],
    "val_t": "object"
}
```

address - is technology specific device address

alias (optional) - device or product name or alias

hash (optional) - product unique identifier

power_source - power source descriptor, ac,battery

status (optional) - device status

wakeup_int (optional) - device wakeup interval, applicable only if device is battery powered.

## Certification Test
Supported by zigbee-ad. When `cmd.cert_test.start` is received, the transceiver starts sending `cmd.binary.set` to the device which node id and endpoint are provided in the payload every 50ms. When `cmd.cert_test.stop` is received the test is stopped.

__Topic__

`pt:j1/mt:cmd/rt:ad/rn:zigbee/ad:1`

__Message__

`val` field in the payload has the format `<node_id>_<endpoint_id>`. The `endpoint_id` is typically `1` for Ikea Trådfri plug and `3` for Osram Smart+ Plug. The `node_id` is the id the device gets when added to the network. Both values can be obtained from the Zigbee service description in FimpUI.

```json
{
    "type": "cmd.cert_test.start",
    "val_t": "string",
    "val": "1_1",
    "props": null,
    "tags": null,
    "src": "thingsplex-ui",
    "ver": "1"
}
```

```json
{
    "type": "cmd.cert_test.stop",
    "val_t": "string",
    "val": "1_1",
    "props": null,
    "tags": null,
    "src": "thingsplex-ui",
    "ver": "1"
}
```
