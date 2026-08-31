# NewHirePacketPublicApiWritableBody

Optional fields that may be set when creating or updating a new hire packet instance. All properties are optional for PUT; for POST, employeeId is required and supplied via a second schema in the request body allOf.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_employee_id** | **int** |  | [optional] 
**requires_personal_information** | **bool** | Whether personal information collection is required. | [optional] 
**requires_photo** | **bool** | Whether a photo is required. | [optional] 
**requires_personal_questions** | **bool** | Whether personal questions are required. | [optional] 
**arrive_by_time** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**send_get_to_know_you_email** | **bool** | Whether to send the Get To Know You email. | [optional] 
**show_payroll_state** | **bool** | Whether to show state payroll fields. | [optional] 
**show_payroll_federal** | **bool** | Whether to show federal payroll fields. | [optional] 
**show_payroll_direct_deposit** | **bool** | Whether to show direct deposit payroll fields. | [optional] 
**nhp_template_id** | **int** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.new_hire_packet_public_api_writable_body import NewHirePacketPublicApiWritableBody

# TODO update the JSON string below
json = "{}"
# create an instance of NewHirePacketPublicApiWritableBody from a JSON string
new_hire_packet_public_api_writable_body_instance = NewHirePacketPublicApiWritableBody.from_json(json)
# print the JSON string representation of the object
print(NewHirePacketPublicApiWritableBody.to_json())

# convert the object into a dict
new_hire_packet_public_api_writable_body_dict = new_hire_packet_public_api_writable_body_instance.to_dict()
# create an instance of NewHirePacketPublicApiWritableBody from a dict
new_hire_packet_public_api_writable_body_from_dict = NewHirePacketPublicApiWritableBody.from_dict(new_hire_packet_public_api_writable_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


