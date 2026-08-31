# ShiftDifferentialPaginatedTimeTrackingShiftDifferentialsResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ShiftDifferentialPaginatedResponseDataV1Meta**](ShiftDifferentialPaginatedResponseDataV1Meta.md) |  | [optional] 
**links** | [**TimeTrackingConfigurationPaginatedResponseDataV1Links**](TimeTrackingConfigurationPaginatedResponseDataV1Links.md) |  | [optional] 
**data** | [**List[ShiftDifferentialTimeTrackingShiftDifferentialV1]**](ShiftDifferentialTimeTrackingShiftDifferentialV1.md) | Collection of time tracking shift differentials. | [optional] 

## Example

```python
from bamboohr_sdk.models.shift_differential_paginated_time_tracking_shift_differentials_response_v1 import ShiftDifferentialPaginatedTimeTrackingShiftDifferentialsResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftDifferentialPaginatedTimeTrackingShiftDifferentialsResponseV1 from a JSON string
shift_differential_paginated_time_tracking_shift_differentials_response_v1_instance = ShiftDifferentialPaginatedTimeTrackingShiftDifferentialsResponseV1.from_json(json)
# print the JSON string representation of the object
print(ShiftDifferentialPaginatedTimeTrackingShiftDifferentialsResponseV1.to_json())

# convert the object into a dict
shift_differential_paginated_time_tracking_shift_differentials_response_v1_dict = shift_differential_paginated_time_tracking_shift_differentials_response_v1_instance.to_dict()
# create an instance of ShiftDifferentialPaginatedTimeTrackingShiftDifferentialsResponseV1 from a dict
shift_differential_paginated_time_tracking_shift_differentials_response_v1_from_dict = ShiftDifferentialPaginatedTimeTrackingShiftDifferentialsResponseV1.from_dict(shift_differential_paginated_time_tracking_shift_differentials_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


