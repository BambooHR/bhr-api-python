# TimeTrackingPaginatedTimeTrackingConfigurationsResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**TimeTrackingConfigurationPaginatedResponseDataV1Meta**](TimeTrackingConfigurationPaginatedResponseDataV1Meta.md) |  | [optional] 
**links** | [**TimeTrackingConfigurationPaginatedResponseDataV1Links**](TimeTrackingConfigurationPaginatedResponseDataV1Links.md) |  | [optional] 
**data** | [**List[TimeTrackingTimeTrackingConfigurationV1]**](TimeTrackingTimeTrackingConfigurationV1.md) | Collection of time tracking configurations. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_paginated_time_tracking_configurations_response_v1 import TimeTrackingPaginatedTimeTrackingConfigurationsResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingPaginatedTimeTrackingConfigurationsResponseV1 from a JSON string
time_tracking_paginated_time_tracking_configurations_response_v1_instance = TimeTrackingPaginatedTimeTrackingConfigurationsResponseV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingPaginatedTimeTrackingConfigurationsResponseV1.to_json())

# convert the object into a dict
time_tracking_paginated_time_tracking_configurations_response_v1_dict = time_tracking_paginated_time_tracking_configurations_response_v1_instance.to_dict()
# create an instance of TimeTrackingPaginatedTimeTrackingConfigurationsResponseV1 from a dict
time_tracking_paginated_time_tracking_configurations_response_v1_from_dict = TimeTrackingPaginatedTimeTrackingConfigurationsResponseV1.from_dict(time_tracking_paginated_time_tracking_configurations_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


