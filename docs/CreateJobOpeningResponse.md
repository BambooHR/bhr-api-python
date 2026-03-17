# CreateJobOpeningResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | Always &#39;success&#39; on a successful request | [optional] 
**job_opening_id** | **str** | The ID of the newly created job opening | [optional] 

## Example

```python
from bamboohr_sdk.models.create_job_opening_response import CreateJobOpeningResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJobOpeningResponse from a JSON string
create_job_opening_response_instance = CreateJobOpeningResponse.from_json(json)
# print the JSON string representation of the object
print(CreateJobOpeningResponse.to_json())

# convert the object into a dict
create_job_opening_response_dict = create_job_opening_response_instance.to_dict()
# create an instance of CreateJobOpeningResponse from a dict
create_job_opening_response_from_dict = CreateJobOpeningResponse.from_dict(create_job_opening_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


