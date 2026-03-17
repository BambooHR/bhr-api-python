# ApplicationDetailsQuestionsAndAnswersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | [**ApplicationDetailsQuestionsAndAnswersInnerQuestion**](ApplicationDetailsQuestionsAndAnswersInnerQuestion.md) |  | [optional] 
**answer** | [**ApplicationDetailsQuestionsAndAnswersInnerAnswer**](ApplicationDetailsQuestionsAndAnswersInnerAnswer.md) |  | [optional] 
**has_revisions** | **bool** | Whether this answer has revision history | [optional] 
**is_archived** | **bool** | Whether this answer is archived | [optional] 
**archived_date** | **datetime** | ISO 8601 datetime when the answer was archived, or null | [optional] 
**edited_date** | **datetime** | ISO 8601 datetime when the answer was last edited, or null | [optional] 
**edited_end_date** | **datetime** | ISO 8601 datetime for the end date of the edit window, or null | [optional] 

## Example

```python
from bamboohr_sdk.models.application_details_questions_and_answers_inner import ApplicationDetailsQuestionsAndAnswersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDetailsQuestionsAndAnswersInner from a JSON string
application_details_questions_and_answers_inner_instance = ApplicationDetailsQuestionsAndAnswersInner.from_json(json)
# print the JSON string representation of the object
print(ApplicationDetailsQuestionsAndAnswersInner.to_json())

# convert the object into a dict
application_details_questions_and_answers_inner_dict = application_details_questions_and_answers_inner_instance.to_dict()
# create an instance of ApplicationDetailsQuestionsAndAnswersInner from a dict
application_details_questions_and_answers_inner_from_dict = ApplicationDetailsQuestionsAndAnswersInner.from_dict(application_details_questions_and_answers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


