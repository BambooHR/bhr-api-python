# SchedulingTimezoneListResponseV1Meta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** | Total number of timezones matching the filter. | [optional] 
**page** | **int** | Current page number. | [optional] 
**page_size** | **int** | Number of items per page. | [optional] 

## Example

```python
from bamboohr_sdk.models.scheduling_timezone_list_response_v1_meta import SchedulingTimezoneListResponseV1Meta

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingTimezoneListResponseV1Meta from a JSON string
scheduling_timezone_list_response_v1_meta_instance = SchedulingTimezoneListResponseV1Meta.from_json(json)
# print the JSON string representation of the object
print(SchedulingTimezoneListResponseV1Meta.to_json())

# convert the object into a dict
scheduling_timezone_list_response_v1_meta_dict = scheduling_timezone_list_response_v1_meta_instance.to_dict()
# create an instance of SchedulingTimezoneListResponseV1Meta from a dict
scheduling_timezone_list_response_v1_meta_from_dict = SchedulingTimezoneListResponseV1Meta.from_dict(scheduling_timezone_list_response_v1_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


