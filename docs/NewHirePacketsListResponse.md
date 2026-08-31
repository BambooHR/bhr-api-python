# NewHirePacketsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_hire_packets** | [**List[NewHirePacketPublicApi]**](NewHirePacketPublicApi.md) | Packet summaries for the current page. | [optional] 
**page** | **int** | Current page number (1-based). | [optional] 
**page_size** | **int** | Page size used for this response. | [optional] 
**total_count** | **int** | Total packet rows matching visibility (across all pages). | [optional] 

## Example

```python
from bamboohr_sdk.models.new_hire_packets_list_response import NewHirePacketsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NewHirePacketsListResponse from a JSON string
new_hire_packets_list_response_instance = NewHirePacketsListResponse.from_json(json)
# print the JSON string representation of the object
print(NewHirePacketsListResponse.to_json())

# convert the object into a dict
new_hire_packets_list_response_dict = new_hire_packets_list_response_instance.to_dict()
# create an instance of NewHirePacketsListResponse from a dict
new_hire_packets_list_response_from_dict = NewHirePacketsListResponse.from_dict(new_hire_packets_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


