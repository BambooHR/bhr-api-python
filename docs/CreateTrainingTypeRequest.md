# CreateTrainingTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the new training type. | 
**frequency** | **int** | The frequency is the (optional) amount of months between renewing trainings. Not valid if training are not renewable. | [optional] 
**renewable** | **bool** | Renewable is optional but if you are setting it to true you must pass a frequency which is the months between renewals. | [optional] 
**category** | [**CreateTrainingTypeRequestCategory**](CreateTrainingTypeRequestCategory.md) |  | [optional] 
**required** | **bool** | Is this a required training? | [optional] 
**due_from_hire_date** | [**CreateTrainingTypeRequestDueFromHireDate**](CreateTrainingTypeRequestDueFromHireDate.md) |  | [optional] 
**link_url** | **str** | Optional URL that can be included with a training. | [optional] 
**description** | **str** | Description for the training. | [optional] 
**allow_employees_to_mark_complete** | **bool** | Allows all employees who can view the training to be able to mark it complete. | [optional] 

## Example

```python
from bamboohr_sdk.models.create_training_type_request import CreateTrainingTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTrainingTypeRequest from a JSON string
create_training_type_request_instance = CreateTrainingTypeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTrainingTypeRequest.to_json())

# convert the object into a dict
create_training_type_request_dict = create_training_type_request_instance.to_dict()
# create an instance of CreateTrainingTypeRequest from a dict
create_training_type_request_from_dict = CreateTrainingTypeRequest.from_dict(create_training_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


