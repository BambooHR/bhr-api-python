# ShiftDifferentialPaginatedResponseDataV1Meta

Pagination metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** |  | 
**total_pages** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 

## Example

```python
from bamboohr_sdk.models.shift_differential_paginated_response_data_v1_meta import ShiftDifferentialPaginatedResponseDataV1Meta

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftDifferentialPaginatedResponseDataV1Meta from a JSON string
shift_differential_paginated_response_data_v1_meta_instance = ShiftDifferentialPaginatedResponseDataV1Meta.from_json(json)
# print the JSON string representation of the object
print(ShiftDifferentialPaginatedResponseDataV1Meta.to_json())

# convert the object into a dict
shift_differential_paginated_response_data_v1_meta_dict = shift_differential_paginated_response_data_v1_meta_instance.to_dict()
# create an instance of ShiftDifferentialPaginatedResponseDataV1Meta from a dict
shift_differential_paginated_response_data_v1_meta_from_dict = ShiftDifferentialPaginatedResponseDataV1Meta.from_dict(shift_differential_paginated_response_data_v1_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


