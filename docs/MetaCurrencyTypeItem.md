# MetaCurrencyTypeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal currency id | [optional] 
**code** | **str** | ISO 4217-style currency code (e.g. USD, EUR) | [optional] 
**name** | **str** | Human-readable currency name (HTML entities decoded in the response) | [optional] 
**symbol** | **str** | Display symbol for the currency in UI | [optional] 
**symbol_position** | **int** | Placement of the symbol relative to the amount: 0 &#x3D; prefix, 1 &#x3D; postfix (this is a numeric code, not a string label). | [optional] 

## Example

```python
from bamboohr_sdk.models.meta_currency_type_item import MetaCurrencyTypeItem

# TODO update the JSON string below
json = "{}"
# create an instance of MetaCurrencyTypeItem from a JSON string
meta_currency_type_item_instance = MetaCurrencyTypeItem.from_json(json)
# print the JSON string representation of the object
print(MetaCurrencyTypeItem.to_json())

# convert the object into a dict
meta_currency_type_item_dict = meta_currency_type_item_instance.to_dict()
# create an instance of MetaCurrencyTypeItem from a dict
meta_currency_type_item_from_dict = MetaCurrencyTypeItem.from_dict(meta_currency_type_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


