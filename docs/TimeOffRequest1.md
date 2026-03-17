# TimeOffRequest1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The time off request ID. | [optional] 
**employee_id** | **int** | The ID of the employee. | [optional] 
**name** | **str** | The employee&#39;s full name. | [optional] 
**start** | **date** | The start date of the request in YYYY-MM-DD format. | [optional] 
**end** | **date** | The end date of the request in YYYY-MM-DD format. | [optional] 
**created** | **date** | The date the request was created in YYYY-MM-DD format (company timezone). | [optional] 
**status** | [**TimeOffRequest1Status**](TimeOffRequest1Status.md) |  | [optional] 
**type** | [**TimeOffRequest1Type**](TimeOffRequest1Type.md) |  | [optional] 
**amount** | [**TimeOffRequest1Amount**](TimeOffRequest1Amount.md) |  | [optional] 
**actions** | [**TimeOffRequest1Actions**](TimeOffRequest1Actions.md) |  | [optional] 
**dates** | **Dict[str, float]** | A map of dates (YYYY-MM-DD) to daily amounts. | [optional] 
**notes** | [**TimeOffRequest1Notes**](TimeOffRequest1Notes.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_off_request1 import TimeOffRequest1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffRequest1 from a JSON string
time_off_request1_instance = TimeOffRequest1.from_json(json)
# print the JSON string representation of the object
print(TimeOffRequest1.to_json())

# convert the object into a dict
time_off_request1_dict = time_off_request1_instance.to_dict()
# create an instance of TimeOffRequest1 from a dict
time_off_request1_from_dict = TimeOffRequest1.from_dict(time_off_request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


