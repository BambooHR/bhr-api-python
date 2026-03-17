# PersonInfoApiTransformer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | Employee ID | [optional] 
**user_id** | **int** | User ID | [optional] 
**display_first_name** | **str** | Display first name | [optional] 
**last_name** | **str** | Last name | [optional] 
**photo_url** | **str** | Photo URL | [optional] 

## Example

```python
from bamboohr_sdk.models.person_info_api_transformer import PersonInfoApiTransformer

# TODO update the JSON string below
json = "{}"
# create an instance of PersonInfoApiTransformer from a JSON string
person_info_api_transformer_instance = PersonInfoApiTransformer.from_json(json)
# print the JSON string representation of the object
print(PersonInfoApiTransformer.to_json())

# convert the object into a dict
person_info_api_transformer_dict = person_info_api_transformer_instance.to_dict()
# create an instance of PersonInfoApiTransformer from a dict
person_info_api_transformer_from_dict = PersonInfoApiTransformer.from_dict(person_info_api_transformer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


