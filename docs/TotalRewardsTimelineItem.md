# TotalRewardsTimelineItem

Schema for total rewards timeline item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**subvalue** | **str** |  | [optional] 
**label** | [**TotalRewardsTimelineItemLabel**](TotalRewardsTimelineItemLabel.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_timeline_item import TotalRewardsTimelineItem

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsTimelineItem from a JSON string
total_rewards_timeline_item_instance = TotalRewardsTimelineItem.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsTimelineItem.to_json())

# convert the object into a dict
total_rewards_timeline_item_dict = total_rewards_timeline_item_instance.to_dict()
# create an instance of TotalRewardsTimelineItem from a dict
total_rewards_timeline_item_from_dict = TotalRewardsTimelineItem.from_dict(total_rewards_timeline_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


