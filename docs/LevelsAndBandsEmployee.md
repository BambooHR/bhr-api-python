# LevelsAndBandsEmployee

Job titles employee object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Employee id | [optional] 
**name** | **str** | Employee name | [optional] 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_employee import LevelsAndBandsEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsEmployee from a JSON string
levels_and_bands_employee_instance = LevelsAndBandsEmployee.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsEmployee.to_json())

# convert the object into a dict
levels_and_bands_employee_dict = levels_and_bands_employee_instance.to_dict()
# create an instance of LevelsAndBandsEmployee from a dict
levels_and_bands_employee_from_dict = LevelsAndBandsEmployee.from_dict(levels_and_bands_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


