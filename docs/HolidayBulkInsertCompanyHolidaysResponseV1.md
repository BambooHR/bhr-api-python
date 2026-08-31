# HolidayBulkInsertCompanyHolidaysResponseV1

Result envelope for a synchronous bulk-insert of company holidays.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Overall batch outcome | [optional] 
**operation** | **str** | Operation type for this bulk request | [optional] 
**total_requested** | **int** | Total number of records in the request | [optional] 
**total_processed** | **int** | Total number of records created successfully | [optional] 
**failed** | **int** | Total number of records that failed | [optional] 
**errors** | [**List[HolidayBulkInsertCompanyHolidayErrorV1]**](HolidayBulkInsertCompanyHolidayErrorV1.md) | Per-record problem-details style errors | [optional] 
**records** | [**List[HolidayBulkInsertCompanyHolidayRecordV1]**](HolidayBulkInsertCompanyHolidayRecordV1.md) | Per-record success results, in request order | [optional] 

## Example

```python
from bamboohr_sdk.models.holiday_bulk_insert_company_holidays_response_v1 import HolidayBulkInsertCompanyHolidaysResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayBulkInsertCompanyHolidaysResponseV1 from a JSON string
holiday_bulk_insert_company_holidays_response_v1_instance = HolidayBulkInsertCompanyHolidaysResponseV1.from_json(json)
# print the JSON string representation of the object
print(HolidayBulkInsertCompanyHolidaysResponseV1.to_json())

# convert the object into a dict
holiday_bulk_insert_company_holidays_response_v1_dict = holiday_bulk_insert_company_holidays_response_v1_instance.to_dict()
# create an instance of HolidayBulkInsertCompanyHolidaysResponseV1 from a dict
holiday_bulk_insert_company_holidays_response_v1_from_dict = HolidayBulkInsertCompanyHolidaysResponseV1.from_dict(holiday_bulk_insert_company_holidays_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


