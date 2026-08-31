# SendRecommendationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.send_recommendations_response import SendRecommendationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendRecommendationsResponse from a JSON string
send_recommendations_response_instance = SendRecommendationsResponse.from_json(json)
# print the JSON string representation of the object
print(SendRecommendationsResponse.to_json())

# convert the object into a dict
send_recommendations_response_dict = send_recommendations_response_instance.to_dict()
# create an instance of SendRecommendationsResponse from a dict
send_recommendations_response_from_dict = SendRecommendationsResponse.from_dict(send_recommendations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


