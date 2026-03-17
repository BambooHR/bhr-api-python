# AssignedTimeOffPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_off_policy_id** | **int** | The ID of the assigned time off policy. | [optional] 
**time_off_type_id** | **int** | The ID of the time off type. | [optional] 
**accrual_start_date** | **date** | The date accruals started in YYYY-MM-DD format. | [optional] 

## Example

```python
from bamboohr_sdk.models.assigned_time_off_policy import AssignedTimeOffPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedTimeOffPolicy from a JSON string
assigned_time_off_policy_instance = AssignedTimeOffPolicy.from_json(json)
# print the JSON string representation of the object
print(AssignedTimeOffPolicy.to_json())

# convert the object into a dict
assigned_time_off_policy_dict = assigned_time_off_policy_instance.to_dict()
# create an instance of AssignedTimeOffPolicy from a dict
assigned_time_off_policy_from_dict = AssignedTimeOffPolicy.from_dict(assigned_time_off_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


