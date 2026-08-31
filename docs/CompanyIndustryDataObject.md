# CompanyIndustryDataObject

Company's enabled industry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**industry_id** | **int** | The company&#39;s industry id. | 
**added_by_customer** | **bool** | If the industry was added by the customer. | 
**added_by_user_id** | **int** |  | 
**added_ymdt** | **str** |  | 

## Example

```python
from bamboohr_sdk.models.company_industry_data_object import CompanyIndustryDataObject

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyIndustryDataObject from a JSON string
company_industry_data_object_instance = CompanyIndustryDataObject.from_json(json)
# print the JSON string representation of the object
print(CompanyIndustryDataObject.to_json())

# convert the object into a dict
company_industry_data_object_dict = company_industry_data_object_instance.to_dict()
# create an instance of CompanyIndustryDataObject from a dict
company_industry_data_object_from_dict = CompanyIndustryDataObject.from_dict(company_industry_data_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


