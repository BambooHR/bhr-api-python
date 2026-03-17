# Field1Id

The field identifier. For subfields this is a dotted string (e.g., \"4340.4\"); for top-level fields it may be an integer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from bamboohr_sdk.models.field1_id import Field1Id

# TODO update the JSON string below
json = "{}"
# create an instance of Field1Id from a JSON string
field1_id_instance = Field1Id.from_json(json)
# print the JSON string representation of the object
print(Field1Id.to_json())

# convert the object into a dict
field1_id_dict = field1_id_instance.to_dict()
# create an instance of Field1Id from a dict
field1_id_from_dict = Field1Id.from_dict(field1_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


