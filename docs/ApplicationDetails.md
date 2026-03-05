# ApplicationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Application ID | [optional] 
**applied_date** | **datetime** | Date when the application was submitted | [optional] 
**status** | [**ApplicationDetailsStatus**](ApplicationDetailsStatus.md) |  | [optional] 
**rating** | **int** | Applicant rating | [optional] 
**education** | **object** | Applicant education information | [optional] 
**resume_file_id** | **int** | ID of the resume file | [optional] 
**cover_letter_file_id** | **int** | ID of the cover letter file | [optional] 
**moved_to** | **List[object]** | Positions the applicant was moved to | [optional] 
**moved_from** | **List[object]** | Positions the applicant was moved from | [optional] 
**also_considered_for_count** | **int** | Count of other positions this applicant is being considered for | [optional] 
**duplicate_application_count** | **int** | Count of duplicate applications | [optional] 
**referred_by** | **str** | Who referred this applicant | [optional] 
**desired_salary** | **str** | Applicant&#39;s desired salary | [optional] 
**comment_count** | **int** | Number of comments on this application | [optional] 
**email_count** | **int** | Number of emails for this application | [optional] 
**event_count** | **int** | Number of events for this application | [optional] 
**questions_and_answers** | [**List[ApplicationDetailsQuestionsAndAnswersInner]**](ApplicationDetailsQuestionsAndAnswersInner.md) | Custom questions and answers | [optional] 
**application_references** | **List[object]** | Application references | [optional] 
**applicant** | [**ApplicationDetailsApplicant**](ApplicationDetailsApplicant.md) |  | [optional] 
**job** | [**ApplicationDetailsJob**](ApplicationDetailsJob.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.application_details import ApplicationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDetails from a JSON string
application_details_instance = ApplicationDetails.from_json(json)
# print the JSON string representation of the object
print(ApplicationDetails.to_json())

# convert the object into a dict
application_details_dict = application_details_instance.to_dict()
# create an instance of ApplicationDetails from a dict
application_details_from_dict = ApplicationDetails.from_dict(application_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


