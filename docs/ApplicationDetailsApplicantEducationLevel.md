# ApplicationDetailsApplicantEducationLevel

Highest level of education

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Education level ID | [optional] 
**label** | **str** | Education level name | [optional] 

## Example

```python
from bamboohr_sdk.models.application_details_applicant_education_level import ApplicationDetailsApplicantEducationLevel

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDetailsApplicantEducationLevel from a JSON string
application_details_applicant_education_level_instance = ApplicationDetailsApplicantEducationLevel.from_json(json)
# print the JSON string representation of the object
print(ApplicationDetailsApplicantEducationLevel.to_json())

# convert the object into a dict
application_details_applicant_education_level_dict = application_details_applicant_education_level_instance.to_dict()
# create an instance of ApplicationDetailsApplicantEducationLevel from a dict
application_details_applicant_education_level_from_dict = ApplicationDetailsApplicantEducationLevel.from_dict(application_details_applicant_education_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


