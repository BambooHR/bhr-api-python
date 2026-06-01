# UpdateGoalSharingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared_with_employee_ids** | **List[Optional[int]]** | List of employee IDs with whom the goal is shared. Must include the employee ID of the goal owner. | [optional] 

## Example

```python
from bamboohr_sdk.models.update_goal_sharing_request import UpdateGoalSharingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGoalSharingRequest from a JSON string
update_goal_sharing_request_instance = UpdateGoalSharingRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGoalSharingRequest.to_json())

# convert the object into a dict
update_goal_sharing_request_dict = update_goal_sharing_request_instance.to_dict()
# create an instance of UpdateGoalSharingRequest from a dict
update_goal_sharing_request_from_dict = UpdateGoalSharingRequest.from_dict(update_goal_sharing_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


