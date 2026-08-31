# GlobalHolidayGlobalHolidayV1

A read-only entry in the global holiday catalog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The catalog entry UUID. Use it to seed a company holiday from this catalog entry. | [optional] [readonly] 
**name** | **str** | The holiday name | [optional] 
**type** | **str** | The holiday type | [optional] 
**start_date** | **date** | The start date of the holiday | [optional] 
**end_date** | **date** |  | [optional] 
**country_code** | **str** | ISO 3166-1 alpha-2 country code | [optional] 
**source** | **str** | The upstream catalog source | [optional] 

## Example

```python
from bamboohr_sdk.models.global_holiday_global_holiday_v1 import GlobalHolidayGlobalHolidayV1

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalHolidayGlobalHolidayV1 from a JSON string
global_holiday_global_holiday_v1_instance = GlobalHolidayGlobalHolidayV1.from_json(json)
# print the JSON string representation of the object
print(GlobalHolidayGlobalHolidayV1.to_json())

# convert the object into a dict
global_holiday_global_holiday_v1_dict = global_holiday_global_holiday_v1_instance.to_dict()
# create an instance of GlobalHolidayGlobalHolidayV1 from a dict
global_holiday_global_holiday_v1_from_dict = GlobalHolidayGlobalHolidayV1.from_dict(global_holiday_global_holiday_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


