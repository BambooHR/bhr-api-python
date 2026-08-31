# TimeTrackingPagePaginatedResponseDataV1

Pagination envelope shared by page-based paginated Time Tracking endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**HolidayCompanyHolidayListResponseV1Meta**](HolidayCompanyHolidayListResponseV1Meta.md) |  | [optional] 
**links** | [**TimeTrackingConfigurationPaginatedResponseDataV1Links**](TimeTrackingConfigurationPaginatedResponseDataV1Links.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_page_paginated_response_data_v1 import TimeTrackingPagePaginatedResponseDataV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingPagePaginatedResponseDataV1 from a JSON string
time_tracking_page_paginated_response_data_v1_instance = TimeTrackingPagePaginatedResponseDataV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingPagePaginatedResponseDataV1.to_json())

# convert the object into a dict
time_tracking_page_paginated_response_data_v1_dict = time_tracking_page_paginated_response_data_v1_instance.to_dict()
# create an instance of TimeTrackingPagePaginatedResponseDataV1 from a dict
time_tracking_page_paginated_response_data_v1_from_dict = TimeTrackingPagePaginatedResponseDataV1.from_dict(time_tracking_page_paginated_response_data_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


