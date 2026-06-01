# MonitorFieldListFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The field ID, returned as a string. | 
**name** | **str** | The human-readable field name. | 
**alias** | **str** |  | 

## Example

```python
from bamboohr_sdk.models.monitor_field_list_fields_inner import MonitorFieldListFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorFieldListFieldsInner from a JSON string
monitor_field_list_fields_inner_instance = MonitorFieldListFieldsInner.from_json(json)
# print the JSON string representation of the object
print(MonitorFieldListFieldsInner.to_json())

# convert the object into a dict
monitor_field_list_fields_inner_dict = monitor_field_list_fields_inner_instance.to_dict()
# create an instance of MonitorFieldListFieldsInner from a dict
monitor_field_list_fields_inner_from_dict = MonitorFieldListFieldsInner.from_dict(monitor_field_list_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


