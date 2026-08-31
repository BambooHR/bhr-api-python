# PatchCompanyProfileCompanyInformationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str** | Legal name of the company (name_of_employer). Required (non-empty) when this field is present in the patch. | [optional] 
**phone** | **str** | Contact phone number. Required (non-empty) when this field is present in the patch. | [optional] 
**address** | [**PatchCompanyProfileCompanyInformationRequestAddress**](PatchCompanyProfileCompanyInformationRequestAddress.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.patch_company_profile_company_information_request import PatchCompanyProfileCompanyInformationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchCompanyProfileCompanyInformationRequest from a JSON string
patch_company_profile_company_information_request_instance = PatchCompanyProfileCompanyInformationRequest.from_json(json)
# print the JSON string representation of the object
print(PatchCompanyProfileCompanyInformationRequest.to_json())

# convert the object into a dict
patch_company_profile_company_information_request_dict = patch_company_profile_company_information_request_instance.to_dict()
# create an instance of PatchCompanyProfileCompanyInformationRequest from a dict
patch_company_profile_company_information_request_from_dict = PatchCompanyProfileCompanyInformationRequest.from_dict(patch_company_profile_company_information_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


