# HiringLeadsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hiring_lead** | [**HiringLead**](HiringLead.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.hiring_leads_list import HiringLeadsList

# TODO update the JSON string below
json = "{}"
# create an instance of HiringLeadsList from a JSON string
hiring_leads_list_instance = HiringLeadsList.from_json(json)
# print the JSON string representation of the object
print(HiringLeadsList.to_json())

# convert the object into a dict
hiring_leads_list_dict = hiring_leads_list_instance.to_dict()
# create an instance of HiringLeadsList from a dict
hiring_leads_list_from_dict = HiringLeadsList.from_dict(hiring_leads_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


