# PayGradesAndBandsPublishedGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** | Compensation level group identifier. | [optional] 
**group_name** | **str** |  | [optional] 
**levels** | [**List[PayGradesAndBandsPublishedLevel]**](PayGradesAndBandsPublishedLevel.md) | Published compensation levels in this group. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_published_group import PayGradesAndBandsPublishedGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsPublishedGroup from a JSON string
pay_grades_and_bands_published_group_instance = PayGradesAndBandsPublishedGroup.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsPublishedGroup.to_json())

# convert the object into a dict
pay_grades_and_bands_published_group_dict = pay_grades_and_bands_published_group_instance.to_dict()
# create an instance of PayGradesAndBandsPublishedGroup from a dict
pay_grades_and_bands_published_group_from_dict = PayGradesAndBandsPublishedGroup.from_dict(pay_grades_and_bands_published_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


