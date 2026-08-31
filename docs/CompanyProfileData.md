# CompanyProfileData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**subdomain** | **str** |  | [optional] 
**legal_name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**address** | [**CompanyProfileDataAddress**](CompanyProfileDataAddress.md) |  | [optional] 
**phone** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**termination_date** | **str** |  | [optional] 
**industry_code** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.company_profile_data import CompanyProfileData

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileData from a JSON string
company_profile_data_instance = CompanyProfileData.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileData.to_json())

# convert the object into a dict
company_profile_data_dict = company_profile_data_instance.to_dict()
# create an instance of CompanyProfileData from a dict
company_profile_data_from_dict = CompanyProfileData.from_dict(company_profile_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


