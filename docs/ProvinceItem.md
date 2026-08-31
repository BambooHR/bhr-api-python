# ProvinceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | State/province ID | [optional] 
**country_id** | **str** | ID of the country this state/province belongs to | [optional] 
**label** | **str** | State/province abbreviation (e.g. \&quot;UT\&quot;) | [optional] 
**iso** | **str** | ISO 3166-2 code (e.g. \&quot;US-UT\&quot;) | [optional] 
**name** | **str** | Full name of the state/province | [optional] 

## Example

```python
from bamboohr_sdk.models.province_item import ProvinceItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProvinceItem from a JSON string
province_item_instance = ProvinceItem.from_json(json)
# print the JSON string representation of the object
print(ProvinceItem.to_json())

# convert the object into a dict
province_item_dict = province_item_instance.to_dict()
# create an instance of ProvinceItem from a dict
province_item_from_dict = ProvinceItem.from_dict(province_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


