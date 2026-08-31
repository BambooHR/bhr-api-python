# UpdateCompanyNameSuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Indicates whether the operation was successful | [optional] 

## Example

```python
from bamboohr_sdk.models.update_company_name_success_response import UpdateCompanyNameSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCompanyNameSuccessResponse from a JSON string
update_company_name_success_response_instance = UpdateCompanyNameSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCompanyNameSuccessResponse.to_json())

# convert the object into a dict
update_company_name_success_response_dict = update_company_name_success_response_instance.to_dict()
# create an instance of UpdateCompanyNameSuccessResponse from a dict
update_company_name_success_response_from_dict = UpdateCompanyNameSuccessResponse.from_dict(update_company_name_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


