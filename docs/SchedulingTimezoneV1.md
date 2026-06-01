# SchedulingTimezoneV1

A timezone resource with its name and current UTC offset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The timezone identifier. | 
**offset** | **str** | The current UTC offset for this timezone. | 

## Example

```python
from bamboohr_sdk.models.scheduling_timezone_v1 import SchedulingTimezoneV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingTimezoneV1 from a JSON string
scheduling_timezone_v1_instance = SchedulingTimezoneV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingTimezoneV1.to_json())

# convert the object into a dict
scheduling_timezone_v1_dict = scheduling_timezone_v1_instance.to_dict()
# create an instance of SchedulingTimezoneV1 from a dict
scheduling_timezone_v1_from_dict = SchedulingTimezoneV1.from_dict(scheduling_timezone_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


