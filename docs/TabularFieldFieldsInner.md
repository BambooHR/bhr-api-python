# TabularFieldFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The field ID. | [optional] 
**name** | **str** | The display name of the field. | [optional] 
**alias** | **str** | The API alias for the field within this table. | [optional] 
**type** | **str** | The data type of the field (e.g., text, date, list). | [optional] 

## Example

```python
from bamboohr_sdk.models.tabular_field_fields_inner import TabularFieldFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TabularFieldFieldsInner from a JSON string
tabular_field_fields_inner_instance = TabularFieldFieldsInner.from_json(json)
# print the JSON string representation of the object
print(TabularFieldFieldsInner.to_json())

# convert the object into a dict
tabular_field_fields_inner_dict = tabular_field_fields_inner_instance.to_dict()
# create an instance of TabularFieldFieldsInner from a dict
tabular_field_fields_inner_from_dict = TabularFieldFieldsInner.from_dict(tabular_field_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


