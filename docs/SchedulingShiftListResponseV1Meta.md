# SchedulingShiftListResponseV1Meta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** | Total number of shifts matching the filter. | [optional] 
**page** | **int** | Current page number. | [optional] 
**page_size** | **int** | Number of items per page. | [optional] 

## Example

```python
from bamboohr_sdk.models.scheduling_shift_list_response_v1_meta import SchedulingShiftListResponseV1Meta

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingShiftListResponseV1Meta from a JSON string
scheduling_shift_list_response_v1_meta_instance = SchedulingShiftListResponseV1Meta.from_json(json)
# print the JSON string representation of the object
print(SchedulingShiftListResponseV1Meta.to_json())

# convert the object into a dict
scheduling_shift_list_response_v1_meta_dict = scheduling_shift_list_response_v1_meta_instance.to_dict()
# create an instance of SchedulingShiftListResponseV1Meta from a dict
scheduling_shift_list_response_v1_meta_from_dict = SchedulingShiftListResponseV1Meta.from_dict(scheduling_shift_list_response_v1_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


