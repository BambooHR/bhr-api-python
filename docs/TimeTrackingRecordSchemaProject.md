# TimeTrackingRecordSchemaProject

Project information associated with this time tracking record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project information | [optional] 
**name** | **str** |  | [optional] 
**task** | [**TimeTrackingRecordSchemaProjectTask**](TimeTrackingRecordSchemaProjectTask.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_record_schema_project import TimeTrackingRecordSchemaProject

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingRecordSchemaProject from a JSON string
time_tracking_record_schema_project_instance = TimeTrackingRecordSchemaProject.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingRecordSchemaProject.to_json())

# convert the object into a dict
time_tracking_record_schema_project_dict = time_tracking_record_schema_project_instance.to_dict()
# create an instance of TimeTrackingRecordSchemaProject from a dict
time_tracking_record_schema_project_from_dict = TimeTrackingRecordSchemaProject.from_dict(time_tracking_record_schema_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


