# LoginXmlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** | Always &#x60;authenticated&#x60; on HTTP 200. | [optional] 
**user_id** | **int** | The authenticated user ID. | [optional] 
**employee_id** | **int** | The employee ID linked to this user. Rendered as &#x60;&lt;employeeId isNull&#x3D;\&quot;yes\&quot;/&gt;&#x60; when no employee record is associated. | [optional] 
**key** | **str** | The API key to use for subsequent requests. | [optional] 
**api_url** | **str** | The base URL for subsequent API calls. | [optional] 

## Example

```python
from bamboohr_sdk.models.login_xml_response import LoginXmlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoginXmlResponse from a JSON string
login_xml_response_instance = LoginXmlResponse.from_json(json)
# print the JSON string representation of the object
print(LoginXmlResponse.to_json())

# convert the object into a dict
login_xml_response_dict = login_xml_response_instance.to_dict()
# create an instance of LoginXmlResponse from a dict
login_xml_response_from_dict = LoginXmlResponse.from_dict(login_xml_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


