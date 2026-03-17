# EmployeeDependent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | The ID of the employee this dependent belongs to. Required. | 
**first_name** | **str** | The dependent&#39;s first name. | [optional] 
**middle_name** | **str** | The dependent&#39;s middle name. | [optional] 
**last_name** | **str** | The dependent&#39;s last name. | [optional] 
**relationship** | **str** | The dependent&#39;s relationship to the employee (e.g. \&quot;spouse\&quot;, \&quot;child\&quot;, \&quot;domestic_partner\&quot;). | [optional] 
**gender** | **str** | The dependent&#39;s gender. | [optional] 
**ssn** | **str** | The dependent&#39;s Social Security Number, provided as plain text. Stored encrypted. Returned as a masked value (e.g. \&quot;xxx-xx-1234\&quot;) on read. | [optional] 
**sin** | **str** | The dependent&#39;s Social Insurance Number (Canadian equivalent of SSN), provided as plain text. Stored encrypted. Returned as a masked value on read. | [optional] 
**date_of_birth** | **date** | The dependent&#39;s date of birth in YYYY-MM-DD format. | [optional] 
**address_line1** | **str** | The first line of the dependent&#39;s address. | [optional] 
**address_line2** | **str** | The second line of the dependent&#39;s address. | [optional] 
**city** | **str** | The dependent&#39;s city. | [optional] 
**state** | **str** | The dependent&#39;s state, provided as a state code (e.g. \&quot;UT\&quot;). Returned as a full state name on read. | [optional] 
**zip_code** | **str** | The dependent&#39;s ZIP or postal code. | [optional] 
**home_phone** | **str** | The dependent&#39;s home phone number. | [optional] 
**country** | **str** | The dependent&#39;s country, provided as an ISO 3166-1 alpha-2 country code (e.g. \&quot;US\&quot;). Returned as a full country name on read. | [optional] 
**is_us_citizen** | **str** | Whether the dependent is a US citizen. Accepted values: \&quot;yes\&quot; or \&quot;no\&quot;. | [optional] 
**is_student** | **str** | Whether the dependent is currently a student. Accepted values: \&quot;yes\&quot; or \&quot;no\&quot;. | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_dependent import EmployeeDependent

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeDependent from a JSON string
employee_dependent_instance = EmployeeDependent.from_json(json)
# print the JSON string representation of the object
print(EmployeeDependent.to_json())

# convert the object into a dict
employee_dependent_dict = employee_dependent_instance.to_dict()
# create an instance of EmployeeDependent from a dict
employee_dependent_from_dict = EmployeeDependent.from_dict(employee_dependent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


