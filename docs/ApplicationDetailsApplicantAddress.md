# ApplicationDetailsApplicantAddress

Applicant address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zipcode** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.application_details_applicant_address import ApplicationDetailsApplicantAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDetailsApplicantAddress from a JSON string
application_details_applicant_address_instance = ApplicationDetailsApplicantAddress.from_json(json)
# print the JSON string representation of the object
print(ApplicationDetailsApplicantAddress.to_json())

# convert the object into a dict
application_details_applicant_address_dict = application_details_applicant_address_instance.to_dict()
# create an instance of ApplicationDetailsApplicantAddress from a dict
application_details_applicant_address_from_dict = ApplicationDetailsApplicantAddress.from_dict(application_details_applicant_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


