# NewHirePacketGtkyAnswerVisibilityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hidden** | **bool** | When true, answers are hidden from typical manager views; when false, answers are shown. | 
**question_ids** | **List[int]** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.new_hire_packet_gtky_answer_visibility_request import NewHirePacketGtkyAnswerVisibilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NewHirePacketGtkyAnswerVisibilityRequest from a JSON string
new_hire_packet_gtky_answer_visibility_request_instance = NewHirePacketGtkyAnswerVisibilityRequest.from_json(json)
# print the JSON string representation of the object
print(NewHirePacketGtkyAnswerVisibilityRequest.to_json())

# convert the object into a dict
new_hire_packet_gtky_answer_visibility_request_dict = new_hire_packet_gtky_answer_visibility_request_instance.to_dict()
# create an instance of NewHirePacketGtkyAnswerVisibilityRequest from a dict
new_hire_packet_gtky_answer_visibility_request_from_dict = NewHirePacketGtkyAnswerVisibilityRequest.from_dict(new_hire_packet_gtky_answer_visibility_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


