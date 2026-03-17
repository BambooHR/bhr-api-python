# LoginResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Always &#x60;true&#x60; on HTTP 200. | 
**user_id** | **int** | The authenticated user ID. | 
**employee_id** | **int** | The employee ID linked to this user. &#x60;null&#x60; when no employee record is associated. | [optional] 
**key** | **str** | The API key to use for subsequent requests. | 
**api_url** | **str** | The base URL for subsequent API calls. | 

## Example

```python
from bamboohr_sdk.models.login_response import LoginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoginResponse from a JSON string
login_response_instance = LoginResponse.from_json(json)
# print the JSON string representation of the object
print(LoginResponse.to_json())

# convert the object into a dict
login_response_dict = login_response_instance.to_dict()
# create an instance of LoginResponse from a dict
login_response_from_dict = LoginResponse.from_dict(login_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


