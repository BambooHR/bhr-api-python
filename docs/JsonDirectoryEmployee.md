# JsonDirectoryEmployee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[JsonDirectoryEmployeeFieldsInner]**](JsonDirectoryEmployeeFieldsInner.md) | Array of field definitions | [optional] 
**employees** | **List[object]** | Array of employee records. Each employee object contains properties matching the &#39;id&#39; values from the &#39;fields&#39; array. Property names are dynamically determined by company configuration. Property values can be strings, numbers, booleans, or null. Common fields include: id, displayName, firstName, lastName, preferredName, jobTitle, workPhone, mobilePhone, workEmail, department, location, division, twitterFeed, pronouns, workPhoneExtension, photoUploaded, photoUrl, canUploadPhoto. | [optional] 

## Example

```python
from bamboohr_sdk.models.json_directory_employee import JsonDirectoryEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDirectoryEmployee from a JSON string
json_directory_employee_instance = JsonDirectoryEmployee.from_json(json)
# print the JSON string representation of the object
print(JsonDirectoryEmployee.to_json())

# convert the object into a dict
json_directory_employee_dict = json_directory_employee_instance.to_dict()
# create an instance of JsonDirectoryEmployee from a dict
json_directory_employee_from_dict = JsonDirectoryEmployee.from_dict(json_directory_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


