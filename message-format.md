# FIMP message format 

Messages send using FIMP are JSON messages containing the following properties:

Property | Type                | Required | Description               
---------|---------------------|----------|------------
corid    | String              | No       | Message correlation id. Used for request - response matching.
ctime    | String              | Yes      | Message creation time, e.g. `"2019-05-31 17:36:31 +0200"`
props    | Map<String, String> | Yes      | Map of properties.
resp_to  | String              | No*      | Response topic where requester will expect to receive response.
serv     | String              | Yes      | Service name the interface is part of.
src      | String              | Yes      | Source or of the message, should be set only for commands.
tags     | List<String>        | No       | List of tags.
type     | String              | Yes      | Interface type, defines message format.
uid      | String              | Yes      | Unique message identifier.
val      | dynamic             | Yes      | "payload" - type is defined by `val_t`.
val_t    | String              | Yes      | Data format of `val` field. See below.
ver      | String              | Yes      | Version of the message format, default: `"1"`.

\*Required for Prime Fimp messages.

Since `val` can be any type, `val_t` defines what type it is. List of supported `val` types: 

`val_t`     | Sample `val`
------------|-------------
string      | `'Hello world!'`
int         | `3`
float       | `3.1415`
bool        | `true`
null        | `null`
str_array   | `['hello, 'world']`
int_array   | `[0, 1, 1, 2, 3, 5, 8, 13]`
float_array | `[3.14, 2.71]`
int_map     | `{"answer": 42}`
str_map     | `{"ip": "192.168.1.1"}`
float_map   | `{"pi: 3.14"}`
bool_map    | `{"normalityRestored": true}`
object*     | `{"nested": {"objects": "supported"}}`
base64      | `U28gbG9uZywgYW5kIHRoYW5rcyBmb3IgYWxsIHRoZSBmaXNoLg==`

\*A complex object which can't be mapped to primitive types. The structure of an object is defined by interface type and is unique for every interface type. 

# Example messages

TODO(alivinco): add sample FIMP messages.
