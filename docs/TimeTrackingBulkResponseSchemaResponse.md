# TimeTrackingBulkResponseSchemaResponse

Response data containing ID and message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the time tracking record | [optional] 
**message** | **str** | Response message, typically used for error details | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_bulk_response_schema_response import TimeTrackingBulkResponseSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingBulkResponseSchemaResponse from a JSON string
time_tracking_bulk_response_schema_response_instance = TimeTrackingBulkResponseSchemaResponse.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingBulkResponseSchemaResponse.to_json())

# convert the object into a dict
time_tracking_bulk_response_schema_response_dict = time_tracking_bulk_response_schema_response_instance.to_dict()
# create an instance of TimeTrackingBulkResponseSchemaResponse from a dict
time_tracking_bulk_response_schema_response_from_dict = TimeTrackingBulkResponseSchemaResponse.from_dict(time_tracking_bulk_response_schema_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


