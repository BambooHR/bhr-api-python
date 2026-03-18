# CreateEmployeeTrainingRecordRequestCost

Optional cost for the training record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | ISO 4217 currency code (e.g. &#39;USD&#39;). | [optional] 
**amount** | **str** | Monetary amount as a decimal string (e.g. &#39;100.00&#39;). | [optional] 

## Example

```python
from bamboohr_sdk.models.create_employee_training_record_request_cost import CreateEmployeeTrainingRecordRequestCost

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmployeeTrainingRecordRequestCost from a JSON string
create_employee_training_record_request_cost_instance = CreateEmployeeTrainingRecordRequestCost.from_json(json)
# print the JSON string representation of the object
print(CreateEmployeeTrainingRecordRequestCost.to_json())

# convert the object into a dict
create_employee_training_record_request_cost_dict = create_employee_training_record_request_cost_instance.to_dict()
# create an instance of CreateEmployeeTrainingRecordRequestCost from a dict
create_employee_training_record_request_cost_from_dict = CreateEmployeeTrainingRecordRequestCost.from_dict(create_employee_training_record_request_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


