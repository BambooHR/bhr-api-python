# CompanyInformationAddress

The primary address of the company.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** | The first line of the address. | [optional] 
**line2** | **str** | The second line of the address. May be an empty string. | [optional] 
**city** | **str** | The city. | [optional] 
**state** | **str** | The state or province abbreviation. | [optional] 
**zip** | **str** | The ZIP or postal code. | [optional] 

## Example

```python
from bamboohr_sdk.models.company_information_address import CompanyInformationAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInformationAddress from a JSON string
company_information_address_instance = CompanyInformationAddress.from_json(json)
# print the JSON string representation of the object
print(CompanyInformationAddress.to_json())

# convert the object into a dict
company_information_address_dict = company_information_address_instance.to_dict()
# create an instance of CompanyInformationAddress from a dict
company_information_address_from_dict = CompanyInformationAddress.from_dict(company_information_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


