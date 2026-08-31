# HolidayBulkInsertCompanyHolidayRecordV1

A successfully created record within a bulk-insert response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the created company holiday | [optional] 
**status** | **str** | Per-record operation outcome | [optional] 
**http_status** | **int** | HTTP status code representing the per-record result | [optional] 
**record** | [**HolidayCompanyHolidayV1**](HolidayCompanyHolidayV1.md) | The full created company holiday. Present only when returnRecords&#x3D;true. | [optional] 

## Example

```python
from bamboohr_sdk.models.holiday_bulk_insert_company_holiday_record_v1 import HolidayBulkInsertCompanyHolidayRecordV1

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayBulkInsertCompanyHolidayRecordV1 from a JSON string
holiday_bulk_insert_company_holiday_record_v1_instance = HolidayBulkInsertCompanyHolidayRecordV1.from_json(json)
# print the JSON string representation of the object
print(HolidayBulkInsertCompanyHolidayRecordV1.to_json())

# convert the object into a dict
holiday_bulk_insert_company_holiday_record_v1_dict = holiday_bulk_insert_company_holiday_record_v1_instance.to_dict()
# create an instance of HolidayBulkInsertCompanyHolidayRecordV1 from a dict
holiday_bulk_insert_company_holiday_record_v1_from_dict = HolidayBulkInsertCompanyHolidayRecordV1.from_dict(holiday_bulk_insert_company_holiday_record_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


