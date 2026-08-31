# WhosOutV1

An approved time off occurrence returned by the Who's Out endpoint. The field set matches the TIME_OFF calendar event variant so a client can swap endpoints without re-mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The time off request ID. Stable across calls. | [optional] [readonly] 
**employee_id** | **int** | The id of the employee taking time off. | [optional] 
**time_off_type_id** | **int** | The id of the time off type. | [optional] 
**start** | **date** | The first day of the time off, in ISO 8601 format (YYYY-MM-DD). All-day inclusive. Interpreted in the company timezone. | [optional] 
**end** | **date** | The last day of the time off, in ISO 8601 format (YYYY-MM-DD). All-day inclusive. Same as start for single-day requests. | [optional] 

## Example

```python
from bamboohr_sdk.models.whos_out_v1 import WhosOutV1

# TODO update the JSON string below
json = "{}"
# create an instance of WhosOutV1 from a JSON string
whos_out_v1_instance = WhosOutV1.from_json(json)
# print the JSON string representation of the object
print(WhosOutV1.to_json())

# convert the object into a dict
whos_out_v1_dict = whos_out_v1_instance.to_dict()
# create an instance of WhosOutV1 from a dict
whos_out_v1_from_dict = WhosOutV1.from_dict(whos_out_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


