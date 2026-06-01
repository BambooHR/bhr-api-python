# BudgetGuidelinesWarnings

Warning messages for saved budget guidelines

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**soft_minimum_warning_message** | **str** |  | [optional] 
**soft_maximum_warning_message** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.budget_guidelines_warnings import BudgetGuidelinesWarnings

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetGuidelinesWarnings from a JSON string
budget_guidelines_warnings_instance = BudgetGuidelinesWarnings.from_json(json)
# print the JSON string representation of the object
print(BudgetGuidelinesWarnings.to_json())

# convert the object into a dict
budget_guidelines_warnings_dict = budget_guidelines_warnings_instance.to_dict()
# create an instance of BudgetGuidelinesWarnings from a dict
budget_guidelines_warnings_from_dict = BudgetGuidelinesWarnings.from_dict(budget_guidelines_warnings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


