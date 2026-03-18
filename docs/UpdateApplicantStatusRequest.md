# UpdateApplicantStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The ID of the status to assign to the application. Use the Get Applicant Statuses endpoint to get available status IDs. | 

## Example

```python
from bamboohr_sdk.models.update_applicant_status_request import UpdateApplicantStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApplicantStatusRequest from a JSON string
update_applicant_status_request_instance = UpdateApplicantStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateApplicantStatusRequest.to_json())

# convert the object into a dict
update_applicant_status_request_dict = update_applicant_status_request_instance.to_dict()
# create an instance of UpdateApplicantStatusRequest from a dict
update_applicant_status_request_from_dict = UpdateApplicantStatusRequest.from_dict(update_applicant_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


