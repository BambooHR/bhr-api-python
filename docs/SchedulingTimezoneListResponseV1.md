# SchedulingTimezoneListResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SchedulingTimezoneV1]**](SchedulingTimezoneV1.md) |  | [optional] 
**meta** | [**SchedulingTimezoneListResponseV1Meta**](SchedulingTimezoneListResponseV1Meta.md) |  | [optional] 
**links** | [**SchedulingScheduleListResponseV1Links**](SchedulingScheduleListResponseV1Links.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.scheduling_timezone_list_response_v1 import SchedulingTimezoneListResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingTimezoneListResponseV1 from a JSON string
scheduling_timezone_list_response_v1_instance = SchedulingTimezoneListResponseV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingTimezoneListResponseV1.to_json())

# convert the object into a dict
scheduling_timezone_list_response_v1_dict = scheduling_timezone_list_response_v1_instance.to_dict()
# create an instance of SchedulingTimezoneListResponseV1 from a dict
scheduling_timezone_list_response_v1_from_dict = SchedulingTimezoneListResponseV1.from_dict(scheduling_timezone_list_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


