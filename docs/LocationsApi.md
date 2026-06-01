# bamboohr_sdk.LocationsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_location**](LocationsApi.md#create_location) | **POST** /api/v1/hris/org/locations | Create a job location
[**delete_location**](LocationsApi.md#delete_location) | **DELETE** /api/v1/hris/org/locations/{id} | Delete a job location
[**get_location**](LocationsApi.md#get_location) | **GET** /api/v1/hris/org/locations/{id} | Get a job location
[**get_locations**](LocationsApi.md#get_locations) | **GET** /api/v1/hris/org/locations | List job locations
[**update_location**](LocationsApi.md#update_location) | **PUT** /api/v1/hris/org/locations/{id} | Update a job location


# **create_location**
> LocationResponseObject create_location(create_location_request)

Create a job location

Creates a new job location. Requires a label and address. If remoteLocation is true, address fields are optional.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.create_location_request import CreateLocationRequest
from bamboohr_sdk.models.location_response_object import LocationResponseObject
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
    api_instance = bamboohr_sdk.LocationsApi(api_client)
    create_location_request = bamboohr_sdk.CreateLocationRequest() # CreateLocationRequest | 

    try:
        # Create a job location
        api_response = api_instance.create_location(create_location_request)
        print("The response of LocationsApi->create_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->create_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_location_request** | [**CreateLocationRequest**](CreateLocationRequest.md)|  | 

### Return type

[**LocationResponseObject**](LocationResponseObject.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created location |  -  |
**403** | Permission denied |  -  |
**404** | Location not found |  -  |
**409** | Duplicate location label |  -  |
**422** | Invalid fields |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_location**
> delete_location(id)

Delete a job location

Deletes a job location by its ID. Returns 204 No Content on success.

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
    api_instance = bamboohr_sdk.LocationsApi(api_client)
    id = 'id_example' # str | The ID of the location to delete

    try:
        # Delete a job location
        api_instance.delete_location(id)
    except Exception as e:
        print("Exception when calling LocationsApi->delete_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the location to delete | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Location deleted successfully |  -  |
**403** | Permission denied |  -  |
**409** | The location is in use and cannot be deleted. You can archive a location in use to prevent future usage. |  -  |
**404** | Location not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location**
> LocationResponseObject get_location(id, expand=expand)

Get a job location

Retrieves a single job location by its ID. Returns the full location resource including address details.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.location_response_object import LocationResponseObject
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
    api_instance = bamboohr_sdk.LocationsApi(api_client)
    id = 'id_example' # str | The ID of the location
    expand = [] # List[str] | Comma-separated list of related resources to expand. Supported values: state, country. Example: expand=state,country (optional) (default to [])

    try:
        # Get a job location
        api_response = api_instance.get_location(id, expand=expand)
        print("The response of LocationsApi->get_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the location | 
 **expand** | [**List[str]**](str.md)| Comma-separated list of related resources to expand. Supported values: state, country. Example: expand&#x3D;state,country | [optional] [default to []]

### Return type

[**LocationResponseObject**](LocationResponseObject.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested location |  -  |
**422** | Invalid expand options |  -  |
**403** | Permission denied |  -  |
**404** | Location not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locations**
> PagedLocationResponse get_locations(page_size=page_size, page=page, sort=sort, select=select, filter=filter, expand=expand)

List job locations

Retrieves a paginated list of job locations. Returns active locations by default. Supports pagination via page and pageSize query parameters.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.paged_location_response import PagedLocationResponse
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
    api_instance = bamboohr_sdk.LocationsApi(api_client)
    page_size = 500 # int | The number of items to return per page. (optional) (default to 500)
    page = 0 # int | The page number to retrieve. (optional) (default to 0)
    sort = '' # str | Ordering by OData (Open Data Protocol) v4 specification. Supported fields: label, archived, manageable, address/address1, address/address2, address/city, address/stateId, address/zipcode, address/countryId, address/timezone, address/remoteLocation, createdAt, archivedAt (optional) (default to '')
    select = '' # str | Projection (field selection) by OData specification. Supported fields: id, label, archived, manageable, address/address1, address/address2, address/city, address/stateId, address/zipcode, address/countryId, address/timezone, address/remoteLocation, createdAt, archivedAt (optional) (default to '')
    filter = '' # str | Filter by an OData (Open Data Protocol) v4 specification. Supported fields: id, label, archived, manageable, address/address1, address/address2, address/city, address/stateId, address/zipcode, address/countryId, address/timezone, address/remoteLocation (optional) (default to '')
    expand = [] # List[str] | Comma-separated list of related resources to expand. Supported values: state, country. Example: expand=state,country (optional) (default to [])

    try:
        # List job locations
        api_response = api_instance.get_locations(page_size=page_size, page=page, sort=sort, select=select, filter=filter, expand=expand)
        print("The response of LocationsApi->get_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 500]
 **page** | **int**| The page number to retrieve. | [optional] [default to 0]
 **sort** | **str**| Ordering by OData (Open Data Protocol) v4 specification. Supported fields: label, archived, manageable, address/address1, address/address2, address/city, address/stateId, address/zipcode, address/countryId, address/timezone, address/remoteLocation, createdAt, archivedAt | [optional] [default to &#39;&#39;]
 **select** | **str**| Projection (field selection) by OData specification. Supported fields: id, label, archived, manageable, address/address1, address/address2, address/city, address/stateId, address/zipcode, address/countryId, address/timezone, address/remoteLocation, createdAt, archivedAt | [optional] [default to &#39;&#39;]
 **filter** | **str**| Filter by an OData (Open Data Protocol) v4 specification. Supported fields: id, label, archived, manageable, address/address1, address/address2, address/city, address/stateId, address/zipcode, address/countryId, address/timezone, address/remoteLocation | [optional] [default to &#39;&#39;]
 **expand** | [**List[str]**](str.md)| Comma-separated list of related resources to expand. Supported values: state, country. Example: expand&#x3D;state,country | [optional] [default to []]

### Return type

[**PagedLocationResponse**](PagedLocationResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of job locations |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Invalid input. |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location**
> LocationResponseObject update_location(id, update_location_request)

Update a job location

Updates an existing job location.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.location_response_object import LocationResponseObject
from bamboohr_sdk.models.update_location_request import UpdateLocationRequest
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
    api_instance = bamboohr_sdk.LocationsApi(api_client)
    id = 'id_example' # str | The ID of the location to update
    update_location_request = bamboohr_sdk.UpdateLocationRequest() # UpdateLocationRequest | 

    try:
        # Update a job location
        api_response = api_instance.update_location(id, update_location_request)
        print("The response of LocationsApi->update_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->update_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the location to update | 
 **update_location_request** | [**UpdateLocationRequest**](UpdateLocationRequest.md)|  | 

### Return type

[**LocationResponseObject**](LocationResponseObject.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated location |  -  |
**403** | Permission denied |  -  |
**404** | Location not found |  -  |
**409** | Duplicate location label |  -  |
**422** | Invalid fields |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

