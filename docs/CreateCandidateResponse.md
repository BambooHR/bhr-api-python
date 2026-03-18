# CreateCandidateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | Always &#39;success&#39; on a successful request | [optional] 
**candidate_id** | **int** | The ID of the newly created candidate | [optional] 

## Example

```python
from bamboohr_sdk.models.create_candidate_response import CreateCandidateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCandidateResponse from a JSON string
create_candidate_response_instance = CreateCandidateResponse.from_json(json)
# print the JSON string representation of the object
print(CreateCandidateResponse.to_json())

# convert the object into a dict
create_candidate_response_dict = create_candidate_response_instance.to_dict()
# create an instance of CreateCandidateResponse from a dict
create_candidate_response_from_dict = CreateCandidateResponse.from_dict(create_candidate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


