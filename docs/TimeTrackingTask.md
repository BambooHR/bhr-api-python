# TimeTrackingTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the task. | [optional] 
**name** | **str** | Name of the task. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_task import TimeTrackingTask

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingTask from a JSON string
time_tracking_task_instance = TimeTrackingTask.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingTask.to_json())

# convert the object into a dict
time_tracking_task_dict = time_tracking_task_instance.to_dict()
# create an instance of TimeTrackingTask from a dict
time_tracking_task_from_dict = TimeTrackingTask.from_dict(time_tracking_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


