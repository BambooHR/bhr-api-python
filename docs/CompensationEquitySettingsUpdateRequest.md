# CompensationEquitySettingsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_type** | **str** |  | [optional] 
**company_valuation** | [**CompensationEquitySettingsResponsePricePerShare**](CompensationEquitySettingsResponsePricePerShare.md) |  | [optional] 
**outstanding_shares** | [**CompensationEquitySettingsResponseSliderMin**](CompensationEquitySettingsResponseSliderMin.md) |  | [optional] 
**price_per_share** | [**CompensationEquitySettingsResponsePricePerShare**](CompensationEquitySettingsResponsePricePerShare.md) |  | [optional] 
**currency_code** | **str** |  | [optional] 
**slider_min** | [**CompensationEquitySettingsResponseSliderMin**](CompensationEquitySettingsResponseSliderMin.md) |  | [optional] 
**slider_max** | [**CompensationEquitySettingsResponseSliderMin**](CompensationEquitySettingsResponseSliderMin.md) |  | [optional] 
**vesting_conditions** | [**CompensationEquitySettingsResponseDisclaimers**](CompensationEquitySettingsResponseDisclaimers.md) |  | [optional] 
**disclaimers** | [**CompensationEquitySettingsResponseDisclaimers**](CompensationEquitySettingsResponseDisclaimers.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_equity_settings_update_request import CompensationEquitySettingsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationEquitySettingsUpdateRequest from a JSON string
compensation_equity_settings_update_request_instance = CompensationEquitySettingsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CompensationEquitySettingsUpdateRequest.to_json())

# convert the object into a dict
compensation_equity_settings_update_request_dict = compensation_equity_settings_update_request_instance.to_dict()
# create an instance of CompensationEquitySettingsUpdateRequest from a dict
compensation_equity_settings_update_request_from_dict = CompensationEquitySettingsUpdateRequest.from_dict(compensation_equity_settings_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


