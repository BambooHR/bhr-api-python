# HolidayUpdateCompanyHolidayRequestV1

JSON Merge Patch payload to update a company holiday. Only the fields present in the document are changed; countryCodes, audience, and holidayPay replace their stored blocks wholesale when supplied. globalHolidayUuid is read-only and rejected if present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the holiday. 1-255 characters. | [optional] 
**start_date** | **date** | The start date of the holiday. | [optional] 
**end_date** | **date** |  | [optional] 
**is_public** | **bool** | Whether the holiday is visible to all employees on calendars, independent of audience. | [optional] 
**country_codes** | **List[str]** | Country filter as ISO 3166-1 alpha-2 codes. Replaces the stored country filter wholesale; an empty array removes the filter. | [optional] 
**audience** | [**HolidayCompanyHolidayAudienceV1**](HolidayCompanyHolidayAudienceV1.md) | Who the holiday applies to. Replaces the stored audience block wholesale; sub-rows that no longer apply to the new mode are cleared. | [optional] 
**holiday_pay** | **object** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.holiday_update_company_holiday_request_v1 import HolidayUpdateCompanyHolidayRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayUpdateCompanyHolidayRequestV1 from a JSON string
holiday_update_company_holiday_request_v1_instance = HolidayUpdateCompanyHolidayRequestV1.from_json(json)
# print the JSON string representation of the object
print(HolidayUpdateCompanyHolidayRequestV1.to_json())

# convert the object into a dict
holiday_update_company_holiday_request_v1_dict = holiday_update_company_holiday_request_v1_instance.to_dict()
# create an instance of HolidayUpdateCompanyHolidayRequestV1 from a dict
holiday_update_company_holiday_request_v1_from_dict = HolidayUpdateCompanyHolidayRequestV1.from_dict(holiday_update_company_holiday_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


