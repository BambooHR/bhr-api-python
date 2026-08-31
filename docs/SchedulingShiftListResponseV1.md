# SchedulingShiftListResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SchedulingSchedulingShiftV1]**](SchedulingSchedulingShiftV1.md) | Array of shifts | [optional] 
**meta** | [**SchedulingShiftListResponseV1Meta**](SchedulingShiftListResponseV1Meta.md) |  | [optional] 
**links** | [**SchedulingShiftListResponseV1Links**](SchedulingShiftListResponseV1Links.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.scheduling_shift_list_response_v1 import SchedulingShiftListResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingShiftListResponseV1 from a JSON string
scheduling_shift_list_response_v1_instance = SchedulingShiftListResponseV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingShiftListResponseV1.to_json())

# convert the object into a dict
scheduling_shift_list_response_v1_dict = scheduling_shift_list_response_v1_instance.to_dict()
# create an instance of SchedulingShiftListResponseV1 from a dict
scheduling_shift_list_response_v1_from_dict = SchedulingShiftListResponseV1.from_dict(scheduling_shift_list_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


