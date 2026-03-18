# GoalCommentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**List[GoalCommentsResponseCommentsInner]**](GoalCommentsResponseCommentsInner.md) | Array of comment objects for the goal. | [optional] 

## Example

```python
from bamboohr_sdk.models.goal_comments_response import GoalCommentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoalCommentsResponse from a JSON string
goal_comments_response_instance = GoalCommentsResponse.from_json(json)
# print the JSON string representation of the object
print(GoalCommentsResponse.to_json())

# convert the object into a dict
goal_comments_response_dict = goal_comments_response_instance.to_dict()
# create an instance of GoalCommentsResponse from a dict
goal_comments_response_from_dict = GoalCommentsResponse.from_dict(goal_comments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


