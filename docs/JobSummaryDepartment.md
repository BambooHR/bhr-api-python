# JobSummaryDepartment

Department information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Department ID | [optional] 
**label** | **str** | Department name | [optional] 

## Example

```python
from bamboohr_sdk.models.job_summary_department import JobSummaryDepartment

# TODO update the JSON string below
json = "{}"
# create an instance of JobSummaryDepartment from a JSON string
job_summary_department_instance = JobSummaryDepartment.from_json(json)
# print the JSON string representation of the object
print(JobSummaryDepartment.to_json())

# convert the object into a dict
job_summary_department_dict = job_summary_department_instance.to_dict()
# create an instance of JobSummaryDepartment from a dict
job_summary_department_from_dict = JobSummaryDepartment.from_dict(job_summary_department_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


