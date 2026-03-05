# TransformedApiEmployeeGoalDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal** | [**TransformedApiEmployeeGoalDetailsGoal**](TransformedApiEmployeeGoalDetailsGoal.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.transformed_api_employee_goal_details import TransformedApiEmployeeGoalDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TransformedApiEmployeeGoalDetails from a JSON string
transformed_api_employee_goal_details_instance = TransformedApiEmployeeGoalDetails.from_json(json)
# print the JSON string representation of the object
print(TransformedApiEmployeeGoalDetails.to_json())

# convert the object into a dict
transformed_api_employee_goal_details_dict = transformed_api_employee_goal_details_instance.to_dict()
# create an instance of TransformedApiEmployeeGoalDetails from a dict
transformed_api_employee_goal_details_from_dict = TransformedApiEmployeeGoalDetails.from_dict(transformed_api_employee_goal_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


