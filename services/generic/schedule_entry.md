### Schedule Entry Service

This service handles a schedule slot for an user who already has valid user access code [user_code](#user-code-service) service. The [year day schedule](z-wave/User_Code.md#schedule_entry_lock) represents two days, any time apart, where the specified user ID’s code is valid. When setting the schedule slot, the start parameters of the time fence needs to occur prior to the stop parameters and the year day schedule is automatically enabled for the identified user.

Note: Each user can only use one type of scheduling at a time.

Detailed specification is avaliable in [User_Code.md](z-wave/User_Code.md) in the z-wave folder.

#### Service names

`schedule_entry`

#### Interface

Type | Interface                     | Value type | Description
-----|-------------------------------|------------|------------
in   | cmd.schedule_entry.get_report | null       | Get schedule entry report for specified slot
in   | cmd.schedule_entry.set        | int_map    | Set schedule entry
in   | cmd.schedule_entry.clear      | int_map    | Clear schedule entry
out  | evt.schedule_entry.report     | int_map    | Schedule entry report



