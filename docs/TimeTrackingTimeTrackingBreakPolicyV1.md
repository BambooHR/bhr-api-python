# TimeTrackingTimeTrackingBreakPolicyV1

A policy governing breaks for time tracking

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the break policy | [optional] [readonly] 
**name** | **str** | Name of the break policy | [optional] 
**description** | **str** | Optional description of the break policy | [optional] 
**all_employees_assigned** | **bool** | Whether all employees are assigned to this break policy | [optional] 
**created_at** | **datetime** | ISO 8601 timestamp when the break policy was created | [optional] [readonly] 
**updated_at** | **datetime** | ISO 8601 timestamp when the break policy was last updated | [optional] [readonly] 
**deleted_at** | **datetime** | ISO 8601 timestamp when the break policy was deleted | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.time_tracking_time_tracking_break_policy_v1 import TimeTrackingTimeTrackingBreakPolicyV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingTimeTrackingBreakPolicyV1 from a JSON string
time_tracking_time_tracking_break_policy_v1_instance = TimeTrackingTimeTrackingBreakPolicyV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingTimeTrackingBreakPolicyV1.to_json())

# convert the object into a dict
time_tracking_time_tracking_break_policy_v1_dict = time_tracking_time_tracking_break_policy_v1_instance.to_dict()
# create an instance of TimeTrackingTimeTrackingBreakPolicyV1 from a dict
time_tracking_time_tracking_break_policy_v1_from_dict = TimeTrackingTimeTrackingBreakPolicyV1.from_dict(time_tracking_time_tracking_break_policy_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


