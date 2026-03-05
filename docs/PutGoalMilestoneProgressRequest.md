# PutGoalMilestoneProgressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete** | **bool** | Whether the milestone is complete or not | 

## Example

```python
from bamboohr_sdk.models.put_goal_milestone_progress_request import PutGoalMilestoneProgressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutGoalMilestoneProgressRequest from a JSON string
put_goal_milestone_progress_request_instance = PutGoalMilestoneProgressRequest.from_json(json)
# print the JSON string representation of the object
print(PutGoalMilestoneProgressRequest.to_json())

# convert the object into a dict
put_goal_milestone_progress_request_dict = put_goal_milestone_progress_request_instance.to_dict()
# create an instance of PutGoalMilestoneProgressRequest from a dict
put_goal_milestone_progress_request_from_dict = PutGoalMilestoneProgressRequest.from_dict(put_goal_milestone_progress_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


