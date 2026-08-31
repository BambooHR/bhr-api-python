# TimeTrackingClockEntryPaginatedResponseDataV1Meta

Pagination metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** |  | 
**total_pages** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 

## Example

```python
from bamboohr_sdk.models.time_tracking_clock_entry_paginated_response_data_v1_meta import TimeTrackingClockEntryPaginatedResponseDataV1Meta

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingClockEntryPaginatedResponseDataV1Meta from a JSON string
time_tracking_clock_entry_paginated_response_data_v1_meta_instance = TimeTrackingClockEntryPaginatedResponseDataV1Meta.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingClockEntryPaginatedResponseDataV1Meta.to_json())

# convert the object into a dict
time_tracking_clock_entry_paginated_response_data_v1_meta_dict = time_tracking_clock_entry_paginated_response_data_v1_meta_instance.to_dict()
# create an instance of TimeTrackingClockEntryPaginatedResponseDataV1Meta from a dict
time_tracking_clock_entry_paginated_response_data_v1_meta_from_dict = TimeTrackingClockEntryPaginatedResponseDataV1Meta.from_dict(time_tracking_clock_entry_paginated_response_data_v1_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


