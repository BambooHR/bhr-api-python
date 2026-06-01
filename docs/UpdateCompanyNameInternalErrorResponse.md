# UpdateCompanyNameInternalErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**UpdateCompanyNameForbiddenResponseError**](UpdateCompanyNameForbiddenResponseError.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.update_company_name_internal_error_response import UpdateCompanyNameInternalErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCompanyNameInternalErrorResponse from a JSON string
update_company_name_internal_error_response_instance = UpdateCompanyNameInternalErrorResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCompanyNameInternalErrorResponse.to_json())

# convert the object into a dict
update_company_name_internal_error_response_dict = update_company_name_internal_error_response_instance.to_dict()
# create an instance of UpdateCompanyNameInternalErrorResponse from a dict
update_company_name_internal_error_response_from_dict = UpdateCompanyNameInternalErrorResponse.from_dict(update_company_name_internal_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


