<a name="__pageTop"></a>
# querido_diario.apis.tags.default_api.DefaultApi

All URIs are relative to *https://queridodiario.ok.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get**](#get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get) | **get** /gazettes/by_theme/entities/{theme} | Get All Available Entities Of A Theme
[**get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get**](#get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get) | **get** /gazettes/by_theme/subthemes/{theme} | Get All Available Subthemes Of A Theme
[**get_all_available_themes_gazettes_by_theme_themes_get**](#get_all_available_themes_gazettes_by_theme_themes_get) | **get** /gazettes/by_theme/themes/ | Get All Available Themes
[**get_city_by_ibgeid_cities_territory_id_get**](#get_city_by_ibgeid_cities_territory_id_get) | **get** /cities/{territory_id} | Get City By Ibge Id
[**get_company_info_by_cnpj_number_company_info_cnpj_get**](#get_company_info_by_cnpj_number_company_info_cnpj_get) | **get** /company/info/{cnpj} | Get Company Info By Cnpj Number
[**get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get**](#get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get) | **get** /company/partners/{cnpj} | Get Company Partners Infos By Cnpj Number
[**search_for_cities_by_name_cities_get**](#search_for_cities_by_name_cities_get) | **get** /cities | Search For Cities By Name.
[**search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get**](#search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get) | **get** /gazettes/by_theme/{theme} | Search For Content In Gazette Excerpts Associated With A Theme
[**search_for_content_in_gazettes_gazettes_get**](#search_for_content_in_gazettes_gazettes_get) | **get** /gazettes | Search For Content In Gazettes
[**send_a_suggestion_suggestions_post**](#send_a_suggestion_suggestions_post) | **post** /suggestions | Send A Suggestion

# **get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get**
<a name="get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get"></a>
> EntitiesSearchResponse get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get(theme)

Get All Available Entities Of A Theme

Get all available entities of a theme that can be used to search in gazettes by theme and further filtering by entities.

### Example

```python
import querido_diario
from querido_diario.apis.tags import default_api
from querido_diario.model.http_exception_message import HTTPExceptionMessage
from querido_diario.model.entities_search_response import EntitiesSearchResponse
from querido_diario.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = querido_diario.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)

# Enter a context with an instance of the API client
with querido_diario.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'theme': "theme_example",
    }
    try:
        # Get All Available Entities Of A Theme
        api_response = api_instance.get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get(
            path_params=path_params,
        )
        pprint(api_response)
    except querido_diario.ApiException as e:
        print("Exception when calling DefaultApi->get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
theme | ThemeSchema | | 

# ThemeSchema

Theme that can be used to search in gazettes by theme.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Theme that can be used to search in gazettes by theme. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get.ApiResponseFor404) | Theme not found.
422 | [ApiResponseFor422](#get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get.ApiResponseFor422) | Validation Error

#### get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntitiesSearchResponse**](../../models/EntitiesSearchResponse.md) |  | 


#### get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPExceptionMessage**](../../models/HTTPExceptionMessage.md) |  | 


#### get_all_available_entities_of_a_theme_gazettes_by_theme_entities_theme_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get**
<a name="get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get"></a>
> SubthemesSearchResponse get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get(theme)

Get All Available Subthemes Of A Theme

Get all available subthemes of a theme that can be used to search in gazettes by theme and further filtering by subthemes.

### Example

```python
import querido_diario
from querido_diario.apis.tags import default_api
from querido_diario.model.subthemes_search_response import SubthemesSearchResponse
from querido_diario.model.http_exception_message import HTTPExceptionMessage
from querido_diario.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = querido_diario.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)

# Enter a context with an instance of the API client
with querido_diario.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'theme': "theme_example",
    }
    try:
        # Get All Available Subthemes Of A Theme
        api_response = api_instance.get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get(
            path_params=path_params,
        )
        pprint(api_response)
    except querido_diario.ApiException as e:
        print("Exception when calling DefaultApi->get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
theme | ThemeSchema | | 

# ThemeSchema

Theme that can be used to search in gazettes by theme.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Theme that can be used to search in gazettes by theme. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get.ApiResponseFor404) | Theme not found.
422 | [ApiResponseFor422](#get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get.ApiResponseFor422) | Validation Error

#### get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SubthemesSearchResponse**](../../models/SubthemesSearchResponse.md) |  | 


#### get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPExceptionMessage**](../../models/HTTPExceptionMessage.md) |  | 


#### get_all_available_subthemes_of_a_theme_gazettes_by_theme_subthemes_theme_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_all_available_themes_gazettes_by_theme_themes_get**
<a name="get_all_available_themes_gazettes_by_theme_themes_get"></a>
> ThemesSearchResponse get_all_available_themes_gazettes_by_theme_themes_get()

Get All Available Themes

Get all available themes that can be used to search in gazettes by theme.

### Example

```python
import querido_diario
from querido_diario.apis.tags import default_api
from querido_diario.model.themes_search_response import ThemesSearchResponse
from pprint import pprint
# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = querido_diario.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)

# Enter a context with an instance of the API client
with querido_diario.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get All Available Themes
        api_response = api_instance.get_all_available_themes_gazettes_by_theme_themes_get()
        pprint(api_response)
    except querido_diario.ApiException as e:
        print("Exception when calling DefaultApi->get_all_available_themes_gazettes_by_theme_themes_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_available_themes_gazettes_by_theme_themes_get.ApiResponseFor200) | Successful Response

#### get_all_available_themes_gazettes_by_theme_themes_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ThemesSearchResponse**](../../models/ThemesSearchResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_city_by_ibgeid_cities_territory_id_get**
<a name="get_city_by_ibgeid_cities_territory_id_get"></a>
> CitySearchResponse get_city_by_ibgeid_cities_territory_id_get(territory_id)

Get City By Ibge Id

Get general info from specific city with 7-digit IBGE ID.

### Example

```python
import querido_diario
from querido_diario.apis.tags import default_api
from querido_diario.model.city_search_response import CitySearchResponse
from querido_diario.model.http_exception_message import HTTPExceptionMessage
from querido_diario.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = querido_diario.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)

# Enter a context with an instance of the API client
with querido_diario.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'territory_id': "territory_id_example",
    }
    try:
        # Get City By Ibge Id
        api_response = api_instance.get_city_by_ibgeid_cities_territory_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except querido_diario.ApiException as e:
        print("Exception when calling DefaultApi->get_city_by_ibgeid_cities_territory_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
territory_id | TerritoryIdSchema | | 

# TerritoryIdSchema

City's 7-digit IBGE ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | City&#x27;s 7-digit IBGE ID. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_city_by_ibgeid_cities_territory_id_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_city_by_ibgeid_cities_territory_id_get.ApiResponseFor404) | City not found
422 | [ApiResponseFor422](#get_city_by_ibgeid_cities_territory_id_get.ApiResponseFor422) | Validation Error

#### get_city_by_ibgeid_cities_territory_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CitySearchResponse**](../../models/CitySearchResponse.md) |  | 


#### get_city_by_ibgeid_cities_territory_id_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPExceptionMessage**](../../models/HTTPExceptionMessage.md) |  | 


#### get_city_by_ibgeid_cities_territory_id_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_company_info_by_cnpj_number_company_info_cnpj_get**
<a name="get_company_info_by_cnpj_number_company_info_cnpj_get"></a>
> CompanySearchResponse get_company_info_by_cnpj_number_company_info_cnpj_get(cnpj)

Get Company Info By Cnpj Number

Get info from specific company by its CNPJ number.

### Example

```python
import querido_diario
from querido_diario.apis.tags import default_api
from querido_diario.model.http_exception_message import HTTPExceptionMessage
from querido_diario.model.company_search_response import CompanySearchResponse
from querido_diario.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = querido_diario.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)

# Enter a context with an instance of the API client
with querido_diario.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'cnpj': "cnpj_example",
    }
    try:
        # Get Company Info By Cnpj Number
        api_response = api_instance.get_company_info_by_cnpj_number_company_info_cnpj_get(
            path_params=path_params,
        )
        pprint(api_response)
    except querido_diario.ApiException as e:
        print("Exception when calling DefaultApi->get_company_info_by_cnpj_number_company_info_cnpj_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cnpj | CnpjSchema | | 

# CnpjSchema

Company's CNPJ number (may include non-digit characters).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Company&#x27;s CNPJ number (may include non-digit characters). | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_company_info_by_cnpj_number_company_info_cnpj_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_company_info_by_cnpj_number_company_info_cnpj_get.ApiResponseFor404) | Company not found.
400 | [ApiResponseFor400](#get_company_info_by_cnpj_number_company_info_cnpj_get.ApiResponseFor400) | CNPJ is not valid.
422 | [ApiResponseFor422](#get_company_info_by_cnpj_number_company_info_cnpj_get.ApiResponseFor422) | Validation Error

#### get_company_info_by_cnpj_number_company_info_cnpj_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CompanySearchResponse**](../../models/CompanySearchResponse.md) |  | 


#### get_company_info_by_cnpj_number_company_info_cnpj_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPExceptionMessage**](../../models/HTTPExceptionMessage.md) |  | 


#### get_company_info_by_cnpj_number_company_info_cnpj_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPExceptionMessage**](../../models/HTTPExceptionMessage.md) |  | 


#### get_company_info_by_cnpj_number_company_info_cnpj_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get**
<a name="get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get"></a>
> PartnersSearchResponse get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get(cnpj)

Get Company Partners Infos By Cnpj Number

Get info of partners of a company by its CNPJ number.

### Example

```python
import querido_diario
from querido_diario.apis.tags import default_api
from querido_diario.model.partners_search_response import PartnersSearchResponse
from querido_diario.model.http_exception_message import HTTPExceptionMessage
from querido_diario.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = querido_diario.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)

# Enter a context with an instance of the API client
with querido_diario.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'cnpj': "cnpj_example",
    }
    try:
        # Get Company Partners Infos By Cnpj Number
        api_response = api_instance.get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get(
            path_params=path_params,
        )
        pprint(api_response)
    except querido_diario.ApiException as e:
        print("Exception when calling DefaultApi->get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cnpj | CnpjSchema | | 

# CnpjSchema

Company's CNPJ number (may include non-digit characters).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Company&#x27;s CNPJ number (may include non-digit characters). | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get.ApiResponseFor400) | CNPJ is not valid.
422 | [ApiResponseFor422](#get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get.ApiResponseFor422) | Validation Error

#### get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PartnersSearchResponse**](../../models/PartnersSearchResponse.md) |  | 


#### get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPExceptionMessage**](../../models/HTTPExceptionMessage.md) |  | 


#### get_company_partners_infos_by_cnpj_number_company_partners_cnpj_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_for_cities_by_name_cities_get**
<a name="search_for_cities_by_name_cities_get"></a>
> CitiesSearchResponse search_for_cities_by_name_cities_get()

Search For Cities By Name.

Search for cities with a name similar to the city_name query.

### Example

```python
import querido_diario
from querido_diario.apis.tags import default_api
from querido_diario.model.cities_search_response import CitiesSearchResponse
from querido_diario.model.city_level import CityLevel
from querido_diario.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = querido_diario.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)

# Enter a context with an instance of the API client
with querido_diario.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'city_name': "",
        'levels': [""],
    }
    try:
        # Search For Cities By Name.
        api_response = api_instance.search_for_cities_by_name_cities_get(
            query_params=query_params,
        )
        pprint(api_response)
    except querido_diario.ApiException as e:
        print("Exception when calling DefaultApi->search_for_cities_by_name_cities_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
city_name | CityNameSchema | | optional
levels | LevelsSchema | | optional


# CityNameSchema

Search for cities with a similar name (empty field returns all cities).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Search for cities with a similar name (empty field returns all cities). | if omitted the server will use the default value of ""

# LevelsSchema

Search for cities within the same openness level (empty field returns from all levels)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Search for cities within the same openness level (empty field returns from all levels) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CityLevel**]({{complexTypePrefix}}CityLevel.md) | [**CityLevel**]({{complexTypePrefix}}CityLevel.md) | [**CityLevel**]({{complexTypePrefix}}CityLevel.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_for_cities_by_name_cities_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#search_for_cities_by_name_cities_get.ApiResponseFor422) | Validation Error

#### search_for_cities_by_name_cities_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CitiesSearchResponse**](../../models/CitiesSearchResponse.md) |  | 


#### search_for_cities_by_name_cities_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get**
<a name="search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get"></a>
> ThemedExcerptSearchResponse search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get(theme)

Search For Content In Gazette Excerpts Associated With A Theme

Search for content in excerpts from available cities that are related to an available theme. Each search result is an excerpt from a gazette.

### Example

```python
import querido_diario
from querido_diario.apis.tags import default_api
from querido_diario.model.http_exception_message import HTTPExceptionMessage
from querido_diario.model.sort_by import SortBy
from querido_diario.model.themed_excerpt_search_response import ThemedExcerptSearchResponse
from querido_diario.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = querido_diario.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)

# Enter a context with an instance of the API client
with querido_diario.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'theme': "theme_example",
    }
    query_params = {
    }
    try:
        # Search For Content In Gazette Excerpts Associated With A Theme
        api_response = api_instance.search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except querido_diario.ApiException as e:
        print("Exception when calling DefaultApi->search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'theme': "theme_example",
    }
    query_params = {
        'entities': [],
        'subthemes': [],
        'territory_ids': [],
        'published_since': "1970-01-01",
        'published_until': "1970-01-01",
        'scraped_since': "1970-01-01T00:00:00.00Z",
        'scraped_until': "1970-01-01T00:00:00.00Z",
        'querystring': "",
        'pre_tags': [""],
        'post_tags': [""],
        'size': 10,
        'offset': 0,
        'sort_by': None,
    }
    try:
        # Search For Content In Gazette Excerpts Associated With A Theme
        api_response = api_instance.search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except querido_diario.ApiException as e:
        print("Exception when calling DefaultApi->search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entities | EntitiesSchema | | optional
subthemes | SubthemesSchema | | optional
territory_ids | TerritoryIdsSchema | | optional
published_since | PublishedSinceSchema | | optional
published_until | PublishedUntilSchema | | optional
scraped_since | ScrapedSinceSchema | | optional
scraped_until | ScrapedUntilSchema | | optional
querystring | QuerystringSchema | | optional
pre_tags | PreTagsSchema | | optional
post_tags | PostTagsSchema | | optional
size | SizeSchema | | optional
offset | OffsetSchema | | optional
sort_by | SortBySchema | | optional


# EntitiesSchema

Search in excerpts which contains any of the given entities (entities are theme-specific).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Search in excerpts which contains any of the given entities (entities are theme-specific). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# SubthemesSchema

Search in excerpts which contains any of the given subthemes (subthemes are theme-specific).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Search in excerpts which contains any of the given subthemes (subthemes are theme-specific). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TerritoryIdsSchema

Search in excerpts from gazettes published by cities with the given 7-digit IBGE IDs (an empty field searches in all available cities).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Search in excerpts from gazettes published by cities with the given 7-digit IBGE IDs (an empty field searches in all available cities). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PublishedSinceSchema

Search in excerpts from gazettes published on given date or after (format: YYYY-MM-DD).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  | Search in excerpts from gazettes published on given date or after (format: YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD

# PublishedUntilSchema

Search in excerpts from gazettes published on given date or before (format: YYYY-MM-DD).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  | Search in excerpts from gazettes published on given date or before (format: YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD

# ScrapedSinceSchema

Search in excerpts from gazettes scraped on given datetime or after (format: YYYY-MM-DDTHH:MM:SS).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | Search in excerpts from gazettes scraped on given datetime or after (format: YYYY-MM-DDTHH:MM:SS). | value must conform to RFC-3339 date-time

# ScrapedUntilSchema

Search in excerpts from gazettes scraped on given datetime or before (format: YYYY-MM-DDTHH:MM:SS).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | Search in excerpts from gazettes scraped on given datetime or before (format: YYYY-MM-DDTHH:MM:SS). | value must conform to RFC-3339 date-time

# QuerystringSchema

Search in excerpts using ElasticSearch's \"simple query string syntax\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Search in excerpts using ElasticSearch&#x27;s \&quot;simple query string syntax\&quot;. | if omitted the server will use the default value of ""

# PreTagsSchema

List of strings (usually HTML tags) to be inserted before the text which matches the query in the excerpts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of strings (usually HTML tags) to be inserted before the text which matches the query in the excerpts. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PostTagsSchema

List of strings (usually HTML tags) to be inserted after the text which matches the query in the excerpts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of strings (usually HTML tags) to be inserted after the text which matches the query in the excerpts. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# SizeSchema

Maximum number of results to be returned in the response (use with caution).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Maximum number of results to be returned in the response (use with caution). | if omitted the server will use the default value of 10

# OffsetSchema

Number of search results to be skipped in the response.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Number of search results to be skipped in the response. | if omitted the server will use the default value of 0

# SortBySchema

How to sort the search results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | How to sort the search results. | if omitted the server will use the default value of relevance

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[SortBy]({{complexTypePrefix}}SortBy.md) | [**SortBy**]({{complexTypePrefix}}SortBy.md) | [**SortBy**]({{complexTypePrefix}}SortBy.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
theme | ThemeSchema | | 

# ThemeSchema

Search in excerpts from gazettes that are associated to the given theme.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Search in excerpts from gazettes that are associated to the given theme. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get.ApiResponseFor404) | Theme not found.
422 | [ApiResponseFor422](#search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get.ApiResponseFor422) | Validation Error

#### search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ThemedExcerptSearchResponse**](../../models/ThemedExcerptSearchResponse.md) |  | 


#### search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPExceptionMessage**](../../models/HTTPExceptionMessage.md) |  | 


#### search_for_content_in_gazette_excerpts_associated_with_a_theme_gazettes_by_theme_theme_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_for_content_in_gazettes_gazettes_get**
<a name="search_for_content_in_gazettes_gazettes_get"></a>
> GazetteSearchResponse search_for_content_in_gazettes_gazettes_get()

Search For Content In Gazettes

Search for content in published gazettes from available cities. Each search result is an individual gazette.

### Example

```python
import querido_diario
from querido_diario.apis.tags import default_api
from querido_diario.model.sort_by import SortBy
from querido_diario.model.gazette_search_response import GazetteSearchResponse
from querido_diario.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = querido_diario.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)

# Enter a context with an instance of the API client
with querido_diario.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'territory_ids': [],
        'published_since': "1970-01-01",
        'published_until': "1970-01-01",
        'scraped_since': "1970-01-01T00:00:00.00Z",
        'scraped_until': "1970-01-01T00:00:00.00Z",
        'querystring': "",
        'excerpt_size': 500,
        'number_of_excerpts': 1,
        'pre_tags': [""],
        'post_tags': [""],
        'size': 10,
        'offset': 0,
        'sort_by': None,
    }
    try:
        # Search For Content In Gazettes
        api_response = api_instance.search_for_content_in_gazettes_gazettes_get(
            query_params=query_params,
        )
        pprint(api_response)
    except querido_diario.ApiException as e:
        print("Exception when calling DefaultApi->search_for_content_in_gazettes_gazettes_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
territory_ids | TerritoryIdsSchema | | optional
published_since | PublishedSinceSchema | | optional
published_until | PublishedUntilSchema | | optional
scraped_since | ScrapedSinceSchema | | optional
scraped_until | ScrapedUntilSchema | | optional
querystring | QuerystringSchema | | optional
excerpt_size | ExcerptSizeSchema | | optional
number_of_excerpts | NumberOfExcerptsSchema | | optional
pre_tags | PreTagsSchema | | optional
post_tags | PostTagsSchema | | optional
size | SizeSchema | | optional
offset | OffsetSchema | | optional
sort_by | SortBySchema | | optional


# TerritoryIdsSchema

Search in gazettes published by cities with the given 7-digit IBGE IDs (an empty field searches in all available cities).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Search in gazettes published by cities with the given 7-digit IBGE IDs (an empty field searches in all available cities). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PublishedSinceSchema

Search in gazettes published on given date or after (format: YYYY-MM-DD).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  | Search in gazettes published on given date or after (format: YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD

# PublishedUntilSchema

Search in gazettes published on given date or before (format: YYYY-MM-DD).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  | Search in gazettes published on given date or before (format: YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD

# ScrapedSinceSchema

Search in gazettes scraped on given datetime or after (format: YYYY-MM-DDTHH:MM:SS).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | Search in gazettes scraped on given datetime or after (format: YYYY-MM-DDTHH:MM:SS). | value must conform to RFC-3339 date-time

# ScrapedUntilSchema

Search in gazettes scraped on given datetime or before (format: YYYY-MM-DDTHH:MM:SS).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | Search in gazettes scraped on given datetime or before (format: YYYY-MM-DDTHH:MM:SS). | value must conform to RFC-3339 date-time

# QuerystringSchema

Search in gazettes using ElasticSearch's \"simple query string syntax\" (an empty field returns no excerpts, only the results metadata).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Search in gazettes using ElasticSearch&#x27;s \&quot;simple query string syntax\&quot; (an empty field returns no excerpts, only the results metadata). | if omitted the server will use the default value of ""

# ExcerptSizeSchema

Maximum number of characters that an excerpt should display (use with caution).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Maximum number of characters that an excerpt should display (use with caution). | if omitted the server will use the default value of 500

# NumberOfExcerptsSchema

Maximum number of excerpts of a gazette to be returned (use with caution).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Maximum number of excerpts of a gazette to be returned (use with caution). | if omitted the server will use the default value of 1

# PreTagsSchema

List of strings (usually HTML tags) to be inserted before the text which matches the query in the excerpts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of strings (usually HTML tags) to be inserted before the text which matches the query in the excerpts. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PostTagsSchema

List of strings (usually HTML tags) to be inserted after the text which matches the query in the excerpts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of strings (usually HTML tags) to be inserted after the text which matches the query in the excerpts. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# SizeSchema

Maximum number of results to be returned in the response (use with caution).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Maximum number of results to be returned in the response (use with caution). | if omitted the server will use the default value of 10

# OffsetSchema

Number of search results to be skipped in the response.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Number of search results to be skipped in the response. | if omitted the server will use the default value of 0

# SortBySchema

How to sort the search results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | How to sort the search results. | if omitted the server will use the default value of relevance

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[SortBy]({{complexTypePrefix}}SortBy.md) | [**SortBy**]({{complexTypePrefix}}SortBy.md) | [**SortBy**]({{complexTypePrefix}}SortBy.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_for_content_in_gazettes_gazettes_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#search_for_content_in_gazettes_gazettes_get.ApiResponseFor422) | Validation Error

#### search_for_content_in_gazettes_gazettes_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GazetteSearchResponse**](../../models/GazetteSearchResponse.md) |  | 


#### search_for_content_in_gazettes_gazettes_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **send_a_suggestion_suggestions_post**
<a name="send_a_suggestion_suggestions_post"></a>
> CreatedSuggestionResponse send_a_suggestion_suggestions_post(create_suggestion_body)

Send A Suggestion

Send a suggestion to the project

### Example

```python
import querido_diario
from querido_diario.apis.tags import default_api
from querido_diario.model.created_suggestion_response import CreatedSuggestionResponse
from querido_diario.model.create_suggestion_body import CreateSuggestionBody
from querido_diario.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://queridodiario.ok.org.br/api
# See configuration.py for a list of all supported configuration parameters.
configuration = querido_diario.Configuration(
    host = "https://queridodiario.ok.org.br/api"
)

# Enter a context with an instance of the API client
with querido_diario.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateSuggestionBody(
        email_address="email_address_example",
        name="name_example",
        content="content_example",
    )
    try:
        # Send A Suggestion
        api_response = api_instance.send_a_suggestion_suggestions_post(
            body=body,
        )
        pprint(api_response)
    except querido_diario.ApiException as e:
        print("Exception when calling DefaultApi->send_a_suggestion_suggestions_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateSuggestionBody**](../../models/CreateSuggestionBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#send_a_suggestion_suggestions_post.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#send_a_suggestion_suggestions_post.ApiResponseFor422) | Validation Error

#### send_a_suggestion_suggestions_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreatedSuggestionResponse**](../../models/CreatedSuggestionResponse.md) |  | 


#### send_a_suggestion_suggestions_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

