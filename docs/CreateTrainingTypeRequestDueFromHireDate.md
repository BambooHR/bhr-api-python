# CreateTrainingTypeRequestDueFromHireDate

Days before the training is due for new hires (only valid when required is true). Accepts an integer number of days or an object with 'unit' and 'amount'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Unit of time, e.g. &#39;day&#39; | [optional] 
**amount** | **int** | Amount of time | [optional] 

## Example

```python
from bamboohr_sdk.models.create_training_type_request_due_from_hire_date import CreateTrainingTypeRequestDueFromHireDate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTrainingTypeRequestDueFromHireDate from a JSON string
create_training_type_request_due_from_hire_date_instance = CreateTrainingTypeRequestDueFromHireDate.from_json(json)
# print the JSON string representation of the object
print(CreateTrainingTypeRequestDueFromHireDate.to_json())

# convert the object into a dict
create_training_type_request_due_from_hire_date_dict = create_training_type_request_due_from_hire_date_instance.to_dict()
# create an instance of CreateTrainingTypeRequestDueFromHireDate from a dict
create_training_type_request_due_from_hire_date_from_dict = CreateTrainingTypeRequestDueFromHireDate.from_dict(create_training_type_request_due_from_hire_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


