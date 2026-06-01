# TrainingRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the training record. | [optional] 
**employee_id** | **str** | The ID of the employee associated with the training, returned as a string. | [optional] 
**completed** | **date** | Completed is a date in the format yyyy-mm-dd. | [optional] 
**notes** | **str** |  | [optional] 
**instructor** | **str** |  | [optional] 
**credits** | **str** |  | [optional] 
**hours** | **str** |  | [optional] 
**cost** | **str** |  | [optional] 
**type** | [**TrainingRecordType**](TrainingRecordType.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.training_record import TrainingRecord

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingRecord from a JSON string
training_record_instance = TrainingRecord.from_json(json)
# print the JSON string representation of the object
print(TrainingRecord.to_json())

# convert the object into a dict
training_record_dict = training_record_instance.to_dict()
# create an instance of TrainingRecord from a dict
training_record_from_dict = TrainingRecord.from_dict(training_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


