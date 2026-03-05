# TimeOffTypesAndDefaultHours


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_off_types** | [**List[TimeOffTypesAndDefaultHoursTimeOffTypesInner]**](TimeOffTypesAndDefaultHoursTimeOffTypesInner.md) |  | 
**default_hours** | [**List[TimeOffTypesAndDefaultHoursDefaultHoursInner]**](TimeOffTypesAndDefaultHoursDefaultHoursInner.md) |  | 

## Example

```python
from bamboohr_sdk.models.time_off_types_and_default_hours import TimeOffTypesAndDefaultHours

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffTypesAndDefaultHours from a JSON string
time_off_types_and_default_hours_instance = TimeOffTypesAndDefaultHours.from_json(json)
# print the JSON string representation of the object
print(TimeOffTypesAndDefaultHours.to_json())

# convert the object into a dict
time_off_types_and_default_hours_dict = time_off_types_and_default_hours_instance.to_dict()
# create an instance of TimeOffTypesAndDefaultHours from a dict
time_off_types_and_default_hours_from_dict = TimeOffTypesAndDefaultHours.from_dict(time_off_types_and_default_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


