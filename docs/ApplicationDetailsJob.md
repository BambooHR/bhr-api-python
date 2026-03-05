# ApplicationDetailsJob

Job details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Job ID | [optional] 
**title** | **str** | Job title | [optional] 
**department** | **object** | Department information | [optional] 
**location** | **object** | Location information | [optional] 
**hiring_lead** | **object** | Hiring lead information | [optional] 

## Example

```python
from bamboohr_sdk.models.application_details_job import ApplicationDetailsJob

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDetailsJob from a JSON string
application_details_job_instance = ApplicationDetailsJob.from_json(json)
# print the JSON string representation of the object
print(ApplicationDetailsJob.to_json())

# convert the object into a dict
application_details_job_dict = application_details_job_instance.to_dict()
# create an instance of ApplicationDetailsJob from a dict
application_details_job_from_dict = ApplicationDetailsJob.from_dict(application_details_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


