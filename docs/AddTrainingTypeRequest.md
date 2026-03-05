# AddTrainingTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the new training type. | 
**frequency** | **int** | The frequency is the (optional) amount of months between renewing trainings. Not valid if training are not renewable. | [optional] 
**renewable** | **bool** | Renewable is optional but if you are setting it to true you must pass a frequency which is the months between renewals. | [optional] 
**category** | [**AddTrainingTypeRequestCategory**](AddTrainingTypeRequestCategory.md) |  | [optional] 
**required** | **bool** | Is this a required training? | 
**due_from_hire_date** | **int** | Number of days before the training is due for new hires. Not valid unless training is required. | [optional] 
**link_url** | **str** | Optional URL that can be included with a training. | [optional] 
**description** | **str** | Description for the training. | [optional] 
**allow_employees_to_mark_complete** | **bool** | Allows all employees who can view the training to be able to mark it complete. | [optional] 

## Example

```python
from bamboohr_sdk.models.add_training_type_request import AddTrainingTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTrainingTypeRequest from a JSON string
add_training_type_request_instance = AddTrainingTypeRequest.from_json(json)
# print the JSON string representation of the object
print(AddTrainingTypeRequest.to_json())

# convert the object into a dict
add_training_type_request_dict = add_training_type_request_instance.to_dict()
# create an instance of AddTrainingTypeRequest from a dict
add_training_type_request_from_dict = AddTrainingTypeRequest.from_dict(add_training_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


