# ApplicationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Application ID | [optional] 
**applied_date** | **datetime** | ISO 8601 datetime when the application was submitted | [optional] 
**status** | [**ApplicationDetailsStatus**](ApplicationDetailsStatus.md) |  | [optional] 
**rating** | **int** | Applicant rating (1-5), or null if not yet rated | [optional] 
**resume_file_id** | **int** | ID of the attached resume file, or null if not provided | [optional] 
**cover_letter_file_id** | **int** | ID of the attached cover letter file, or null if not provided | [optional] 
**attachment_count** | **int** | Total number of attachments on this application, or null | [optional] 
**attachments** | [**List[ApplicationDetailsAttachmentsInner]**](ApplicationDetailsAttachmentsInner.md) | List of attachments on this application, or null if none exist | [optional] 
**moved_to** | **List[object]** | List of applications this applicant was moved to, or null if not moved | [optional] 
**moved_from** | **List[object]** | List of applications this applicant was moved from, or null if not moved | [optional] 
**also_considered_for_count** | **int** | Count of other job openings this applicant is also being considered for | [optional] 
**duplicate_application_count** | **int** | Count of duplicate applications from this applicant | [optional] 
**referred_by** | **str** | Name of the person who referred this applicant, or null | [optional] 
**desired_salary** | **str** | Applicant&#39;s desired salary, or null if not provided | [optional] 
**comment_count** | **int** | Number of comments on this application | [optional] 
**email_count** | **int** | Number of emails sent for this application | [optional] 
**event_count** | **int** | Number of events associated with this application | [optional] 
**questions_and_answers** | [**List[ApplicationDetailsQuestionsAndAnswersInner]**](ApplicationDetailsQuestionsAndAnswersInner.md) | List of custom application questions and the applicant&#39;s answers | [optional] 
**application_references** | **str** | Free-text references provided by the applicant, or null | [optional] 
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


