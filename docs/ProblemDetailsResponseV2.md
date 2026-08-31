# ProblemDetailsResponseV2

problem fields shared by problem responses and record-level errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Problem type URI identifying the error category | [optional] 
**title** | **str** | Short, human-readable summary of the problem type | [optional] 
**status** | **int** | HTTP status code for the error | [optional] 
**detail** | **str** | Detailed, human-readable explanation specific to this occurrence of the problem | [optional] 
**instance** | **str** | URI reference that identifies the specific occurrence of the problem | [optional] 
**code** | **str** | Application-specific error code | [optional] 
**fields** | **Dict[str, str]** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.problem_details_response_v2 import ProblemDetailsResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemDetailsResponseV2 from a JSON string
problem_details_response_v2_instance = ProblemDetailsResponseV2.from_json(json)
# print the JSON string representation of the object
print(ProblemDetailsResponseV2.to_json())

# convert the object into a dict
problem_details_response_v2_dict = problem_details_response_v2_instance.to_dict()
# create an instance of ProblemDetailsResponseV2 from a dict
problem_details_response_v2_from_dict = ProblemDetailsResponseV2.from_dict(problem_details_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


