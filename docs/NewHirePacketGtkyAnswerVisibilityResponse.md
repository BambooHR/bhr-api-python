# NewHirePacketGtkyAnswerVisibilityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gtkys** | [**List[NewHirePacketGtkyAnswerVisibilityItem]**](NewHirePacketGtkyAnswerVisibilityItem.md) | GTKY personal-question answer rows with visibility flags. | 

## Example

```python
from bamboohr_sdk.models.new_hire_packet_gtky_answer_visibility_response import NewHirePacketGtkyAnswerVisibilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NewHirePacketGtkyAnswerVisibilityResponse from a JSON string
new_hire_packet_gtky_answer_visibility_response_instance = NewHirePacketGtkyAnswerVisibilityResponse.from_json(json)
# print the JSON string representation of the object
print(NewHirePacketGtkyAnswerVisibilityResponse.to_json())

# convert the object into a dict
new_hire_packet_gtky_answer_visibility_response_dict = new_hire_packet_gtky_answer_visibility_response_instance.to_dict()
# create an instance of NewHirePacketGtkyAnswerVisibilityResponse from a dict
new_hire_packet_gtky_answer_visibility_response_from_dict = NewHirePacketGtkyAnswerVisibilityResponse.from_dict(new_hire_packet_gtky_answer_visibility_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


