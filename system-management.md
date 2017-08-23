## Connecting a system to FH system .   

    Connection process consists of 2 steps : 
    1. An application sends "system connect" command to adapter. 
    2. Adapter generates multiple inclusion_report events in return , one report per device.


#### System connect command:

Topic : pt:j1/mt:cmd/rt:ad/rn:ikea/ad:1 (ikea is just an example, it has to be replaces with real adapter name)

Message :
```json 
{"serv":"zwave-ad",
 "type":"cmd.system.connect",
 "val_t":"str_map",
 "val":{"security_key":"12324234324","address":"192.168.80.2"},
 "props":null,
 "tags":null,
 "ctime":"2017-08-23T12:07:00+0200",
 "uid":"124235254"
}
```

#### Connection report:

Topic : pt:j1/mt:evt/rt:ad/rn:ikea/ad:1

In response the system should generate one inclusion report per device. 

[Inclusion report](thing-management.md)


#### System disconnect command:

Topic : pt:j1/mt:cmd/rt:ad/rn:ikea/ad:1

Message :
 ```json 
{
    "serv": "zwave-ad",
    "type": "cmd.system.disconnect",
    "val_t": "string",
    "val": "",
    "props": null,
    "tags": null,
    "ctime":"2017-08-23T12:07:00+0200",
    "uid":"124235254"
}
```

#### Disconnection report:

Topic : pt:j1/mt:evt/rt:ad/rn:ikea/ad:1

In response the system should generate one exclusion report per device. 

[Inclusion report](thing-management.md)