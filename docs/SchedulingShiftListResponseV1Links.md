# SchedulingShiftListResponseV1Links


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | [**SchedulingShiftListResponseV1LinksPrev**](SchedulingShiftListResponseV1LinksPrev.md) |  | [optional] 
**next** | [**SchedulingShiftListResponseV1LinksNext**](SchedulingShiftListResponseV1LinksNext.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.scheduling_shift_list_response_v1_links import SchedulingShiftListResponseV1Links

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingShiftListResponseV1Links from a JSON string
scheduling_shift_list_response_v1_links_instance = SchedulingShiftListResponseV1Links.from_json(json)
# print the JSON string representation of the object
print(SchedulingShiftListResponseV1Links.to_json())

# convert the object into a dict
scheduling_shift_list_response_v1_links_dict = scheduling_shift_list_response_v1_links_instance.to_dict()
# create an instance of SchedulingShiftListResponseV1Links from a dict
scheduling_shift_list_response_v1_links_from_dict = SchedulingShiftListResponseV1Links.from_dict(scheduling_shift_list_response_v1_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


