### Gateway service

The service represents gateway, hub or host computer. Adapter topic should be used to communicate with gateway service, *pt:j1/mt:evt/rt:ad/rn:gateway/ad:1* and *pt:j1/mt:evt/rt:ad/rn:gateway/ad:1*.


#### Service names

`gateway`

#### Interface

Type | Interface                 | Value type | Description
-----|---------------------------|------------|------------
in   | cmd.gateway.factory_reset | null       | Instructs gateway to perform factory reset
in   | cmd.gateway.reboot        | null       | Gateways reboot
in   | cmd.gateway.shutdown      | null       | Gateways shutdown
out  | evt.gateway.factory_reset | null       | Factory reset event