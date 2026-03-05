# FieldOptionsRequestSchema

Schema for field options request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **List[str]** | List of field names to get options for | 
**dependent_fields** | **Dict[str, List[FieldOptionsRequestSchemaDependentFieldsValueInner]]** | Dependent fields and their values that affect the options of the requested fields | [optional] 
**filters** | **object** | Optional filters to apply when retrieving field options. Filters limit the returned options based on other field values. | [optional] 

## Example

```python
from bamboohr_sdk.models.field_options_request_schema import FieldOptionsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FieldOptionsRequestSchema from a JSON string
field_options_request_schema_instance = FieldOptionsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(FieldOptionsRequestSchema.to_json())

# convert the object into a dict
field_options_request_schema_dict = field_options_request_schema_instance.to_dict()
# create an instance of FieldOptionsRequestSchema from a dict
field_options_request_schema_from_dict = FieldOptionsRequestSchema.from_dict(field_options_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


