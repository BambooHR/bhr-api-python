# WhosOutPersonV1

Display-relevant subset of an employee, embedded under the persons map when includePersons=true. Richer fields are available from the public Employee resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Employee ID. | [optional] [readonly] 
**first_name** | **str** | Employee&#39;s first name. | [optional] 
**last_name** | **str** | Employee&#39;s last name. | [optional] 
**display_name** | **str** | Preferred display name (preferred name if set, else first name), followed by the last name. | [optional] 
**job_title** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.whos_out_person_v1 import WhosOutPersonV1

# TODO update the JSON string below
json = "{}"
# create an instance of WhosOutPersonV1 from a JSON string
whos_out_person_v1_instance = WhosOutPersonV1.from_json(json)
# print the JSON string representation of the object
print(WhosOutPersonV1.to_json())

# convert the object into a dict
whos_out_person_v1_dict = whos_out_person_v1_instance.to_dict()
# create an instance of WhosOutPersonV1 from a dict
whos_out_person_v1_from_dict = WhosOutPersonV1.from_dict(whos_out_person_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


