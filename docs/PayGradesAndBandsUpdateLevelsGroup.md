# PayGradesAndBandsUpdateLevelsGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** |  | [optional] 
**group_name** | **str** |  | [optional] 
**levels** | [**List[PayGradesAndBandsUpdateLevel]**](PayGradesAndBandsUpdateLevel.md) | Levels within the group to create or update. Levels not included are left unchanged. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_update_levels_group import PayGradesAndBandsUpdateLevelsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsUpdateLevelsGroup from a JSON string
pay_grades_and_bands_update_levels_group_instance = PayGradesAndBandsUpdateLevelsGroup.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsUpdateLevelsGroup.to_json())

# convert the object into a dict
pay_grades_and_bands_update_levels_group_dict = pay_grades_and_bands_update_levels_group_instance.to_dict()
# create an instance of PayGradesAndBandsUpdateLevelsGroup from a dict
pay_grades_and_bands_update_levels_group_from_dict = PayGradesAndBandsUpdateLevelsGroup.from_dict(pay_grades_and_bands_update_levels_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


