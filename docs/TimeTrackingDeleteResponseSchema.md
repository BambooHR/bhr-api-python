# TimeTrackingDeleteResponseSchema

Schema for time tracking delete operation response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the delete operation | [optional] 
**message** | **str** | Response message indicating the result of the operation | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_delete_response_schema import TimeTrackingDeleteResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingDeleteResponseSchema from a JSON string
time_tracking_delete_response_schema_instance = TimeTrackingDeleteResponseSchema.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingDeleteResponseSchema.to_json())

# convert the object into a dict
time_tracking_delete_response_schema_dict = time_tracking_delete_response_schema_instance.to_dict()
# create an instance of TimeTrackingDeleteResponseSchema from a dict
time_tracking_delete_response_schema_from_dict = TimeTrackingDeleteResponseSchema.from_dict(time_tracking_delete_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


