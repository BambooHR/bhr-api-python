# GoalFiltersV1

Array containing goal filters and their counts for API v1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[GoalFiltersV1FiltersInner]**](GoalFiltersV1FiltersInner.md) | Array of goal filter objects with counts | [optional] 

## Example

```python
from bamboohr_sdk.models.goal_filters_v1 import GoalFiltersV1

# TODO update the JSON string below
json = "{}"
# create an instance of GoalFiltersV1 from a JSON string
goal_filters_v1_instance = GoalFiltersV1.from_json(json)
# print the JSON string representation of the object
print(GoalFiltersV1.to_json())

# convert the object into a dict
goal_filters_v1_dict = goal_filters_v1_instance.to_dict()
# create an instance of GoalFiltersV1 from a dict
goal_filters_v1_from_dict = GoalFiltersV1.from_dict(goal_filters_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


