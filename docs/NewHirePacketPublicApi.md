# NewHirePacketPublicApi

Flat new hire packet instance for public read APIs (list and detail).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**employee_id** | **int** | Employee this packet belongs to. | [optional] 
**contact_employee_id** | **int** |  | [optional] 
**requires_personal_information** | **bool** |  | [optional] 
**requires_photo** | **bool** |  | [optional] 
**requires_personal_questions** | **bool** |  | [optional] 
**arrive_by_time** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**sent_datetime** | **str** |  | [optional] 
**viewed_datetime** | **str** |  | [optional] 
**completed_datetime** | **str** |  | [optional] 
**created_by_user_id** | **int** |  | [optional] 
**created_datetime** | **str** |  | [optional] 
**send_get_to_know_you_email** | **bool** |  | [optional] 
**get_to_know_you_email_sent** | **bool** |  | [optional] 
**show_payroll_state** | **bool** |  | [optional] 
**show_payroll_federal** | **bool** |  | [optional] 
**show_payroll_direct_deposit** | **bool** |  | [optional] 
**nhp_configuration_id** | **int** |  | [optional] 
**nhp_template_id** | **int** |  | [optional] 
**count_nhp_gtky_sent** | **int** |  | [optional] 
**cancelled** | **bool** |  | [optional] 
**include_photo_option** | **bool** | Whether photo collection is offered based on configuration. | [optional] 
**status** | **str** | Derived lifecycle status for the instance. | [optional] 

## Example

```python
from bamboohr_sdk.models.new_hire_packet_public_api import NewHirePacketPublicApi

# TODO update the JSON string below
json = "{}"
# create an instance of NewHirePacketPublicApi from a JSON string
new_hire_packet_public_api_instance = NewHirePacketPublicApi.from_json(json)
# print the JSON string representation of the object
print(NewHirePacketPublicApi.to_json())

# convert the object into a dict
new_hire_packet_public_api_dict = new_hire_packet_public_api_instance.to_dict()
# create an instance of NewHirePacketPublicApi from a dict
new_hire_packet_public_api_from_dict = NewHirePacketPublicApi.from_dict(new_hire_packet_public_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


