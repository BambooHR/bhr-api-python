# RemoveTotalRewardsEmployeesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_ids** | **List[Optional[int]]** | List of employee IDs to remove from Total Rewards. | 

## Example

```python
from bamboohr_sdk.models.remove_total_rewards_employees_request import RemoveTotalRewardsEmployeesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveTotalRewardsEmployeesRequest from a JSON string
remove_total_rewards_employees_request_instance = RemoveTotalRewardsEmployeesRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveTotalRewardsEmployeesRequest.to_json())

# convert the object into a dict
remove_total_rewards_employees_request_dict = remove_total_rewards_employees_request_instance.to_dict()
# create an instance of RemoveTotalRewardsEmployeesRequest from a dict
remove_total_rewards_employees_request_from_dict = RemoveTotalRewardsEmployeesRequest.from_dict(remove_total_rewards_employees_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


