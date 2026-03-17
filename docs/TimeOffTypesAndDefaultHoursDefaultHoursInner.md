# TimeOffTypesAndDefaultHoursDefaultHoursInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Day of week | 
**amount** | **str** | Default hours for the day. Returned as a stringified decimal value. | 

## Example

```python
from bamboohr_sdk.models.time_off_types_and_default_hours_default_hours_inner import TimeOffTypesAndDefaultHoursDefaultHoursInner

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffTypesAndDefaultHoursDefaultHoursInner from a JSON string
time_off_types_and_default_hours_default_hours_inner_instance = TimeOffTypesAndDefaultHoursDefaultHoursInner.from_json(json)
# print the JSON string representation of the object
print(TimeOffTypesAndDefaultHoursDefaultHoursInner.to_json())

# convert the object into a dict
time_off_types_and_default_hours_default_hours_inner_dict = time_off_types_and_default_hours_default_hours_inner_instance.to_dict()
# create an instance of TimeOffTypesAndDefaultHoursDefaultHoursInner from a dict
time_off_types_and_default_hours_default_hours_inner_from_dict = TimeOffTypesAndDefaultHoursDefaultHoursInner.from_dict(time_off_types_and_default_hours_default_hours_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


