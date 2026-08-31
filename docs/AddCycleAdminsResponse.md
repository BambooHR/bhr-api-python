# AddCycleAdminsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added** | [**List[AddCycleAdminsResponseAddedInner]**](AddCycleAdminsResponseAddedInner.md) |  | [optional] 
**skipped** | [**List[AddCycleAdminsResponseSkippedInner]**](AddCycleAdminsResponseSkippedInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.add_cycle_admins_response import AddCycleAdminsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddCycleAdminsResponse from a JSON string
add_cycle_admins_response_instance = AddCycleAdminsResponse.from_json(json)
# print the JSON string representation of the object
print(AddCycleAdminsResponse.to_json())

# convert the object into a dict
add_cycle_admins_response_dict = add_cycle_admins_response_instance.to_dict()
# create an instance of AddCycleAdminsResponse from a dict
add_cycle_admins_response_from_dict = AddCycleAdminsResponse.from_dict(add_cycle_admins_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


