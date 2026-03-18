# TimeOffPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The policy ID. | [optional] 
**time_off_type_id** | **int** | The ID of the time off type this policy belongs to. | [optional] 
**name** | **str** | The policy name. | [optional] 
**effective_date** | **str** | Deprecated. Always null. | [optional] 
**type** | **str** | The policy type. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_off_policy import TimeOffPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffPolicy from a JSON string
time_off_policy_instance = TimeOffPolicy.from_json(json)
# print the JSON string representation of the object
print(TimeOffPolicy.to_json())

# convert the object into a dict
time_off_policy_dict = time_off_policy_instance.to_dict()
# create an instance of TimeOffPolicy from a dict
time_off_policy_from_dict = TimeOffPolicy.from_dict(time_off_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


