# CreateEmployeeTrainingRecordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **str** | Completed is a required field and must be in yyyy-mm-dd format. | 
**cost** | [**CreateEmployeeTrainingRecordRequestCost**](CreateEmployeeTrainingRecordRequestCost.md) |  | [optional] 
**instructor** | **str** | Name of the training instructor. | [optional] 
**hours** | **float** | Number of hours for the training. | [optional] 
**credits** | **float** | Credits earned for the training. | [optional] 
**notes** | **str** | Optional notes about the training record. | [optional] 
**type** | **int** | This must be an existing training type ID. | 

## Example

```python
from bamboohr_sdk.models.create_employee_training_record_request import CreateEmployeeTrainingRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmployeeTrainingRecordRequest from a JSON string
create_employee_training_record_request_instance = CreateEmployeeTrainingRecordRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEmployeeTrainingRecordRequest.to_json())

# convert the object into a dict
create_employee_training_record_request_dict = create_employee_training_record_request_instance.to_dict()
# create an instance of CreateEmployeeTrainingRecordRequest from a dict
create_employee_training_record_request_from_dict = CreateEmployeeTrainingRecordRequest.from_dict(create_employee_training_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


