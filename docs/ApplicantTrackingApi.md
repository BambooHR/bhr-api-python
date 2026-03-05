# bamboohr_sdk.ApplicantTrackingApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_candidate**](ApplicantTrackingApi.md#add_new_candidate) | **POST** /api/v1/applicant_tracking/application | Create Candidate
[**add_new_job_opening**](ApplicantTrackingApi.md#add_new_job_opening) | **POST** /api/v1/applicant_tracking/job_opening | Create Job Opening
[**get_application_details**](ApplicantTrackingApi.md#get_application_details) | **GET** /api/v1/applicant_tracking/applications/{applicationId} | Get Job Application Details
[**get_applications**](ApplicantTrackingApi.md#get_applications) | **GET** /api/v1/applicant_tracking/applications | Get Job Applications
[**get_company_locations**](ApplicantTrackingApi.md#get_company_locations) | **GET** /api/v1/applicant_tracking/locations | Get Company Locations
[**get_hiring_leads**](ApplicantTrackingApi.md#get_hiring_leads) | **GET** /api/v1/applicant_tracking/hiring_leads | Get Hiring Leads
[**get_job_summaries**](ApplicantTrackingApi.md#get_job_summaries) | **GET** /api/v1/applicant_tracking/jobs | Get Job Summaries
[**get_statuses**](ApplicantTrackingApi.md#get_statuses) | **GET** /api/v1/applicant_tracking/statuses | Get Applicant Statuses
[**post_applicant_status**](ApplicantTrackingApi.md#post_applicant_status) | **POST** /api/v1/applicant_tracking/applications/{applicationId}/status | Update Applicant Status
[**post_application_comment**](ApplicantTrackingApi.md#post_application_comment) | **POST** /api/v1/applicant_tracking/applications/{applicationId}/comments | Create Job Application Comment


# **add_new_candidate**
> add_new_candidate(first_name, last_name, job_id, email=email, phone_number=phone_number, source=source, address=address, city=city, state=state, zip=zip, country=country, linkedin_url=linkedin_url, date_available=date_available, desired_salary=desired_salary, referred_by=referred_by, website_url=website_url, highest_education=highest_education, college_name=college_name, references=references, resume=resume, cover_letter=cover_letter)

Create Candidate

Add a new candidate application to a job opening. The owner of the API key used must have access to ATS settings.

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
    api_instance = bamboohr_sdk.ApplicantTrackingApi(api_client)
    first_name = 'first_name_example' # str | The first name of the candidate.
    last_name = 'last_name_example' # str | The last name of the candidate.
    job_id = 56 # int | The id of the job opening for the candidate application.
    email = 'email_example' # str | The email address of the candidate. (optional)
    phone_number = 'phone_number_example' # str | The phone number of the candidate. (optional)
    source = 'source_example' # str | The source of the candidate application, e.g. LinkedIn, Indeed, etc. (optional)
    address = 'address_example' # str | The street address of the candidate. (optional)
    city = 'city_example' # str | The city of the candidate. (optional)
    state = 'state_example' # str | The state or province of the candidate. Accepts state name, abbreviation, or ISO code. (optional)
    zip = 'zip_example' # str | The zip code or postal code of the candidate. (optional)
    country = 'country_example' # str | The country of the candidate. Accepts country name or ISO code. (optional)
    linkedin_url = 'linkedin_url_example' # str | The LinkedIn profile url of the candidate. (optional)
    date_available = 'date_available_example' # str | The available start date of the candidate with the format YYYY-MM-DD. (optional)
    desired_salary = 'desired_salary_example' # str | The desired salary of the candidate. (optional)
    referred_by = 'referred_by_example' # str | The person or entity that referred the candidate. (optional)
    website_url = 'website_url_example' # str | The personal website, blog, or online portfolio of the candidate. (optional)
    highest_education = 'highest_education_example' # str | The highest completed education level of the candidate. (optional)
    college_name = 'college_name_example' # str | The college or university of the candidate. (optional)
    references = 'references_example' # str | A list of references supplied by the candidate. (optional)
    resume = 'resume_example' # str | Resume of the candidate. (optional)
    cover_letter = 'cover_letter_example' # str | Cover letter of the candidate. (optional)

    try:
        # Create Candidate
        api_instance.add_new_candidate(first_name, last_name, job_id, email=email, phone_number=phone_number, source=source, address=address, city=city, state=state, zip=zip, country=country, linkedin_url=linkedin_url, date_available=date_available, desired_salary=desired_salary, referred_by=referred_by, website_url=website_url, highest_education=highest_education, college_name=college_name, references=references, resume=resume, cover_letter=cover_letter)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->add_new_candidate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**| The first name of the candidate. | 
 **last_name** | **str**| The last name of the candidate. | 
 **job_id** | **int**| The id of the job opening for the candidate application. | 
 **email** | **str**| The email address of the candidate. | [optional] 
 **phone_number** | **str**| The phone number of the candidate. | [optional] 
 **source** | **str**| The source of the candidate application, e.g. LinkedIn, Indeed, etc. | [optional] 
 **address** | **str**| The street address of the candidate. | [optional] 
 **city** | **str**| The city of the candidate. | [optional] 
 **state** | **str**| The state or province of the candidate. Accepts state name, abbreviation, or ISO code. | [optional] 
 **zip** | **str**| The zip code or postal code of the candidate. | [optional] 
 **country** | **str**| The country of the candidate. Accepts country name or ISO code. | [optional] 
 **linkedin_url** | **str**| The LinkedIn profile url of the candidate. | [optional] 
 **date_available** | **str**| The available start date of the candidate with the format YYYY-MM-DD. | [optional] 
 **desired_salary** | **str**| The desired salary of the candidate. | [optional] 
 **referred_by** | **str**| The person or entity that referred the candidate. | [optional] 
 **website_url** | **str**| The personal website, blog, or online portfolio of the candidate. | [optional] 
 **highest_education** | **str**| The highest completed education level of the candidate. | [optional] 
 **college_name** | **str**| The college or university of the candidate. | [optional] 
 **references** | **str**| A list of references supplied by the candidate. | [optional] 
 **resume** | **str**| Resume of the candidate. | [optional] 
 **cover_letter** | **str**| Cover letter of the candidate. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |
**422** | Unprocessable entity. One or more parameters failed validation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_new_job_opening**
> add_new_job_opening(posting_title, job_status, hiring_lead, employment_type, job_description, department=department, minimum_experience=minimum_experience, compensation=compensation, job_location=job_location, application_question_resume=application_question_resume, application_question_address=application_question_address, application_question_linkedin_url=application_question_linkedin_url, application_question_date_available=application_question_date_available, application_question_desired_salary=application_question_desired_salary, application_question_cover_letter=application_question_cover_letter, application_question_referred_by=application_question_referred_by, application_question_website_url=application_question_website_url, application_question_highest_education=application_question_highest_education, application_question_college=application_question_college, application_question_references=application_question_references, internal_job_code=internal_job_code)

Create Job Opening

Add a new job opening. The owner of the API key used must have access to ATS settings.

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
    api_instance = bamboohr_sdk.ApplicantTrackingApi(api_client)
    posting_title = 'posting_title_example' # str | The posting title of the job opening.
    job_status = 'job_status_example' # str | The status of the job opening.
    hiring_lead = 56 # int | The employee id (from the v1/applicant_tracking/hiring_leads endpoint) of the hiring lead for the job opening.
    employment_type = 'employment_type_example' # str | The type of employment offered in the job opening, e.g. Full-Time, Part-Time, Contractor, etc.
    job_description = 'job_description_example' # str | The long-form text description of the job opening.
    department = 'department_example' # str | The department of the job opening. (optional)
    minimum_experience = 'minimum_experience_example' # str | The minimum experience level that qualifies a candidate for the job opening. (optional)
    compensation = 'compensation_example' # str | The pay rate or compensation for the job opening. (optional)
    job_location = 56 # int | The location id (from the v1/applicant_tracking/locations endpoint) of the job opening. Omit this parameter for a remote job location. (optional)
    application_question_resume = 'application_question_resume_example' # str | Whether the job opening application has a standard question for resume (true) or not (false) or if uploading a resume is mandatory (required). (optional)
    application_question_address = 'application_question_address_example' # str | Whether the job opening application has a standard question for address (true) or not (false) or if entering an address is mandatory (required). (optional)
    application_question_linkedin_url = 'application_question_linkedin_url_example' # str | Whether the job opening application has a standard question for LinkedIn profile url (true) or not (false) or if entering a LinkedIn profile url is mandatory (required). (optional)
    application_question_date_available = 'application_question_date_available_example' # str | Whether the job opening application has a standard question for availability date (true) or not (false) or if entering an availability date is mandatory (required). (optional)
    application_question_desired_salary = 'application_question_desired_salary_example' # str | Whether the job opening application has a standard question for desired salary (true) or not (false) or if entering a desired salary is mandatory (required). (optional)
    application_question_cover_letter = 'application_question_cover_letter_example' # str | Whether the job opening application has a standard question for cover letter (true) or not (false) or if uploading a cover letter is mandatory (required). (optional)
    application_question_referred_by = 'application_question_referred_by_example' # str | Whether the job opening application has a standard question for referred by (true) or not (false) or if entering referred by is mandatory (required). (optional)
    application_question_website_url = 'application_question_website_url_example' # str | Whether the job opening application has a standard question for website url (true) or not (false) or if entering a website url is mandatory (required). (optional)
    application_question_highest_education = 'application_question_highest_education_example' # str | Whether the job opening application has a standard question for highest education (true) or not (false) or if entering highest education is mandatory (required). (optional)
    application_question_college = 'application_question_college_example' # str | Whether the job opening application has a standard question for college (true) or not (false) or if entering a college is mandatory (required). (optional)
    application_question_references = 'application_question_references_example' # str | Whether the job opening application has a standard question for references (true) or not (false) or if entering references is mandatory (required). (optional)
    internal_job_code = 'internal_job_code_example' # str | The internal job code for the job opening. (optional)

    try:
        # Create Job Opening
        api_instance.add_new_job_opening(posting_title, job_status, hiring_lead, employment_type, job_description, department=department, minimum_experience=minimum_experience, compensation=compensation, job_location=job_location, application_question_resume=application_question_resume, application_question_address=application_question_address, application_question_linkedin_url=application_question_linkedin_url, application_question_date_available=application_question_date_available, application_question_desired_salary=application_question_desired_salary, application_question_cover_letter=application_question_cover_letter, application_question_referred_by=application_question_referred_by, application_question_website_url=application_question_website_url, application_question_highest_education=application_question_highest_education, application_question_college=application_question_college, application_question_references=application_question_references, internal_job_code=internal_job_code)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->add_new_job_opening: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **posting_title** | **str**| The posting title of the job opening. | 
 **job_status** | **str**| The status of the job opening. | 
 **hiring_lead** | **int**| The employee id (from the v1/applicant_tracking/hiring_leads endpoint) of the hiring lead for the job opening. | 
 **employment_type** | **str**| The type of employment offered in the job opening, e.g. Full-Time, Part-Time, Contractor, etc. | 
 **job_description** | **str**| The long-form text description of the job opening. | 
 **department** | **str**| The department of the job opening. | [optional] 
 **minimum_experience** | **str**| The minimum experience level that qualifies a candidate for the job opening. | [optional] 
 **compensation** | **str**| The pay rate or compensation for the job opening. | [optional] 
 **job_location** | **int**| The location id (from the v1/applicant_tracking/locations endpoint) of the job opening. Omit this parameter for a remote job location. | [optional] 
 **application_question_resume** | **str**| Whether the job opening application has a standard question for resume (true) or not (false) or if uploading a resume is mandatory (required). | [optional] 
 **application_question_address** | **str**| Whether the job opening application has a standard question for address (true) or not (false) or if entering an address is mandatory (required). | [optional] 
 **application_question_linkedin_url** | **str**| Whether the job opening application has a standard question for LinkedIn profile url (true) or not (false) or if entering a LinkedIn profile url is mandatory (required). | [optional] 
 **application_question_date_available** | **str**| Whether the job opening application has a standard question for availability date (true) or not (false) or if entering an availability date is mandatory (required). | [optional] 
 **application_question_desired_salary** | **str**| Whether the job opening application has a standard question for desired salary (true) or not (false) or if entering a desired salary is mandatory (required). | [optional] 
 **application_question_cover_letter** | **str**| Whether the job opening application has a standard question for cover letter (true) or not (false) or if uploading a cover letter is mandatory (required). | [optional] 
 **application_question_referred_by** | **str**| Whether the job opening application has a standard question for referred by (true) or not (false) or if entering referred by is mandatory (required). | [optional] 
 **application_question_website_url** | **str**| Whether the job opening application has a standard question for website url (true) or not (false) or if entering a website url is mandatory (required). | [optional] 
 **application_question_highest_education** | **str**| Whether the job opening application has a standard question for highest education (true) or not (false) or if entering highest education is mandatory (required). | [optional] 
 **application_question_college** | **str**| Whether the job opening application has a standard question for college (true) or not (false) or if entering a college is mandatory (required). | [optional] 
 **application_question_references** | **str**| Whether the job opening application has a standard question for references (true) or not (false) or if entering references is mandatory (required). | [optional] 
 **internal_job_code** | **str**| The internal job code for the job opening. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |
**422** | Unprocessable entity. One or more parameters failed validation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_details**
> ApplicationDetails get_application_details(application_id)

Get Job Application Details

Get the details of an application. The owner of the API key used must have access to ATS settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.application_details import ApplicationDetails
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
    api_instance = bamboohr_sdk.ApplicantTrackingApi(api_client)
    application_id = 56 # int | The ID of the application to look up details.

    try:
        # Get Job Application Details
        api_response = api_instance.get_application_details(application_id)
        print("The response of ApplicantTrackingApi->get_application_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->get_application_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the application to look up details. | 

### Return type

[**ApplicationDetails**](ApplicationDetails.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications**
> ApplicationsList get_applications(page=page, job_id=job_id, application_status_id=application_status_id, application_status=application_status, job_status_groups=job_status_groups, search_string=search_string, sort_by=sort_by, sort_order=sort_order, new_since=new_since)

Get Job Applications

Get a list of applications. The owner of the API key used must have access to ATS settings. Combine as many different optional parameter filters as you like.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.applications_list import ApplicationsList
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
    api_instance = bamboohr_sdk.ApplicantTrackingApi(api_client)
    page = 56 # int | The page number (optional)
    job_id = 56 # int | A Job Id to limit results to (optional)
    application_status_id = 56 # int | Application status id to filter by. (optional)
    application_status = 'application_status_example' # str | A list of application status groups to filter by. (optional)
    job_status_groups = 'job_status_groups_example' # str | A list of position status groups to filter by. (optional)
    search_string = 'search_string_example' # str | A general search criteria by which to find applications. (optional)
    sort_by = 'sort_by_example' # str | A specific field to sort the results by. (optional)
    sort_order = 'sort_order_example' # str | Order by which to sort results. (optional)
    new_since = '2013-10-20T19:20:30+01:00' # datetime | Only get applications newer than a given UTC timestamp, for example 2024-01-01 13:00:00 (optional)

    try:
        # Get Job Applications
        api_response = api_instance.get_applications(page=page, job_id=job_id, application_status_id=application_status_id, application_status=application_status, job_status_groups=job_status_groups, search_string=search_string, sort_by=sort_by, sort_order=sort_order, new_since=new_since)
        print("The response of ApplicantTrackingApi->get_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->get_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number | [optional] 
 **job_id** | **int**| A Job Id to limit results to | [optional] 
 **application_status_id** | **int**| Application status id to filter by. | [optional] 
 **application_status** | **str**| A list of application status groups to filter by. | [optional] 
 **job_status_groups** | **str**| A list of position status groups to filter by. | [optional] 
 **search_string** | **str**| A general search criteria by which to find applications. | [optional] 
 **sort_by** | **str**| A specific field to sort the results by. | [optional] 
 **sort_order** | **str**| Order by which to sort results. | [optional] 
 **new_since** | **datetime**| Only get applications newer than a given UTC timestamp, for example 2024-01-01 13:00:00 | [optional] 

### Return type

[**ApplicationsList**](ApplicationsList.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns a paginated list of applications. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_locations**
> List[LocationsList] get_company_locations()

Get Company Locations

Get company locations for use in creating a new job opening. The owner of the API key used must have access to ATS settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.locations_list import LocationsList
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
    api_instance = bamboohr_sdk.ApplicantTrackingApi(api_client)

    try:
        # Get Company Locations
        api_response = api_instance.get_company_locations()
        print("The response of ApplicantTrackingApi->get_company_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->get_company_locations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[LocationsList]**](LocationsList.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hiring_leads**
> List[HiringLeadsList] get_hiring_leads()

Get Hiring Leads

Get potential hiring leads for use in creating a new job opening. The owner of the API key used must have access to ATS settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.hiring_leads_list import HiringLeadsList
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
    api_instance = bamboohr_sdk.ApplicantTrackingApi(api_client)

    try:
        # Get Hiring Leads
        api_response = api_instance.get_hiring_leads()
        print("The response of ApplicantTrackingApi->get_hiring_leads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->get_hiring_leads: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[HiringLeadsList]**](HiringLeadsList.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_summaries**
> get_job_summaries(status_groups=status_groups, sort_by=sort_by, sort_order=sort_order)

Get Job Summaries

Get a list of job summaries. The owner of the API key used must have access to ATS settings. Combine as many different optional parameter filters as you like.

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
    api_instance = bamboohr_sdk.ApplicantTrackingApi(api_client)
    status_groups = 'status_groups_example' # str | A list of status groups to filter positions by. (optional)
    sort_by = 'sort_by_example' # str | A specific field to sort the results by. (optional)
    sort_order = 'sort_order_example' # str | Order by which to sort results. (optional)

    try:
        # Get Job Summaries
        api_instance.get_job_summaries(status_groups=status_groups, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->get_job_summaries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_groups** | **str**| A list of status groups to filter positions by. | [optional] 
 **sort_by** | **str**| A specific field to sort the results by. | [optional] 
 **sort_order** | **str**| Order by which to sort results. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statuses**
> get_statuses()

Get Applicant Statuses

Get a list of statuses for a company. The owner of the API key used must have access to ATS settings.

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
    api_instance = bamboohr_sdk.ApplicantTrackingApi(api_client)

    try:
        # Get Applicant Statuses
        api_instance.get_statuses()
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->get_statuses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_applicant_status**
> post_applicant_status(application_id, post_applicant_status_request)

Update Applicant Status

Change applicant\'s status. The owner of the API key used must have access to ATS settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.post_applicant_status_request import PostApplicantStatusRequest
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
    api_instance = bamboohr_sdk.ApplicantTrackingApi(api_client)
    application_id = 0 # int | The ID of the application to add a comment to. (default to 0)
    post_applicant_status_request = bamboohr_sdk.PostApplicantStatusRequest() # PostApplicantStatusRequest | Sample Post Data.

    try:
        # Update Applicant Status
        api_instance.post_applicant_status(application_id, post_applicant_status_request)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->post_applicant_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the application to add a comment to. | [default to 0]
 **post_applicant_status_request** | [**PostApplicantStatusRequest**](PostApplicantStatusRequest.md)| Sample Post Data. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **post_application_comment**
> post_application_comment(application_id, post_application_comment_request)

Create Job Application Comment

Add a comment to an application. The owner of the API key used must have access to ATS settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.post_application_comment_request import PostApplicationCommentRequest
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
    api_instance = bamboohr_sdk.ApplicantTrackingApi(api_client)
    application_id = 0 # int | The ID of the application to add a comment to. (default to 0)
    post_application_comment_request = bamboohr_sdk.PostApplicationCommentRequest() # PostApplicationCommentRequest | Comment object to post

    try:
        # Create Job Application Comment
        api_instance.post_application_comment(application_id, post_application_comment_request)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->post_application_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the application to add a comment to. | [default to 0]
 **post_application_comment_request** | [**PostApplicationCommentRequest**](PostApplicationCommentRequest.md)| Comment object to post | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

