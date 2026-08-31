# NewHireWidgetItem

Single upcoming new hire as projected for the public welcome-new-hires widget endpoint. Strips sensitive contact fields (work email, home email) and normalizes the domain's dynamic BasicEmployee decorations into a stable shape.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Employee id. | 
**preferred_first_name** | **str** | Nickname when set, otherwise first name. | 
**last_name** | **str** |  | 
**hire_date** | **date** |  | 
**profile_picture_url** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**can_see_employee** | **bool** | Whether the authenticated user can navigate to the employee&#39;s profile. | 
**get_to_know_you** | [**List[CompletedQuestionsAndResponseDataObject]**](CompletedQuestionsAndResponseDataObject.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.new_hire_widget_item import NewHireWidgetItem

# TODO update the JSON string below
json = "{}"
# create an instance of NewHireWidgetItem from a JSON string
new_hire_widget_item_instance = NewHireWidgetItem.from_json(json)
# print the JSON string representation of the object
print(NewHireWidgetItem.to_json())

# convert the object into a dict
new_hire_widget_item_dict = new_hire_widget_item_instance.to_dict()
# create an instance of NewHireWidgetItem from a dict
new_hire_widget_item_from_dict = NewHireWidgetItem.from_dict(new_hire_widget_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


