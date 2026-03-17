# bamboohr_sdk.ApplicantTrackingApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application_comment**](ApplicantTrackingApi.md#create_application_comment) | **POST** /api/v1/applicant_tracking/applications/{applicationId}/comments | Create Job Application Comment
[**create_candidate**](ApplicantTrackingApi.md#create_candidate) | **POST** /api/v1/applicant_tracking/application | Create Candidate
[**create_job_opening**](ApplicantTrackingApi.md#create_job_opening) | **POST** /api/v1/applicant_tracking/job_opening | Create Job Opening
[**get_application_details**](ApplicantTrackingApi.md#get_application_details) | **GET** /api/v1/applicant_tracking/applications/{applicationId} | Get Job Application Details
[**get_applications**](ApplicantTrackingApi.md#get_applications) | **GET** /api/v1/applicant_tracking/applications | Get Job Applications
[**get_company_locations**](ApplicantTrackingApi.md#get_company_locations) | **GET** /api/v1/applicant_tracking/locations | Get Company Locations
[**get_hiring_leads**](ApplicantTrackingApi.md#get_hiring_leads) | **GET** /api/v1/applicant_tracking/hiring_leads | Get Hiring Leads
[**get_job_summaries**](ApplicantTrackingApi.md#get_job_summaries) | **GET** /api/v1/applicant_tracking/jobs | Get Job Summaries
[**get_statuses**](ApplicantTrackingApi.md#get_statuses) | **GET** /api/v1/applicant_tracking/statuses | Get Applicant Statuses
[**update_applicant_status**](ApplicantTrackingApi.md#update_applicant_status) | **POST** /api/v1/applicant_tracking/applications/{applicationId}/status | Update Applicant Status


# **create_application_comment**
> CreateCommentResponse create_application_comment(application_id, create_application_comment_request)

Create Job Application Comment

Add a comment to an application. The owner of the API key used must have access to ATS settings. The `type` field defaults to `comment` if omitted.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.create_application_comment_request import CreateApplicationCommentRequest
from bamboohr_sdk.models.create_comment_response import CreateCommentResponse
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
    application_id = 56 # int | The ID of the application to add a comment to.
    create_application_comment_request = bamboohr_sdk.CreateApplicationCommentRequest() # CreateApplicationCommentRequest | Comment object to post

    try:
        # Create Job Application Comment
        api_response = api_instance.create_application_comment(application_id, create_application_comment_request)
        print("The response of ApplicantTrackingApi->create_application_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->create_application_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the application to add a comment to. | 
 **create_application_comment_request** | [**CreateApplicationCommentRequest**](CreateApplicationCommentRequest.md)| Comment object to post | 

### Return type

[**CreateCommentResponse**](CreateCommentResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns the type and ID of the created comment. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_candidate**
> CreateCandidateResponse create_candidate(first_name, last_name, job_id, email=email, phone_number=phone_number, source=source, address=address, city=city, state=state, zip=zip, country=country, linkedin_url=linkedin_url, date_available=date_available, desired_salary=desired_salary, referred_by=referred_by, website_url=website_url, highest_education=highest_education, college_name=college_name, references=references, resume=resume, cover_letter=cover_letter)

Create Candidate

Create a new candidate application for a job opening. The owner of the API key used must have access to ATS settings. On success, returns the new candidate ID. Only fields required by the target job opening's standard questions need to be provided beyond firstName, lastName, and jobId.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.create_candidate_response import CreateCandidateResponse
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
    email = 'email_example' # str | The email address of the candidate. Must be a valid email address. (optional)
    phone_number = 'phone_number_example' # str | The phone number of the candidate. (optional)
    source = 'source_example' # str | The source of the candidate application, e.g. LinkedIn, Indeed, etc. (optional)
    address = 'address_example' # str | The street address of the candidate. (optional)
    city = 'city_example' # str | The city of the candidate. (optional)
    state = 'state_example' # str | The state or province of the candidate. Accepts state name, abbreviation, or ISO code. (optional)
    zip = 'zip_example' # str | The zip code or postal code of the candidate. (optional)
    country = 'country_example' # str | The country of the candidate. Accepts country name or ISO code. (optional)
    linkedin_url = 'linkedin_url_example' # str | The LinkedIn profile URL of the candidate. Must match `https?://(.*\\\\.)?linkedin.com/...`. (optional)
    date_available = '2013-10-20' # date | The available start date of the candidate. Format: `Y-m-d` (e.g. `2024-06-01`). (optional)
    desired_salary = 'desired_salary_example' # str | The desired salary of the candidate. (optional)
    referred_by = 'referred_by_example' # str | The person or entity that referred the candidate. (optional)
    website_url = 'website_url_example' # str | The personal website, blog, or online portfolio of the candidate. Must be a valid URL. (optional)
    highest_education = 'highest_education_example' # str | The highest completed education level of the candidate. (optional)
    college_name = 'college_name_example' # str | The college or university of the candidate. (optional)
    references = 'references_example' # str | A list of references supplied by the candidate. (optional)
    resume = None # bytearray | Resume file for the candidate. Accepted MIME types: `application/pdf`, `application/msword`, `application/vnd.openxmlformats-officedocument.wordprocessingml.document`, `text/plain`, `application/rtf`, `image/jpeg`, `image/gif`, `image/png`, `image/tiff`, `image/bmp`. (optional)
    cover_letter = None # bytearray | Cover letter file for the candidate. Accepted MIME types: `application/pdf`, `application/msword`, `application/vnd.openxmlformats-officedocument.wordprocessingml.document`, `text/plain`, `application/rtf`, `image/jpeg`, `image/gif`, `image/png`, `image/tiff`, `image/bmp`. (optional)

    try:
        # Create Candidate
        api_response = api_instance.create_candidate(first_name, last_name, job_id, email=email, phone_number=phone_number, source=source, address=address, city=city, state=state, zip=zip, country=country, linkedin_url=linkedin_url, date_available=date_available, desired_salary=desired_salary, referred_by=referred_by, website_url=website_url, highest_education=highest_education, college_name=college_name, references=references, resume=resume, cover_letter=cover_letter)
        print("The response of ApplicantTrackingApi->create_candidate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->create_candidate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**| The first name of the candidate. | 
 **last_name** | **str**| The last name of the candidate. | 
 **job_id** | **int**| The id of the job opening for the candidate application. | 
 **email** | **str**| The email address of the candidate. Must be a valid email address. | [optional] 
 **phone_number** | **str**| The phone number of the candidate. | [optional] 
 **source** | **str**| The source of the candidate application, e.g. LinkedIn, Indeed, etc. | [optional] 
 **address** | **str**| The street address of the candidate. | [optional] 
 **city** | **str**| The city of the candidate. | [optional] 
 **state** | **str**| The state or province of the candidate. Accepts state name, abbreviation, or ISO code. | [optional] 
 **zip** | **str**| The zip code or postal code of the candidate. | [optional] 
 **country** | **str**| The country of the candidate. Accepts country name or ISO code. | [optional] 
 **linkedin_url** | **str**| The LinkedIn profile URL of the candidate. Must match &#x60;https?://(.*\\\\.)?linkedin.com/...&#x60;. | [optional] 
 **date_available** | **date**| The available start date of the candidate. Format: &#x60;Y-m-d&#x60; (e.g. &#x60;2024-06-01&#x60;). | [optional] 
 **desired_salary** | **str**| The desired salary of the candidate. | [optional] 
 **referred_by** | **str**| The person or entity that referred the candidate. | [optional] 
 **website_url** | **str**| The personal website, blog, or online portfolio of the candidate. Must be a valid URL. | [optional] 
 **highest_education** | **str**| The highest completed education level of the candidate. | [optional] 
 **college_name** | **str**| The college or university of the candidate. | [optional] 
 **references** | **str**| A list of references supplied by the candidate. | [optional] 
 **resume** | **bytearray**| Resume file for the candidate. Accepted MIME types: &#x60;application/pdf&#x60;, &#x60;application/msword&#x60;, &#x60;application/vnd.openxmlformats-officedocument.wordprocessingml.document&#x60;, &#x60;text/plain&#x60;, &#x60;application/rtf&#x60;, &#x60;image/jpeg&#x60;, &#x60;image/gif&#x60;, &#x60;image/png&#x60;, &#x60;image/tiff&#x60;, &#x60;image/bmp&#x60;. | [optional] 
 **cover_letter** | **bytearray**| Cover letter file for the candidate. Accepted MIME types: &#x60;application/pdf&#x60;, &#x60;application/msword&#x60;, &#x60;application/vnd.openxmlformats-officedocument.wordprocessingml.document&#x60;, &#x60;text/plain&#x60;, &#x60;application/rtf&#x60;, &#x60;image/jpeg&#x60;, &#x60;image/gif&#x60;, &#x60;image/png&#x60;, &#x60;image/tiff&#x60;, &#x60;image/bmp&#x60;. | [optional] 

### Return type

[**CreateCandidateResponse**](CreateCandidateResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns the result status and the new candidate ID. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |
**422** | Unprocessable entity. One or more parameters failed validation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job_opening**
> CreateJobOpeningResponse create_job_opening(posting_title, job_status, hiring_lead, employment_type, job_description, department=department, minimum_experience=minimum_experience, compensation=compensation, job_location=job_location, application_question_resume=application_question_resume, application_question_address=application_question_address, application_question_linkedin_url=application_question_linkedin_url, application_question_date_available=application_question_date_available, application_question_desired_salary=application_question_desired_salary, application_question_cover_letter=application_question_cover_letter, application_question_referred_by=application_question_referred_by, application_question_website_url=application_question_website_url, application_question_highest_education=application_question_highest_education, application_question_college=application_question_college, application_question_references=application_question_references, internal_job_code=internal_job_code, location_type=location_type)

Create Job Opening

Create a new job opening. The owner of the API key used must have access to ATS settings. Use the Get Company Locations and Get Hiring Leads endpoints to obtain valid IDs for `jobLocation` and `hiringLead`. On success, returns the new job opening ID.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.create_job_opening_response import CreateJobOpeningResponse
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
    location_type = 56 # int | The location type for the job opening. `0` = on-site (requires `jobLocation`), `1` = remote (no `jobLocation`), `2` = hybrid (requires `jobLocation`). Defaults to `1` if omitted and no `jobLocation` is provided, or `0` if `jobLocation` is provided. (optional)

    try:
        # Create Job Opening
        api_response = api_instance.create_job_opening(posting_title, job_status, hiring_lead, employment_type, job_description, department=department, minimum_experience=minimum_experience, compensation=compensation, job_location=job_location, application_question_resume=application_question_resume, application_question_address=application_question_address, application_question_linkedin_url=application_question_linkedin_url, application_question_date_available=application_question_date_available, application_question_desired_salary=application_question_desired_salary, application_question_cover_letter=application_question_cover_letter, application_question_referred_by=application_question_referred_by, application_question_website_url=application_question_website_url, application_question_highest_education=application_question_highest_education, application_question_college=application_question_college, application_question_references=application_question_references, internal_job_code=internal_job_code, location_type=location_type)
        print("The response of ApplicantTrackingApi->create_job_opening:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->create_job_opening: %s\n" % e)
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
 **location_type** | **int**| The location type for the job opening. &#x60;0&#x60; &#x3D; on-site (requires &#x60;jobLocation&#x60;), &#x60;1&#x60; &#x3D; remote (no &#x60;jobLocation&#x60;), &#x60;2&#x60; &#x3D; hybrid (requires &#x60;jobLocation&#x60;). Defaults to &#x60;1&#x60; if omitted and no &#x60;jobLocation&#x60; is provided, or &#x60;0&#x60; if &#x60;jobLocation&#x60; is provided. | [optional] 

### Return type

[**CreateJobOpeningResponse**](CreateJobOpeningResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns the result status and the new job opening ID. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |
**422** | Unprocessable entity. One or more parameters failed validation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_details**
> ApplicationDetails get_application_details(application_id)

Get Job Application Details

Get the full details of a single application including applicant info, job details, questions and answers, and status history. The owner of the API key used must have access to ATS settings.

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
    application_id = 56 # int | The ID of the application to retrieve details for.

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
 **application_id** | **int**| The ID of the application to retrieve details for. | 

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
**200** | Success. Returns the full application detail object. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Application not found. |  -  |

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
    application_status_id = 'application_status_id_example' # str | One or more application status IDs to filter by, comma-separated (e.g. `1,2,3`). (optional)
    application_status = 'application_status_example' # str | One or more application status group codes to filter by, comma-separated (e.g. `NEW,ACTIVE`). Allowed values: `ALL`, `ALL_ACTIVE`, `NEW`, `ACTIVE`, `INACTIVE`, `HIRED`. (optional)
    job_status_groups = 'job_status_groups_example' # str | One or more position status groups to filter by, comma-separated (e.g. `Draft,Open`). Allowed values: `ALL`, `DRAFT_AND_OPEN`, `Open`, `Filled`, `Draft`, `Deleted`, `On Hold`, `Canceled`. (optional)
    search_string = 'search_string_example' # str | A general search criteria by which to find applications. (optional)
    sort_by = 'sort_by_example' # str | A specific field to sort the results by. (optional)
    sort_order = 'sort_order_example' # str | Order by which to sort results. (optional)
    new_since = '2024-01-01 13:00:00' # str | Only return applications submitted after this UTC timestamp. Format: `Y-m-d H:i:s` (e.g. `2024-01-01 13:00:00`). (optional)

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
 **application_status_id** | **str**| One or more application status IDs to filter by, comma-separated (e.g. &#x60;1,2,3&#x60;). | [optional] 
 **application_status** | **str**| One or more application status group codes to filter by, comma-separated (e.g. &#x60;NEW,ACTIVE&#x60;). Allowed values: &#x60;ALL&#x60;, &#x60;ALL_ACTIVE&#x60;, &#x60;NEW&#x60;, &#x60;ACTIVE&#x60;, &#x60;INACTIVE&#x60;, &#x60;HIRED&#x60;. | [optional] 
 **job_status_groups** | **str**| One or more position status groups to filter by, comma-separated (e.g. &#x60;Draft,Open&#x60;). Allowed values: &#x60;ALL&#x60;, &#x60;DRAFT_AND_OPEN&#x60;, &#x60;Open&#x60;, &#x60;Filled&#x60;, &#x60;Draft&#x60;, &#x60;Deleted&#x60;, &#x60;On Hold&#x60;, &#x60;Canceled&#x60;. | [optional] 
 **search_string** | **str**| A general search criteria by which to find applications. | [optional] 
 **sort_by** | **str**| A specific field to sort the results by. | [optional] 
 **sort_order** | **str**| Order by which to sort results. | [optional] 
 **new_since** | **str**| Only return applications submitted after this UTC timestamp. Format: &#x60;Y-m-d H:i:s&#x60; (e.g. &#x60;2024-01-01 13:00:00&#x60;). | [optional] 

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
> List[Location] get_company_locations()

Get Company Locations

Get all company locations available for use when creating a job opening. The owner of the API key used must have access to ATS settings. Use the returned location IDs as the `jobLocation` field when calling the Create Job Opening endpoint.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.location import Location
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

[**List[Location]**](Location.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns an array of location objects. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hiring_leads**
> List[HiringLead] get_hiring_leads()

Get Hiring Leads

Get the list of employees who can be assigned as a hiring lead when creating a new job opening. The owner of the API key used must have access to ATS settings. Use the returned `employeeId` values as the `hiringLead` field when calling the Create Job Opening endpoint.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.hiring_lead import HiringLead
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

[**List[HiringLead]**](HiringLead.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns an array of employees who can be assigned as hiring leads. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_summaries**
> List[JobSummary] get_job_summaries(status_groups=status_groups, status_ids=status_ids, sort_by=sort_by, sort_order=sort_order)

Get Job Summaries

Get a list of job opening summaries. The owner of the API key used must have access to ATS settings. Results can be filtered by status group and sorted by various fields. By default returns all non-deleted job openings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.job_summary import JobSummary
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
    status_groups = 'status_groups_example' # str | One or more status groups to filter positions by, comma-separated (e.g. `Draft,Open`). Allowed values: `ALL`, `DRAFT_AND_OPEN`, `Open`, `Filled`, `Draft`, `Deleted`, `On Hold`, `Canceled`. Defaults to all non-deleted positions. (optional)
    status_ids = 'status_ids_example' # str | One or more specific job opening status IDs to filter by, comma-separated (e.g. `1,2`). Combined with `statusGroups` when both are provided. (optional)
    sort_by = 'sort_by_example' # str | A specific field to sort the results by. (optional)
    sort_order = 'sort_order_example' # str | Order by which to sort results. (optional)

    try:
        # Get Job Summaries
        api_response = api_instance.get_job_summaries(status_groups=status_groups, status_ids=status_ids, sort_by=sort_by, sort_order=sort_order)
        print("The response of ApplicantTrackingApi->get_job_summaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->get_job_summaries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_groups** | **str**| One or more status groups to filter positions by, comma-separated (e.g. &#x60;Draft,Open&#x60;). Allowed values: &#x60;ALL&#x60;, &#x60;DRAFT_AND_OPEN&#x60;, &#x60;Open&#x60;, &#x60;Filled&#x60;, &#x60;Draft&#x60;, &#x60;Deleted&#x60;, &#x60;On Hold&#x60;, &#x60;Canceled&#x60;. Defaults to all non-deleted positions. | [optional] 
 **status_ids** | **str**| One or more specific job opening status IDs to filter by, comma-separated (e.g. &#x60;1,2&#x60;). Combined with &#x60;statusGroups&#x60; when both are provided. | [optional] 
 **sort_by** | **str**| A specific field to sort the results by. | [optional] 
 **sort_order** | **str**| Order by which to sort results. | [optional] 

### Return type

[**List[JobSummary]**](JobSummary.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns an array of job opening summary objects. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statuses**
> List[ApplicantStatus] get_statuses()

Get Applicant Statuses

Get a list of applicant statuses configured for the company. The owner of the API key used must have access to ATS settings. Returns both system-defined and custom statuses.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.applicant_status import ApplicantStatus
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
        api_response = api_instance.get_statuses()
        print("The response of ApplicantTrackingApi->get_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->get_statuses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApplicantStatus]**](ApplicantStatus.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns an array of applicant status objects. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_applicant_status**
> UpdateApplicantStatusResponse update_applicant_status(application_id, update_applicant_status_request)

Update Applicant Status

Update the status of an application. The owner of the API key used must have access to ATS settings. Use the Get Applicant Statuses endpoint to obtain valid status IDs.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.update_applicant_status_request import UpdateApplicantStatusRequest
from bamboohr_sdk.models.update_applicant_status_response import UpdateApplicantStatusResponse
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
    application_id = 56 # int | The ID of the application whose status should be updated.
    update_applicant_status_request = bamboohr_sdk.UpdateApplicantStatusRequest() # UpdateApplicantStatusRequest | The new status to assign to the application.

    try:
        # Update Applicant Status
        api_response = api_instance.update_applicant_status(application_id, update_applicant_status_request)
        print("The response of ApplicantTrackingApi->update_applicant_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantTrackingApi->update_applicant_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the application whose status should be updated. | 
 **update_applicant_status_request** | [**UpdateApplicantStatusRequest**](UpdateApplicantStatusRequest.md)| The new status to assign to the application. | 

### Return type

[**UpdateApplicantStatusResponse**](UpdateApplicantStatusResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns the type and ID of the status change record. |  -  |
**400** | Bad request. The error message is returned in the &#x60;x-bamboohr-error-message&#x60; response header; the body is empty. |  * x-bamboohr-error-message - Human-readable error message describing why the request failed (e.g. &#39;Invalid status&#39;). <br>  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

