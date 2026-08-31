# PayGradesAndBandsReviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[PayGradesAndBandsReviewGroup]**](PayGradesAndBandsReviewGroup.md) | Compensation level groups under review. Empty when none are configured. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_review_response import PayGradesAndBandsReviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsReviewResponse from a JSON string
pay_grades_and_bands_review_response_instance = PayGradesAndBandsReviewResponse.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsReviewResponse.to_json())

# convert the object into a dict
pay_grades_and_bands_review_response_dict = pay_grades_and_bands_review_response_instance.to_dict()
# create an instance of PayGradesAndBandsReviewResponse from a dict
pay_grades_and_bands_review_response_from_dict = PayGradesAndBandsReviewResponse.from_dict(pay_grades_and_bands_review_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


