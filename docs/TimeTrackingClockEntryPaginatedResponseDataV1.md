# TimeTrackingClockEntryPaginatedResponseDataV1

Pagination envelope shared by paginated clock entry endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**TimeTrackingClockEntryPaginatedResponseDataV1Meta**](TimeTrackingClockEntryPaginatedResponseDataV1Meta.md) |  | [optional] 
**links** | [**TimeTrackingConfigurationPaginatedResponseDataV1Links**](TimeTrackingConfigurationPaginatedResponseDataV1Links.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_clock_entry_paginated_response_data_v1 import TimeTrackingClockEntryPaginatedResponseDataV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingClockEntryPaginatedResponseDataV1 from a JSON string
time_tracking_clock_entry_paginated_response_data_v1_instance = TimeTrackingClockEntryPaginatedResponseDataV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingClockEntryPaginatedResponseDataV1.to_json())

# convert the object into a dict
time_tracking_clock_entry_paginated_response_data_v1_dict = time_tracking_clock_entry_paginated_response_data_v1_instance.to_dict()
# create an instance of TimeTrackingClockEntryPaginatedResponseDataV1 from a dict
time_tracking_clock_entry_paginated_response_data_v1_from_dict = TimeTrackingClockEntryPaginatedResponseDataV1.from_dict(time_tracking_clock_entry_paginated_response_data_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


