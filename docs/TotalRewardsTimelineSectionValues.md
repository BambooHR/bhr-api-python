# TotalRewardsTimelineSectionValues

Schema for total rewards overview section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comp_summary** | [**TotalRewardsCompSummaryValues**](TotalRewardsCompSummaryValues.md) | Compensation summary | [optional] 
**timeline_data** | [**List[TotalRewardsTimelineItem]**](TotalRewardsTimelineItem.md) | Timeline data | [optional] 
**placeholder_text** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_timeline_section_values import TotalRewardsTimelineSectionValues

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsTimelineSectionValues from a JSON string
total_rewards_timeline_section_values_instance = TotalRewardsTimelineSectionValues.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsTimelineSectionValues.to_json())

# convert the object into a dict
total_rewards_timeline_section_values_dict = total_rewards_timeline_section_values_instance.to_dict()
# create an instance of TotalRewardsTimelineSectionValues from a dict
total_rewards_timeline_section_values_from_dict = TotalRewardsTimelineSectionValues.from_dict(total_rewards_timeline_section_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


