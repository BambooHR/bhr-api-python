# BenefitCoveragesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefit_coverages** | [**List[BenefitCoveragesResponseBenefitCoveragesInner]**](BenefitCoveragesResponseBenefitCoveragesInner.md) | Array of benefit coverage level objects. | [optional] 

## Example

```python
from bamboohr_sdk.models.benefit_coverages_response import BenefitCoveragesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BenefitCoveragesResponse from a JSON string
benefit_coverages_response_instance = BenefitCoveragesResponse.from_json(json)
# print the JSON string representation of the object
print(BenefitCoveragesResponse.to_json())

# convert the object into a dict
benefit_coverages_response_dict = benefit_coverages_response_instance.to_dict()
# create an instance of BenefitCoveragesResponse from a dict
benefit_coverages_response_from_dict = BenefitCoveragesResponse.from_dict(benefit_coverages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


