# TimeOffRequest1Amount

The amount of time off requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | The unit of measurement. | [optional] 
**amount** | **float** | The total amount requested. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_off_request1_amount import TimeOffRequest1Amount

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffRequest1Amount from a JSON string
time_off_request1_amount_instance = TimeOffRequest1Amount.from_json(json)
# print the JSON string representation of the object
print(TimeOffRequest1Amount.to_json())

# convert the object into a dict
time_off_request1_amount_dict = time_off_request1_amount_instance.to_dict()
# create an instance of TimeOffRequest1Amount from a dict
time_off_request1_amount_from_dict = TimeOffRequest1Amount.from_dict(time_off_request1_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


