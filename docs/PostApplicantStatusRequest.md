# PostApplicantStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Associates a status id with an application. | 

## Example

```python
from bamboohr_sdk.models.post_applicant_status_request import PostApplicantStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostApplicantStatusRequest from a JSON string
post_applicant_status_request_instance = PostApplicantStatusRequest.from_json(json)
# print the JSON string representation of the object
print(PostApplicantStatusRequest.to_json())

# convert the object into a dict
post_applicant_status_request_dict = post_applicant_status_request_instance.to_dict()
# create an instance of PostApplicantStatusRequest from a dict
post_applicant_status_request_from_dict = PostApplicantStatusRequest.from_dict(post_applicant_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


