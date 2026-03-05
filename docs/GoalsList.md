# GoalsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goals** | [**List[TransformedApiGoal]**](TransformedApiGoal.md) | All goals of the selected employee | [optional] 

## Example

```python
from bamboohr_sdk.models.goals_list import GoalsList

# TODO update the JSON string below
json = "{}"
# create an instance of GoalsList from a JSON string
goals_list_instance = GoalsList.from_json(json)
# print the JSON string representation of the object
print(GoalsList.to_json())

# convert the object into a dict
goals_list_dict = goals_list_instance.to_dict()
# create an instance of GoalsList from a dict
goals_list_from_dict = GoalsList.from_dict(goals_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


