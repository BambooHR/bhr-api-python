# TabularField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | The API alias for the table (e.g., jobInfo, compensation). | [optional] 
**fields** | [**List[TabularFieldFieldsInner]**](TabularFieldFieldsInner.md) | The fields in this table. | [optional] 

## Example

```python
from bamboohr_sdk.models.tabular_field import TabularField

# TODO update the JSON string below
json = "{}"
# create an instance of TabularField from a JSON string
tabular_field_instance = TabularField.from_json(json)
# print the JSON string representation of the object
print(TabularField.to_json())

# convert the object into a dict
tabular_field_dict = tabular_field_instance.to_dict()
# create an instance of TabularField from a dict
tabular_field_from_dict = TabularField.from_dict(tabular_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


