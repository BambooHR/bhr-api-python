# PayGradesAndBandsDeleteLevelResponse

Returned when a single level was deleted: the updated draft groups-and-levels hierarchy with validation state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[PayGradesAndBandsDeleteHierarchyGroup]**](PayGradesAndBandsDeleteHierarchyGroup.md) | Compensation level groups after the deletion. Empty when none remain. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_delete_level_response import PayGradesAndBandsDeleteLevelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsDeleteLevelResponse from a JSON string
pay_grades_and_bands_delete_level_response_instance = PayGradesAndBandsDeleteLevelResponse.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsDeleteLevelResponse.to_json())

# convert the object into a dict
pay_grades_and_bands_delete_level_response_dict = pay_grades_and_bands_delete_level_response_instance.to_dict()
# create an instance of PayGradesAndBandsDeleteLevelResponse from a dict
pay_grades_and_bands_delete_level_response_from_dict = PayGradesAndBandsDeleteLevelResponse.from_dict(pay_grades_and_bands_delete_level_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


