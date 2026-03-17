# ApplicationDetailsApplicantEducation

Applicant's education information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution** | **str** | Name of the educational institution | [optional] 
**level** | [**ApplicationDetailsApplicantEducationLevel**](ApplicationDetailsApplicantEducationLevel.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.application_details_applicant_education import ApplicationDetailsApplicantEducation

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDetailsApplicantEducation from a JSON string
application_details_applicant_education_instance = ApplicationDetailsApplicantEducation.from_json(json)
# print the JSON string representation of the object
print(ApplicationDetailsApplicantEducation.to_json())

# convert the object into a dict
application_details_applicant_education_dict = application_details_applicant_education_instance.to_dict()
# create an instance of ApplicationDetailsApplicantEducation from a dict
application_details_applicant_education_from_dict = ApplicationDetailsApplicantEducation.from_dict(application_details_applicant_education_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


