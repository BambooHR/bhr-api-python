# InlineObjectInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Plan ID | [optional] 
**type** | **str** | Plan category | [optional] 
**name** | **str** | Plan name | [optional] 
**carrier_name** | **str** | Carrier name | [optional] 
**syncing_capabilities** | **List[str]** | Which integration the plan is capable of being synced with | [optional] 

## Example

```python
from bamboohr_sdk.models.inline_object_inner import InlineObjectInner

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObjectInner from a JSON string
inline_object_inner_instance = InlineObjectInner.from_json(json)
# print the JSON string representation of the object
print(InlineObjectInner.to_json())

# convert the object into a dict
inline_object_inner_dict = inline_object_inner_instance.to_dict()
# create an instance of InlineObjectInner from a dict
inline_object_inner_from_dict = InlineObjectInner.from_dict(inline_object_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


