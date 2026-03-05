# TimeTrackingPaginatedBreakPoliciesResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**TimeTrackingOffsetPaginatedResponseDataV1Meta**](TimeTrackingOffsetPaginatedResponseDataV1Meta.md) |  | [optional] 
**links** | [**TimeTrackingOffsetPaginatedResponseDataV1Links**](TimeTrackingOffsetPaginatedResponseDataV1Links.md) |  | [optional] 
**data** | [**List[TimeTrackingTimeTrackingBreakPolicyV1]**](TimeTrackingTimeTrackingBreakPolicyV1.md) | Collection of time tracking break policies | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_paginated_break_policies_response_v1 import TimeTrackingPaginatedBreakPoliciesResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingPaginatedBreakPoliciesResponseV1 from a JSON string
time_tracking_paginated_break_policies_response_v1_instance = TimeTrackingPaginatedBreakPoliciesResponseV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingPaginatedBreakPoliciesResponseV1.to_json())

# convert the object into a dict
time_tracking_paginated_break_policies_response_v1_dict = time_tracking_paginated_break_policies_response_v1_instance.to_dict()
# create an instance of TimeTrackingPaginatedBreakPoliciesResponseV1 from a dict
time_tracking_paginated_break_policies_response_v1_from_dict = TimeTrackingPaginatedBreakPoliciesResponseV1.from_dict(time_tracking_paginated_break_policies_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


