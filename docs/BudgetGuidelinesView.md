# BudgetGuidelinesView

Budget guidelines for compensation planning budgets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_guidelines** | **bool** | Whether to use budget guidelines | [optional] 
**soft_minimum** | **float** |  | [optional] 
**soft_maximum** | **float** |  | [optional] 
**guidelines_warning_errors** | [**BudgetGuidelinesWarnings**](BudgetGuidelinesWarnings.md) | Budget guidelines warning errors | [optional] 
**require_comments** | **bool** | Whether a comment is required for recommendations outside of guidelines | [optional] 

## Example

```python
from bamboohr_sdk.models.budget_guidelines_view import BudgetGuidelinesView

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetGuidelinesView from a JSON string
budget_guidelines_view_instance = BudgetGuidelinesView.from_json(json)
# print the JSON string representation of the object
print(BudgetGuidelinesView.to_json())

# convert the object into a dict
budget_guidelines_view_dict = budget_guidelines_view_instance.to_dict()
# create an instance of BudgetGuidelinesView from a dict
budget_guidelines_view_from_dict = BudgetGuidelinesView.from_dict(budget_guidelines_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


