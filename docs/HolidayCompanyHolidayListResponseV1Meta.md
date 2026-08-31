# HolidayCompanyHolidayListResponseV1Meta

Pagination metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_size** | **int** |  | 
**total_pages** | **int** |  | 
**total_items** | **int** |  | 

## Example

```python
from bamboohr_sdk.models.holiday_company_holiday_list_response_v1_meta import HolidayCompanyHolidayListResponseV1Meta

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayCompanyHolidayListResponseV1Meta from a JSON string
holiday_company_holiday_list_response_v1_meta_instance = HolidayCompanyHolidayListResponseV1Meta.from_json(json)
# print the JSON string representation of the object
print(HolidayCompanyHolidayListResponseV1Meta.to_json())

# convert the object into a dict
holiday_company_holiday_list_response_v1_meta_dict = holiday_company_holiday_list_response_v1_meta_instance.to_dict()
# create an instance of HolidayCompanyHolidayListResponseV1Meta from a dict
holiday_company_holiday_list_response_v1_meta_from_dict = HolidayCompanyHolidayListResponseV1Meta.from_dict(holiday_company_holiday_list_response_v1_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


