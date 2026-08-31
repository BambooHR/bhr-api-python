# ShiftDifferentialPaginatedResponseDataV1

Pagination envelope shared by paginated Shift Differential endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ShiftDifferentialPaginatedResponseDataV1Meta**](ShiftDifferentialPaginatedResponseDataV1Meta.md) |  | [optional] 
**links** | [**TimeTrackingConfigurationPaginatedResponseDataV1Links**](TimeTrackingConfigurationPaginatedResponseDataV1Links.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.shift_differential_paginated_response_data_v1 import ShiftDifferentialPaginatedResponseDataV1

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftDifferentialPaginatedResponseDataV1 from a JSON string
shift_differential_paginated_response_data_v1_instance = ShiftDifferentialPaginatedResponseDataV1.from_json(json)
# print the JSON string representation of the object
print(ShiftDifferentialPaginatedResponseDataV1.to_json())

# convert the object into a dict
shift_differential_paginated_response_data_v1_dict = shift_differential_paginated_response_data_v1_instance.to_dict()
# create an instance of ShiftDifferentialPaginatedResponseDataV1 from a dict
shift_differential_paginated_response_data_v1_from_dict = ShiftDifferentialPaginatedResponseDataV1.from_dict(shift_differential_paginated_response_data_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


