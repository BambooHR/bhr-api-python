# DetailsAndCurrencyRequestDataObject

Request data for updating compensation planning cycle details and currency settings. Pre-condition: User must have permission to update cycle. Post-condition: Cycle configuration is updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the cycle to update | [optional] 
**cycle_name** | **str** | Name of the cycle to update | [optional] 
**cycle_currency** | **str** |  | [optional] 
**cycle_window_start_ymd** | **date** | Start date of the cycle window | [optional] 
**cycle_window_end_ymd** | **date** | End date of the cycle window | [optional] 
**recommendations_due_ymd** | **date** | Date when recommendations are due | [optional] 
**approvals_due_ymd** | **date** | Date when approvals are due | [optional] 
**cycle_effective_date** | **date** | Effective date of the cycle | [optional] 
**salary_included** | **bool** | Whether salary is included in this cycle | [optional] 
**bonus_included** | **bool** | Whether bonus is included in this cycle | [optional] 
**equity_included** | **bool** | Whether equity is included in this cycle | [optional] 
**cycle_currency_conversion_rates** | [**List[ConversionRateDataObject]**](ConversionRateDataObject.md) | Currency conversion rates | [optional] 
**paycheck_date_ymd** | **date** | Date of first paycheck with new compensation updates | [optional] 

## Example

```python
from bamboohr_sdk.models.details_and_currency_request_data_object import DetailsAndCurrencyRequestDataObject

# TODO update the JSON string below
json = "{}"
# create an instance of DetailsAndCurrencyRequestDataObject from a JSON string
details_and_currency_request_data_object_instance = DetailsAndCurrencyRequestDataObject.from_json(json)
# print the JSON string representation of the object
print(DetailsAndCurrencyRequestDataObject.to_json())

# convert the object into a dict
details_and_currency_request_data_object_dict = details_and_currency_request_data_object_instance.to_dict()
# create an instance of DetailsAndCurrencyRequestDataObject from a dict
details_and_currency_request_data_object_from_dict = DetailsAndCurrencyRequestDataObject.from_dict(details_and_currency_request_data_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


