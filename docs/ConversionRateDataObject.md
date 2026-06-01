# ConversionRateDataObject

Represents a currency conversion rate from a source to a target currency.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_name** | **str** | The full name of the target currency. | [optional] 
**currency_code** | **str** | The code of the target currency (e.g. USD, EUR, JPY). | [optional] 
**conversion_rate** | **float** | The numeric conversion rate to the target currency. | [optional] 

## Example

```python
from bamboohr_sdk.models.conversion_rate_data_object import ConversionRateDataObject

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionRateDataObject from a JSON string
conversion_rate_data_object_instance = ConversionRateDataObject.from_json(json)
# print the JSON string representation of the object
print(ConversionRateDataObject.to_json())

# convert the object into a dict
conversion_rate_data_object_dict = conversion_rate_data_object_instance.to_dict()
# create an instance of ConversionRateDataObject from a dict
conversion_rate_data_object_from_dict = ConversionRateDataObject.from_dict(conversion_rate_data_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


