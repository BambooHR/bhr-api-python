# UpdateApplicantStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Always &#39;positionApplicantStatus&#39; | [optional] 
**id** | **int** | The ID of the created status change record | [optional] 

## Example

```python
from bamboohr_sdk.models.update_applicant_status_response import UpdateApplicantStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApplicantStatusResponse from a JSON string
update_applicant_status_response_instance = UpdateApplicantStatusResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateApplicantStatusResponse.to_json())

# convert the object into a dict
update_applicant_status_response_dict = update_applicant_status_response_instance.to_dict()
# create an instance of UpdateApplicantStatusResponse from a dict
update_applicant_status_response_from_dict = UpdateApplicantStatusResponse.from_dict(update_applicant_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


