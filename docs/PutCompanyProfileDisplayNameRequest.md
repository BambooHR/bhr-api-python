# PutCompanyProfileDisplayNameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | The new display name for the company. Must be a non-empty string with a maximum length of 255 characters (character count, not bytes, so multibyte UTF-8 characters are properly supported). | 

## Example

```python
from bamboohr_sdk.models.put_company_profile_display_name_request import PutCompanyProfileDisplayNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutCompanyProfileDisplayNameRequest from a JSON string
put_company_profile_display_name_request_instance = PutCompanyProfileDisplayNameRequest.from_json(json)
# print the JSON string representation of the object
print(PutCompanyProfileDisplayNameRequest.to_json())

# convert the object into a dict
put_company_profile_display_name_request_dict = put_company_profile_display_name_request_instance.to_dict()
# create an instance of PutCompanyProfileDisplayNameRequest from a dict
put_company_profile_display_name_request_from_dict = PutCompanyProfileDisplayNameRequest.from_dict(put_company_profile_display_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


