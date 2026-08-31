# WhosOutListResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WhosOutV1]**](WhosOutV1.md) | Collection of approved time off occurrences | [optional] 
**persons** | [**Dict[str, WhosOutPersonV1]**](WhosOutPersonV1.md) | Employee display data keyed by employee id. Present only when includePersons&#x3D;true. | [optional] 
**links** | [**WhosOutListResponseV1Links**](WhosOutListResponseV1Links.md) |  | [optional] 
**meta** | [**WhosOutListResponseV1Meta**](WhosOutListResponseV1Meta.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.whos_out_list_response_v1 import WhosOutListResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of WhosOutListResponseV1 from a JSON string
whos_out_list_response_v1_instance = WhosOutListResponseV1.from_json(json)
# print the JSON string representation of the object
print(WhosOutListResponseV1.to_json())

# convert the object into a dict
whos_out_list_response_v1_dict = whos_out_list_response_v1_instance.to_dict()
# create an instance of WhosOutListResponseV1 from a dict
whos_out_list_response_v1_from_dict = WhosOutListResponseV1.from_dict(whos_out_list_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


