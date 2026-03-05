# ReportsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reports** | [**List[Report]**](Report.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.reports_response import ReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportsResponse from a JSON string
reports_response_instance = ReportsResponse.from_json(json)
# print the JSON string representation of the object
print(ReportsResponse.to_json())

# convert the object into a dict
reports_response_dict = reports_response_instance.to_dict()
# create an instance of ReportsResponse from a dict
reports_response_from_dict = ReportsResponse.from_dict(reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


