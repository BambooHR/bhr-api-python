# TrainingTypeDueFromHireDate

Days before the training is due for new hires. Returns an object with 'unit' and 'amount' when set, or an empty array when not configured.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Unit of time, e.g. &#39;day&#39; | [optional] 
**amount** | **str** | Amount as a string, e.g. &#39;30&#39; | [optional] 

## Example

```python
from bamboohr_sdk.models.training_type_due_from_hire_date import TrainingTypeDueFromHireDate

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingTypeDueFromHireDate from a JSON string
training_type_due_from_hire_date_instance = TrainingTypeDueFromHireDate.from_json(json)
# print the JSON string representation of the object
print(TrainingTypeDueFromHireDate.to_json())

# convert the object into a dict
training_type_due_from_hire_date_dict = training_type_due_from_hire_date_instance.to_dict()
# create an instance of TrainingTypeDueFromHireDate from a dict
training_type_due_from_hire_date_from_dict = TrainingTypeDueFromHireDate.from_dict(training_type_due_from_hire_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


