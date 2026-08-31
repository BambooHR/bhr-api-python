# CompensationEquitySettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_type** | **str** |  | [optional] 
**company_valuation** | [**CompensationEquitySettingsResponseCompanyValuation**](CompensationEquitySettingsResponseCompanyValuation.md) |  | [optional] 
**outstanding_shares** | [**CompensationEquitySettingsResponseOutstandingShares**](CompensationEquitySettingsResponseOutstandingShares.md) |  | [optional] 
**price_per_share** | [**CompensationEquitySettingsResponsePricePerShare**](CompensationEquitySettingsResponsePricePerShare.md) |  | [optional] 
**currency_code** | **str** |  | [optional] 
**slider_min** | [**CompensationEquitySettingsResponseSliderMin**](CompensationEquitySettingsResponseSliderMin.md) |  | [optional] 
**slider_max** | [**CompensationEquitySettingsResponseSliderMin**](CompensationEquitySettingsResponseSliderMin.md) |  | [optional] 
**vesting_conditions** | [**CompensationEquitySettingsResponseVestingConditions**](CompensationEquitySettingsResponseVestingConditions.md) |  | [optional] 
**disclaimers** | [**CompensationEquitySettingsResponseDisclaimers**](CompensationEquitySettingsResponseDisclaimers.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_equity_settings_response import CompensationEquitySettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationEquitySettingsResponse from a JSON string
compensation_equity_settings_response_instance = CompensationEquitySettingsResponse.from_json(json)
# print the JSON string representation of the object
print(CompensationEquitySettingsResponse.to_json())

# convert the object into a dict
compensation_equity_settings_response_dict = compensation_equity_settings_response_instance.to_dict()
# create an instance of CompensationEquitySettingsResponse from a dict
compensation_equity_settings_response_from_dict = CompensationEquitySettingsResponse.from_dict(compensation_equity_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


