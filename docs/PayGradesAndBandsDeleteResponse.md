# PayGradesAndBandsDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**groups** | [**List[PayGradesAndBandsDeleteHierarchyGroup]**](PayGradesAndBandsDeleteHierarchyGroup.md) | Compensation level groups after the deletion. Empty when none remain. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_delete_response import PayGradesAndBandsDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsDeleteResponse from a JSON string
pay_grades_and_bands_delete_response_instance = PayGradesAndBandsDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsDeleteResponse.to_json())

# convert the object into a dict
pay_grades_and_bands_delete_response_dict = pay_grades_and_bands_delete_response_instance.to_dict()
# create an instance of PayGradesAndBandsDeleteResponse from a dict
pay_grades_and_bands_delete_response_from_dict = PayGradesAndBandsDeleteResponse.from_dict(pay_grades_and_bands_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


