# ShareOptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**persons** | [**List[PersonInfoApiTransformer]**](PersonInfoApiTransformer.md) | List of employees with whom goals can be shared. | [optional] 

## Example

```python
from bamboohr_sdk.models.share_options_response import ShareOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShareOptionsResponse from a JSON string
share_options_response_instance = ShareOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(ShareOptionsResponse.to_json())

# convert the object into a dict
share_options_response_dict = share_options_response_instance.to_dict()
# create an instance of ShareOptionsResponse from a dict
share_options_response_from_dict = ShareOptionsResponse.from_dict(share_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


