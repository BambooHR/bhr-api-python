# UpdateEmployeeTrainingRecordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **str** | Completed is the only required field and must be in yyyy-mm-dd format. The other parameters are optional. | 
**cost** | [**CreateEmployeeTrainingRecordRequestCost**](CreateEmployeeTrainingRecordRequestCost.md) |  | [optional] 
**instructor** | **str** | Name of the training instructor. | [optional] 
**hours** | **float** | Number of hours for the training. | [optional] 
**credits** | **float** | Credits earned for the training. | [optional] 
**notes** | **str** | Optional notes about the training record. | [optional] 

## Example

```python
from bamboohr_sdk.models.update_employee_training_record_request import UpdateEmployeeTrainingRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEmployeeTrainingRecordRequest from a JSON string
update_employee_training_record_request_instance = UpdateEmployeeTrainingRecordRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEmployeeTrainingRecordRequest.to_json())

# convert the object into a dict
update_employee_training_record_request_dict = update_employee_training_record_request_instance.to_dict()
# create an instance of UpdateEmployeeTrainingRecordRequest from a dict
update_employee_training_record_request_from_dict = UpdateEmployeeTrainingRecordRequest.from_dict(update_employee_training_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


