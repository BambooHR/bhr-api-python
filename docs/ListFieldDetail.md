# ListFieldDetail

A single list field and its available options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **str** | The field ID. | [optional] 
**name** | **str** | The display name of the list field. | [optional] 
**alias** | **str** | The API alias for the list field. | [optional] 
**manageable** | **str** | Whether the list field options can be modified via the API. One of: yes, no. | [optional] 
**multiple** | **str** | Whether this field supports multiple values. One of: yes, no. | [optional] 
**options** | [**List[ListFieldOption]**](ListFieldOption.md) | The available options for this list field. | [optional] 

## Example

```python
from bamboohr_sdk.models.list_field_detail import ListFieldDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ListFieldDetail from a JSON string
list_field_detail_instance = ListFieldDetail.from_json(json)
# print the JSON string representation of the object
print(ListFieldDetail.to_json())

# convert the object into a dict
list_field_detail_dict = list_field_detail_instance.to_dict()
# create an instance of ListFieldDetail from a dict
list_field_detail_from_dict = ListFieldDetail.from_dict(list_field_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


