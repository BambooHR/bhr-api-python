# PayGradesAndBandsJobTitleAssignmentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[PayGradesAndBandsJobTitleAssignmentsGroup]**](PayGradesAndBandsJobTitleAssignmentsGroup.md) | Compensation level groups from the working configuration (the draft when one exists, otherwise the currently published configuration). Empty when none are configured. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_job_title_assignments_response import PayGradesAndBandsJobTitleAssignmentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsJobTitleAssignmentsResponse from a JSON string
pay_grades_and_bands_job_title_assignments_response_instance = PayGradesAndBandsJobTitleAssignmentsResponse.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsJobTitleAssignmentsResponse.to_json())

# convert the object into a dict
pay_grades_and_bands_job_title_assignments_response_dict = pay_grades_and_bands_job_title_assignments_response_instance.to_dict()
# create an instance of PayGradesAndBandsJobTitleAssignmentsResponse from a dict
pay_grades_and_bands_job_title_assignments_response_from_dict = PayGradesAndBandsJobTitleAssignmentsResponse.from_dict(pay_grades_and_bands_job_title_assignments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


