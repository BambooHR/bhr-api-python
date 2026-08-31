# InlineObject2Inner


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
from bamboohr_sdk.models.inline_object2_inner import InlineObject2Inner

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject2Inner from a JSON string
inline_object2_inner_instance = InlineObject2Inner.from_json(json)
# print the JSON string representation of the object
print(InlineObject2Inner.to_json())

# convert the object into a dict
inline_object2_inner_dict = inline_object2_inner_instance.to_dict()
# create an instance of InlineObject2Inner from a dict
inline_object2_inner_from_dict = InlineObject2Inner.from_dict(inline_object2_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


