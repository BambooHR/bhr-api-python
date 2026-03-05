# TimeTrackingOffsetPaginatedResponseDataV1

Additional data for paginated responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**TimeTrackingOffsetPaginatedResponseDataV1Meta**](TimeTrackingOffsetPaginatedResponseDataV1Meta.md) |  | [optional] 
**links** | [**TimeTrackingOffsetPaginatedResponseDataV1Links**](TimeTrackingOffsetPaginatedResponseDataV1Links.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_offset_paginated_response_data_v1 import TimeTrackingOffsetPaginatedResponseDataV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingOffsetPaginatedResponseDataV1 from a JSON string
time_tracking_offset_paginated_response_data_v1_instance = TimeTrackingOffsetPaginatedResponseDataV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingOffsetPaginatedResponseDataV1.to_json())

# convert the object into a dict
time_tracking_offset_paginated_response_data_v1_dict = time_tracking_offset_paginated_response_data_v1_instance.to_dict()
# create an instance of TimeTrackingOffsetPaginatedResponseDataV1 from a dict
time_tracking_offset_paginated_response_data_v1_from_dict = TimeTrackingOffsetPaginatedResponseDataV1.from_dict(time_tracking_offset_paginated_response_data_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


