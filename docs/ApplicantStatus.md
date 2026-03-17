# ApplicantStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Status ID | [optional] 
**code** | **str** | Internal status code, or null for custom statuses | [optional] 
**name** | **str** | Status display name | [optional] 
**translated_name** | **str** | Translated display name | [optional] 
**description** | **str** | Optional description of the status | [optional] 
**enabled** | **bool** | Whether the status is currently active and selectable | [optional] 
**manageable** | **bool** | Whether the status can be managed (edited/deleted) by the company | [optional] 

## Example

```python
from bamboohr_sdk.models.applicant_status import ApplicantStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicantStatus from a JSON string
applicant_status_instance = ApplicantStatus.from_json(json)
# print the JSON string representation of the object
print(ApplicantStatus.to_json())

# convert the object into a dict
applicant_status_dict = applicant_status_instance.to_dict()
# create an instance of ApplicantStatus from a dict
applicant_status_from_dict = ApplicantStatus.from_dict(applicant_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


