# TimeTrackingPaginatedTimesheetsResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TimeTrackingTimesheetV1]**](TimeTrackingTimesheetV1.md) | Collection of timesheets. | [optional] 
**meta** | [**TimeTrackingPaginatedTimesheetsResponseV1Meta**](TimeTrackingPaginatedTimesheetsResponseV1Meta.md) |  | [optional] 
**links** | **object** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_paginated_timesheets_response_v1 import TimeTrackingPaginatedTimesheetsResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingPaginatedTimesheetsResponseV1 from a JSON string
time_tracking_paginated_timesheets_response_v1_instance = TimeTrackingPaginatedTimesheetsResponseV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingPaginatedTimesheetsResponseV1.to_json())

# convert the object into a dict
time_tracking_paginated_timesheets_response_v1_dict = time_tracking_paginated_timesheets_response_v1_instance.to_dict()
# create an instance of TimeTrackingPaginatedTimesheetsResponseV1 from a dict
time_tracking_paginated_timesheets_response_v1_from_dict = TimeTrackingPaginatedTimesheetsResponseV1.from_dict(time_tracking_paginated_timesheets_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


