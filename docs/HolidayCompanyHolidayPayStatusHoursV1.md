# HolidayCompanyHolidayPayStatusHoursV1

Paid-hour override for one employment status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employment_status_list_value_id** | **int** | List-value ID from the company&#39;s Employment Status list | [optional] 
**hours** | **str** | Paid hours for the employment status | [optional] 

## Example

```python
from bamboohr_sdk.models.holiday_company_holiday_pay_status_hours_v1 import HolidayCompanyHolidayPayStatusHoursV1

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayCompanyHolidayPayStatusHoursV1 from a JSON string
holiday_company_holiday_pay_status_hours_v1_instance = HolidayCompanyHolidayPayStatusHoursV1.from_json(json)
# print the JSON string representation of the object
print(HolidayCompanyHolidayPayStatusHoursV1.to_json())

# convert the object into a dict
holiday_company_holiday_pay_status_hours_v1_dict = holiday_company_holiday_pay_status_hours_v1_instance.to_dict()
# create an instance of HolidayCompanyHolidayPayStatusHoursV1 from a dict
holiday_company_holiday_pay_status_hours_v1_from_dict = HolidayCompanyHolidayPayStatusHoursV1.from_dict(holiday_company_holiday_pay_status_hours_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


