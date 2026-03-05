# TimeTrackingPaginatedBreaksResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**TimeTrackingOffsetPaginatedResponseDataV1Meta**](TimeTrackingOffsetPaginatedResponseDataV1Meta.md) |  | [optional] 
**links** | [**TimeTrackingOffsetPaginatedResponseDataV1Links**](TimeTrackingOffsetPaginatedResponseDataV1Links.md) |  | [optional] 
**data** | [**List[TimeTrackingTimeTrackingBreakV1]**](TimeTrackingTimeTrackingBreakV1.md) | Collection of time tracking breaks | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_paginated_breaks_response_v1 import TimeTrackingPaginatedBreaksResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingPaginatedBreaksResponseV1 from a JSON string
time_tracking_paginated_breaks_response_v1_instance = TimeTrackingPaginatedBreaksResponseV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingPaginatedBreaksResponseV1.to_json())

# convert the object into a dict
time_tracking_paginated_breaks_response_v1_dict = time_tracking_paginated_breaks_response_v1_instance.to_dict()
# create an instance of TimeTrackingPaginatedBreaksResponseV1 from a dict
time_tracking_paginated_breaks_response_v1_from_dict = TimeTrackingPaginatedBreaksResponseV1.from_dict(time_tracking_paginated_breaks_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


