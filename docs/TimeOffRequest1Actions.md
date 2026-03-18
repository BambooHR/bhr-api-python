# TimeOffRequest1Actions

Actions the current user can perform on this request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **bool** | Whether the user can view this request. | [optional] 
**edit** | **bool** | Whether the user can edit this request. | [optional] 
**cancel** | **bool** | Whether the user can cancel this request. | [optional] 
**approve** | **bool** | Whether the user can approve this request. | [optional] 
**deny** | **bool** | Whether the user can deny this request. | [optional] 
**bypass** | **bool** | Whether the user can bypass the approval workflow. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_off_request1_actions import TimeOffRequest1Actions

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffRequest1Actions from a JSON string
time_off_request1_actions_instance = TimeOffRequest1Actions.from_json(json)
# print the JSON string representation of the object
print(TimeOffRequest1Actions.to_json())

# convert the object into a dict
time_off_request1_actions_dict = time_off_request1_actions_instance.to_dict()
# create an instance of TimeOffRequest1Actions from a dict
time_off_request1_actions_from_dict = TimeOffRequest1Actions.from_dict(time_off_request1_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


