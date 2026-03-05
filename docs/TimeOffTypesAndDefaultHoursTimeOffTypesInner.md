# TimeOffTypesAndDefaultHoursTimeOffTypesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Time off type ID | 
**name** | **str** | Time off type name | 
**units** | **str** | Units for time off | 
**color** | **str** | Hex color code | 
**icon** | **str** | Icon identifier for the time off type | 
**source** | **str** | Source of the time off type | 

## Example

```python
from bamboohr_sdk.models.time_off_types_and_default_hours_time_off_types_inner import TimeOffTypesAndDefaultHoursTimeOffTypesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffTypesAndDefaultHoursTimeOffTypesInner from a JSON string
time_off_types_and_default_hours_time_off_types_inner_instance = TimeOffTypesAndDefaultHoursTimeOffTypesInner.from_json(json)
# print the JSON string representation of the object
print(TimeOffTypesAndDefaultHoursTimeOffTypesInner.to_json())

# convert the object into a dict
time_off_types_and_default_hours_time_off_types_inner_dict = time_off_types_and_default_hours_time_off_types_inner_instance.to_dict()
# create an instance of TimeOffTypesAndDefaultHoursTimeOffTypesInner from a dict
time_off_types_and_default_hours_time_off_types_inner_from_dict = TimeOffTypesAndDefaultHoursTimeOffTypesInner.from_dict(time_off_types_and_default_hours_time_off_types_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


