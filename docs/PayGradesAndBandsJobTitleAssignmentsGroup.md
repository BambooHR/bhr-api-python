# PayGradesAndBandsJobTitleAssignmentsGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** |  | [optional] 
**group_name** | **str** |  | [optional] 
**levels** | [**List[PayGradesAndBandsJobTitleAssignmentsLevel]**](PayGradesAndBandsJobTitleAssignmentsLevel.md) | Compensation levels in this group. | [optional] 
**errors** | **List[str]** | Validation errors for this group. | [optional] 
**warnings** | **List[str]** | Validation warnings for this group. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_job_title_assignments_group import PayGradesAndBandsJobTitleAssignmentsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsJobTitleAssignmentsGroup from a JSON string
pay_grades_and_bands_job_title_assignments_group_instance = PayGradesAndBandsJobTitleAssignmentsGroup.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsJobTitleAssignmentsGroup.to_json())

# convert the object into a dict
pay_grades_and_bands_job_title_assignments_group_dict = pay_grades_and_bands_job_title_assignments_group_instance.to_dict()
# create an instance of PayGradesAndBandsJobTitleAssignmentsGroup from a dict
pay_grades_and_bands_job_title_assignments_group_from_dict = PayGradesAndBandsJobTitleAssignmentsGroup.from_dict(pay_grades_and_bands_job_title_assignments_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


