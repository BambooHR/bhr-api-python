# MonitorFieldList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[MonitorFieldListFieldsInner]**](MonitorFieldListFieldsInner.md) | The list of employee fields available for webhook monitoring. | 

## Example

```python
from bamboohr_sdk.models.monitor_field_list import MonitorFieldList

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorFieldList from a JSON string
monitor_field_list_instance = MonitorFieldList.from_json(json)
# print the JSON string representation of the object
print(MonitorFieldList.to_json())

# convert the object into a dict
monitor_field_list_dict = monitor_field_list_instance.to_dict()
# create an instance of MonitorFieldList from a dict
monitor_field_list_from_dict = MonitorFieldList.from_dict(monitor_field_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


