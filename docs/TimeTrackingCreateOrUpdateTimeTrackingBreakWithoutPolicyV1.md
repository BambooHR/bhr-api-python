# TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1

Data contract for creating or updating a break

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | The name of the break | [optional] 
**paid** | **bool** | Whether the break is paid | [optional] 
**duration** | **int** | Duration of the break in minutes | [optional] 
**availability_type** | **str** | When the break is available to be taken | [optional] 
**availability_min_hours_worked** | **float** |  | [optional] 
**availability_max_hours_worked** | **float** |  | [optional] 
**availability_start_time** | **str** |  | [optional] 
**availability_end_time** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_create_or_update_time_tracking_break_without_policy_v1 import TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1 from a JSON string
time_tracking_create_or_update_time_tracking_break_without_policy_v1_instance = TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1.to_json())

# convert the object into a dict
time_tracking_create_or_update_time_tracking_break_without_policy_v1_dict = time_tracking_create_or_update_time_tracking_break_without_policy_v1_instance.to_dict()
# create an instance of TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1 from a dict
time_tracking_create_or_update_time_tracking_break_without_policy_v1_from_dict = TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1.from_dict(time_tracking_create_or_update_time_tracking_break_without_policy_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


