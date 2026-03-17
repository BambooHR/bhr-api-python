# CompanyProfileIntegrations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integrations** | **List[str]** | List of installed integration identifiers. | [optional] 

## Example

```python
from bamboohr_sdk.models.company_profile_integrations import CompanyProfileIntegrations

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileIntegrations from a JSON string
company_profile_integrations_instance = CompanyProfileIntegrations.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileIntegrations.to_json())

# convert the object into a dict
company_profile_integrations_dict = company_profile_integrations_instance.to_dict()
# create an instance of CompanyProfileIntegrations from a dict
company_profile_integrations_from_dict = CompanyProfileIntegrations.from_dict(company_profile_integrations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


