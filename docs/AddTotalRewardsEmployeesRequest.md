# AddTotalRewardsEmployeesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_ids** | **List[Optional[int]]** | List of employee IDs to add to Total Rewards. | 

## Example

```python
from bamboohr_sdk.models.add_total_rewards_employees_request import AddTotalRewardsEmployeesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTotalRewardsEmployeesRequest from a JSON string
add_total_rewards_employees_request_instance = AddTotalRewardsEmployeesRequest.from_json(json)
# print the JSON string representation of the object
print(AddTotalRewardsEmployeesRequest.to_json())

# convert the object into a dict
add_total_rewards_employees_request_dict = add_total_rewards_employees_request_instance.to_dict()
# create an instance of AddTotalRewardsEmployeesRequest from a dict
add_total_rewards_employees_request_from_dict = AddTotalRewardsEmployeesRequest.from_dict(add_total_rewards_employees_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


