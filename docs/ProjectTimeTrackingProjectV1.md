# ProjectTimeTrackingProjectV1

A time tracking project. Projects are organizational units used to classify hours worked.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the project. | [optional] [readonly] 
**name** | **str** | The name of the project. | [optional] 
**billable** | **bool** | Whether or not the project is billable. | [optional] 
**include_in_payroll** | **bool** | Whether hours logged to this project will show in payroll and payroll reports. | [optional] 
**all_employees_assigned** | **bool** | Whether all time &amp; attendance employees are assigned or not. | [optional] 
**archived** | **bool** | Whether or not the project is archived. | [optional] 
**has_tasks** | **bool** | Whether time is logged to tasks under the project (true) or directly to the project (false). | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**deleted_at** | **datetime** |  | [optional] [readonly] 
**employee_ids** | **List[int]** | Array of employeeIds assigned to the project. | [optional] 

## Example

```python
from bamboohr_sdk.models.project_time_tracking_project_v1 import ProjectTimeTrackingProjectV1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTimeTrackingProjectV1 from a JSON string
project_time_tracking_project_v1_instance = ProjectTimeTrackingProjectV1.from_json(json)
# print the JSON string representation of the object
print(ProjectTimeTrackingProjectV1.to_json())

# convert the object into a dict
project_time_tracking_project_v1_dict = project_time_tracking_project_v1_instance.to_dict()
# create an instance of ProjectTimeTrackingProjectV1 from a dict
project_time_tracking_project_v1_from_dict = ProjectTimeTrackingProjectV1.from_dict(project_time_tracking_project_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


