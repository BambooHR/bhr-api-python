# SetTotalRewardsCustomDisclaimerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_disclaimer** | **str** | Custom disclaimer text. | 

## Example

```python
from bamboohr_sdk.models.set_total_rewards_custom_disclaimer_request import SetTotalRewardsCustomDisclaimerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetTotalRewardsCustomDisclaimerRequest from a JSON string
set_total_rewards_custom_disclaimer_request_instance = SetTotalRewardsCustomDisclaimerRequest.from_json(json)
# print the JSON string representation of the object
print(SetTotalRewardsCustomDisclaimerRequest.to_json())

# convert the object into a dict
set_total_rewards_custom_disclaimer_request_dict = set_total_rewards_custom_disclaimer_request_instance.to_dict()
# create an instance of SetTotalRewardsCustomDisclaimerRequest from a dict
set_total_rewards_custom_disclaimer_request_from_dict = SetTotalRewardsCustomDisclaimerRequest.from_dict(set_total_rewards_custom_disclaimer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


