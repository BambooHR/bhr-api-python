# TableRowUpdate

A dictionary of table field names and values for creating or updating a row in an employee table. The listed properties are common examples, but accepted fields depend on the specific table being targeted. Some string-valued fields are backed by lists or lookups, so callers should use valid option values from BambooHR metadata rather than assuming any free-text string will persist as entered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The effective date for the row in YYYY-MM-DD format. | [optional] 
**location** | **str** | The employee location value for the row. | [optional] 
**division** | **str** | The division value for the row. | [optional] 
**department** | **str** | The department value for the row. | [optional] 
**job_title** | **str** | The job title value for the row. | [optional] 
**reports_to** | **str** | The manager or reports-to value for the row. | [optional] 
**teams** | **List[str]** | Team values associated with the row. | [optional] 

## Example

```python
from bamboohr_sdk.models.table_row_update import TableRowUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TableRowUpdate from a JSON string
table_row_update_instance = TableRowUpdate.from_json(json)
# print the JSON string representation of the object
print(TableRowUpdate.to_json())

# convert the object into a dict
table_row_update_dict = table_row_update_instance.to_dict()
# create an instance of TableRowUpdate from a dict
table_row_update_from_dict = TableRowUpdate.from_dict(table_row_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


