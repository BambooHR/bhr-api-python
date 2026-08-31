# HolidayCreateCompanyHolidayRequestV1

Payload to create a company holiday. May be fully-specified or reference a global catalog entry via globalHolidayUuid. name and startDate are required unless seeded by globalHolidayUuid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_holiday_uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**is_public** | **bool** | Whether the holiday is visible to all employees on calendars, independent of audience. Defaults to true. | [optional] [default to True]
**country_codes** | **List[str]** |  | [optional] 
**audience** | [**HolidayCompanyHolidayAudienceV1**](HolidayCompanyHolidayAudienceV1.md) | Who the holiday applies to | 
**holiday_pay** | **object** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.holiday_create_company_holiday_request_v1 import HolidayCreateCompanyHolidayRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayCreateCompanyHolidayRequestV1 from a JSON string
holiday_create_company_holiday_request_v1_instance = HolidayCreateCompanyHolidayRequestV1.from_json(json)
# print the JSON string representation of the object
print(HolidayCreateCompanyHolidayRequestV1.to_json())

# convert the object into a dict
holiday_create_company_holiday_request_v1_dict = holiday_create_company_holiday_request_v1_instance.to_dict()
# create an instance of HolidayCreateCompanyHolidayRequestV1 from a dict
holiday_create_company_holiday_request_v1_from_dict = HolidayCreateCompanyHolidayRequestV1.from_dict(holiday_create_company_holiday_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


