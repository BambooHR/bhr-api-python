# UpdateCompanyNameForbiddenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**UpdateCompanyNameForbiddenResponseError**](UpdateCompanyNameForbiddenResponseError.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.update_company_name_forbidden_response import UpdateCompanyNameForbiddenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCompanyNameForbiddenResponse from a JSON string
update_company_name_forbidden_response_instance = UpdateCompanyNameForbiddenResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCompanyNameForbiddenResponse.to_json())

# convert the object into a dict
update_company_name_forbidden_response_dict = update_company_name_forbidden_response_instance.to_dict()
# create an instance of UpdateCompanyNameForbiddenResponse from a dict
update_company_name_forbidden_response_from_dict = UpdateCompanyNameForbiddenResponse.from_dict(update_company_name_forbidden_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


