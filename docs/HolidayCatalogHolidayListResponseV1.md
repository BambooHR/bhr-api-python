# HolidayCatalogHolidayListResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GlobalHolidayGlobalHolidayV1]**](GlobalHolidayGlobalHolidayV1.md) | Catalog holidays for the current page | [optional] 
**links** | [**HolidayCatalogHolidayListResponseV1Links**](HolidayCatalogHolidayListResponseV1Links.md) |  | [optional] 
**meta** | [**PaginationMetaData**](PaginationMetaData.md) | Pagination metadata | [optional] 

## Example

```python
from bamboohr_sdk.models.holiday_catalog_holiday_list_response_v1 import HolidayCatalogHolidayListResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayCatalogHolidayListResponseV1 from a JSON string
holiday_catalog_holiday_list_response_v1_instance = HolidayCatalogHolidayListResponseV1.from_json(json)
# print the JSON string representation of the object
print(HolidayCatalogHolidayListResponseV1.to_json())

# convert the object into a dict
holiday_catalog_holiday_list_response_v1_dict = holiday_catalog_holiday_list_response_v1_instance.to_dict()
# create an instance of HolidayCatalogHolidayListResponseV1 from a dict
holiday_catalog_holiday_list_response_v1_from_dict = HolidayCatalogHolidayListResponseV1.from_dict(holiday_catalog_holiday_list_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


