# UpdateGoalMilestoneProgressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete** | **bool** | Whether the milestone is complete or not | 

## Example

```python
from bamboohr_sdk.models.update_goal_milestone_progress_request import UpdateGoalMilestoneProgressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGoalMilestoneProgressRequest from a JSON string
update_goal_milestone_progress_request_instance = UpdateGoalMilestoneProgressRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGoalMilestoneProgressRequest.to_json())

# convert the object into a dict
update_goal_milestone_progress_request_dict = update_goal_milestone_progress_request_instance.to_dict()
# create an instance of UpdateGoalMilestoneProgressRequest from a dict
update_goal_milestone_progress_request_from_dict = UpdateGoalMilestoneProgressRequest.from_dict(update_goal_milestone_progress_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


