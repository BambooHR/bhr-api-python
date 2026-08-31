# PayGradesAndBandsPublishedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[PayGradesAndBandsPublishedGroup]**](PayGradesAndBandsPublishedGroup.md) | Published compensation level groups. Empty when nothing has been published. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_published_response import PayGradesAndBandsPublishedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsPublishedResponse from a JSON string
pay_grades_and_bands_published_response_instance = PayGradesAndBandsPublishedResponse.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsPublishedResponse.to_json())

# convert the object into a dict
pay_grades_and_bands_published_response_dict = pay_grades_and_bands_published_response_instance.to_dict()
# create an instance of PayGradesAndBandsPublishedResponse from a dict
pay_grades_and_bands_published_response_from_dict = PayGradesAndBandsPublishedResponse.from_dict(pay_grades_and_bands_published_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


