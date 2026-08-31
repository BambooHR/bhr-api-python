# UpdateCompanyNameBadRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**UpdateCompanyNameBadRequestResponseError**](UpdateCompanyNameBadRequestResponseError.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.update_company_name_bad_request_response import UpdateCompanyNameBadRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCompanyNameBadRequestResponse from a JSON string
update_company_name_bad_request_response_instance = UpdateCompanyNameBadRequestResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCompanyNameBadRequestResponse.to_json())

# convert the object into a dict
update_company_name_bad_request_response_dict = update_company_name_bad_request_response_instance.to_dict()
# create an instance of UpdateCompanyNameBadRequestResponse from a dict
update_company_name_bad_request_response_from_dict = UpdateCompanyNameBadRequestResponse.from_dict(update_company_name_bad_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


