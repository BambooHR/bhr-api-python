# PatchCompanyProfileCompanyInformationRequestAddress

Company address. When `address` is included in the patch (non-null object), `city`, `state`, and `zip` must all be sent as non-empty strings. `line1` and `line2` are optional (JSON null removes a line per merge-patch).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** |  | [optional] 
**line2** | **str** |  | [optional] 
**city** | **str** | City. Required (non-empty) when address is patched. | [optional] 
**state** | **str** | State. Required (non-empty) when address is patched. | [optional] 
**zip** | **str** | Zip or postal code. Required (non-empty) when address is patched. | [optional] 

## Example

```python
from bamboohr_sdk.models.patch_company_profile_company_information_request_address import PatchCompanyProfileCompanyInformationRequestAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PatchCompanyProfileCompanyInformationRequestAddress from a JSON string
patch_company_profile_company_information_request_address_instance = PatchCompanyProfileCompanyInformationRequestAddress.from_json(json)
# print the JSON string representation of the object
print(PatchCompanyProfileCompanyInformationRequestAddress.to_json())

# convert the object into a dict
patch_company_profile_company_information_request_address_dict = patch_company_profile_company_information_request_address_instance.to_dict()
# create an instance of PatchCompanyProfileCompanyInformationRequestAddress from a dict
patch_company_profile_company_information_request_address_from_dict = PatchCompanyProfileCompanyInformationRequestAddress.from_dict(patch_company_profile_company_information_request_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


