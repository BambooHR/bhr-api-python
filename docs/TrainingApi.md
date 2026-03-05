# bamboohr_sdk.TrainingApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_employee_training_record**](TrainingApi.md#add_new_employee_training_record) | **POST** /api/v1/training/record/employee/{employeeId} | Create Employee Training Record
[**add_training_category**](TrainingApi.md#add_training_category) | **POST** /api/v1/training/category | Create Training Category
[**add_training_type**](TrainingApi.md#add_training_type) | **POST** /api/v1/training/type | Create Training Type
[**delete_employee_training_record**](TrainingApi.md#delete_employee_training_record) | **DELETE** /api/v1/training/record/{employeeTrainingRecordId} | Delete Employee Training Record
[**delete_training_category**](TrainingApi.md#delete_training_category) | **DELETE** /api/v1/training/category/{trainingCategoryId} | Delete Training Category
[**delete_training_type**](TrainingApi.md#delete_training_type) | **DELETE** /api/v1/training/type/{trainingTypeId} | Delete Training Type
[**list_employee_trainings**](TrainingApi.md#list_employee_trainings) | **GET** /api/v1/training/record/employee/{employeeId} | Get Employee Trainings
[**list_training_categories**](TrainingApi.md#list_training_categories) | **GET** /api/v1/training/category | Get Training Categories
[**list_training_types**](TrainingApi.md#list_training_types) | **GET** /api/v1/training/type | Get Training Types
[**update_employee_training_record**](TrainingApi.md#update_employee_training_record) | **PUT** /api/v1/training/record/{employeeTrainingRecordId} | Update Employee Training Record
[**update_training_category**](TrainingApi.md#update_training_category) | **PUT** /api/v1/training/category/{trainingCategoryId} | Update Training Category
[**update_training_type**](TrainingApi.md#update_training_type) | **PUT** /api/v1/training/type/{trainingTypeId} | Update Training Type


# **add_new_employee_training_record**
> TrainingRecord add_new_employee_training_record(employee_id, add_new_employee_training_record_request)

Create Employee Training Record

Add a new employee training record. The owner of the API key used must have permission to add trainings for the selected employee.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.add_new_employee_training_record_request import AddNewEmployeeTrainingRecordRequest
from bamboohr_sdk.models.training_record import TrainingRecord
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    employee_id = 0 # int | The ID of the employee to add a training record to. (default to 0)
    add_new_employee_training_record_request = bamboohr_sdk.AddNewEmployeeTrainingRecordRequest() # AddNewEmployeeTrainingRecordRequest | Training object to post

    try:
        # Create Employee Training Record
        api_response = api_instance.add_new_employee_training_record(employee_id, add_new_employee_training_record_request)
        print("The response of TrainingApi->add_new_employee_training_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->add_new_employee_training_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee to add a training record to. | [default to 0]
 **add_new_employee_training_record_request** | [**AddNewEmployeeTrainingRecordRequest**](AddNewEmployeeTrainingRecordRequest.md)| Training object to post | 

### Return type

[**TrainingRecord**](TrainingRecord.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_training_category**
> TrainingCategory add_training_category(add_training_category_request)

Create Training Category

Add a training category. The owner of the API key used must have access to training settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.add_training_category_request import AddTrainingCategoryRequest
from bamboohr_sdk.models.training_category import TrainingCategory
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    add_training_category_request = bamboohr_sdk.AddTrainingCategoryRequest() # AddTrainingCategoryRequest | Training category to post

    try:
        # Create Training Category
        api_response = api_instance.add_training_category(add_training_category_request)
        print("The response of TrainingApi->add_training_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->add_training_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_training_category_request** | [**AddTrainingCategoryRequest**](AddTrainingCategoryRequest.md)| Training category to post | 

### Return type

[**TrainingCategory**](TrainingCategory.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_training_type**
> TrainingType add_training_type(add_training_type_request)

Create Training Type

Add a training type. The owner of the API key used must have access to training settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.add_training_type_request import AddTrainingTypeRequest
from bamboohr_sdk.models.training_type import TrainingType
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    add_training_type_request = bamboohr_sdk.AddTrainingTypeRequest() # AddTrainingTypeRequest | Training object to post

    try:
        # Create Training Type
        api_response = api_instance.add_training_type(add_training_type_request)
        print("The response of TrainingApi->add_training_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->add_training_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_training_type_request** | [**AddTrainingTypeRequest**](AddTrainingTypeRequest.md)| Training object to post | 

### Return type

[**TrainingType**](TrainingType.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee_training_record**
> delete_employee_training_record(employee_training_record_id)

Delete Employee Training Record

Delete an existing employee training record. The owner of the API key used must have permission to view and edit the employee and training type.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    employee_training_record_id = 0 # int | The ID of the training record to delete. (default to 0)

    try:
        # Delete Employee Training Record
        api_instance.delete_employee_training_record(employee_training_record_id)
    except Exception as e:
        print("Exception when calling TrainingApi->delete_employee_training_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_training_record_id** | **int**| The ID of the training record to delete. | [default to 0]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url or training record does not exist. |  -  |
**405** | Unable to delete training record. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_training_category**
> delete_training_category(training_category_id)

Delete Training Category

Delete an existing training category. The owner of the API key used must have access to training settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    training_category_id = 0 # int | The ID of the training category to delete. (default to 0)

    try:
        # Delete Training Category
        api_instance.delete_training_category(training_category_id)
    except Exception as e:
        print("Exception when calling TrainingApi->delete_training_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **training_category_id** | **int**| The ID of the training category to delete. | [default to 0]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url or training category does not exist. |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_training_type**
> delete_training_type(training_type_id)

Delete Training Type

Delete an existing training type. The owner of the API key used must have access to training settings. Deleting a training type will only be successful if all employee trainings for this type have been removed prior to this request.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    training_type_id = 0 # int | The ID of the training type to delete. (default to 0)

    try:
        # Delete Training Type
        api_instance.delete_training_type(training_type_id)
    except Exception as e:
        print("Exception when calling TrainingApi->delete_training_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **training_type_id** | **int**| The ID of the training type to delete. | [default to 0]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url or training type does not exist. |  -  |
**405** | Training type was unable to be deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_trainings**
> List[TrainingRecordList] list_employee_trainings(employee_id, training_type_id=training_type_id)

Get Employee Trainings

Get all employee training records. The owner of the API key used must have access to view the employee. The API will only return trainings for the employee that the owner of the API key has permission to see. Included with each employee training is the training information that has been selected for tracking in settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.training_record_list import TrainingRecordList
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    employee_id = 0 # int | The ID of the employee to get a list of trainings for. (default to 0)
    training_type_id = 0 # int | The training type id is optional. Not supplying a training type id will return the collection of all training records for the employee. (optional) (default to 0)

    try:
        # Get Employee Trainings
        api_response = api_instance.list_employee_trainings(employee_id, training_type_id=training_type_id)
        print("The response of TrainingApi->list_employee_trainings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->list_employee_trainings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee to get a list of trainings for. | [default to 0]
 **training_type_id** | **int**| The training type id is optional. Not supplying a training type id will return the collection of all training records for the employee. | [optional] [default to 0]

### Return type

[**List[TrainingRecordList]**](TrainingRecordList.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_training_categories**
> List[TrainingCategoryList] list_training_categories()

Get Training Categories

Get a list of training categories. The owner of the API key used must have access to training settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.training_category_list import TrainingCategoryList
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TrainingApi(api_client)

    try:
        # Get Training Categories
        api_response = api_instance.list_training_categories()
        print("The response of TrainingApi->list_training_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->list_training_categories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TrainingCategoryList]**](TrainingCategoryList.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_training_types**
> List[TrainingTypeList] list_training_types()

Get Training Types

Get a list of training types. The owner of the API key used must have access to training settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.training_type_list import TrainingTypeList
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TrainingApi(api_client)

    try:
        # Get Training Types
        api_response = api_instance.list_training_types()
        print("The response of TrainingApi->list_training_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->list_training_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TrainingTypeList]**](TrainingTypeList.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_training_record**
> TrainingRecord update_employee_training_record(employee_training_record_id, update_employee_training_record_request)

Update Employee Training Record

Update an existing exmployee training record. The owner of the API key used must have permission to add trainings for the selected employee

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.training_record import TrainingRecord
from bamboohr_sdk.models.update_employee_training_record_request import UpdateEmployeeTrainingRecordRequest
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    employee_training_record_id = 0 # int | The ID of the training record to update. (default to 0)
    update_employee_training_record_request = bamboohr_sdk.UpdateEmployeeTrainingRecordRequest() # UpdateEmployeeTrainingRecordRequest | Training object to update

    try:
        # Update Employee Training Record
        api_response = api_instance.update_employee_training_record(employee_training_record_id, update_employee_training_record_request)
        print("The response of TrainingApi->update_employee_training_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->update_employee_training_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_training_record_id** | **int**| The ID of the training record to update. | [default to 0]
 **update_employee_training_record_request** | [**UpdateEmployeeTrainingRecordRequest**](UpdateEmployeeTrainingRecordRequest.md)| Training object to update | 

### Return type

[**TrainingRecord**](TrainingRecord.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_training_category**
> TrainingCategory update_training_category(training_category_id, update_training_category_request)

Update Training Category

Update an existing training category. The owner of the API key used must have access to training settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.training_category import TrainingCategory
from bamboohr_sdk.models.update_training_category_request import UpdateTrainingCategoryRequest
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    training_category_id = 0 # int | The ID of the training category to update. (default to 0)
    update_training_category_request = bamboohr_sdk.UpdateTrainingCategoryRequest() # UpdateTrainingCategoryRequest | Training category to update

    try:
        # Update Training Category
        api_response = api_instance.update_training_category(training_category_id, update_training_category_request)
        print("The response of TrainingApi->update_training_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->update_training_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **training_category_id** | **int**| The ID of the training category to update. | [default to 0]
 **update_training_category_request** | [**UpdateTrainingCategoryRequest**](UpdateTrainingCategoryRequest.md)| Training category to update | 

### Return type

[**TrainingCategory**](TrainingCategory.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_training_type**
> TrainingType update_training_type(training_type_id, update_training_type_request)

Update Training Type

Update an existing training type. The owner of the API key used must have access to training settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.training_type import TrainingType
from bamboohr_sdk.models.update_training_type_request import UpdateTrainingTypeRequest
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    training_type_id = 0 # int | The ID of the training type to update. (default to 0)
    update_training_type_request = bamboohr_sdk.UpdateTrainingTypeRequest() # UpdateTrainingTypeRequest | Training type object to update to

    try:
        # Update Training Type
        api_response = api_instance.update_training_type(training_type_id, update_training_type_request)
        print("The response of TrainingApi->update_training_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->update_training_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **training_type_id** | **int**| The ID of the training type to update. | [default to 0]
 **update_training_type_request** | [**UpdateTrainingTypeRequest**](UpdateTrainingTypeRequest.md)| Training type object to update to | 

### Return type

[**TrainingType**](TrainingType.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

