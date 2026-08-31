# HolidayBulkInsertCompanyHolidaysFailureResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Problem type URI identifying the error category | [optional] 
**title** | **str** | Short, human-readable summary of the problem type | [optional] 
**status** | **str** | Overall batch outcome | [optional] 
**detail** | **str** | Detailed, human-readable explanation specific to this occurrence of the problem | [optional] 
**instance** | **str** | URI reference that identifies the specific occurrence of the problem | [optional] 
**code** | **str** | Application-specific error code | [optional] 
**fields** | **Dict[str, str]** |  | [optional] 
**operation** | **str** | Operation type for this bulk request | [optional] 
**total_requested** | **int** | Total number of records in the request | [optional] 
**total_processed** | **int** | Total number of records created successfully | [optional] 
**failed** | **int** | Total number of records that failed | [optional] 
**errors** | [**List[HolidayBulkInsertCompanyHolidayErrorV1]**](HolidayBulkInsertCompanyHolidayErrorV1.md) | Per-record problem-details style errors | [optional] 
**records** | [**List[HolidayBulkInsertCompanyHolidayRecordV1]**](HolidayBulkInsertCompanyHolidayRecordV1.md) | Per-record success results, in request order | [optional] 

## Example

```python
from bamboohr_sdk.models.holiday_bulk_insert_company_holidays_failure_response_v1 import HolidayBulkInsertCompanyHolidaysFailureResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayBulkInsertCompanyHolidaysFailureResponseV1 from a JSON string
holiday_bulk_insert_company_holidays_failure_response_v1_instance = HolidayBulkInsertCompanyHolidaysFailureResponseV1.from_json(json)
# print the JSON string representation of the object
print(HolidayBulkInsertCompanyHolidaysFailureResponseV1.to_json())

# convert the object into a dict
holiday_bulk_insert_company_holidays_failure_response_v1_dict = holiday_bulk_insert_company_holidays_failure_response_v1_instance.to_dict()
# create an instance of HolidayBulkInsertCompanyHolidaysFailureResponseV1 from a dict
holiday_bulk_insert_company_holidays_failure_response_v1_from_dict = HolidayBulkInsertCompanyHolidaysFailureResponseV1.from_dict(holiday_bulk_insert_company_holidays_failure_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


