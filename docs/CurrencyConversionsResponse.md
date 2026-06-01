# CurrencyConversionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_currency** | **str** | ISO 4217 base currency code | [optional] 
**last_updated** | **datetime** | ISO 8601 UTC timestamp of the last rate update | [optional] 
**next_update** | **datetime** | ISO 8601 UTC timestamp of the next scheduled rate update | [optional] 
**rates** | **Dict[str, Optional[float]]** | Map of ISO 4217 currency codes to numeric conversion rates relative to the base currency | [optional] 

## Example

```python
from bamboohr_sdk.models.currency_conversions_response import CurrencyConversionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyConversionsResponse from a JSON string
currency_conversions_response_instance = CurrencyConversionsResponse.from_json(json)
# print the JSON string representation of the object
print(CurrencyConversionsResponse.to_json())

# convert the object into a dict
currency_conversions_response_dict = currency_conversions_response_instance.to_dict()
# create an instance of CurrencyConversionsResponse from a dict
currency_conversions_response_from_dict = CurrencyConversionsResponse.from_dict(currency_conversions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


