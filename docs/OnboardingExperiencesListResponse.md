# OnboardingExperiencesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**onboarding_experiences** | [**List[OnboardingExperiencePublicApi]**](OnboardingExperiencePublicApi.md) | Onboarding experience summaries (empty when no running workflow for this employee). | [optional] 

## Example

```python
from bamboohr_sdk.models.onboarding_experiences_list_response import OnboardingExperiencesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingExperiencesListResponse from a JSON string
onboarding_experiences_list_response_instance = OnboardingExperiencesListResponse.from_json(json)
# print the JSON string representation of the object
print(OnboardingExperiencesListResponse.to_json())

# convert the object into a dict
onboarding_experiences_list_response_dict = onboarding_experiences_list_response_instance.to_dict()
# create an instance of OnboardingExperiencesListResponse from a dict
onboarding_experiences_list_response_from_dict = OnboardingExperiencesListResponse.from_dict(onboarding_experiences_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


