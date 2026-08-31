# HolidayCompanyHolidayV1

A company holiday

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the holiday | [optional] [readonly] 
**name** | **str** | The name of the holiday | [optional] 
**start_date** | **date** | The start date of the holiday | [optional] 
**end_date** | **date** |  | [optional] 
**is_public** | **bool** | Whether the holiday is visible to all employees on calendars, independent of audience | [optional] 
**country_codes** | **List[str]** | Country filter as ISO 3166-1 alpha-2 codes. Empty means no country filter. | [optional] 
**audience** | [**HolidayCompanyHolidayAudienceV1**](HolidayCompanyHolidayAudienceV1.md) | Who the holiday applies to | [optional] 
**holiday_pay** | **object** |  | [optional] 
**global_holiday_uuid** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** | ISO 8601 timestamp when the holiday was created | [optional] [readonly] 
**updated_at** | **datetime** | ISO 8601 timestamp when the holiday was last updated | [optional] [readonly] 
**deleted_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.holiday_company_holiday_v1 import HolidayCompanyHolidayV1

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayCompanyHolidayV1 from a JSON string
holiday_company_holiday_v1_instance = HolidayCompanyHolidayV1.from_json(json)
# print the JSON string representation of the object
print(HolidayCompanyHolidayV1.to_json())

# convert the object into a dict
holiday_company_holiday_v1_dict = holiday_company_holiday_v1_instance.to_dict()
# create an instance of HolidayCompanyHolidayV1 from a dict
holiday_company_holiday_v1_from_dict = HolidayCompanyHolidayV1.from_dict(holiday_company_holiday_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


