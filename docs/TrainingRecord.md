# TrainingRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the training record. | [optional] 
**employee_id** | **int** | The ID of the employee associated with the training. | [optional] 
**completed** | **str** | Completed is a date in the format yyyy-mm-dd. | [optional] 
**notes** | **str** | Notes left on the training record. | [optional] 
**instructor** | **str** | Name of the instructor. | [optional] 
**credits** | **float** | What was credited for the training record. | [optional] 
**hours** | **float** | Hours associated with the training record. | [optional] 
**cost** | **str** | The currency and cost for the training record. | [optional] 
**type** | **int** | The training type ID. | [optional] 

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


