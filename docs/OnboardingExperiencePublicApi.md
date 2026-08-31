# OnboardingExperiencePublicApi

Onboarding experience for public APIs; links to the new hire packet instance by id only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Onboarding experience id (same as the new hire packet instance primary key). | [optional] 
**employee_id** | **int** | Employee this onboarding experience belongs to. | [optional] 
**new_hire_packet_id** | **int** | Primary key of the linked new hire packet instance (NHP row). | [optional] 
**nhp_template_id** | **int** |  | [optional] 
**nhp_configuration_id** | **int** |  | [optional] 
**status** | **str** | Derived lifecycle status for the linked new hire packet instance. | [optional] 

## Example

```python
from bamboohr_sdk.models.onboarding_experience_public_api import OnboardingExperiencePublicApi

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingExperiencePublicApi from a JSON string
onboarding_experience_public_api_instance = OnboardingExperiencePublicApi.from_json(json)
# print the JSON string representation of the object
print(OnboardingExperiencePublicApi.to_json())

# convert the object into a dict
onboarding_experience_public_api_dict = onboarding_experience_public_api_instance.to_dict()
# create an instance of OnboardingExperiencePublicApi from a dict
onboarding_experience_public_api_from_dict = OnboardingExperiencePublicApi.from_dict(onboarding_experience_public_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


