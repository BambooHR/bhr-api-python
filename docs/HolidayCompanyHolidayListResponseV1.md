# HolidayCompanyHolidayListResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HolidayCompanyHolidayV1]**](HolidayCompanyHolidayV1.md) | Collection of company holidays | [optional] 
**meta** | [**HolidayCompanyHolidayListResponseV1Meta**](HolidayCompanyHolidayListResponseV1Meta.md) |  | [optional] 
**links** | [**HolidayCompanyHolidayListResponseV1Links**](HolidayCompanyHolidayListResponseV1Links.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.holiday_company_holiday_list_response_v1 import HolidayCompanyHolidayListResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayCompanyHolidayListResponseV1 from a JSON string
holiday_company_holiday_list_response_v1_instance = HolidayCompanyHolidayListResponseV1.from_json(json)
# print the JSON string representation of the object
print(HolidayCompanyHolidayListResponseV1.to_json())

# convert the object into a dict
holiday_company_holiday_list_response_v1_dict = holiday_company_holiday_list_response_v1_instance.to_dict()
# create an instance of HolidayCompanyHolidayListResponseV1 from a dict
holiday_company_holiday_list_response_v1_from_dict = HolidayCompanyHolidayListResponseV1.from_dict(holiday_company_holiday_list_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


