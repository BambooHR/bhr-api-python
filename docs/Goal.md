# Goal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique identifier for the record. Use this ID to reference this goal. | 
**title** | **str** | The goal title. | 
**description** | **str** | The goal description. | [optional] 
**percent_complete** | **int** | The goal completion percentage (0 - 100). | [optional] 
**aligns_with_option_id** | **str** | The option ID that aligns with this goal. | [optional] 
**shared_with_employee_ids** | **List[int]** | Employee IDs of employees with whom the goal is shared. All goal owners are considered \&quot;shared with\&quot;. | [optional] 
**due_date** | **str** | The goal due date in YYYY-mm-dd format. | [optional] 
**completion_date** | **float** | The date the goal was completed. | [optional] 

## Example

```python
from bamboohr_sdk.models.goal import Goal

# TODO update the JSON string below
json = "{}"
# create an instance of Goal from a JSON string
goal_instance = Goal.from_json(json)
# print the JSON string representation of the object
print(Goal.to_json())

# convert the object into a dict
goal_dict = goal_instance.to_dict()
# create an instance of Goal from a dict
goal_from_dict = Goal.from_dict(goal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


