### Application and adapter discovery protocol 

Every applicatoin or adapter has to subscribe to well known discovery topic . 
**Well known discovery topic** : pt:j1/mt:cmd/rt:discovery

In order to discover application or adapter , an application have to send discovery request message to well known address .
Whenever an application or adapter receives discovery request it has to respond with dicovery event . 

**Discovery response event topic** : pt:j1/mt:evt/rt:discovery 


Discovery request : 

```json

```
