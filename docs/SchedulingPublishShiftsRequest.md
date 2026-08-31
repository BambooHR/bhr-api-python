# SchedulingPublishShiftsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shift_ids** | **List[Optional[str]]** | Shift IDs to publish. | 

## Example

```python
from bamboohr_sdk.models.scheduling_publish_shifts_request import SchedulingPublishShiftsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingPublishShiftsRequest from a JSON string
scheduling_publish_shifts_request_instance = SchedulingPublishShiftsRequest.from_json(json)
# print the JSON string representation of the object
print(SchedulingPublishShiftsRequest.to_json())

# convert the object into a dict
scheduling_publish_shifts_request_dict = scheduling_publish_shifts_request_instance.to_dict()
# create an instance of SchedulingPublishShiftsRequest from a dict
scheduling_publish_shifts_request_from_dict = SchedulingPublishShiftsRequest.from_dict(scheduling_publish_shifts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


