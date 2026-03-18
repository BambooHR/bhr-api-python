# HiringLead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | The employee ID to use as the &#x60;hiringLead&#x60; value in the Create Job Opening request | [optional] 
**preferred_full_name** | **str** | The employee&#39;s preferred full name | [optional] 

## Example

```python
from bamboohr_sdk.models.hiring_lead import HiringLead

# TODO update the JSON string below
json = "{}"
# create an instance of HiringLead from a JSON string
hiring_lead_instance = HiringLead.from_json(json)
# print the JSON string representation of the object
print(HiringLead.to_json())

# convert the object into a dict
hiring_lead_dict = hiring_lead_instance.to_dict()
# create an instance of HiringLead from a dict
hiring_lead_from_dict = HiringLead.from_dict(hiring_lead_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


