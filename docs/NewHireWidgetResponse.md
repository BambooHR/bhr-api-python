# NewHireWidgetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_hires** | [**List[NewHireWidgetItem]**](NewHireWidgetItem.md) | Upcoming new hires visible to the authenticated user, sorted by hire date descending. Empty when the user lacks new-hire-packet or company-directory access. | 

## Example

```python
from bamboohr_sdk.models.new_hire_widget_response import NewHireWidgetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NewHireWidgetResponse from a JSON string
new_hire_widget_response_instance = NewHireWidgetResponse.from_json(json)
# print the JSON string representation of the object
print(NewHireWidgetResponse.to_json())

# convert the object into a dict
new_hire_widget_response_dict = new_hire_widget_response_instance.to_dict()
# create an instance of NewHireWidgetResponse from a dict
new_hire_widget_response_from_dict = NewHireWidgetResponse.from_dict(new_hire_widget_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


