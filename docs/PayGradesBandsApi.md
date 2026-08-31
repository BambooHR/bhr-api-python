# bamboohr_sdk.PayGradesBandsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_compensation_level_groups_or_level**](PayGradesBandsApi.md#delete_compensation_level_groups_or_level) | **DELETE** /api/v1/pay-grades-and-bands/levels/{segment} | Delete Compensation Level Groups or Level
[**get_compensation_level_group_status_counts**](PayGradesBandsApi.md#get_compensation_level_group_status_counts) | **GET** /api/v1/pay-grades-and-bands/status-counts | Get Compensation Level Group Status Counts
[**get_job_title_level_assignments**](PayGradesBandsApi.md#get_job_title_level_assignments) | **GET** /api/v1/pay-grades-and-bands/job-titles | Get Job Titles and Level Assignments
[**get_levels_and_bands_review**](PayGradesBandsApi.md#get_levels_and_bands_review) | **GET** /api/v1/pay-grades-and-bands/review | Get Levels and Bands Review
[**get_levels_and_bands_status**](PayGradesBandsApi.md#get_levels_and_bands_status) | **GET** /api/v1/pay-grades-and-bands/status | Get Levels and Bands Status
[**get_pay_bands**](PayGradesBandsApi.md#get_pay_bands) | **GET** /api/v1/pay-grades-and-bands/pay-bands | Get Pay Bands
[**get_published_levels_and_bands**](PayGradesBandsApi.md#get_published_levels_and_bands) | **GET** /api/v1/pay-grades-and-bands | Get Published Levels and Bands
[**list_compensation_level_groups_and_levels**](PayGradesBandsApi.md#list_compensation_level_groups_and_levels) | **GET** /api/v1/pay-grades-and-bands/levels | List Compensation Level Groups and Levels
[**list_job_titles_with_employees**](PayGradesBandsApi.md#list_job_titles_with_employees) | **GET** /api/v1/pay-grades-and-bands/job-titles-with-employees | List Job Titles with Employees
[**publish_draft_compensation_level_groups**](PayGradesBandsApi.md#publish_draft_compensation_level_groups) | **POST** /api/v1/pay-grades-and-bands/publish | Publish Draft Compensation Level Groups
[**replace_job_title_level_assignments**](PayGradesBandsApi.md#replace_job_title_level_assignments) | **PUT** /api/v1/pay-grades-and-bands/job-titles | Replace Job Title Level Assignments
[**update_compensation_level_groups_and_levels**](PayGradesBandsApi.md#update_compensation_level_groups_and_levels) | **PUT** /api/v1/pay-grades-and-bands/levels | Update Compensation Level Groups and Levels
[**update_pay_bands**](PayGradesBandsApi.md#update_pay_bands) | **PUT** /api/v1/pay-grades-and-bands/pay-bands | Update Pay Bands
[**upload_levels_and_bands_csv**](PayGradesBandsApi.md#upload_levels_and_bands_csv) | **POST** /api/v1/pay-grades-and-bands/import | Upload Levels and Bands CSV


# **delete_compensation_level_groups_or_level**
> PayGradesAndBandsDeleteResponse delete_compensation_level_groups_or_level(segment)

Delete Compensation Level Groups or Level

Deletes compensation level configuration, with the behavior chosen by the `{segment}` path value. When `{segment}` is a group status (`draft`, `published`, or `historic`), every compensation level group in that status is deleted and the response is the object `{"status":"success"}`; deleting `draft` discards all in-progress edits and is the way to reset the working draft. When `{segment}` is a numeric compensation level ID, only that single level is deleted and the response is the updated groups-and-levels hierarchy, the same object shape returned by List Compensation Level Groups and Levels (`list-compensation-level-groups-and-levels`). Deleting a numeric level ID that does not exist is a no-op that returns 200 with the unchanged hierarchy. The accepted `{segment}` values are the group lifecycle statuses `draft`, `published`, and `historic`, or a numeric level ID. Discover level IDs with List Compensation Level Groups and Levels (`list-compensation-level-groups-and-levels`). Edit level and group structure with Update Compensation Level Groups and Levels (`update-compensation-level-groups-and-levels`), and promote draft changes to published with Publish Draft Compensation Level Groups (`publish-draft-compensation-level-groups`). This operation mutates the stored configuration directly and cannot be undone.

OAuth Scopes: pay_grades_and_bands.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.pay_grades_and_bands_delete_response import PayGradesAndBandsDeleteResponse
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
    api_instance = bamboohr_sdk.PayGradesBandsApi(api_client)
    segment = 'draft' # str | Selects what to delete. A group status (`draft`, `published`, or `historic`) deletes all compensation level groups in that status; a numeric compensation level ID deletes that single level. Any other value returns 400.

    try:
        # Delete Compensation Level Groups or Level
        api_response = api_instance.delete_compensation_level_groups_or_level(segment)
        print("The response of PayGradesBandsApi->delete_compensation_level_groups_or_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayGradesBandsApi->delete_compensation_level_groups_or_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment** | **str**| Selects what to delete. A group status (&#x60;draft&#x60;, &#x60;published&#x60;, or &#x60;historic&#x60;) deletes all compensation level groups in that status; a numeric compensation level ID deletes that single level. Any other value returns 400. | 

### Return type

[**PayGradesAndBandsDeleteResponse**](PayGradesAndBandsDeleteResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deletion succeeded. For a group-status segment the body is &#x60;{\&quot;status\&quot;:\&quot;success\&quot;}&#x60;. For a numeric level-ID segment the body is the updated compensation level groups-and-levels hierarchy. |  -  |
**400** | The &#x60;{segment}&#x60; value is not a group status or a numeric level ID, or the deletion could not be completed. |  -  |
**403** | The authenticated caller lacks permission to modify pay grades and bands. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compensation_level_group_status_counts**
> LevelsAndBandsGroupStatusCounts get_compensation_level_group_status_counts()

Get Compensation Level Group Status Counts

Returns the number of compensation level groups in each lifecycle status. The response is a JSON object of integer counts keyed by status: `draft`, `historic`, and `published`. When a published baseline exists, the `draft` count includes only draft groups that have at least one visited setup step (groups the user has actually started editing), not every draft group; when no published groups exist, it counts all draft groups. Use this for a tally of how many groups sit in each status; for the overall setup configuration status (whether each setup step is complete, with its blocking errors and warnings), use Get Levels and Bands Status (`get-levels-and-bands-status`) instead.

OAuth Scopes: pay_grades_and_bands

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.levels_and_bands_group_status_counts import LevelsAndBandsGroupStatusCounts
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
    api_instance = bamboohr_sdk.PayGradesBandsApi(api_client)

    try:
        # Get Compensation Level Group Status Counts
        api_response = api_instance.get_compensation_level_group_status_counts()
        print("The response of PayGradesBandsApi->get_compensation_level_group_status_counts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayGradesBandsApi->get_compensation_level_group_status_counts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LevelsAndBandsGroupStatusCounts**](LevelsAndBandsGroupStatusCounts.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compensation level group counts by status, as a JSON object with integer &#x60;draft&#x60;, &#x60;historic&#x60;, and &#x60;published&#x60; counts. |  -  |
**403** | Insufficient permissions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_title_level_assignments**
> PayGradesAndBandsJobTitleAssignmentsResponse get_job_title_level_assignments()

Get Job Titles and Level Assignments

Returns the working draft configuration showing which job titles are assigned to each compensation level, as used by the pay grades and bands setup wizard. When no draft configuration exists, the endpoint returns the currently published configuration instead. The response is a JSON object with a `groups` array; each group carries its `levels`, and each level lists the `jobTitles` assigned to it alongside its pay band flattened into `min`, `mid`, `max`, and `percentageRange` value objects (each wrapping a numeric `value` plus its own `errors` and `warnings`), `currencyCode`, and `compensationType`. The per-group and per-level `errors` and `warnings` arrays are always empty on this view; job-title assignment issues are reported by Get Levels and Bands Status (`get-levels-and-bands-status`) instead. Each job title carries a job title identifier and its name; no employee data is included. To see which employees currently hold each job title, use List Job Titles with Employees (`list-job-titles-with-employees`) instead. This is a read-only view. For the same group/level tree focused on level configuration use List Compensation Level Groups and Levels (`list-compensation-level-groups-and-levels`), for pay band values use Get Pay Bands (`get-pay-bands`), and for the published configuration without validation state use Get Published Levels and Bands (`get-published-levels-and-bands`) instead.

OAuth Scopes: pay_grades_and_bands

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.pay_grades_and_bands_job_title_assignments_response import PayGradesAndBandsJobTitleAssignmentsResponse
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
    api_instance = bamboohr_sdk.PayGradesBandsApi(api_client)

    try:
        # Get Job Titles and Level Assignments
        api_response = api_instance.get_job_title_level_assignments()
        print("The response of PayGradesBandsApi->get_job_title_level_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayGradesBandsApi->get_job_title_level_assignments: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PayGradesAndBandsJobTitleAssignmentsResponse**](PayGradesAndBandsJobTitleAssignmentsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The working pay grades and bands configuration (the draft when one exists, otherwise the currently published configuration): job-title-to-level assignments with validation state, as an object with a &#x60;groups&#x60; array. |  -  |
**403** | Insufficient permissions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_levels_and_bands_review**
> PayGradesAndBandsReviewResponse get_levels_and_bands_review()

Get Levels and Bands Review

Returns the pre-publish review of compensation level groups and levels with validation `errors` and `warnings` consolidated across every setup-wizard step: level naming, group-level checks, and pay band values. This reflects the working draft configuration; when no draft exists it falls back to the currently published configuration. Requesting this review marks all setup steps as visited for the draft, which changes subsequent Get Levels and Bands Status (`get-levels-and-bands-status`) results. The response is a JSON object with a `groups` array; each group carries its `levels` plus its own `errors` and `warnings`, and each level flattens its pay band into `min`, `mid`, `max`, and `percentageRange` value objects (each wrapping a numeric `value` with its own `errors` and `warnings`), along with `currencyCode`, `compensationType`, and the `jobTitles` assigned to that level. Use this for the complete validation picture that determines whether the configuration can be published. For the editable draft view that validates level and group issues but not pay band values, use List Compensation Level Groups and Levels (`list-compensation-level-groups-and-levels`) instead. For the currently published pay grades and bands without any validation state, use Get Published Levels and Bands (`get-published-levels-and-bands`) instead.

OAuth Scopes: pay_grades_and_bands

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.pay_grades_and_bands_review_response import PayGradesAndBandsReviewResponse
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
    api_instance = bamboohr_sdk.PayGradesBandsApi(api_client)

    try:
        # Get Levels and Bands Review
        api_response = api_instance.get_levels_and_bands_review()
        print("The response of PayGradesBandsApi->get_levels_and_bands_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayGradesBandsApi->get_levels_and_bands_review: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PayGradesAndBandsReviewResponse**](PayGradesAndBandsReviewResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compensation level groups and levels with consolidated validation state, as an object with a &#x60;groups&#x60; array. |  -  |
**403** | Insufficient permissions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_levels_and_bands_status**
> PayGradesAndBandsConfigurationStatus get_levels_and_bands_status()

Get Levels and Bands Status

Returns the configuration status of the Pay Grades & Bands (levels and bands) setup, broken down by setup step. The response is an object with four step keys, `levels`, `payBands`, `jobTitles`, and `review`, each reporting an `isComplete` flag plus `errors` (blocking issues) and `warnings` (non-blocking issues) arrays; the arrays are empty when a step has no outstanding issues. A setup step that has not yet been visited reports `isComplete: false` with empty `errors` and `warnings`, so empty arrays do not necessarily mean the step has no outstanding issues; the step simply has not been evaluated yet. For the `levels`, `payBands`, and `review` steps, each error or warning identifies the offending compensation level group and level; a `levelId` of `0` is a sentinel meaning the issue applies to the group as a whole rather than to a specific level. For `jobTitles`, each warning is a job title that is not yet assigned to a level. Use this to check whether the setup is complete before publishing. For the number of compensation level groups in each status (draft, published, historic), use Get Compensation Level Group Status Counts (`get-compensation-level-group-status-counts`) instead.

OAuth Scopes: pay_grades_and_bands

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.pay_grades_and_bands_configuration_status import PayGradesAndBandsConfigurationStatus
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
    api_instance = bamboohr_sdk.PayGradesBandsApi(api_client)

    try:
        # Get Levels and Bands Status
        api_response = api_instance.get_levels_and_bands_status()
        print("The response of PayGradesBandsApi->get_levels_and_bands_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayGradesBandsApi->get_levels_and_bands_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PayGradesAndBandsConfigurationStatus**](PayGradesAndBandsConfigurationStatus.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. Returns an object keyed by setup step (&#x60;levels&#x60;, &#x60;payBands&#x60;, &#x60;jobTitles&#x60;, &#x60;review&#x60;). |  -  |
**403** | Insufficient permissions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_bands**
> PayGradesAndBandsPayBandsResponse get_pay_bands()

Get Pay Bands

Returns the working draft pay band configuration for every compensation level, including the pay-band-step validation `errors` and `warnings` used by the setup wizard. When no draft configuration exists, the endpoint returns the currently published configuration instead. The response is a JSON object with a `groups` array; each group carries its `levels`, and each level flattens its pay band into `min`, `mid`, `max`, and `percentageRange` value objects (each wrapping a numeric `value` plus its own `errors` and `warnings`), along with `currencyCode`, `compensationType`, and the `jobTitles` assigned to that level. A level is a percentage-based band when `percentageRange.value` is set, and a min-mid-max band when `percentageRange.value` is null. This view surfaces validation for the pay-band setup step; for the same structure with levels-step validation use List Compensation Level Groups and Levels (`list-compensation-level-groups-and-levels`), and for the published configuration without validation state use Get Published Levels and Bands (`get-published-levels-and-bands`).

OAuth Scopes: pay_grades_and_bands

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.pay_grades_and_bands_pay_bands_response import PayGradesAndBandsPayBandsResponse
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
    api_instance = bamboohr_sdk.PayGradesBandsApi(api_client)

    try:
        # Get Pay Bands
        api_response = api_instance.get_pay_bands()
        print("The response of PayGradesBandsApi->get_pay_bands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayGradesBandsApi->get_pay_bands: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PayGradesAndBandsPayBandsResponse**](PayGradesAndBandsPayBandsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The working pay grades and bands configuration (the draft when one exists, otherwise the currently published configuration): pay band values with validation state, as an object with a &#x60;groups&#x60; array. |  -  |
**403** | Insufficient permissions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_published_levels_and_bands**
> PayGradesAndBandsPublishedResponse get_published_levels_and_bands()

Get Published Levels and Bands

Returns the currently published pay grades and bands as a JSON object with a `groups` array. Each group carries its published compensation levels, and each level flattens its pay band into `min`, `mid`, `max`, `currencyCode`, `percentageRange`, and `compensationType`, plus the job titles assigned to that level. Note the asymmetry: `min`, `mid`, and `max` are plain numbers, while `percentageRange` is an object (`LevelsAndBands-PayBandValue`) carrying its own validation state whose `value` is null for min-mid-max bands. Only published groups are returned; the `groups` array is empty when nothing has been published (this is a status filter, not a permission filter). Unlike the configuration-wizard endpoints, this published view omits the per-group and per-level validation `errors` and `warnings`. For the editable draft configuration with validation state, use List Compensation Level Groups and Levels (`list-compensation-level-groups-and-levels`) instead.

OAuth Scopes: pay_grades_and_bands

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.pay_grades_and_bands_published_response import PayGradesAndBandsPublishedResponse
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
    api_instance = bamboohr_sdk.PayGradesBandsApi(api_client)

    try:
        # Get Published Levels and Bands
        api_response = api_instance.get_published_levels_and_bands()
        print("The response of PayGradesBandsApi->get_published_levels_and_bands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayGradesBandsApi->get_published_levels_and_bands: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PayGradesAndBandsPublishedResponse**](PayGradesAndBandsPublishedResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Published pay grades and bands as an object with a &#x60;groups&#x60; array. |  -  |
**403** | Insufficient permissions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compensation_level_groups_and_levels**
> PayGradesAndBandsLevelsResponse list_compensation_level_groups_and_levels()

List Compensation Level Groups and Levels

Returns the working draft configuration of compensation level groups and levels, including the per-group and per-level validation `errors` and `warnings` used by the setup wizard. When no draft configuration exists, the endpoint returns the currently published configuration instead. The response is a JSON object with a `groups` array; each group carries its `levels`, and each level flattens its pay band into `min`, `mid`, `max`, and `percentageRange` value objects (each wrapping a numeric `value` plus its own `errors` and `warnings`), along with `currencyCode`, `compensationType`, and the `jobTitles` assigned to that level. The pay band value objects are returned on this view, but their `errors` and `warnings` are not populated here; pay band values are validated only at review/publish. This is the editable draft/editor view: it reflects in-progress edits and surfaces levels-step validation state. For the same draft structure with pay-band-value validation populated use Get Pay Bands (`get-pay-bands`), and for the consolidated pre-publish validation across every step use Get Levels and Bands Review (`get-levels-and-bands-review`). For the currently published pay grades and bands without validation state, use Get Published Levels and Bands (`get-published-levels-and-bands`) instead.

OAuth Scopes: pay_grades_and_bands

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.pay_grades_and_bands_levels_response import PayGradesAndBandsLevelsResponse
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
    api_instance = bamboohr_sdk.PayGradesBandsApi(api_client)

    try:
        # List Compensation Level Groups and Levels
        api_response = api_instance.list_compensation_level_groups_and_levels()
        print("The response of PayGradesBandsApi->list_compensation_level_groups_and_levels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayGradesBandsApi->list_compensation_level_groups_and_levels: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PayGradesAndBandsLevelsResponse**](PayGradesAndBandsLevelsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The working pay grades and bands configuration (the draft when one exists, otherwise the currently published configuration): compensation level groups and levels with validation state, as an object with a &#x60;groups&#x60; array. |  -  |
**403** | Insufficient permissions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_job_titles_with_employees**
> List[PayGradesAndBandsJobTitleWithEmployees] list_job_titles_with_employees()

List Job Titles with Employees

Returns every active, non-archived company job title (not only titles used in the pay grades and bands configuration) together with the employees who currently hold each title. The response is a JSON array of job title objects; each carries the job title `id`, its `title` name, and an `employees` array. Each employee entry exposes the internal employee ID (`id` here; the same identifier is `employeeId` on List Employees and `eeid` on the employee dataset) alongside the employee display `name`. This internal employee ID is not the editable Employee # (`employeeNumber`); using `employeeNumber` in its place may resolve to a different employee. An employee is omitted from a title's `employees` array when the authenticated caller lacks permission to view a required employee field (name, job title, or id), so an empty `employees` array does not necessarily mean no one holds that title; it can also mean the caller cannot see the employees who do. The array is empty when no job titles exist. This is a read-only view. Use this to see which employees occupy each job title; for the draft assignment of job titles to compensation levels (which returns no employee data), use Get Job Titles and Level Assignments (`get-job-title-level-assignments`) instead.

OAuth Scopes: pay_grades_and_bands

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.pay_grades_and_bands_job_title_with_employees import PayGradesAndBandsJobTitleWithEmployees
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
    api_instance = bamboohr_sdk.PayGradesBandsApi(api_client)

    try:
        # List Job Titles with Employees
        api_response = api_instance.list_job_titles_with_employees()
        print("The response of PayGradesBandsApi->list_job_titles_with_employees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayGradesBandsApi->list_job_titles_with_employees: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PayGradesAndBandsJobTitleWithEmployees]**](PayGradesAndBandsJobTitleWithEmployees.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job titles with the employees holding each, as a JSON array. Empty only when the company has no active, non-archived job titles. |  -  |
**403** | Insufficient permissions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_draft_compensation_level_groups**
> PayGradesAndBandsPublishResponse publish_draft_compensation_level_groups()

Publish Draft Compensation Level Groups

Publishes the company draft compensation configuration, promoting every draft compensation level group, along with its levels, pay bands, and job-title assignments, to the live published set. Any previously published groups are marked historic in the same operation. This is a bodyless POST that takes no request body and always publishes the entire current draft. Build the draft first with Update Compensation Level Groups and Levels (`update-compensation-level-groups-and-levels`), Update Pay Bands (`update-pay-bands`), and Replace Job Title Level Assignments (`replace-job-title-level-assignments`), then publish. Publishing is rejected with a 400 when the draft has unresolved validation errors or warnings. When no draft exists the call is a no-op and still returns success. On success the response is the JSON object `{"status":"success"}`. Read the published result back with Get Published Levels and Bands (`get-published-levels-and-bands`).

OAuth Scopes: pay_grades_and_bands.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.pay_grades_and_bands_publish_response import PayGradesAndBandsPublishResponse
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
    api_instance = bamboohr_sdk.PayGradesBandsApi(api_client)

    try:
        # Publish Draft Compensation Level Groups
        api_response = api_instance.publish_draft_compensation_level_groups()
        print("The response of PayGradesBandsApi->publish_draft_compensation_level_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayGradesBandsApi->publish_draft_compensation_level_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PayGradesAndBandsPublishResponse**](PayGradesAndBandsPublishResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Draft compensation level groups published, or no draft existed and nothing changed. Returns the JSON object &#x60;{\&quot;status\&quot;:\&quot;success\&quot;}&#x60;. |  -  |
**400** | The draft has unresolved validation errors or warnings and cannot be published. |  -  |
**403** | Insufficient permissions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_job_title_level_assignments**
> PayGradesAndBandsUpdateJobTitlesResponse replace_job_title_level_assignments(levels_and_bands_job_title_assignments_request)

Replace Job Title Level Assignments

Replaces the complete set of draft job title-to-compensation-level assignments with the associations in the request. This is a full replacement: all existing draft job title assignments are deleted and replaced with those supplied, so any assignment omitted from the request is removed from the draft. Each entry pairs a job title with the compensation level it should map to. This endpoint writes only job-title assignments; define group and level structure with Update Compensation Level Groups and Levels (`update-compensation-level-groups-and-levels`) and set pay band values with Update Pay Bands (`update-pay-bands`). If no draft exists yet, one is created from the published structure and the supplied published level IDs are remapped onto the newly created draft levels, so later reads return draft-specific level IDs. Every target level must belong to a draft group, otherwise the request fails with 400. Discover job title and level IDs with Get Job Titles and Level Assignments (`get-job-title-level-assignments`). Assignments are written to the draft only; publish them with Publish Draft Compensation Level Groups (`publish-draft-compensation-level-groups`). Returns an object with a single `status` field set to `success`.

OAuth Scopes: pay_grades_and_bands.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.levels_and_bands_job_title_assignments_request import LevelsAndBandsJobTitleAssignmentsRequest
from bamboohr_sdk.models.pay_grades_and_bands_update_job_titles_response import PayGradesAndBandsUpdateJobTitlesResponse
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
    api_instance = bamboohr_sdk.PayGradesBandsApi(api_client)
    levels_and_bands_job_title_assignments_request = bamboohr_sdk.LevelsAndBandsJobTitleAssignmentsRequest() # LevelsAndBandsJobTitleAssignmentsRequest | 

    try:
        # Replace Job Title Level Assignments
        api_response = api_instance.replace_job_title_level_assignments(levels_and_bands_job_title_assignments_request)
        print("The response of PayGradesBandsApi->replace_job_title_level_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayGradesBandsApi->replace_job_title_level_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **levels_and_bands_job_title_assignments_request** | [**LevelsAndBandsJobTitleAssignmentsRequest**](LevelsAndBandsJobTitleAssignmentsRequest.md)|  | 

### Return type

[**PayGradesAndBandsUpdateJobTitlesResponse**](PayGradesAndBandsUpdateJobTitlesResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Draft job title assignments replaced. Returns an object with a &#x60;status&#x60; field set to &#x60;success&#x60;. |  -  |
**400** | Returned when a target level does not belong to a draft group. |  -  |
**403** | The authenticated caller lacks permission to update pay grades and bands. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_compensation_level_groups_and_levels**
> PayGradesAndBandsSaveLevelsResponse update_compensation_level_groups_and_levels(pay_grades_and_bands_update_levels_request)

Update Compensation Level Groups and Levels

Creates or updates compensation level groups and their levels in the company draft configuration. If no draft exists yet, one is created from the currently published configuration before changes are applied, and published group and level identifiers are mapped to their new draft counterparts. This is a partial upsert. Groups and levels omitted from the request are left unchanged, so it does not overwrite the full set. A group is deleted when its `groupName` is blank or null and it has no levels. A level is deleted when its `levelName` is blank or null and a `levelId` is supplied. Only group and level names and structure are persisted here. The per-level `compensationType` in the request is not applied by this endpoint; a newly created level derives its compensation type from the group's existing compensation type (or `Salary` when the group has none), and existing levels keep their compensation type unchanged. Pay band values (`min`, `mid`, `max`, `percentageRange`, `currencyCode`) and job-title assignments may be present in the payload but are not saved by this endpoint; set pay band values with Update Pay Bands (`update-pay-bands`) and set job-title assignments with Replace Job Title Level Assignments (`replace-job-title-level-assignments`). Changes stay in draft until promoted. Publish them with Publish Draft Compensation Level Groups (`publish-draft-compensation-level-groups`). Read the current draft back with List Compensation Level Groups and Levels (`list-compensation-level-groups-and-levels`). On success the response is a JSON object `{"status":"success"}`.

OAuth Scopes: pay_grades_and_bands.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.pay_grades_and_bands_save_levels_response import PayGradesAndBandsSaveLevelsResponse
from bamboohr_sdk.models.pay_grades_and_bands_update_levels_request import PayGradesAndBandsUpdateLevelsRequest
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
    api_instance = bamboohr_sdk.PayGradesBandsApi(api_client)
    pay_grades_and_bands_update_levels_request = bamboohr_sdk.PayGradesAndBandsUpdateLevelsRequest() # PayGradesAndBandsUpdateLevelsRequest | 

    try:
        # Update Compensation Level Groups and Levels
        api_response = api_instance.update_compensation_level_groups_and_levels(pay_grades_and_bands_update_levels_request)
        print("The response of PayGradesBandsApi->update_compensation_level_groups_and_levels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayGradesBandsApi->update_compensation_level_groups_and_levels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_grades_and_bands_update_levels_request** | [**PayGradesAndBandsUpdateLevelsRequest**](PayGradesAndBandsUpdateLevelsRequest.md)|  | 

### Return type

[**PayGradesAndBandsSaveLevelsResponse**](PayGradesAndBandsSaveLevelsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Groups and levels saved to the draft configuration. Returns the JSON object &#x60;{\&quot;status\&quot;:\&quot;success\&quot;}&#x60;. |  -  |
**400** | Invalid request body, for example a missing &#x60;groups&#x60; array or a level assigned to the wrong group. |  -  |
**403** | Insufficient permissions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pay_bands**
> PayGradesAndBandsUpdatePayBandsResponse update_pay_bands(update_pay_bands_request)

Update Pay Bands

Updates the pay band values (`min`, `mid`, `max`, `percentageRange`) for compensation levels in the company's draft pay grades and bands. This is the only endpoint that persists pay band values; Update Compensation Level Groups and Levels (`update-compensation-level-groups-and-levels`) defines the group and level structure but does not save band values. Job-title assignments are set separately with Replace Job Title Level Assignments (`replace-job-title-level-assignments`). Supply the level IDs returned by Get Pay Bands (`get-pay-bands`). If no draft exists yet, one is created from the published structure and the supplied published level IDs are remapped onto the newly created draft levels, so later reads return draft-specific level IDs. When `payBandType` is `percentRange`, `min` and `max` are derived from `mid` and `percentageRange` and any supplied `min`/`max` are ignored; when `minMidMax`, the supplied `min`/`mid`/`max` are stored and `percentageRange` is cleared. Every target level must belong to a draft group, otherwise the request fails with 400. Values are written to the draft only; publish them with Publish Draft Compensation Level Groups (`publish-draft-compensation-level-groups`). Returns an object with a single `status` field set to `success`.

OAuth Scopes: pay_grades_and_bands.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.pay_grades_and_bands_update_pay_bands_response import PayGradesAndBandsUpdatePayBandsResponse
from bamboohr_sdk.models.update_pay_bands_request import UpdatePayBandsRequest
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
    api_instance = bamboohr_sdk.PayGradesBandsApi(api_client)
    update_pay_bands_request = bamboohr_sdk.UpdatePayBandsRequest() # UpdatePayBandsRequest | 

    try:
        # Update Pay Bands
        api_response = api_instance.update_pay_bands(update_pay_bands_request)
        print("The response of PayGradesBandsApi->update_pay_bands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayGradesBandsApi->update_pay_bands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_pay_bands_request** | [**UpdatePayBandsRequest**](UpdatePayBandsRequest.md)|  | 

### Return type

[**PayGradesAndBandsUpdatePayBandsResponse**](PayGradesAndBandsUpdatePayBandsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pay bands updated. Returns an object with a &#x60;status&#x60; field set to &#x60;success&#x60;. |  -  |
**400** | Returned when a pay band entry is missing its &#x60;levelId&#x60;, &#x60;payBandType&#x60; or &#x60;compensationType&#x60; is not a recognized value, or a target level does not belong to a draft group. |  -  |
**403** | The authenticated caller lacks permission to update pay grades and bands. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_levels_and_bands_csv**
> LevelsAndBandsUploadResponse upload_levels_and_bands_csv(file)

Upload Levels and Bands CSV

Parses an uploaded levels and bands CSV and returns a preview of the parsed rows along with a suggested column mapping. This validates and previews only; it does not persist anything or create a draft. The response is a JSON object with `uploadData`, an array of row arrays holding the raw cell strings for each data row, and `columnMap`, which pairs each CSV column header with the field it maps to (`expectedColumnKey`), or null when the header is not recognized. Recognized field keys are `groupName`, `levelName`, `min`, `mid`, `max`, `compensationType`, `currency`, and `jobTitles`. Use this to confirm a spreadsheet before writing; to persist the data, build the draft with Update Compensation Level Groups and Levels (`update-compensation-level-groups-and-levels`), Update Pay Bands (`update-pay-bands`), and Replace Job Title Level Assignments (`replace-job-title-level-assignments`), then publish it with Publish Draft Compensation Level Groups (`publish-draft-compensation-level-groups`).

OAuth Scopes: pay_grades_and_bands.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.levels_and_bands_upload_response import LevelsAndBandsUploadResponse
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
    api_instance = bamboohr_sdk.PayGradesBandsApi(api_client)
    file = None # bytearray | Levels and bands CSV file to parse and preview.

    try:
        # Upload Levels and Bands CSV
        api_response = api_instance.upload_levels_and_bands_csv(file)
        print("The response of PayGradesBandsApi->upload_levels_and_bands_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayGradesBandsApi->upload_levels_and_bands_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| Levels and bands CSV file to parse and preview. | 

### Return type

[**LevelsAndBandsUploadResponse**](LevelsAndBandsUploadResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the parsed CSV preview as a JSON object with &#x60;uploadData&#x60; (row arrays) and &#x60;columnMap&#x60; (header-to-field mapping). Nothing is persisted. |  -  |
**400** | The multipart request did not include a &#x60;file&#x60; part. |  -  |
**403** | The authenticated user lacks permission to import levels and bands. |  -  |
**422** | The uploaded CSV could not be parsed or contained no valid data rows. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

