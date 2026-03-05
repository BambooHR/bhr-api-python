# TimeTrackingRecordSchemaShiftDifferential

Shift differential information associated with this time tracking record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shift Differential information | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_record_schema_shift_differential import TimeTrackingRecordSchemaShiftDifferential

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingRecordSchemaShiftDifferential from a JSON string
time_tracking_record_schema_shift_differential_instance = TimeTrackingRecordSchemaShiftDifferential.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingRecordSchemaShiftDifferential.to_json())

# convert the object into a dict
time_tracking_record_schema_shift_differential_dict = time_tracking_record_schema_shift_differential_instance.to_dict()
# create an instance of TimeTrackingRecordSchemaShiftDifferential from a dict
time_tracking_record_schema_shift_differential_from_dict = TimeTrackingRecordSchemaShiftDifferential.from_dict(time_tracking_record_schema_shift_differential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


