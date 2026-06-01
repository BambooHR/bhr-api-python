# SchedulingPublishShiftsResultV1

Result of a bulk publish operation, containing both successfully published shifts and any failures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**published** | [**List[SchedulingSchedulingShiftV1]**](SchedulingSchedulingShiftV1.md) | The shifts that were successfully published. | 
**failed** | [**List[SchedulingPublishShiftsFailureV1]**](SchedulingPublishShiftsFailureV1.md) | The shifts that failed to publish due to conflicts. | 

## Example

```python
from bamboohr_sdk.models.scheduling_publish_shifts_result_v1 import SchedulingPublishShiftsResultV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingPublishShiftsResultV1 from a JSON string
scheduling_publish_shifts_result_v1_instance = SchedulingPublishShiftsResultV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingPublishShiftsResultV1.to_json())

# convert the object into a dict
scheduling_publish_shifts_result_v1_dict = scheduling_publish_shifts_result_v1_instance.to_dict()
# create an instance of SchedulingPublishShiftsResultV1 from a dict
scheduling_publish_shifts_result_v1_from_dict = SchedulingPublishShiftsResultV1.from_dict(scheduling_publish_shifts_result_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


