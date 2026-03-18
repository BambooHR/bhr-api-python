# TrainingType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the training | [optional] 
**name** | **str** | Name of the training type. | [optional] 
**renewable** | **bool** | If true, training will be renewed based off of frequency. | [optional] 
**frequency** | **int** | The frequency is the (optional) amount of months between renewing trainings. Not valid if training are not renewable. | [optional] 
**due_from_hire_date** | [**TrainingTypeDueFromHireDate**](TrainingTypeDueFromHireDate.md) |  | [optional] 
**required** | **bool** | Whether this is a required training. Null when not set. | [optional] 
**category** | [**TrainingTypeCategory**](TrainingTypeCategory.md) |  | [optional] 
**link_url** | **str** | Optional URL that can be included with a training. Null when not set. | [optional] 
**description** | **str** | Description for the training. Null when not set. | [optional] 
**allow_employees_to_mark_complete** | **bool** | Allows all employees who can view the training to be able to mark it complete. | [optional] 

## Example

```python
from bamboohr_sdk.models.training_type import TrainingType

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingType from a JSON string
training_type_instance = TrainingType.from_json(json)
# print the JSON string representation of the object
print(TrainingType.to_json())

# convert the object into a dict
training_type_dict = training_type_instance.to_dict()
# create an instance of TrainingType from a dict
training_type_from_dict = TrainingType.from_dict(training_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


