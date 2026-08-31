# PayGradesAndBandsReviewJobTitle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Job title identifier. | [optional] 
**job_title** | **str** | Job title name. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_review_job_title import PayGradesAndBandsReviewJobTitle

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsReviewJobTitle from a JSON string
pay_grades_and_bands_review_job_title_instance = PayGradesAndBandsReviewJobTitle.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsReviewJobTitle.to_json())

# convert the object into a dict
pay_grades_and_bands_review_job_title_dict = pay_grades_and_bands_review_job_title_instance.to_dict()
# create an instance of PayGradesAndBandsReviewJobTitle from a dict
pay_grades_and_bands_review_job_title_from_dict = PayGradesAndBandsReviewJobTitle.from_dict(pay_grades_and_bands_review_job_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


