# UpdateGoalV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | [Required] The goal title. | 
**description** | **str** | [Optional] The goal description. If omitted, the existing value will be overwritten with an empty string. | [optional] 
**percent_complete** | **int** | [Optional] The goal completion percentage (0-100). If omitted, the existing value will be overwritten with 0. | [optional] 
**aligns_with_option_id** | **str** |  | [optional] 
**shared_with_employee_ids** | **List[int]** | [Required] Employee IDs of employees with whom the goal is shared. All goal owners are considered \&quot;shared with\&quot;. This must include the employee for whom the goal is created. | 
**due_date** | **date** | [Required] The goal due date in YYYY-MM-DD format. | 
**completion_date** | **date** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.update_goal_v1 import UpdateGoalV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGoalV1 from a JSON string
update_goal_v1_instance = UpdateGoalV1.from_json(json)
# print the JSON string representation of the object
print(UpdateGoalV1.to_json())

# convert the object into a dict
update_goal_v1_dict = update_goal_v1_instance.to_dict()
# create an instance of UpdateGoalV1 from a dict
update_goal_v1_from_dict = UpdateGoalV1.from_dict(update_goal_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


