# AlignmentOptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aligns_with_options** | [**List[AlignmentOptionsResponseAlignsWithOptionsInner]**](AlignmentOptionsResponseAlignsWithOptionsInner.md) | Array of goals available as alignment targets for the employee. | [optional] 

## Example

```python
from bamboohr_sdk.models.alignment_options_response import AlignmentOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlignmentOptionsResponse from a JSON string
alignment_options_response_instance = AlignmentOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(AlignmentOptionsResponse.to_json())

# convert the object into a dict
alignment_options_response_dict = alignment_options_response_instance.to_dict()
# create an instance of AlignmentOptionsResponse from a dict
alignment_options_response_from_dict = AlignmentOptionsResponse.from_dict(alignment_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


