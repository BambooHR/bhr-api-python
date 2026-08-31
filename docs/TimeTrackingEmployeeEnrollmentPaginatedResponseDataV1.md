# TimeTrackingEmployeeEnrollmentPaginatedResponseDataV1

Pagination envelope shared by paginated employee time tracking enrollment endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**TimeTrackingConfigurationPaginatedResponseDataV1Meta**](TimeTrackingConfigurationPaginatedResponseDataV1Meta.md) |  | [optional] 
**links** | [**TimeTrackingConfigurationPaginatedResponseDataV1Links**](TimeTrackingConfigurationPaginatedResponseDataV1Links.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_employee_enrollment_paginated_response_data_v1 import TimeTrackingEmployeeEnrollmentPaginatedResponseDataV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingEmployeeEnrollmentPaginatedResponseDataV1 from a JSON string
time_tracking_employee_enrollment_paginated_response_data_v1_instance = TimeTrackingEmployeeEnrollmentPaginatedResponseDataV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingEmployeeEnrollmentPaginatedResponseDataV1.to_json())

# convert the object into a dict
time_tracking_employee_enrollment_paginated_response_data_v1_dict = time_tracking_employee_enrollment_paginated_response_data_v1_instance.to_dict()
# create an instance of TimeTrackingEmployeeEnrollmentPaginatedResponseDataV1 from a dict
time_tracking_employee_enrollment_paginated_response_data_v1_from_dict = TimeTrackingEmployeeEnrollmentPaginatedResponseDataV1.from_dict(time_tracking_employee_enrollment_paginated_response_data_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


