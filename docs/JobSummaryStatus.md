# JobSummaryStatus

Job opening status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Status ID | [optional] 
**label** | **str** | Status name | [optional] 

## Example

```python
from bamboohr_sdk.models.job_summary_status import JobSummaryStatus

# TODO update the JSON string below
json = "{}"
# create an instance of JobSummaryStatus from a JSON string
job_summary_status_instance = JobSummaryStatus.from_json(json)
# print the JSON string representation of the object
print(JobSummaryStatus.to_json())

# convert the object into a dict
job_summary_status_dict = job_summary_status_instance.to_dict()
# create an instance of JobSummaryStatus from a dict
job_summary_status_from_dict = JobSummaryStatus.from_dict(job_summary_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


