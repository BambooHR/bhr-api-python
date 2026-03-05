# TimeTrackingUpdateTimeTrackingBreakPolicyV1

Data contract for updating a break policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the break policy | [optional] 
**description** | **str** | Optional description of the break policy | [optional] 
**all_employees_assigned** | **bool** | Whether all employees are assigned to this break policy | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_update_time_tracking_break_policy_v1 import TimeTrackingUpdateTimeTrackingBreakPolicyV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingUpdateTimeTrackingBreakPolicyV1 from a JSON string
time_tracking_update_time_tracking_break_policy_v1_instance = TimeTrackingUpdateTimeTrackingBreakPolicyV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingUpdateTimeTrackingBreakPolicyV1.to_json())

# convert the object into a dict
time_tracking_update_time_tracking_break_policy_v1_dict = time_tracking_update_time_tracking_break_policy_v1_instance.to_dict()
# create an instance of TimeTrackingUpdateTimeTrackingBreakPolicyV1 from a dict
time_tracking_update_time_tracking_break_policy_v1_from_dict = TimeTrackingUpdateTimeTrackingBreakPolicyV1.from_dict(time_tracking_update_time_tracking_break_policy_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


