# Field1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Field1Id**](Field1Id.md) |  | 
**name** | **str** | The display name of the field. | 
**type** | **str** | The data type of the field (e.g., text, date, list, checkbox). | 
**alias** | **str** | The API alias for the field. Only present when the field has an alias. | [optional] 
**deprecated** | **bool** | Whether the field is deprecated and should no longer be used. Only present for deprecated fields. | [optional] 

## Example

```python
from bamboohr_sdk.models.field1 import Field1

# TODO update the JSON string below
json = "{}"
# create an instance of Field1 from a JSON string
field1_instance = Field1.from_json(json)
# print the JSON string representation of the object
print(Field1.to_json())

# convert the object into a dict
field1_dict = field1_instance.to_dict()
# create an instance of Field1 from a dict
field1_from_dict = Field1.from_dict(field1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


