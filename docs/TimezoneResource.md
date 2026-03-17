# TimezoneResource

A timezone resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The timezone ID. | [optional] 
**gmt_offset** | **str** | The GMT offset label (e.g. \&quot;(GMT-07:00)\&quot;). | [optional] 
**name** | **str** | The display name of the timezone. | [optional] 
**utc_name** | **str** | The IANA/UTC timezone identifier. | [optional] 

## Example

```python
from bamboohr_sdk.models.timezone_resource import TimezoneResource

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneResource from a JSON string
timezone_resource_instance = TimezoneResource.from_json(json)
# print the JSON string representation of the object
print(TimezoneResource.to_json())

# convert the object into a dict
timezone_resource_dict = timezone_resource_instance.to_dict()
# create an instance of TimezoneResource from a dict
timezone_resource_from_dict = TimezoneResource.from_dict(timezone_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


