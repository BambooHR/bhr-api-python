# CompanyProfileDataAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** |  | [optional] 
**line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.company_profile_data_address import CompanyProfileDataAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileDataAddress from a JSON string
company_profile_data_address_instance = CompanyProfileDataAddress.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileDataAddress.to_json())

# convert the object into a dict
company_profile_data_address_dict = company_profile_data_address_instance.to_dict()
# create an instance of CompanyProfileDataAddress from a dict
company_profile_data_address_from_dict = CompanyProfileDataAddress.from_dict(company_profile_data_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


