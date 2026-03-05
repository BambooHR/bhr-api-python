# GoalFiltersV11

Array containing goal filters, their counts, and actions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[GoalFiltersV11FiltersInner]**](GoalFiltersV11FiltersInner.md) | Array of goal filter objects with counts | [optional] 

## Example

```python
from bamboohr_sdk.models.goal_filters_v11 import GoalFiltersV11

# TODO update the JSON string below
json = "{}"
# create an instance of GoalFiltersV11 from a JSON string
goal_filters_v11_instance = GoalFiltersV11.from_json(json)
# print the JSON string representation of the object
print(GoalFiltersV11.to_json())

# convert the object into a dict
goal_filters_v11_dict = goal_filters_v11_instance.to_dict()
# create an instance of GoalFiltersV11 from a dict
goal_filters_v11_from_dict = GoalFiltersV11.from_dict(goal_filters_v11_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


