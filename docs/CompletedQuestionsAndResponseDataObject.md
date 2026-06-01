# CompletedQuestionsAndResponseDataObject

Data object for completed questions and responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | The question that was completed | [optional] 
**is_required** | **bool** | Indicates if the question is required | [optional] 
**archived** | **bool** | Indicates if the question is archived | [optional] 
**sort_order** | **int** | The sort order of the question | [optional] 
**employee_id** | **int** | The employee ID associated with the question | [optional] 
**employee_personal_question_id** | **int** | The employee personal question ID associated with the question | [optional] 
**employee_response** | **str** | The response to the question | [optional] 
**hidden** | **bool** | Indicates if the question is hidden | [optional] 

## Example

```python
from bamboohr_sdk.models.completed_questions_and_response_data_object import CompletedQuestionsAndResponseDataObject

# TODO update the JSON string below
json = "{}"
# create an instance of CompletedQuestionsAndResponseDataObject from a JSON string
completed_questions_and_response_data_object_instance = CompletedQuestionsAndResponseDataObject.from_json(json)
# print the JSON string representation of the object
print(CompletedQuestionsAndResponseDataObject.to_json())

# convert the object into a dict
completed_questions_and_response_data_object_dict = completed_questions_and_response_data_object_instance.to_dict()
# create an instance of CompletedQuestionsAndResponseDataObject from a dict
completed_questions_and_response_data_object_from_dict = CompletedQuestionsAndResponseDataObject.from_dict(completed_questions_and_response_data_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


