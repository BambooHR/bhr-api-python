# JobSummaryHiringLead

The hiring lead for this job opening

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | Employee ID | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**avatar** | **str** | URL to avatar image | [optional] 
**job_title** | **object** | Hiring lead&#39;s job title | [optional] 

## Example

```python
from bamboohr_sdk.models.job_summary_hiring_lead import JobSummaryHiringLead

# TODO update the JSON string below
json = "{}"
# create an instance of JobSummaryHiringLead from a JSON string
job_summary_hiring_lead_instance = JobSummaryHiringLead.from_json(json)
# print the JSON string representation of the object
print(JobSummaryHiringLead.to_json())

# convert the object into a dict
job_summary_hiring_lead_dict = job_summary_hiring_lead_instance.to_dict()
# create an instance of JobSummaryHiringLead from a dict
job_summary_hiring_lead_from_dict = JobSummaryHiringLead.from_dict(job_summary_hiring_lead_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


