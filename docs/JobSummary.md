# JobSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Job opening ID | [optional] 
**title** | [**ApplicationDetailsJobTitle**](ApplicationDetailsJobTitle.md) |  | [optional] 
**posted_date** | **datetime** | ISO 8601 datetime when the job opening was posted | [optional] 
**location** | [**JobSummaryLocation**](JobSummaryLocation.md) |  | [optional] 
**department** | [**JobSummaryDepartment**](JobSummaryDepartment.md) |  | [optional] 
**status** | [**JobSummaryStatus**](JobSummaryStatus.md) |  | [optional] 
**hiring_lead** | [**JobSummaryHiringLead**](JobSummaryHiringLead.md) |  | [optional] 
**new_applicants_count** | **int** | Number of applicants in &#39;New&#39; status | [optional] 
**active_applicants_count** | **int** | Number of applicants in an active status | [optional] 
**total_applicants_count** | **int** | Total number of applicants | [optional] 
**posting_url** | **str** | Public URL for the job posting, or null if not posted | [optional] 

## Example

```python
from bamboohr_sdk.models.job_summary import JobSummary

# TODO update the JSON string below
json = "{}"
# create an instance of JobSummary from a JSON string
job_summary_instance = JobSummary.from_json(json)
# print the JSON string representation of the object
print(JobSummary.to_json())

# convert the object into a dict
job_summary_dict = job_summary_instance.to_dict()
# create an instance of JobSummary from a dict
job_summary_from_dict = JobSummary.from_dict(job_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


