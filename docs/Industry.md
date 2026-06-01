# Industry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Industry ID | [optional] 
**name** | **str** | Industry name | [optional] 

## Example

```python
from bamboohr_sdk.models.industry import Industry

# TODO update the JSON string below
json = "{}"
# create an instance of Industry from a JSON string
industry_instance = Industry.from_json(json)
# print the JSON string representation of the object
print(Industry.to_json())

# convert the object into a dict
industry_dict = industry_instance.to_dict()
# create an instance of Industry from a dict
industry_from_dict = Industry.from_dict(industry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


