# CanCreateGoalsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_create_goals** | **bool** | Whether the API user can create a goal for this employee. | [optional] 

## Example

```python
from bamboohr_sdk.models.can_create_goals_response import CanCreateGoalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CanCreateGoalsResponse from a JSON string
can_create_goals_response_instance = CanCreateGoalsResponse.from_json(json)
# print the JSON string representation of the object
print(CanCreateGoalsResponse.to_json())

# convert the object into a dict
can_create_goals_response_dict = can_create_goals_response_instance.to_dict()
# create an instance of CanCreateGoalsResponse from a dict
can_create_goals_response_from_dict = CanCreateGoalsResponse.from_dict(can_create_goals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


