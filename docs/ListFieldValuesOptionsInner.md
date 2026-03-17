# ListFieldValuesOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The existing option ID. Omit this field to create a new option. | [optional] 
**value** | **str** | The display value for the option. | [optional] 
**archived** | **str** | Whether the option should be archived. Use &#x60;yes&#x60; to archive an option or &#x60;no&#x60; to keep it active. | [optional] 
**adp_code** | **str** | Optional payroll-mapping code associated with the option. | [optional] 

## Example

```python
from bamboohr_sdk.models.list_field_values_options_inner import ListFieldValuesOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListFieldValuesOptionsInner from a JSON string
list_field_values_options_inner_instance = ListFieldValuesOptionsInner.from_json(json)
# print the JSON string representation of the object
print(ListFieldValuesOptionsInner.to_json())

# convert the object into a dict
list_field_values_options_inner_dict = list_field_values_options_inner_instance.to_dict()
# create an instance of ListFieldValuesOptionsInner from a dict
list_field_values_options_inner_from_dict = ListFieldValuesOptionsInner.from_dict(list_field_values_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


