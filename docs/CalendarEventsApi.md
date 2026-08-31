# bamboohr_sdk.CalendarEventsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_calendar_events**](CalendarEventsApi.md#list_calendar_events) | **GET** /api/v1/calendar-events | List Calendar Events


# **list_calendar_events**
> CalendarCalendarEventsListResponseV1 list_calendar_events(start, end, filter=filter, direct_reports_only=direct_reports_only, include_persons=include_persons, page=page, page_size=page_size)

List Calendar Events

Lists calendar events (time off, holidays, birthdays, and anniversaries) overlapping the requested date range. Events are sorted by start ascending, then type ascending (ANNIVERSARY, BIRTHDAY, HOLIDAY, TIME_OFF), then id ascending. TIME_OFF events represent approved requests only. Events the caller cannot view are silently omitted.

OAuth Scopes: calendar:events

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.calendar_calendar_events_list_response_v1 import CalendarCalendarEventsListResponseV1
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
    api_instance = bamboohr_sdk.CalendarEventsApi(api_client)
    start = '2013-10-20' # date | Inclusive start date (YYYY-MM-DD). Interpreted in the company timezone.
    end = '2013-10-20' # date | Inclusive end date (YYYY-MM-DD). Must be on or after start; the range must span less than one year.
    filter = 'filter_example' # str | OData filter expression applied to calendar events. Supported operators: `eq` (equals), `in` (value in list), `and` (combine clauses). Filterable fields: `type` (one of `TIME_OFF`, `HOLIDAY`, `BIRTHDAY`, `ANNIVERSARY`), `employeeId` (int), `department` (int), `division` (int), `location` (int). Per-employee filters have no effect on HOLIDAY events. Example: `type in ('TIME_OFF','HOLIDAY') and department in (10,20)`. (optional)
    direct_reports_only = False # bool | When true, restrict employee-bound events to the caller's direct reports. HOLIDAY events are unaffected. Callers with no direct reports receive an empty result for employee-bound types. (optional) (default to False)
    include_persons = False # bool | When true, embed a persons map (keyed by employee id) alongside the events. (optional) (default to False)
    page = 1 # int | The page number to retrieve. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List Calendar Events
        api_response = api_instance.list_calendar_events(start, end, filter=filter, direct_reports_only=direct_reports_only, include_persons=include_persons, page=page, page_size=page_size)
        print("The response of CalendarEventsApi->list_calendar_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarEventsApi->list_calendar_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| Inclusive start date (YYYY-MM-DD). Interpreted in the company timezone. | 
 **end** | **date**| Inclusive end date (YYYY-MM-DD). Must be on or after start; the range must span less than one year. | 
 **filter** | **str**| OData filter expression applied to calendar events. Supported operators: &#x60;eq&#x60; (equals), &#x60;in&#x60; (value in list), &#x60;and&#x60; (combine clauses). Filterable fields: &#x60;type&#x60; (one of &#x60;TIME_OFF&#x60;, &#x60;HOLIDAY&#x60;, &#x60;BIRTHDAY&#x60;, &#x60;ANNIVERSARY&#x60;), &#x60;employeeId&#x60; (int), &#x60;department&#x60; (int), &#x60;division&#x60; (int), &#x60;location&#x60; (int). Per-employee filters have no effect on HOLIDAY events. Example: &#x60;type in (&#39;TIME_OFF&#39;,&#39;HOLIDAY&#39;) and department in (10,20)&#x60;. | [optional] 
 **direct_reports_only** | **bool**| When true, restrict employee-bound events to the caller&#39;s direct reports. HOLIDAY events are unaffected. Callers with no direct reports receive an empty result for employee-bound types. | [optional] [default to False]
 **include_persons** | **bool**| When true, embed a persons map (keyed by employee id) alongside the events. | [optional] [default to False]
 **page** | **int**| The page number to retrieve. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**CalendarCalendarEventsListResponseV1**](CalendarCalendarEventsListResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of calendar events. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. The caller lacks the calendar events scope or permission. |  -  |
**422** | Invalid query parameters (missing or malformed start/end, end before start, range spanning a year or more, invalid pageSize, or a malformed filter). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

