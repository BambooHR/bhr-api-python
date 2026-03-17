# CompanyInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str** | The legal name of the company. | [optional] 
**display_name** | **str** | The display name of the company. | [optional] 
**address** | [**CompanyInformationAddress**](CompanyInformationAddress.md) |  | [optional] 
**phone** | **str** | The primary contact phone number of the company. | [optional] 

## Example

```python
from bamboohr_sdk.models.company_information import CompanyInformation

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInformation from a JSON string
company_information_instance = CompanyInformation.from_json(json)
# print the JSON string representation of the object
print(CompanyInformation.to_json())

# convert the object into a dict
company_information_dict = company_information_instance.to_dict()
# create an instance of CompanyInformation from a dict
company_information_from_dict = CompanyInformation.from_dict(company_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


