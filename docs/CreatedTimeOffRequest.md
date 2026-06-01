# CreatedTimeOffRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The newly created time off request ID. Use this to chain follow-up operations such as approving, canceling, or superseding the request. | [optional] 
**employee_id** | **int** | The ID of the employee the request was created for. | [optional] 
**name** | **str** | The employee&#39;s full name. Only present when the employee record could be loaded. | [optional] 
**start** | **date** | The start date of the request in YYYY-MM-DD format. | [optional] 
**end** | **date** | The end date of the request in YYYY-MM-DD format. | [optional] 
**created** | **date** | The date the request was created in YYYY-MM-DD format (company timezone). | [optional] 
**status** | [**CreatedTimeOffRequestStatus**](CreatedTimeOffRequestStatus.md) |  | [optional] 
**type** | [**CreatedTimeOffRequestType**](CreatedTimeOffRequestType.md) |  | [optional] 
**amount** | [**CreatedTimeOffRequestAmount**](CreatedTimeOffRequestAmount.md) |  | [optional] 
**dates** | **Dict[str, Optional[float]]** | A map of dates (YYYY-MM-DD) to daily amounts. Only present when daily details were attached to the request. | [optional] 
**notes** | [**CreatedTimeOffRequestNotes**](CreatedTimeOffRequestNotes.md) |  | [optional] 
**comments** | **List[Optional[object]]** | Comments attached to the request. Always present; empty array when no comments exist. | [optional] 
**approvers** | **List[List[EmployeeTimeOffRequestApproverResponseInner]]** | The approval chain for this request. Only present when the request has approvers. | [optional] 
**actions** | **Dict[str, Optional[bool]]** | Actions the current user can perform on this request. Only present when PTO action permissions are available. Keys are restricted to &#x60;view&#x60;, &#x60;edit&#x60;, &#x60;cancel&#x60;, &#x60;approve&#x60;, &#x60;deny&#x60;, &#x60;bypass&#x60;; values are booleans. | [optional] 
**overlapping_requests** | **List[Optional[object]]** | Other existing time off requests whose date ranges overlap this request. Only present when overlap data was loaded with the request. | [optional] 
**policy_type** | **str** | The policy type backing this request (e.g. accruing, manual, unlimited). | [optional] 
**used_year_to_date** | **float** |  | [optional] 
**balance_on_date_of_request** | **float** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.created_time_off_request import CreatedTimeOffRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedTimeOffRequest from a JSON string
created_time_off_request_instance = CreatedTimeOffRequest.from_json(json)
# print the JSON string representation of the object
print(CreatedTimeOffRequest.to_json())

# convert the object into a dict
created_time_off_request_dict = created_time_off_request_instance.to_dict()
# create an instance of CreatedTimeOffRequest from a dict
created_time_off_request_from_dict = CreatedTimeOffRequest.from_dict(created_time_off_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


