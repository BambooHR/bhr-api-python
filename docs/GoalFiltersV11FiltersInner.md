# GoalFiltersV11FiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Filter identifier based on goal status. | [optional] 
**name** | **str** | Display name of the filter | [optional] 
**count** | **int** | Number of goals matching this filter | [optional] 
**actions** | [**GoalFiltersV11FiltersInnerActions**](GoalFiltersV11FiltersInnerActions.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.goal_filters_v11_filters_inner import GoalFiltersV11FiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GoalFiltersV11FiltersInner from a JSON string
goal_filters_v11_filters_inner_instance = GoalFiltersV11FiltersInner.from_json(json)
# print the JSON string representation of the object
print(GoalFiltersV11FiltersInner.to_json())

# convert the object into a dict
goal_filters_v11_filters_inner_dict = goal_filters_v11_filters_inner_instance.to_dict()
# create an instance of GoalFiltersV11FiltersInner from a dict
goal_filters_v11_filters_inner_from_dict = GoalFiltersV11FiltersInner.from_dict(goal_filters_v11_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


