# TimeTrackingOffsetPaginatedResponseDataV1Meta

Pagination metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** |  | 
**offset** | **int** |  | 
**limit** | **int** |  | 

## Example

```python
from bamboohr_sdk.models.time_tracking_offset_paginated_response_data_v1_meta import TimeTrackingOffsetPaginatedResponseDataV1Meta

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingOffsetPaginatedResponseDataV1Meta from a JSON string
time_tracking_offset_paginated_response_data_v1_meta_instance = TimeTrackingOffsetPaginatedResponseDataV1Meta.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingOffsetPaginatedResponseDataV1Meta.to_json())

# convert the object into a dict
time_tracking_offset_paginated_response_data_v1_meta_dict = time_tracking_offset_paginated_response_data_v1_meta_instance.to_dict()
# create an instance of TimeTrackingOffsetPaginatedResponseDataV1Meta from a dict
time_tracking_offset_paginated_response_data_v1_meta_from_dict = TimeTrackingOffsetPaginatedResponseDataV1Meta.from_dict(time_tracking_offset_paginated_response_data_v1_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


