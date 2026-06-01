# GetDataFromDatasetV2Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **List[Optional[str]]** | Field names to return for each row. Names are dataset-specific; discover valid names via Get Fields from Dataset (v1.2) (&#x60;get-fields-from-dataset-v1-2&#x60;). The field-name vocabulary differs from the dedicated employee endpoints (e.g., the &#x60;employee&#x60; dataset uses &#x60;jobInformationReportsTo&#x60; / &#x60;jobInformationDepartment&#x60; / &#x60;employmentStatus&#x60; rather than List Employees&#39; &#x60;reportsTo&#x60; / &#x60;department&#x60; / &#x60;status&#x60;). | 
**filter** | **str** |  | [optional] 
**order_by** | **str** |  | [optional] 
**page** | **int** | Page number to retrieve (1-indexed). Defaults to 1. | [optional] [default to 1]
**page_size** | **int** | Number of records per page. Defaults to 100. Maximum is 1000. | [optional] [default to 100]

## Example

```python
from bamboohr_sdk.models.get_data_from_dataset_v2_request import GetDataFromDatasetV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataFromDatasetV2Request from a JSON string
get_data_from_dataset_v2_request_instance = GetDataFromDatasetV2Request.from_json(json)
# print the JSON string representation of the object
print(GetDataFromDatasetV2Request.to_json())

# convert the object into a dict
get_data_from_dataset_v2_request_dict = get_data_from_dataset_v2_request_instance.to_dict()
# create an instance of GetDataFromDatasetV2Request from a dict
get_data_from_dataset_v2_request_from_dict = GetDataFromDatasetV2Request.from_dict(get_data_from_dataset_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


