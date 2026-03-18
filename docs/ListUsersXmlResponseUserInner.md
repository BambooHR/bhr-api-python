# ListUsersXmlResponseUserInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The user ID. | [optional] 
**employee_id** | **int** | The employee record ID. Present as an XML attribute only when the user has an associated employee record. | [optional] 
**first_name** | **str** | First name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**email** | **str** | The user&#39;s email address. | [optional] 
**status** | **str** | Account status. | [optional] 
**last_login** | **datetime** | ISO 8601 timestamp of the most recent login. Omitted when the user has never logged in. | [optional] 

## Example

```python
from bamboohr_sdk.models.list_users_xml_response_user_inner import ListUsersXmlResponseUserInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsersXmlResponseUserInner from a JSON string
list_users_xml_response_user_inner_instance = ListUsersXmlResponseUserInner.from_json(json)
# print the JSON string representation of the object
print(ListUsersXmlResponseUserInner.to_json())

# convert the object into a dict
list_users_xml_response_user_inner_dict = list_users_xml_response_user_inner_instance.to_dict()
# create an instance of ListUsersXmlResponseUserInner from a dict
list_users_xml_response_user_inner_from_dict = ListUsersXmlResponseUserInner.from_dict(list_users_xml_response_user_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


