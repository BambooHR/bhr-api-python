# TimeTrackingConfigurationPaginatedResponseDataV1Links

Pagination links. Keys are omitted when there is no previous/next page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | [**TimeTrackingConfigurationPaginatedResponseDataV1LinksPrev**](TimeTrackingConfigurationPaginatedResponseDataV1LinksPrev.md) |  | [optional] 
**next** | [**TimeTrackingConfigurationPaginatedResponseDataV1LinksNext**](TimeTrackingConfigurationPaginatedResponseDataV1LinksNext.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_configuration_paginated_response_data_v1_links import TimeTrackingConfigurationPaginatedResponseDataV1Links

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingConfigurationPaginatedResponseDataV1Links from a JSON string
time_tracking_configuration_paginated_response_data_v1_links_instance = TimeTrackingConfigurationPaginatedResponseDataV1Links.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingConfigurationPaginatedResponseDataV1Links.to_json())

# convert the object into a dict
time_tracking_configuration_paginated_response_data_v1_links_dict = time_tracking_configuration_paginated_response_data_v1_links_instance.to_dict()
# create an instance of TimeTrackingConfigurationPaginatedResponseDataV1Links from a dict
time_tracking_configuration_paginated_response_data_v1_links_from_dict = TimeTrackingConfigurationPaginatedResponseDataV1Links.from_dict(time_tracking_configuration_paginated_response_data_v1_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


