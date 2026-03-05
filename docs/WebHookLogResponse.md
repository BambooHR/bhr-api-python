# WebHookLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **int** | The id of the webhook. | [optional] 
**url** | **str** | The URL of the webhook. | [optional] 
**last_attempted** | **str** | timestamp of last time the webhook was sent | [optional] 
**last_success** | **str** | timestamp of last time the webhook was sent successfully | [optional] 
**failure_count** | **int** | Count of how many times this call failed since last success | [optional] 
**status** | **int** | Status code of last request | [optional] 
**employee_ids** | **List[int]** | A list of employee ids that were changed. | [optional] 

## Example

```python
from bamboohr_sdk.models.web_hook_log_response import WebHookLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookLogResponse from a JSON string
web_hook_log_response_instance = WebHookLogResponse.from_json(json)
# print the JSON string representation of the object
print(WebHookLogResponse.to_json())

# convert the object into a dict
web_hook_log_response_dict = web_hook_log_response_instance.to_dict()
# create an instance of WebHookLogResponse from a dict
web_hook_log_response_from_dict = WebHookLogResponse.from_dict(web_hook_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


