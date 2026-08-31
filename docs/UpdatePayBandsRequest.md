# UpdatePayBandsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_band_type** | **str** | Selects how band values are interpreted. &#x60;percentRange&#x60; derives &#x60;min&#x60;/&#x60;max&#x60; from &#x60;mid&#x60; and &#x60;percentageRange&#x60;; &#x60;minMidMax&#x60; stores the supplied &#x60;min&#x60;/&#x60;mid&#x60;/&#x60;max&#x60; and clears &#x60;percentageRange&#x60;. Defaults to &#x60;minMidMax&#x60; when omitted. | [optional] 
**pay_bands** | [**List[PayGradesAndBandsUpdatePayBandItem]**](PayGradesAndBandsUpdatePayBandItem.md) | Pay band values to apply, one entry per level. Each entry requires the level ID; &#x60;min&#x60;, &#x60;mid&#x60;, &#x60;max&#x60;, and &#x60;percentageRange&#x60; are the raw numeric values (not the object form returned by Get Pay Bands). | 

## Example

```python
from bamboohr_sdk.models.update_pay_bands_request import UpdatePayBandsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePayBandsRequest from a JSON string
update_pay_bands_request_instance = UpdatePayBandsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePayBandsRequest.to_json())

# convert the object into a dict
update_pay_bands_request_dict = update_pay_bands_request_instance.to_dict()
# create an instance of UpdatePayBandsRequest from a dict
update_pay_bands_request_from_dict = UpdatePayBandsRequest.from_dict(update_pay_bands_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


