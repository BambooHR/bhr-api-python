# PutGoalSharedWithRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared_with_employee_ids** | **List[int]** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.put_goal_shared_with_request import PutGoalSharedWithRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutGoalSharedWithRequest from a JSON string
put_goal_shared_with_request_instance = PutGoalSharedWithRequest.from_json(json)
# print the JSON string representation of the object
print(PutGoalSharedWithRequest.to_json())

# convert the object into a dict
put_goal_shared_with_request_dict = put_goal_shared_with_request_instance.to_dict()
# create an instance of PutGoalSharedWithRequest from a dict
put_goal_shared_with_request_from_dict = PutGoalSharedWithRequest.from_dict(put_goal_shared_with_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


