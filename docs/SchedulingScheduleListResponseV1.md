# SchedulingScheduleListResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SchedulingScheduleV1]**](SchedulingScheduleV1.md) | Array of schedule resource objects | [optional] 
**meta** | [**SchedulingScheduleListResponseV1Meta**](SchedulingScheduleListResponseV1Meta.md) |  | [optional] 
**links** | [**SchedulingScheduleListResponseV1Links**](SchedulingScheduleListResponseV1Links.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.scheduling_schedule_list_response_v1 import SchedulingScheduleListResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingScheduleListResponseV1 from a JSON string
scheduling_schedule_list_response_v1_instance = SchedulingScheduleListResponseV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingScheduleListResponseV1.to_json())

# convert the object into a dict
scheduling_schedule_list_response_v1_dict = scheduling_schedule_list_response_v1_instance.to_dict()
# create an instance of SchedulingScheduleListResponseV1 from a dict
scheduling_schedule_list_response_v1_from_dict = SchedulingScheduleListResponseV1.from_dict(scheduling_schedule_list_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


