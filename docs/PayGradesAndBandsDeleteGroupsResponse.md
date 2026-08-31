# PayGradesAndBandsDeleteGroupsResponse

Returned when a group status was deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_delete_groups_response import PayGradesAndBandsDeleteGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsDeleteGroupsResponse from a JSON string
pay_grades_and_bands_delete_groups_response_instance = PayGradesAndBandsDeleteGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsDeleteGroupsResponse.to_json())

# convert the object into a dict
pay_grades_and_bands_delete_groups_response_dict = pay_grades_and_bands_delete_groups_response_instance.to_dict()
# create an instance of PayGradesAndBandsDeleteGroupsResponse from a dict
pay_grades_and_bands_delete_groups_response_from_dict = PayGradesAndBandsDeleteGroupsResponse.from_dict(pay_grades_and_bands_delete_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


