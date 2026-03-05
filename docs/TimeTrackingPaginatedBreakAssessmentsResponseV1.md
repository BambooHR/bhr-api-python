# TimeTrackingPaginatedBreakAssessmentsResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**TimeTrackingOffsetPaginatedResponseDataV1Meta**](TimeTrackingOffsetPaginatedResponseDataV1Meta.md) |  | [optional] 
**links** | [**TimeTrackingOffsetPaginatedResponseDataV1Links**](TimeTrackingOffsetPaginatedResponseDataV1Links.md) |  | [optional] 
**data** | [**List[TimeTrackingTimeTrackingBreakAssessmentV1]**](TimeTrackingTimeTrackingBreakAssessmentV1.md) | Collection of time tracking break assessments | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_paginated_break_assessments_response_v1 import TimeTrackingPaginatedBreakAssessmentsResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingPaginatedBreakAssessmentsResponseV1 from a JSON string
time_tracking_paginated_break_assessments_response_v1_instance = TimeTrackingPaginatedBreakAssessmentsResponseV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingPaginatedBreakAssessmentsResponseV1.to_json())

# convert the object into a dict
time_tracking_paginated_break_assessments_response_v1_dict = time_tracking_paginated_break_assessments_response_v1_instance.to_dict()
# create an instance of TimeTrackingPaginatedBreakAssessmentsResponseV1 from a dict
time_tracking_paginated_break_assessments_response_v1_from_dict = TimeTrackingPaginatedBreakAssessmentsResponseV1.from_dict(time_tracking_paginated_break_assessments_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


