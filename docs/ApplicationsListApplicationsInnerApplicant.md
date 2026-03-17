# ApplicationsListApplicationsInnerApplicant

Information about the applicant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Applicant ID | [optional] 
**first_name** | **str** | Applicant&#39;s first name | [optional] 
**last_name** | **str** | Applicant&#39;s last name | [optional] 
**avatar** | **str** | URL to applicant&#39;s avatar image, or null | [optional] 
**email** | **str** | Applicant&#39;s email address | [optional] 
**source** | **str** | Source of the application | [optional] 

## Example

```python
from bamboohr_sdk.models.applications_list_applications_inner_applicant import ApplicationsListApplicationsInnerApplicant

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsListApplicationsInnerApplicant from a JSON string
applications_list_applications_inner_applicant_instance = ApplicationsListApplicationsInnerApplicant.from_json(json)
# print the JSON string representation of the object
print(ApplicationsListApplicationsInnerApplicant.to_json())

# convert the object into a dict
applications_list_applications_inner_applicant_dict = applications_list_applications_inner_applicant_instance.to_dict()
# create an instance of ApplicationsListApplicationsInnerApplicant from a dict
applications_list_applications_inner_applicant_from_dict = ApplicationsListApplicationsInnerApplicant.from_dict(applications_list_applications_inner_applicant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


