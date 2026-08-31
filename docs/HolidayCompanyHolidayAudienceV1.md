# HolidayCompanyHolidayAudienceV1

Defines which employees a company holiday applies to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | How the holiday audience is determined | [optional] 
**filter_list_value_ids** | **List[int]** | List-value IDs that filter the audience. Only populated in FILTERED mode. | [optional] 
**specific_employee_ids** | **List[int]** | Employee IDs that define the audience. Only populated in SPECIFIC_EMPLOYEES mode. | [optional] 
**additional_employee_ids** | **List[int]** | Employee IDs explicitly included on top of the mode&#39;s default audience. | [optional] 
**exempt_employee_ids** | **List[int]** | Employee IDs explicitly excluded from the mode&#39;s default audience. | [optional] 

## Example

```python
from bamboohr_sdk.models.holiday_company_holiday_audience_v1 import HolidayCompanyHolidayAudienceV1

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayCompanyHolidayAudienceV1 from a JSON string
holiday_company_holiday_audience_v1_instance = HolidayCompanyHolidayAudienceV1.from_json(json)
# print the JSON string representation of the object
print(HolidayCompanyHolidayAudienceV1.to_json())

# convert the object into a dict
holiday_company_holiday_audience_v1_dict = holiday_company_holiday_audience_v1_instance.to_dict()
# create an instance of HolidayCompanyHolidayAudienceV1 from a dict
holiday_company_holiday_audience_v1_from_dict = HolidayCompanyHolidayAudienceV1.from_dict(holiday_company_holiday_audience_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


