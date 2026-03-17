# LoginFailureXmlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** | Always &#x60;declined&#x60;. | [optional] 

## Example

```python
from bamboohr_sdk.models.login_failure_xml_response import LoginFailureXmlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoginFailureXmlResponse from a JSON string
login_failure_xml_response_instance = LoginFailureXmlResponse.from_json(json)
# print the JSON string representation of the object
print(LoginFailureXmlResponse.to_json())

# convert the object into a dict
login_failure_xml_response_dict = login_failure_xml_response_instance.to_dict()
# create an instance of LoginFailureXmlResponse from a dict
login_failure_xml_response_from_dict = LoginFailureXmlResponse.from_dict(login_failure_xml_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


