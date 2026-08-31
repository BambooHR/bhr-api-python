# TimeTrackingPaginatedTimesheetsResponseV1Meta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_paginated_timesheets_response_v1_meta import TimeTrackingPaginatedTimesheetsResponseV1Meta

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingPaginatedTimesheetsResponseV1Meta from a JSON string
time_tracking_paginated_timesheets_response_v1_meta_instance = TimeTrackingPaginatedTimesheetsResponseV1Meta.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingPaginatedTimesheetsResponseV1Meta.to_json())

# convert the object into a dict
time_tracking_paginated_timesheets_response_v1_meta_dict = time_tracking_paginated_timesheets_response_v1_meta_instance.to_dict()
# create an instance of TimeTrackingPaginatedTimesheetsResponseV1Meta from a dict
time_tracking_paginated_timesheets_response_v1_meta_from_dict = TimeTrackingPaginatedTimesheetsResponseV1Meta.from_dict(time_tracking_paginated_timesheets_response_v1_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


