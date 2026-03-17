# ApplicationDetailsJobTitle

Job title

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Title ID, or null if not set | [optional] 
**label** | **str** | Title text | [optional] 

## Example

```python
from bamboohr_sdk.models.application_details_job_title import ApplicationDetailsJobTitle

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDetailsJobTitle from a JSON string
application_details_job_title_instance = ApplicationDetailsJobTitle.from_json(json)
# print the JSON string representation of the object
print(ApplicationDetailsJobTitle.to_json())

# convert the object into a dict
application_details_job_title_dict = application_details_job_title_instance.to_dict()
# create an instance of ApplicationDetailsJobTitle from a dict
application_details_job_title_from_dict = ApplicationDetailsJobTitle.from_dict(application_details_job_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


