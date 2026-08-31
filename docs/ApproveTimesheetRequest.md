# ApproveTimesheetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timesheet_id** | **int** | ID of the timesheet to approve. | 
**last_changed_at** | **datetime** | The timesheet&#39;s &#x60;hoursLastChangedAt&#x60; value as last fetched by the caller, in ISO 8601 UTC. This is specifically &#x60;hoursLastChangedAt&#x60;, not &#x60;updatedAt&#x60;: hours are stored separately, so the timesheet row&#39;s &#x60;updatedAt&#x60; may not move when hours change (and vice versa). The approval is rejected with 409 if the timesheet&#39;s hours changed after this instant, so callers never approve a version they have not seen. | 

## Example

```python
from bamboohr_sdk.models.approve_timesheet_request import ApproveTimesheetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveTimesheetRequest from a JSON string
approve_timesheet_request_instance = ApproveTimesheetRequest.from_json(json)
# print the JSON string representation of the object
print(ApproveTimesheetRequest.to_json())

# convert the object into a dict
approve_timesheet_request_dict = approve_timesheet_request_instance.to_dict()
# create an instance of ApproveTimesheetRequest from a dict
approve_timesheet_request_from_dict = ApproveTimesheetRequest.from_dict(approve_timesheet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


