# ApplicationDetailsJobHiringLead

The hiring lead for this job opening

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | Employee ID of the hiring lead | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**avatar** | **str** | URL to avatar image | [optional] 
**job_title** | [**ApplicationDetailsJobHiringLeadJobTitle**](ApplicationDetailsJobHiringLeadJobTitle.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.application_details_job_hiring_lead import ApplicationDetailsJobHiringLead

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDetailsJobHiringLead from a JSON string
application_details_job_hiring_lead_instance = ApplicationDetailsJobHiringLead.from_json(json)
# print the JSON string representation of the object
print(ApplicationDetailsJobHiringLead.to_json())

# convert the object into a dict
application_details_job_hiring_lead_dict = application_details_job_hiring_lead_instance.to_dict()
# create an instance of ApplicationDetailsJobHiringLead from a dict
application_details_job_hiring_lead_from_dict = ApplicationDetailsJobHiringLead.from_dict(application_details_job_hiring_lead_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


