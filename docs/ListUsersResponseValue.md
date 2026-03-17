# ListUsersResponseValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The user ID. | [optional] 
**employee_id** | **int** | The ID of the employee record linked to this user. Always present in the JSON response; &#x60;0&#x60; when no employee record is associated. | [optional] 
**first_name** | **str** | First name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**email** | **str** | The user&#39;s email address. Resolved in priority order: work email, home email, account email. | [optional] 
**status** | **str** | Account status. | [optional] 
**last_login** | **datetime** | ISO 8601 timestamp of the most recent login. Omitted when the user has never logged in. | [optional] 

## Example

```python
from bamboohr_sdk.models.list_users_response_value import ListUsersResponseValue

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsersResponseValue from a JSON string
list_users_response_value_instance = ListUsersResponseValue.from_json(json)
# print the JSON string representation of the object
print(ListUsersResponseValue.to_json())

# convert the object into a dict
list_users_response_value_dict = list_users_response_value_instance.to_dict()
# create an instance of ListUsersResponseValue from a dict
list_users_response_value_from_dict = ListUsersResponseValue.from_dict(list_users_response_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


