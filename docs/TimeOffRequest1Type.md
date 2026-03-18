# TimeOffRequest1Type

The time off type for this request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The time off type ID. | [optional] 
**name** | **str** | The time off type name. | [optional] 
**icon** | **str** | The icon name for the time off type. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_off_request1_type import TimeOffRequest1Type

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffRequest1Type from a JSON string
time_off_request1_type_instance = TimeOffRequest1Type.from_json(json)
# print the JSON string representation of the object
print(TimeOffRequest1Type.to_json())

# convert the object into a dict
time_off_request1_type_dict = time_off_request1_type_instance.to_dict()
# create an instance of TimeOffRequest1Type from a dict
time_off_request1_type_from_dict = TimeOffRequest1Type.from_dict(time_off_request1_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


