# bamboohr_sdk.CompensationPlanningApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**a05b6d5f564f805d688ff2c1e37c3990**](CompensationPlanningApi.md#a05b6d5f564f805d688ff2c1e37c3990) | **POST** /api/v1/compensation/planning_cycles/{id}/recommendations/send | Send recommendations to next stage
[**a6b8da1348a3151fe95adc03aaf64447**](CompensationPlanningApi.md#a6b8da1348a3151fe95adc03aaf64447) | **GET** /api/v1/compensation/planning_cycles/{id}/employees | List employees in compensation planning cycle
[**b1e467e0eef72350eec61fcfeaf4e19d**](CompensationPlanningApi.md#b1e467e0eef72350eec61fcfeaf4e19d) | **DELETE** /api/v1/compensation/planning_cycles/{id}/approvals/employee/{employeeId} | Remove from approval flow
[**b3c51254de6918637a971fe4af382a53**](CompensationPlanningApi.md#b3c51254de6918637a971fe4af382a53) | **GET** /api/v1/compensation/planning_cycles/{id}/admins | List compensation planning cycle admins
[**b65f246186b41a9783a9397c11c703b4**](CompensationPlanningApi.md#b65f246186b41a9783a9397c11c703b4) | **GET** /api/v1/compensation/planning_cycles | List compensation planning cycles
[**c79f9c5950f983e59d2626faa30c00a1**](CompensationPlanningApi.md#c79f9c5950f983e59d2626faa30c00a1) | **PUT** /api/v1/compensation/planning_cycles/{id}/change_comm/template | Save change comm template
[**c7c32ed5278ac67e2e518bf7484a75dc**](CompensationPlanningApi.md#c7c32ed5278ac67e2e518bf7484a75dc) | **POST** /api/v1/compensation/planning_cycles/{id}/admins | Add cycle admins
[**call_100b0cf8c5207b35697ff10370fd5fe1**](CompensationPlanningApi.md#call_100b0cf8c5207b35697ff10370fd5fe1) | **PUT** /api/v1/compensation/planning_cycles/{id} | Update compensation planning cycle
[**call_1d1fc0f164cb51973a0206b8e2fb2d2d**](CompensationPlanningApi.md#call_1d1fc0f164cb51973a0206b8e2fb2d2d) | **POST** /api/v1/compensation/planning_cycles/{id}/budgets/import | Import budget breakdown
[**call_1d64402ee192568adbd5e3179a91e6e2**](CompensationPlanningApi.md#call_1d64402ee192568adbd5e3179a91e6e2) | **PUT** /api/v1/compensation/planning_cycles/{id}/budgets/breakdown | Save budget breakdown
[**call_22ad75be25455279e2987c80851af5fc**](CompensationPlanningApi.md#call_22ad75be25455279e2987c80851af5fc) | **DELETE** /api/v1/compensation/planning_cycles/{id} | Delete compensation planning cycle
[**call_329acecaa6df729733d0752aa9f6b204**](CompensationPlanningApi.md#call_329acecaa6df729733d0752aa9f6b204) | **GET** /api/v1/compensation/planning_cycles/{id}/worksheet | Get compensation planning cycle worksheet
[**call_3958585c861325ea7a2cd30a8c74f042**](CompensationPlanningApi.md#call_3958585c861325ea7a2cd30a8c74f042) | **POST** /api/v1/compensation/planning_cycles/{id}/employees | Add employees to cycle
[**call_3a19f07aa737dc826ba43b9a1c1cd257**](CompensationPlanningApi.md#call_3a19f07aa737dc826ba43b9a1c1cd257) | **PUT** /api/v1/compensation/planning_cycles/{id}/launch | Launch compensation planning cycle
[**call_4e886b18264480611f380805301c49c4**](CompensationPlanningApi.md#call_4e886b18264480611f380805301c49c4) | **GET** /api/v1/compensation/planning_cycles/{id}/approvals | Get compensation planning approval flows
[**call_593d5bff120edf2a218a92022a682728**](CompensationPlanningApi.md#call_593d5bff120edf2a218a92022a682728) | **GET** /api/v1/compensation/planning_cycles/{id}/worksheet/export | Export compensation planning cycle worksheet to CSV
[**call_5c2b55158b0950b1e9211655666645b6**](CompensationPlanningApi.md#call_5c2b55158b0950b1e9211655666645b6) | **GET** /api/v1/compensation/planning_cycles/{id} | Get compensation planning cycle details
[**call_5c4aab35a34f5760ec044104b5232bf5**](CompensationPlanningApi.md#call_5c4aab35a34f5760ec044104b5232bf5) | **POST** /api/v1/compensation/planning_cycles/{id}/approvals/final_approver/{employeeId} | Set final approver
[**call_7efceaee2c010f88244dd01ee81e6e7b**](CompensationPlanningApi.md#call_7efceaee2c010f88244dd01ee81e6e7b) | **GET** /api/v1/compensation/planning_cycles/{id}/budgets | Get compensation planning cycle budgets
[**call_89a5068111ec499135c7d6e9a53d5a30**](CompensationPlanningApi.md#call_89a5068111ec499135c7d6e9a53d5a30) | **DELETE** /api/v1/compensation/planning_cycles/{id}/employees | Remove employees from cycle
[**call_9bc279d788f6e86b4cd8b2e0d3de91b1**](CompensationPlanningApi.md#call_9bc279d788f6e86b4cd8b2e0d3de91b1) | **GET** /api/v1/compensation/planning_cycles/{id}/summary | Get compensation planning cycle summary
[**cf87b8e09a001b6fb81dfce6c20ab9e3**](CompensationPlanningApi.md#cf87b8e09a001b6fb81dfce6c20ab9e3) | **PUT** /api/v1/compensation/planning_cycles/{id}/approvals/{templateId} | Update approval flow
[**d6987e300672a00c7cfe59afebb64156**](CompensationPlanningApi.md#d6987e300672a00c7cfe59afebb64156) | **GET** /api/v1/compensation/planning_cycles/{id}/change_comm | Get change communication letter details
[**dacd313af2106213fc4696175941ce65**](CompensationPlanningApi.md#dacd313af2106213fc4696175941ce65) | **PUT** /api/v1/compensation/planning_cycles/{id}/budgets/guidelines | Save budget guidelines
[**e2ac4e1535f296cb8901f209e04caa83**](CompensationPlanningApi.md#e2ac4e1535f296cb8901f209e04caa83) | **POST** /api/v1/compensation/planning_cycles | Create compensation planning cycle
[**ef7619b0ee4c8dc079aaea870cfbe81b**](CompensationPlanningApi.md#ef7619b0ee4c8dc079aaea870cfbe81b) | **DELETE** /api/v1/compensation/planning_cycles/{id}/admins/{employeeId} | Remove cycle admin
[**f3883a522dadbe9e11b34f8b656e3adb**](CompensationPlanningApi.md#f3883a522dadbe9e11b34f8b656e3adb) | **POST** /api/v1/compensation/planning_cycles/{id}/recommendations | Save recommendations
[**f4b431363af6573af46750f32632e88b**](CompensationPlanningApi.md#f4b431363af6573af46750f32632e88b) | **PUT** /api/v1/compensation/planning_cycles/{id}/complete | Complete compensation planning cycle


# **a05b6d5f564f805d688ff2c1e37c3990**
> SendRecommendationsResponse a05b6d5f564f805d688ff2c1e37c3990(id, a05b6d5f564f805d688ff2c1e37c3990_request)

Send recommendations to next stage

Send recommendations to the next approval stage for a specific approval flow template.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.a05b6d5f564f805d688ff2c1e37c3990_request import A05b6d5f564f805d688ff2c1e37c3990Request
from bamboohr_sdk.models.send_recommendations_response import SendRecommendationsResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    a05b6d5f564f805d688ff2c1e37c3990_request = bamboohr_sdk.A05b6d5f564f805d688ff2c1e37c3990Request() # A05b6d5f564f805d688ff2c1e37c3990Request | 

    try:
        # Send recommendations to next stage
        api_response = api_instance.a05b6d5f564f805d688ff2c1e37c3990(id, a05b6d5f564f805d688ff2c1e37c3990_request)
        print("The response of CompensationPlanningApi->a05b6d5f564f805d688ff2c1e37c3990:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->a05b6d5f564f805d688ff2c1e37c3990: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **a05b6d5f564f805d688ff2c1e37c3990_request** | [**A05b6d5f564f805d688ff2c1e37c3990Request**](A05b6d5f564f805d688ff2c1e37c3990Request.md)|  | 

### Return type

[**SendRecommendationsResponse**](SendRecommendationsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recommendations sent successfully |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **a6b8da1348a3151fe95adc03aaf64447**
> Dict[str, object] a6b8da1348a3151fe95adc03aaf64447(id)

List employees in compensation planning cycle

List employees in the compensation planning cycle (picker data: company roster and membership).

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 

    try:
        # List employees in compensation planning cycle
        api_response = api_instance.a6b8da1348a3151fe95adc03aaf64447(id)
        print("The response of CompensationPlanningApi->a6b8da1348a3151fe95adc03aaf64447:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->a6b8da1348a3151fe95adc03aaf64447: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**Dict[str, object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **b1e467e0eef72350eec61fcfeaf4e19d**
> Dict[str, object] b1e467e0eef72350eec61fcfeaf4e19d(id, employee_id, group_by=group_by)

Remove from approval flow

Remove an employee from all approval chains for a specific cycle.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    employee_id = 'employee_id_example' # str | 
    group_by = 'group_by_example' # str | Optional grouping for returned flows (e.g. department) (optional)

    try:
        # Remove from approval flow
        api_response = api_instance.b1e467e0eef72350eec61fcfeaf4e19d(id, employee_id, group_by=group_by)
        print("The response of CompensationPlanningApi->b1e467e0eef72350eec61fcfeaf4e19d:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->b1e467e0eef72350eec61fcfeaf4e19d: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **employee_id** | **str**|  | 
 **group_by** | **str**| Optional grouping for returned flows (e.g. department) | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated approval flows after removal |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **b3c51254de6918637a971fe4af382a53**
> CompensationPlanningCycleAdminsResponse b3c51254de6918637a971fe4af382a53(id)

List compensation planning cycle admins

List compensation planning cycle admins.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.compensation_planning_cycle_admins_response import CompensationPlanningCycleAdminsResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 

    try:
        # List compensation planning cycle admins
        api_response = api_instance.b3c51254de6918637a971fe4af382a53(id)
        print("The response of CompensationPlanningApi->b3c51254de6918637a971fe4af382a53:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->b3c51254de6918637a971fe4af382a53: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CompensationPlanningCycleAdminsResponse**](CompensationPlanningCycleAdminsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **b65f246186b41a9783a9397c11c703b4**
> Dict[str, object] b65f246186b41a9783a9397c11c703b4()

List compensation planning cycles

List all compensation planning cycles for the company, including status and employee counts.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)

    try:
        # List compensation planning cycles
        api_response = api_instance.b65f246186b41a9783a9397c11c703b4()
        print("The response of CompensationPlanningApi->b65f246186b41a9783a9397c11c703b4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->b65f246186b41a9783a9397c11c703b4: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **c79f9c5950f983e59d2626faa30c00a1**
> SaveChangeCommTemplateResponse c79f9c5950f983e59d2626faa30c00a1(id, c79f9c5950f983e59d2626faa30c00a1_request)

Save change comm template

Save the change communication email template for a compensation planning cycle.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.c79f9c5950f983e59d2626faa30c00a1_request import C79f9c5950f983e59d2626faa30c00a1Request
from bamboohr_sdk.models.save_change_comm_template_response import SaveChangeCommTemplateResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    c79f9c5950f983e59d2626faa30c00a1_request = bamboohr_sdk.C79f9c5950f983e59d2626faa30c00a1Request() # C79f9c5950f983e59d2626faa30c00a1Request | 

    try:
        # Save change comm template
        api_response = api_instance.c79f9c5950f983e59d2626faa30c00a1(id, c79f9c5950f983e59d2626faa30c00a1_request)
        print("The response of CompensationPlanningApi->c79f9c5950f983e59d2626faa30c00a1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->c79f9c5950f983e59d2626faa30c00a1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **c79f9c5950f983e59d2626faa30c00a1_request** | [**C79f9c5950f983e59d2626faa30c00a1Request**](C79f9c5950f983e59d2626faa30c00a1Request.md)|  | 

### Return type

[**SaveChangeCommTemplateResponse**](SaveChangeCommTemplateResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template saved successfully |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **c7c32ed5278ac67e2e518bf7484a75dc**
> AddCycleAdminsResponse c7c32ed5278ac67e2e518bf7484a75dc(id, c7c32ed5278ac67e2e518bf7484a75dc_request)

Add cycle admins

Add one or more cycle admins by employee IDs.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.add_cycle_admins_response import AddCycleAdminsResponse
from bamboohr_sdk.models.c7c32ed5278ac67e2e518bf7484a75dc_request import C7c32ed5278ac67e2e518bf7484a75dcRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    c7c32ed5278ac67e2e518bf7484a75dc_request = bamboohr_sdk.C7c32ed5278ac67e2e518bf7484a75dcRequest() # C7c32ed5278ac67e2e518bf7484a75dcRequest | 

    try:
        # Add cycle admins
        api_response = api_instance.c7c32ed5278ac67e2e518bf7484a75dc(id, c7c32ed5278ac67e2e518bf7484a75dc_request)
        print("The response of CompensationPlanningApi->c7c32ed5278ac67e2e518bf7484a75dc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->c7c32ed5278ac67e2e518bf7484a75dc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **c7c32ed5278ac67e2e518bf7484a75dc_request** | [**C7c32ed5278ac67e2e518bf7484a75dcRequest**](C7c32ed5278ac67e2e518bf7484a75dcRequest.md)|  | 

### Return type

[**AddCycleAdminsResponse**](AddCycleAdminsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of adding cycle admins |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_100b0cf8c5207b35697ff10370fd5fe1**
> Dict[str, object] call_100b0cf8c5207b35697ff10370fd5fe1(id, details_and_currency_request_data_object)

Update compensation planning cycle

Update compensation planning cycle details and currency settings.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.details_and_currency_request_data_object import DetailsAndCurrencyRequestDataObject
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    details_and_currency_request_data_object = bamboohr_sdk.DetailsAndCurrencyRequestDataObject() # DetailsAndCurrencyRequestDataObject | Cycle details and currency settings to update

    try:
        # Update compensation planning cycle
        api_response = api_instance.call_100b0cf8c5207b35697ff10370fd5fe1(id, details_and_currency_request_data_object)
        print("The response of CompensationPlanningApi->call_100b0cf8c5207b35697ff10370fd5fe1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->call_100b0cf8c5207b35697ff10370fd5fe1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **details_and_currency_request_data_object** | [**DetailsAndCurrencyRequestDataObject**](DetailsAndCurrencyRequestDataObject.md)| Cycle details and currency settings to update | 

### Return type

**Dict[str, object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cycle updated successfully |  -  |
**400** | Invalid request data |  -  |
**403** | Insufficient permissions |  -  |
**404** | Resource not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_1d1fc0f164cb51973a0206b8e2fb2d2d**
> BudgetBreakdownImportResponse call_1d1fc0f164cb51973a0206b8e2fb2d2d(id, model1d1fc0f164cb51973a0206b8e2fb2d2d_request)

Import budget breakdown

Import budget breakdown from structured data and apply to allocations.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.budget_breakdown_import_response import BudgetBreakdownImportResponse
from bamboohr_sdk.models.model1d1fc0f164cb51973a0206b8e2fb2d2d_request import Model1d1fc0f164cb51973a0206b8e2fb2d2dRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    model1d1fc0f164cb51973a0206b8e2fb2d2d_request = bamboohr_sdk.Model1d1fc0f164cb51973a0206b8e2fb2d2dRequest() # Model1d1fc0f164cb51973a0206b8e2fb2d2dRequest | Budget breakdown import data

    try:
        # Import budget breakdown
        api_response = api_instance.call_1d1fc0f164cb51973a0206b8e2fb2d2d(id, model1d1fc0f164cb51973a0206b8e2fb2d2d_request)
        print("The response of CompensationPlanningApi->call_1d1fc0f164cb51973a0206b8e2fb2d2d:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->call_1d1fc0f164cb51973a0206b8e2fb2d2d: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **model1d1fc0f164cb51973a0206b8e2fb2d2d_request** | [**Model1d1fc0f164cb51973a0206b8e2fb2d2dRequest**](Model1d1fc0f164cb51973a0206b8e2fb2d2dRequest.md)| Budget breakdown import data | 

### Return type

[**BudgetBreakdownImportResponse**](BudgetBreakdownImportResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Budget breakdown imported successfully |  -  |
**400** | Invalid request data |  -  |
**403** | Insufficient permissions |  -  |
**404** | Resource not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_1d64402ee192568adbd5e3179a91e6e2**
> call_1d64402ee192568adbd5e3179a91e6e2(id, model1d64402ee192568adbd5e3179a91e6e2_request_inner)

Save budget breakdown

Save budget breakdown for a compensation planning cycle.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.model1d64402ee192568adbd5e3179a91e6e2_request_inner import Model1d64402ee192568adbd5e3179a91e6e2RequestInner
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    model1d64402ee192568adbd5e3179a91e6e2_request_inner = [bamboohr_sdk.Model1d64402ee192568adbd5e3179a91e6e2RequestInner()] # List[Model1d64402ee192568adbd5e3179a91e6e2RequestInner] | Budget breakdown data

    try:
        # Save budget breakdown
        api_instance.call_1d64402ee192568adbd5e3179a91e6e2(id, model1d64402ee192568adbd5e3179a91e6e2_request_inner)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->call_1d64402ee192568adbd5e3179a91e6e2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **model1d64402ee192568adbd5e3179a91e6e2_request_inner** | [**List[Model1d64402ee192568adbd5e3179a91e6e2RequestInner]**](Model1d64402ee192568adbd5e3179a91e6e2RequestInner.md)| Budget breakdown data | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Budget breakdown saved successfully |  -  |
**400** | Invalid request data |  -  |
**403** | Insufficient permissions |  -  |
**404** | Resource not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_22ad75be25455279e2987c80851af5fc**
> call_22ad75be25455279e2987c80851af5fc(id)

Delete compensation planning cycle

Delete a compensation planning cycle.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 

    try:
        # Delete compensation planning cycle
        api_instance.call_22ad75be25455279e2987c80851af5fc(id)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->call_22ad75be25455279e2987c80851af5fc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Cycle deleted successfully |  -  |
**403** | Insufficient permissions |  -  |
**404** | Resource not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_329acecaa6df729733d0752aa9f6b204**
> Dict[str, object] call_329acecaa6df729733d0752aa9f6b204(id, type=type)

Get compensation planning cycle worksheet

Get compensation planning worksheet details for the cycle (recommendations, approvals, or overview context). Omit `type` to use the default view for the current user.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    type = 'type_example' # str | Worksheet context: recommendations, approvals, or overview (overview requires cycle admin). (optional)

    try:
        # Get compensation planning cycle worksheet
        api_response = api_instance.call_329acecaa6df729733d0752aa9f6b204(id, type=type)
        print("The response of CompensationPlanningApi->call_329acecaa6df729733d0752aa9f6b204:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->call_329acecaa6df729733d0752aa9f6b204: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **type** | **str**| Worksheet context: recommendations, approvals, or overview (overview requires cycle admin). | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_3958585c861325ea7a2cd30a8c74f042**
> call_3958585c861325ea7a2cd30a8c74f042(id, model3958585c861325ea7a2cd30a8c74f042_request)

Add employees to cycle

Add employees to a compensation planning cycle.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.model3958585c861325ea7a2cd30a8c74f042_request import Model3958585c861325ea7a2cd30a8c74f042Request
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    model3958585c861325ea7a2cd30a8c74f042_request = bamboohr_sdk.Model3958585c861325ea7a2cd30a8c74f042Request() # Model3958585c861325ea7a2cd30a8c74f042Request | Employee IDs to add

    try:
        # Add employees to cycle
        api_instance.call_3958585c861325ea7a2cd30a8c74f042(id, model3958585c861325ea7a2cd30a8c74f042_request)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->call_3958585c861325ea7a2cd30a8c74f042: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **model3958585c861325ea7a2cd30a8c74f042_request** | [**Model3958585c861325ea7a2cd30a8c74f042Request**](Model3958585c861325ea7a2cd30a8c74f042Request.md)| Employee IDs to add | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Employees added successfully |  -  |
**400** | Invalid request data |  -  |
**403** | Insufficient permissions |  -  |
**404** | Resource not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_3a19f07aa737dc826ba43b9a1c1cd257**
> call_3a19f07aa737dc826ba43b9a1c1cd257(id)

Launch compensation planning cycle

Launch a compensation planning cycle. Validates all cycle data and sets status to Live.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 

    try:
        # Launch compensation planning cycle
        api_instance.call_3a19f07aa737dc826ba43b9a1c1cd257(id)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->call_3a19f07aa737dc826ba43b9a1c1cd257: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Cycle launched successfully |  -  |
**400** | Invalid request data |  -  |
**403** | Insufficient permissions |  -  |
**404** | Resource not found |  -  |
**409** | Cycle is not ready to launch |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_4e886b18264480611f380805301c49c4**
> Dict[str, object] call_4e886b18264480611f380805301c49c4(id, group_by=group_by)

Get compensation planning approval flows

Get approval flows for the compensation planning cycle (grouped by department by default).

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    group_by = 'group_by_example' # str | Optional grouping for flows (e.g. department) (optional)

    try:
        # Get compensation planning approval flows
        api_response = api_instance.call_4e886b18264480611f380805301c49c4(id, group_by=group_by)
        print("The response of CompensationPlanningApi->call_4e886b18264480611f380805301c49c4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->call_4e886b18264480611f380805301c49c4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **group_by** | **str**| Optional grouping for flows (e.g. department) | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Cycle not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_593d5bff120edf2a218a92022a682728**
> bytearray call_593d5bff120edf2a218a92022a682728(id, type=type)

Export compensation planning cycle worksheet to CSV

Download compensation planning worksheet data as a UTF-8 CSV (Excel-friendly BOM). Same data scope as GET worksheet; omit `type` for the default view.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    type = 'type_example' # str | Worksheet context: recommendations, approvals, or overview (overview requires cycle admin). (optional)

    try:
        # Export compensation planning cycle worksheet to CSV
        api_response = api_instance.call_593d5bff120edf2a218a92022a682728(id, type=type)
        print("The response of CompensationPlanningApi->call_593d5bff120edf2a218a92022a682728:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->call_593d5bff120edf2a218a92022a682728: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **type** | **str**| Worksheet context: recommendations, approvals, or overview (overview requires cycle admin). | [optional] 

### Return type

**bytearray**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV file download |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Worksheet not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_5c2b55158b0950b1e9211655666645b6**
> Dict[str, object] call_5c2b55158b0950b1e9211655666645b6(id)

Get compensation planning cycle details

Get compensation planning cycle details and currency settings for a cycle.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 

    try:
        # Get compensation planning cycle details
        api_response = api_instance.call_5c2b55158b0950b1e9211655666645b6(id)
        print("The response of CompensationPlanningApi->call_5c2b55158b0950b1e9211655666645b6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->call_5c2b55158b0950b1e9211655666645b6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**Dict[str, object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_5c4aab35a34f5760ec044104b5232bf5**
> Dict[str, object] call_5c4aab35a34f5760ec044104b5232bf5(id, employee_id, group_by=group_by)

Set final approver

Set or update the final approver for all approval flows in a cycle.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    employee_id = 'employee_id_example' # str | 
    group_by = 'group_by_example' # str | Optional grouping for returned flows (e.g. department) (optional)

    try:
        # Set final approver
        api_response = api_instance.call_5c4aab35a34f5760ec044104b5232bf5(id, employee_id, group_by=group_by)
        print("The response of CompensationPlanningApi->call_5c4aab35a34f5760ec044104b5232bf5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->call_5c4aab35a34f5760ec044104b5232bf5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **employee_id** | **str**|  | 
 **group_by** | **str**| Optional grouping for returned flows (e.g. department) | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated approval flows for the cycle |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_7efceaee2c010f88244dd01ee81e6e7b**
> Dict[str, object] call_7efceaee2c010f88244dd01ee81e6e7b(id)

Get compensation planning cycle budgets

Get budget guidelines and breakdown for the compensation planning cycle.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 

    try:
        # Get compensation planning cycle budgets
        api_response = api_instance.call_7efceaee2c010f88244dd01ee81e6e7b(id)
        print("The response of CompensationPlanningApi->call_7efceaee2c010f88244dd01ee81e6e7b:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->call_7efceaee2c010f88244dd01ee81e6e7b: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**Dict[str, object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_89a5068111ec499135c7d6e9a53d5a30**
> call_89a5068111ec499135c7d6e9a53d5a30(id, model89a5068111ec499135c7d6e9a53d5a30_request)

Remove employees from cycle

Remove employees from a compensation planning cycle.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.model89a5068111ec499135c7d6e9a53d5a30_request import Model89a5068111ec499135c7d6e9a53d5a30Request
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    model89a5068111ec499135c7d6e9a53d5a30_request = bamboohr_sdk.Model89a5068111ec499135c7d6e9a53d5a30Request() # Model89a5068111ec499135c7d6e9a53d5a30Request | Employee IDs to remove

    try:
        # Remove employees from cycle
        api_instance.call_89a5068111ec499135c7d6e9a53d5a30(id, model89a5068111ec499135c7d6e9a53d5a30_request)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->call_89a5068111ec499135c7d6e9a53d5a30: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **model89a5068111ec499135c7d6e9a53d5a30_request** | [**Model89a5068111ec499135c7d6e9a53d5a30Request**](Model89a5068111ec499135c7d6e9a53d5a30Request.md)| Employee IDs to remove | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Employees removed successfully |  -  |
**400** | Invalid request data |  -  |
**403** | Insufficient permissions |  -  |
**404** | Resource not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_9bc279d788f6e86b4cd8b2e0d3de91b1**
> Dict[str, object] call_9bc279d788f6e86b4cd8b2e0d3de91b1(id)

Get compensation planning cycle summary

Get compensation planning cycle summary (progress, stats).

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 

    try:
        # Get compensation planning cycle summary
        api_response = api_instance.call_9bc279d788f6e86b4cd8b2e0d3de91b1(id)
        print("The response of CompensationPlanningApi->call_9bc279d788f6e86b4cd8b2e0d3de91b1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->call_9bc279d788f6e86b4cd8b2e0d3de91b1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**Dict[str, object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf87b8e09a001b6fb81dfce6c20ab9e3**
> Dict[str, object] cf87b8e09a001b6fb81dfce6c20ab9e3(id, template_id, cf87b8e09a001b6fb81dfce6c20ab9e3_request, group_by=group_by)

Update approval flow

Update an approval flow for a compensation planning cycle. Allows modifying recommenders and approvers for a specific approval flow template.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.cf87b8e09a001b6fb81dfce6c20ab9e3_request import Cf87b8e09a001b6fb81dfce6c20ab9e3Request
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    template_id = 'template_id_example' # str | 
    cf87b8e09a001b6fb81dfce6c20ab9e3_request = bamboohr_sdk.Cf87b8e09a001b6fb81dfce6c20ab9e3Request() # Cf87b8e09a001b6fb81dfce6c20ab9e3Request | 
    group_by = 'group_by_example' # str | Optional grouping for returned flows (e.g. department) (optional)

    try:
        # Update approval flow
        api_response = api_instance.cf87b8e09a001b6fb81dfce6c20ab9e3(id, template_id, cf87b8e09a001b6fb81dfce6c20ab9e3_request, group_by=group_by)
        print("The response of CompensationPlanningApi->cf87b8e09a001b6fb81dfce6c20ab9e3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->cf87b8e09a001b6fb81dfce6c20ab9e3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **template_id** | **str**|  | 
 **cf87b8e09a001b6fb81dfce6c20ab9e3_request** | [**Cf87b8e09a001b6fb81dfce6c20ab9e3Request**](Cf87b8e09a001b6fb81dfce6c20ab9e3Request.md)|  | 
 **group_by** | **str**| Optional grouping for returned flows (e.g. department) | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated approval flows for the cycle |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d6987e300672a00c7cfe59afebb64156**
> Dict[str, object] d6987e300672a00c7cfe59afebb64156(id)

Get change communication letter details

Get change communication letter details for the compensation planning cycle.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 

    try:
        # Get change communication letter details
        api_response = api_instance.d6987e300672a00c7cfe59afebb64156(id)
        print("The response of CompensationPlanningApi->d6987e300672a00c7cfe59afebb64156:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->d6987e300672a00c7cfe59afebb64156: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**Dict[str, object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dacd313af2106213fc4696175941ce65**
> BudgetGuidelinesView dacd313af2106213fc4696175941ce65(id, dacd313af2106213fc4696175941ce65_request)

Save budget guidelines

Save budget guidelines for a compensation planning cycle.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.budget_guidelines_view import BudgetGuidelinesView
from bamboohr_sdk.models.dacd313af2106213fc4696175941ce65_request import Dacd313af2106213fc4696175941ce65Request
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    dacd313af2106213fc4696175941ce65_request = bamboohr_sdk.Dacd313af2106213fc4696175941ce65Request() # Dacd313af2106213fc4696175941ce65Request | Budget guideline settings

    try:
        # Save budget guidelines
        api_response = api_instance.dacd313af2106213fc4696175941ce65(id, dacd313af2106213fc4696175941ce65_request)
        print("The response of CompensationPlanningApi->dacd313af2106213fc4696175941ce65:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->dacd313af2106213fc4696175941ce65: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **dacd313af2106213fc4696175941ce65_request** | [**Dacd313af2106213fc4696175941ce65Request**](Dacd313af2106213fc4696175941ce65Request.md)| Budget guideline settings | 

### Return type

[**BudgetGuidelinesView**](BudgetGuidelinesView.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Guidelines saved successfully |  -  |
**400** | Invalid request data |  -  |
**403** | Insufficient permissions |  -  |
**404** | Resource not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **e2ac4e1535f296cb8901f209e04caa83**
> Dict[str, object] e2ac4e1535f296cb8901f209e04caa83()

Create compensation planning cycle

Create a new compensation planning cycle with default settings.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)

    try:
        # Create compensation planning cycle
        api_response = api_instance.e2ac4e1535f296cb8901f209e04caa83()
        print("The response of CompensationPlanningApi->e2ac4e1535f296cb8901f209e04caa83:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->e2ac4e1535f296cb8901f209e04caa83: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Cycle created successfully |  -  |
**400** | Invalid request data |  -  |
**403** | Insufficient permissions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ef7619b0ee4c8dc079aaea870cfbe81b**
> RemoveCycleAdminSelfResponse ef7619b0ee4c8dc079aaea870cfbe81b(id, employee_id)

Remove cycle admin

Remove a cycle admin by employee ID. Full account admins cannot be removed.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.remove_cycle_admin_self_response import RemoveCycleAdminSelfResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    employee_id = 'employee_id_example' # str | 

    try:
        # Remove cycle admin
        api_response = api_instance.ef7619b0ee4c8dc079aaea870cfbe81b(id, employee_id)
        print("The response of CompensationPlanningApi->ef7619b0ee4c8dc079aaea870cfbe81b:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->ef7619b0ee4c8dc079aaea870cfbe81b: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **employee_id** | **str**|  | 

### Return type

[**RemoveCycleAdminSelfResponse**](RemoveCycleAdminSelfResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Admin removed - current user removed themselves |  -  |
**204** | Cycle admin successfully removed |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **f3883a522dadbe9e11b34f8b656e3adb**
> Dict[str, object] f3883a522dadbe9e11b34f8b656e3adb(id, f3883a522dadbe9e11b34f8b656e3adb_request)

Save recommendations

Save compensation recommendations for an employee in a cycle.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.f3883a522dadbe9e11b34f8b656e3adb_request import F3883a522dadbe9e11b34f8b656e3adbRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 
    f3883a522dadbe9e11b34f8b656e3adb_request = bamboohr_sdk.F3883a522dadbe9e11b34f8b656e3adbRequest() # F3883a522dadbe9e11b34f8b656e3adbRequest | 

    try:
        # Save recommendations
        api_response = api_instance.f3883a522dadbe9e11b34f8b656e3adb(id, f3883a522dadbe9e11b34f8b656e3adb_request)
        print("The response of CompensationPlanningApi->f3883a522dadbe9e11b34f8b656e3adb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->f3883a522dadbe9e11b34f8b656e3adb: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **f3883a522dadbe9e11b34f8b656e3adb_request** | [**F3883a522dadbe9e11b34f8b656e3adbRequest**](F3883a522dadbe9e11b34f8b656e3adbRequest.md)|  | 

### Return type

**Dict[str, object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saved recommendation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **f4b431363af6573af46750f32632e88b**
> CompensationPlanningCycleCompleteResponse f4b431363af6573af46750f32632e88b(id)

Complete compensation planning cycle

Complete a compensation planning cycle and finalize employee compensation records.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.compensation_planning_cycle_complete_response import CompensationPlanningCycleCompleteResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CompensationPlanningApi(api_client)
    id = 56 # int | 

    try:
        # Complete compensation planning cycle
        api_response = api_instance.f4b431363af6573af46750f32632e88b(id)
        print("The response of CompensationPlanningApi->f4b431363af6573af46750f32632e88b:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationPlanningApi->f4b431363af6573af46750f32632e88b: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CompensationPlanningCycleCompleteResponse**](CompensationPlanningCycleCompleteResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cycle completed successfully |  -  |
**403** | Insufficient permissions |  -  |
**404** | Resource not found |  -  |
**409** | Cycle cannot be completed |  -  |
**422** | Employees with pay rate errors |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

