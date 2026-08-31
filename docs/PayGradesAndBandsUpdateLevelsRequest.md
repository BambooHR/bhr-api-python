# PayGradesAndBandsUpdateLevelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[PayGradesAndBandsUpdateLevelsGroup]**](PayGradesAndBandsUpdateLevelsGroup.md) | Compensation level groups to create or update. Groups not included in the request are left unchanged. | 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_update_levels_request import PayGradesAndBandsUpdateLevelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsUpdateLevelsRequest from a JSON string
pay_grades_and_bands_update_levels_request_instance = PayGradesAndBandsUpdateLevelsRequest.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsUpdateLevelsRequest.to_json())

# convert the object into a dict
pay_grades_and_bands_update_levels_request_dict = pay_grades_and_bands_update_levels_request_instance.to_dict()
# create an instance of PayGradesAndBandsUpdateLevelsRequest from a dict
pay_grades_and_bands_update_levels_request_from_dict = PayGradesAndBandsUpdateLevelsRequest.from_dict(pay_grades_and_bands_update_levels_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


