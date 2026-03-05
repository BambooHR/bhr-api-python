# TimeTrackingBulkResponseSchema

Schema for time tracking bulk operation response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Indicates whether the operation was successful | [optional] 
**response** | [**TimeTrackingBulkResponseSchemaResponse**](TimeTrackingBulkResponseSchemaResponse.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_bulk_response_schema import TimeTrackingBulkResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingBulkResponseSchema from a JSON string
time_tracking_bulk_response_schema_instance = TimeTrackingBulkResponseSchema.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingBulkResponseSchema.to_json())

# convert the object into a dict
time_tracking_bulk_response_schema_dict = time_tracking_bulk_response_schema_instance.to_dict()
# create an instance of TimeTrackingBulkResponseSchema from a dict
time_tracking_bulk_response_schema_from_dict = TimeTrackingBulkResponseSchema.from_dict(time_tracking_bulk_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


