# InlineObject1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**InlineObject1Status**](InlineObject1Status.md) |  | [optional] 
**employees** | [**List[InlineObject1EmployeesInner]**](InlineObject1EmployeesInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.inline_object1 import InlineObject1

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject1 from a JSON string
inline_object1_instance = InlineObject1.from_json(json)
# print the JSON string representation of the object
print(InlineObject1.to_json())

# convert the object into a dict
inline_object1_dict = inline_object1_instance.to_dict()
# create an instance of InlineObject1 from a dict
inline_object1_from_dict = InlineObject1.from_dict(inline_object1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


