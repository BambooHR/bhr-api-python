# TimeTrackingOffsetPaginatedResponseDataV1Links

Pagination links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | [**TimeTrackingOffsetPaginatedResponseDataV1LinksPrev**](TimeTrackingOffsetPaginatedResponseDataV1LinksPrev.md) |  | 
**next** | [**TimeTrackingOffsetPaginatedResponseDataV1LinksNext**](TimeTrackingOffsetPaginatedResponseDataV1LinksNext.md) |  | 

## Example

```python
from bamboohr_sdk.models.time_tracking_offset_paginated_response_data_v1_links import TimeTrackingOffsetPaginatedResponseDataV1Links

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingOffsetPaginatedResponseDataV1Links from a JSON string
time_tracking_offset_paginated_response_data_v1_links_instance = TimeTrackingOffsetPaginatedResponseDataV1Links.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingOffsetPaginatedResponseDataV1Links.to_json())

# convert the object into a dict
time_tracking_offset_paginated_response_data_v1_links_dict = time_tracking_offset_paginated_response_data_v1_links_instance.to_dict()
# create an instance of TimeTrackingOffsetPaginatedResponseDataV1Links from a dict
time_tracking_offset_paginated_response_data_v1_links_from_dict = TimeTrackingOffsetPaginatedResponseDataV1Links.from_dict(time_tracking_offset_paginated_response_data_v1_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


