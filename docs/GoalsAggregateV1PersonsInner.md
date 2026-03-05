# GoalsAggregateV1PersonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | The id of this employee. | [optional] 
**user_id** | **int** | The user id of the person if applicable. | [optional] 
**display_first_name** | **str** | First name of the person. | [optional] 
**last_name** | **str** | Last name of the person. | [optional] 
**photo_url** | **str** | url of the user profile image. | [optional] 

## Example

```python
from bamboohr_sdk.models.goals_aggregate_v1_persons_inner import GoalsAggregateV1PersonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GoalsAggregateV1PersonsInner from a JSON string
goals_aggregate_v1_persons_inner_instance = GoalsAggregateV1PersonsInner.from_json(json)
# print the JSON string representation of the object
print(GoalsAggregateV1PersonsInner.to_json())

# convert the object into a dict
goals_aggregate_v1_persons_inner_dict = goals_aggregate_v1_persons_inner_instance.to_dict()
# create an instance of GoalsAggregateV1PersonsInner from a dict
goals_aggregate_v1_persons_inner_from_dict = GoalsAggregateV1PersonsInner.from_dict(goals_aggregate_v1_persons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


