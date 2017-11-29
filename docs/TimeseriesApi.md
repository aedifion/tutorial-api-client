# swagger_client.TimeseriesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_first_after**](TimeseriesApi.md#get_first_after) | **GET** /v1/getFirstAfter | Query first observation made after a certain point in time.
[**get_last_before**](TimeseriesApi.md#get_last_before) | **GET** /v1/getLastBefore | Query last observation made before a certain point in time.
[**get_timeseries_by_id**](TimeseriesApi.md#get_timeseries_by_id) | **GET** /v1/getTimeseriesByID | Query observations for datapoint Ids within time interval.


# **get_first_after**
> list[NextLast] get_first_after(project, timestamp, datapoint_id)

Query first observation made after a certain point in time.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.TimeseriesApi()
project = 'project_example' # str | Name of the project where data will be queried from.
timestamp = 'timestamp_example' # str | Timestamp for the requested data. Please use one of these date formats: \"YYYY-MM-DD hh:mm:ss\" or \"YYYY-MM-DDThh:mm:ssZ\" incase blanks cannot be used.
datapoint_id = 'datapoint_id_example' # str | This is the unique identifier for the queried datapoint formated \"name=anyUniqueName\".

try: 
    # Query first observation made after a certain point in time.
    api_response = api_instance.get_first_after(project, timestamp, datapoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeseriesApi->get_first_after: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Name of the project where data will be queried from. | 
 **timestamp** | **str**| Timestamp for the requested data. Please use one of these date formats: \&quot;YYYY-MM-DD hh:mm:ss\&quot; or \&quot;YYYY-MM-DDThh:mm:ssZ\&quot; incase blanks cannot be used. | 
 **datapoint_id** | **str**| This is the unique identifier for the queried datapoint formated \&quot;name&#x3D;anyUniqueName\&quot;. | 

### Return type

[**list[NextLast]**](NextLast.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_before**
> list[NextLast] get_last_before(project, timestamp, datapoint_id)

Query last observation made before a certain point in time.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.TimeseriesApi()
project = 'project_example' # str | Name of the project where data will be queried from.
timestamp = 'timestamp_example' # str | Timestamp for the requested data. Please use one of these date formats: \"YYYY-MM-DD hh:mm:ss\" or \"YYYY-MM-DDThh:mm:ssZ\" incase blanks cannot be used.
datapoint_id = 'datapoint_id_example' # str | This is the unique identifier for the queried datapoint formated \"name=anyUniqueName\".

try: 
    # Query last observation made before a certain point in time.
    api_response = api_instance.get_last_before(project, timestamp, datapoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeseriesApi->get_last_before: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Name of the project where data will be queried from. | 
 **timestamp** | **str**| Timestamp for the requested data. Please use one of these date formats: \&quot;YYYY-MM-DD hh:mm:ss\&quot; or \&quot;YYYY-MM-DDThh:mm:ssZ\&quot; incase blanks cannot be used. | 
 **datapoint_id** | **str**| This is the unique identifier for the queried datapoint formated \&quot;name&#x3D;anyUniqueName\&quot;. | 

### Return type

[**list[NextLast]**](NextLast.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timeseries_by_id**
> list[ByTag] get_timeseries_by_id(project, timestamp_start, timestamp_end, datapoint_id)

Query observations for datapoint Ids within time interval.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.TimeseriesApi()
project = 'project_example' # str | Name of the project where data will be queried from.
timestamp_start = 'timestamp_start_example' # str | Timestamp starting the time interval for the requested data. Please use one of these date formats: \"YYYY-MM-DD hh:mm:ss\" or \"YYYY-MM-DDThh:mm:ssZ\" incase blanks cannot be used.
timestamp_end = 'timestamp_end_example' # str | Timestamp ending the time interval for the requested data. Please use one of these date formats: \"YYYY-MM-DD hh:mm:ss\" or \"YYYY-MM-DDThh:mm:ssZ\" incase blanks cannot be used.
datapoint_id = ['datapoint_id_example'] # list[str] | This is the unique identifier for the queried datapoint formated \"name=anyUniqueName\".

try: 
    # Query observations for datapoint Ids within time interval.
    api_response = api_instance.get_timeseries_by_id(project, timestamp_start, timestamp_end, datapoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeseriesApi->get_timeseries_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Name of the project where data will be queried from. | 
 **timestamp_start** | **str**| Timestamp starting the time interval for the requested data. Please use one of these date formats: \&quot;YYYY-MM-DD hh:mm:ss\&quot; or \&quot;YYYY-MM-DDThh:mm:ssZ\&quot; incase blanks cannot be used. | 
 **timestamp_end** | **str**| Timestamp ending the time interval for the requested data. Please use one of these date formats: \&quot;YYYY-MM-DD hh:mm:ss\&quot; or \&quot;YYYY-MM-DDThh:mm:ssZ\&quot; incase blanks cannot be used. | 
 **datapoint_id** | [**list[str]**](str.md)| This is the unique identifier for the queried datapoint formated \&quot;name&#x3D;anyUniqueName\&quot;. | 

### Return type

[**list[ByTag]**](ByTag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

