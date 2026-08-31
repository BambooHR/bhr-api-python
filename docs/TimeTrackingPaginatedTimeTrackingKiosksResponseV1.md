# TimeTrackingPaginatedTimeTrackingKiosksResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**HolidayCompanyHolidayListResponseV1Meta**](HolidayCompanyHolidayListResponseV1Meta.md) |  | [optional] 
**links** | [**TimeTrackingConfigurationPaginatedResponseDataV1Links**](TimeTrackingConfigurationPaginatedResponseDataV1Links.md) |  | [optional] 
**data** | [**List[TimeTrackingTimeTrackingKioskV1]**](TimeTrackingTimeTrackingKioskV1.md) | Collection of time tracking kiosks. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_paginated_time_tracking_kiosks_response_v1 import TimeTrackingPaginatedTimeTrackingKiosksResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingPaginatedTimeTrackingKiosksResponseV1 from a JSON string
time_tracking_paginated_time_tracking_kiosks_response_v1_instance = TimeTrackingPaginatedTimeTrackingKiosksResponseV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingPaginatedTimeTrackingKiosksResponseV1.to_json())

# convert the object into a dict
time_tracking_paginated_time_tracking_kiosks_response_v1_dict = time_tracking_paginated_time_tracking_kiosks_response_v1_instance.to_dict()
# create an instance of TimeTrackingPaginatedTimeTrackingKiosksResponseV1 from a dict
time_tracking_paginated_time_tracking_kiosks_response_v1_from_dict = TimeTrackingPaginatedTimeTrackingKiosksResponseV1.from_dict(time_tracking_paginated_time_tracking_kiosks_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


