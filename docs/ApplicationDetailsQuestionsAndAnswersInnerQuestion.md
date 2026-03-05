# ApplicationDetailsQuestionsAndAnswersInnerQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Question ID | [optional] 
**label** | **str** | Question text | [optional] 

## Example

```python
from bamboohr_sdk.models.application_details_questions_and_answers_inner_question import ApplicationDetailsQuestionsAndAnswersInnerQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDetailsQuestionsAndAnswersInnerQuestion from a JSON string
application_details_questions_and_answers_inner_question_instance = ApplicationDetailsQuestionsAndAnswersInnerQuestion.from_json(json)
# print the JSON string representation of the object
print(ApplicationDetailsQuestionsAndAnswersInnerQuestion.to_json())

# convert the object into a dict
application_details_questions_and_answers_inner_question_dict = application_details_questions_and_answers_inner_question_instance.to_dict()
# create an instance of ApplicationDetailsQuestionsAndAnswersInnerQuestion from a dict
application_details_questions_and_answers_inner_question_from_dict = ApplicationDetailsQuestionsAndAnswersInnerQuestion.from_dict(application_details_questions_and_answers_inner_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


