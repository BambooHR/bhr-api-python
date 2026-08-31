# SchedulingPublishShiftsFailureV1

A shift that failed to publish due to a conflict

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shift_id** | **str** | The ID of the shift that failed to publish. | 
**reason** | **str** | The reason the shift failed to publish. | 

## Example

```python
from bamboohr_sdk.models.scheduling_publish_shifts_failure_v1 import SchedulingPublishShiftsFailureV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingPublishShiftsFailureV1 from a JSON string
scheduling_publish_shifts_failure_v1_instance = SchedulingPublishShiftsFailureV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingPublishShiftsFailureV1.to_json())

# convert the object into a dict
scheduling_publish_shifts_failure_v1_dict = scheduling_publish_shifts_failure_v1_instance.to_dict()
# create an instance of SchedulingPublishShiftsFailureV1 from a dict
scheduling_publish_shifts_failure_v1_from_dict = SchedulingPublishShiftsFailureV1.from_dict(scheduling_publish_shifts_failure_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


