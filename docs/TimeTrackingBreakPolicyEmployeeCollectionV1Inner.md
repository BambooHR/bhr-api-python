# TimeTrackingBreakPolicyEmployeeCollectionV1Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The employee ID | 
**name** | **str** | The employee name {Preferred Last} | 
**photo_url** | **str** | The employee profile photo | 

## Example

```python
from bamboohr_sdk.models.time_tracking_break_policy_employee_collection_v1_inner import TimeTrackingBreakPolicyEmployeeCollectionV1Inner

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingBreakPolicyEmployeeCollectionV1Inner from a JSON string
time_tracking_break_policy_employee_collection_v1_inner_instance = TimeTrackingBreakPolicyEmployeeCollectionV1Inner.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingBreakPolicyEmployeeCollectionV1Inner.to_json())

# convert the object into a dict
time_tracking_break_policy_employee_collection_v1_inner_dict = time_tracking_break_policy_employee_collection_v1_inner_instance.to_dict()
# create an instance of TimeTrackingBreakPolicyEmployeeCollectionV1Inner from a dict
time_tracking_break_policy_employee_collection_v1_inner_from_dict = TimeTrackingBreakPolicyEmployeeCollectionV1Inner.from_dict(time_tracking_break_policy_employee_collection_v1_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


