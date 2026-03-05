# TableRowUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**division** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**reports_to** | **str** |  | [optional] 
**teams** | **List[str]** |  | [optional] 

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


