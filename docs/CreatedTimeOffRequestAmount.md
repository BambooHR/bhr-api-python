# CreatedTimeOffRequestAmount

The amount of time off requested. Only present when the underlying time off type record could be loaded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | The unit of measurement. | [optional] 
**amount** | **float** | The total amount requested. | [optional] 

## Example

```python
from bamboohr_sdk.models.created_time_off_request_amount import CreatedTimeOffRequestAmount

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedTimeOffRequestAmount from a JSON string
created_time_off_request_amount_instance = CreatedTimeOffRequestAmount.from_json(json)
# print the JSON string representation of the object
print(CreatedTimeOffRequestAmount.to_json())

# convert the object into a dict
created_time_off_request_amount_dict = created_time_off_request_amount_instance.to_dict()
# create an instance of CreatedTimeOffRequestAmount from a dict
created_time_off_request_amount_from_dict = CreatedTimeOffRequestAmount.from_dict(created_time_off_request_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


