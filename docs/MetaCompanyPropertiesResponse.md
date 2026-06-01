# MetaCompanyPropertiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Bamboo company identifier (numeric). | [optional] 
**name** | **str** | Company display name. | [optional] 
**domain** | **str** | Company’s Bamboo subdomain (same value used in the &#x60;baseApiUrl&#x60; path segment after &#x60;gateway.php/&#x60;) | [optional] 
**base_api_url** | **str** | Full HTTPS URL of the public API gateway for this company, typically &#x60;https://&#x60; + the data-center–specific API host for this tenant + &#x60; /api/gateway.php/&#x60; + the company’s &#x60;domain&#x60; from this response. This is the entry point the integrator uses for legacy gateway-style API traffic, not a generic “base URL” name alone. | [optional] 

## Example

```python
from bamboohr_sdk.models.meta_company_properties_response import MetaCompanyPropertiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MetaCompanyPropertiesResponse from a JSON string
meta_company_properties_response_instance = MetaCompanyPropertiesResponse.from_json(json)
# print the JSON string representation of the object
print(MetaCompanyPropertiesResponse.to_json())

# convert the object into a dict
meta_company_properties_response_dict = meta_company_properties_response_instance.to_dict()
# create an instance of MetaCompanyPropertiesResponse from a dict
meta_company_properties_response_from_dict = MetaCompanyPropertiesResponse.from_dict(meta_company_properties_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


