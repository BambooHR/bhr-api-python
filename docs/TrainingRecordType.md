# TrainingRecordType

The training type ID. Returned as a string on update/list responses, and as an integer on create responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from bamboohr_sdk.models.training_record_type import TrainingRecordType

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingRecordType from a JSON string
training_record_type_instance = TrainingRecordType.from_json(json)
# print the JSON string representation of the object
print(TrainingRecordType.to_json())

# convert the object into a dict
training_record_type_dict = training_record_type_instance.to_dict()
# create an instance of TrainingRecordType from a dict
training_record_type_from_dict = TrainingRecordType.from_dict(training_record_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


