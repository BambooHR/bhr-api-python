# ApplicationDetailsApplicant

Information about the applicant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Applicant ID | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**email** | **str** | Email address | [optional] 
**phone_number** | **str** | Phone number | [optional] 
**avatar** | **str** | URL to the applicant&#39;s avatar image, or null | [optional] 
**source** | **str** | Source of the application (e.g. &#39;LinkedIn&#39;, &#39;Referral&#39;), or null | [optional] 
**twitter_username** | **str** | Applicant&#39;s Twitter/X username, or null | [optional] 
**address** | [**ApplicationDetailsApplicantAddress**](ApplicationDetailsApplicantAddress.md) |  | [optional] 
**linkedin_url** | **str** | LinkedIn profile URL | [optional] 
**website_url** | **str** | Personal website URL | [optional] 
**available_start_date** | **date** | Candidate&#39;s available start date (yyyy-mm-dd) | [optional] 
**education** | [**ApplicationDetailsApplicantEducation**](ApplicationDetailsApplicantEducation.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.application_details_applicant import ApplicationDetailsApplicant

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDetailsApplicant from a JSON string
application_details_applicant_instance = ApplicationDetailsApplicant.from_json(json)
# print the JSON string representation of the object
print(ApplicationDetailsApplicant.to_json())

# convert the object into a dict
application_details_applicant_dict = application_details_applicant_instance.to_dict()
# create an instance of ApplicationDetailsApplicant from a dict
application_details_applicant_from_dict = ApplicationDetailsApplicant.from_dict(application_details_applicant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


