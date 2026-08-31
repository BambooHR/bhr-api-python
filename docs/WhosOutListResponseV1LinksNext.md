# WhosOutListResponseV1LinksNext

Link object for the next page. Omitted when there is no next page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.whos_out_list_response_v1_links_next import WhosOutListResponseV1LinksNext

# TODO update the JSON string below
json = "{}"
# create an instance of WhosOutListResponseV1LinksNext from a JSON string
whos_out_list_response_v1_links_next_instance = WhosOutListResponseV1LinksNext.from_json(json)
# print the JSON string representation of the object
print(WhosOutListResponseV1LinksNext.to_json())

# convert the object into a dict
whos_out_list_response_v1_links_next_dict = whos_out_list_response_v1_links_next_instance.to_dict()
# create an instance of WhosOutListResponseV1LinksNext from a dict
whos_out_list_response_v1_links_next_from_dict = WhosOutListResponseV1LinksNext.from_dict(whos_out_list_response_v1_links_next_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


