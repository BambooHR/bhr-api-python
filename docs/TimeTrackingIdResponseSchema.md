# TimeTrackingIdResponseSchema

Schema for time tracking ID response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the time tracking record | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_id_response_schema import TimeTrackingIdResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingIdResponseSchema from a JSON string
time_tracking_id_response_schema_instance = TimeTrackingIdResponseSchema.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingIdResponseSchema.to_json())

# convert the object into a dict
time_tracking_id_response_schema_dict = time_tracking_id_response_schema_instance.to_dict()
# create an instance of TimeTrackingIdResponseSchema from a dict
time_tracking_id_response_schema_from_dict = TimeTrackingIdResponseSchema.from_dict(time_tracking_id_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


