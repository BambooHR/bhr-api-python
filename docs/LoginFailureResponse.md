# LoginFailureResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Always &#x60;false&#x60;. | 

## Example

```python
from bamboohr_sdk.models.login_failure_response import LoginFailureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoginFailureResponse from a JSON string
login_failure_response_instance = LoginFailureResponse.from_json(json)
# print the JSON string representation of the object
print(LoginFailureResponse.to_json())

# convert the object into a dict
login_failure_response_dict = login_failure_response_instance.to_dict()
# create an instance of LoginFailureResponse from a dict
login_failure_response_from_dict = LoginFailureResponse.from_dict(login_failure_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


