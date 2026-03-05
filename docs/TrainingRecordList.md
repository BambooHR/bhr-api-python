# TrainingRecordList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**training_id** | [**TrainingRecord**](TrainingRecord.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.training_record_list import TrainingRecordList

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingRecordList from a JSON string
training_record_list_instance = TrainingRecordList.from_json(json)
# print the JSON string representation of the object
print(TrainingRecordList.to_json())

# convert the object into a dict
training_record_list_dict = training_record_list_instance.to_dict()
# create an instance of TrainingRecordList from a dict
training_record_list_from_dict = TrainingRecordList.from_dict(training_record_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


