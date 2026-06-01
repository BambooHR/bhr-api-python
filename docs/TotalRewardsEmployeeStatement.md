# TotalRewardsEmployeeStatement

Schema for a total rewards statement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** |  | [optional] 
**employee_name** | **str** | Employee Name | [optional] 
**job_title** | **str** |  | [optional] 
**has_mixed_currency_types** | **bool** |  | [optional] 
**overview_section** | [**TotalRewardsOverviewSectionValues**](TotalRewardsOverviewSectionValues.md) | Total Rewards overview section object | [optional] 
**pay_section** | [**TotalRewardsTimelineSectionValues**](TotalRewardsTimelineSectionValues.md) | Total Rewards pay timeline object | [optional] 
**bonus_section** | [**TotalRewardsTimelineSectionValues**](TotalRewardsTimelineSectionValues.md) | Total Rewards bonus section timeline object | [optional] 
**commission_section** | [**TotalRewardsTimelineSectionValues**](TotalRewardsTimelineSectionValues.md) | Total Rewards commission section timeline object | [optional] 
**benefit_section** | [**TotalRewardsBenefitSectionValues**](TotalRewardsBenefitSectionValues.md) | Total Rewards benefit section object | [optional] 
**equity_section** | [**TotalRewardsEquitySectionValues**](TotalRewardsEquitySectionValues.md) | Total Rewards equity section object | [optional] 
**calendar_section** | [**TotalRewardsCalendarSectionValues**](TotalRewardsCalendarSectionValues.md) | Total Rewards equity section object | [optional] 
**extra_pay_section** | [**TotalRewardsExtraPaySectionValues**](TotalRewardsExtraPaySectionValues.md) | Total Rewards extra pay section object | [optional] 
**custom_disclaimer_info** | [**TotalRewardsCustomDisclaimerInfo**](TotalRewardsCustomDisclaimerInfo.md) | Total Rewards custom disclaimer object | [optional] 
**company_name** | **str** |  | [optional] 
**company_logo_url** | **str** |  | [optional] 
**statement_year** | **int** |  | [optional] 
**min_statement_year** | **int** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_employee_statement import TotalRewardsEmployeeStatement

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsEmployeeStatement from a JSON string
total_rewards_employee_statement_instance = TotalRewardsEmployeeStatement.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsEmployeeStatement.to_json())

# convert the object into a dict
total_rewards_employee_statement_dict = total_rewards_employee_statement_instance.to_dict()
# create an instance of TotalRewardsEmployeeStatement from a dict
total_rewards_employee_statement_from_dict = TotalRewardsEmployeeStatement.from_dict(total_rewards_employee_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


