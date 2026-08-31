# WhosOutListResponseV1Meta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.whos_out_list_response_v1_meta import WhosOutListResponseV1Meta

# TODO update the JSON string below
json = "{}"
# create an instance of WhosOutListResponseV1Meta from a JSON string
whos_out_list_response_v1_meta_instance = WhosOutListResponseV1Meta.from_json(json)
# print the JSON string representation of the object
print(WhosOutListResponseV1Meta.to_json())

# convert the object into a dict
whos_out_list_response_v1_meta_dict = whos_out_list_response_v1_meta_instance.to_dict()
# create an instance of WhosOutListResponseV1Meta from a dict
whos_out_list_response_v1_meta_from_dict = WhosOutListResponseV1Meta.from_dict(whos_out_list_response_v1_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


