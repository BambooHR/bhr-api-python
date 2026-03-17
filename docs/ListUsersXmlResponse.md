# ListUsersXmlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**List[ListUsersXmlResponseUserInner]**](ListUsersXmlResponseUserInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.list_users_xml_response import ListUsersXmlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsersXmlResponse from a JSON string
list_users_xml_response_instance = ListUsersXmlResponse.from_json(json)
# print the JSON string representation of the object
print(ListUsersXmlResponse.to_json())

# convert the object into a dict
list_users_xml_response_dict = list_users_xml_response_instance.to_dict()
# create an instance of ListUsersXmlResponse from a dict
list_users_xml_response_from_dict = ListUsersXmlResponse.from_dict(list_users_xml_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


