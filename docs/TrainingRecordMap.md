# TrainingRecordMap

Returns an empty array when the employee has no records, or an object keyed by training record ID when records exist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from bamboohr_sdk.models.training_record_map import TrainingRecordMap

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingRecordMap from a JSON string
training_record_map_instance = TrainingRecordMap.from_json(json)
# print the JSON string representation of the object
print(TrainingRecordMap.to_json())

# convert the object into a dict
training_record_map_dict = training_record_map_instance.to_dict()
# create an instance of TrainingRecordMap from a dict
training_record_map_from_dict = TrainingRecordMap.from_dict(training_record_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


