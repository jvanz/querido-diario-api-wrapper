# querido_diario.model.themed_excerpt_item.ThemedExcerptItem

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD
**scraped_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**territory_name** | str,  | str,  |  | 
**excerpt** | str,  | str,  |  | 
**state_code** | str,  | str,  |  | 
**territory_id** | str,  | str,  |  | 
**url** | str,  | str,  |  | 
**[subthemes](#subthemes)** | list, tuple,  | tuple,  |  | 
**[entities](#entities)** | list, tuple,  | tuple,  |  | [optional] 
**edition** | str,  | str,  |  | [optional] 
**is_extra_edition** | bool,  | BoolClass,  |  | [optional] 
**txt_url** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subthemes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# entities

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

