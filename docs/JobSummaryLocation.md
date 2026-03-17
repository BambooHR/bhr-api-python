# JobSummaryLocation

Location information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Location ID | [optional] 
**label** | **str** | Location display name | [optional] 
**address** | **object** | Full address of the location | [optional] 

## Example

```python
from bamboohr_sdk.models.job_summary_location import JobSummaryLocation

# TODO update the JSON string below
json = "{}"
# create an instance of JobSummaryLocation from a JSON string
job_summary_location_instance = JobSummaryLocation.from_json(json)
# print the JSON string representation of the object
print(JobSummaryLocation.to_json())

# convert the object into a dict
job_summary_location_dict = job_summary_location_instance.to_dict()
# create an instance of JobSummaryLocation from a dict
job_summary_location_from_dict = JobSummaryLocation.from_dict(job_summary_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


