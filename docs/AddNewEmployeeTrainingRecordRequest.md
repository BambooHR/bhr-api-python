# AddNewEmployeeTrainingRecordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **str** | Completed is a required field and must be in yyyy-mm-dd format. | 
**cost** | [**AddNewEmployeeTrainingRecordRequestCost**](AddNewEmployeeTrainingRecordRequestCost.md) |  | [optional] 
**instructor** | **str** |  | [optional] 
**hours** | **float** |  | [optional] 
**credits** | **float** |  | [optional] 
**notes** | **str** |  | [optional] 
**type** | **int** | This must be an existing training type id. | 

## Example

```python
from bamboohr_sdk.models.add_new_employee_training_record_request import AddNewEmployeeTrainingRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddNewEmployeeTrainingRecordRequest from a JSON string
add_new_employee_training_record_request_instance = AddNewEmployeeTrainingRecordRequest.from_json(json)
# print the JSON string representation of the object
print(AddNewEmployeeTrainingRecordRequest.to_json())

# convert the object into a dict
add_new_employee_training_record_request_dict = add_new_employee_training_record_request_instance.to_dict()
# create an instance of AddNewEmployeeTrainingRecordRequest from a dict
add_new_employee_training_record_request_from_dict = AddNewEmployeeTrainingRecordRequest.from_dict(add_new_employee_training_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


