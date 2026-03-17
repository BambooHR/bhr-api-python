# bamboohr_sdk.LoginApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](LoginApi.md#login) | **POST** /api/v1/login | Login


# **login**
> LoginResponse login(application_key, user, password, accept_header_parameter=accept_header_parameter, format=format, device_id=device_id)

Login

Exchanges username, password, and application key for a persistent API key scoped to that user and application. No pre-existing authentication is required; credentials are passed in the request body.

This endpoint is deprecated. Prefer OAuth or OpenID for new integrations.

`applicationKey` must correspond to a registered non-mobile application; iOS and Android app keys are explicitly rejected with a 403 (no body). The optional `deviceId` associates the generated key with a specific device.

Response format is determined by the `Accept` request header. Send `Accept: application/json` to receive JSON; omit the header or send any other value to receive XML. Alternatively, set `?format=json` in the query string to force JSON regardless of the `Accept` header.

### Example


```python
import bamboohr_sdk
from bamboohr_sdk.models.login_response import LoginResponse
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)


# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.LoginApi(api_client)
    application_key = 'application_key_example' # str | The API key of the registered application making the login request. Mobile application keys (iOS/Android) are not accepted.
    user = 'user_example' # str | The user's email address or username.
    password = 'password_example' # str | The user's password.
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)
    format = 'format_example' # str | When set to `json`, forces a JSON response regardless of the `Accept` header. (optional)
    device_id = 'device_id_example' # str | Optional device identifier. When provided, the generated API key is associated with this device. (optional)

    try:
        # Login
        api_response = api_instance.login(application_key, user, password, accept_header_parameter=accept_header_parameter, format=format, device_id=device_id)
        print("The response of LoginApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_key** | **str**| The API key of the registered application making the login request. Mobile application keys (iOS/Android) are not accepted. | 
 **user** | **str**| The user&#39;s email address or username. | 
 **password** | **str**| The user&#39;s password. | 
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **format** | **str**| When set to &#x60;json&#x60;, forces a JSON response regardless of the &#x60;Accept&#x60; header. | [optional] 
 **device_id** | **str**| Optional device identifier. When provided, the generated API key is associated with this device. | [optional] 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful authentication. |  -  |
**403** | Forbidden. Credential or key failure. Credential and key failures include a response body; mobile application key rejections return an empty body. |  -  |
**500** | Internal Server Error. API key creation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

