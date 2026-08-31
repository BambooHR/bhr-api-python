# HolidayBulkInsertCompanyHolidayErrorV1

A problem-details style error for a single record within a bulk-insert request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_index** | **int** | Zero-based index of the failed record in the request body array | [optional] 
**type** | **str** | Problem type URI identifying the error category | [optional] 
**title** | **str** | Short, human-readable summary of the problem type | [optional] 
**status** | **int** | HTTP status code the record would have received from the single-create endpoint | [optional] 
**detail** | **str** | Human-readable explanation specific to this record failure | [optional] 
**code** | **str** | Application-specific error code | [optional] 

## Example

```python
from bamboohr_sdk.models.holiday_bulk_insert_company_holiday_error_v1 import HolidayBulkInsertCompanyHolidayErrorV1

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayBulkInsertCompanyHolidayErrorV1 from a JSON string
holiday_bulk_insert_company_holiday_error_v1_instance = HolidayBulkInsertCompanyHolidayErrorV1.from_json(json)
# print the JSON string representation of the object
print(HolidayBulkInsertCompanyHolidayErrorV1.to_json())

# convert the object into a dict
holiday_bulk_insert_company_holiday_error_v1_dict = holiday_bulk_insert_company_holiday_error_v1_instance.to_dict()
# create an instance of HolidayBulkInsertCompanyHolidayErrorV1 from a dict
holiday_bulk_insert_company_holiday_error_v1_from_dict = HolidayBulkInsertCompanyHolidayErrorV1.from_dict(holiday_bulk_insert_company_holiday_error_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


