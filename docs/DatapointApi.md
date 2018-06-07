# swagger_client.DatapointApi

All URIs are relative to *https://api.aedifion.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_alert**](DatapointApi.md#delete_alert) | **DELETE** /v2/datapoint/alert/ | Delete an alert.
[**delete_datapoint_favorite**](DatapointApi.md#delete_datapoint_favorite) | **DELETE** /v2/datapoint/favorite | Remove a personal favorite data point.
[**delete_datapoint_renaming**](DatapointApi.md#delete_datapoint_renaming) | **DELETE** /v2/datapoint/renaming/{id} | Delete an alternative name for a given data point under a given data point key.
[**delete_datapoint_tag**](DatapointApi.md#delete_datapoint_tag) | **DELETE** /v2/datapoint/tag/{id} | Remove tag from data point.
[**get_alert**](DatapointApi.md#get_alert) | **GET** /v2/datapoint/alert/ | Get alert details.
[**get_allalerts**](DatapointApi.md#get_allalerts) | **GET** /v2/datapoint/allalerts/ | Get all alerts on a datapoint.
[**get_datapoint**](DatapointApi.md#get_datapoint) | **GET** /v2/datapoint | Get details about data point.
[**get_datapoint_timeseries**](DatapointApi.md#get_datapoint_timeseries) | **GET** /v2/datapoint/timeseries | Get the time series data of a data point.
[**post_alert**](DatapointApi.md#post_alert) | **POST** /v2/datapoint/alert | Create a new alert.
[**post_datapoint_favorite**](DatapointApi.md#post_datapoint_favorite) | **POST** /v2/datapoint/favorite | Set a data point as personal favorite.
[**post_datapoint_renaming**](DatapointApi.md#post_datapoint_renaming) | **POST** /v2/datapoint/renaming | Add an alternative name associated with a specific data point key for a data point.
[**post_datapoint_tag**](DatapointApi.md#post_datapoint_tag) | **POST** /v2/datapoint/tag | Add a tag.
[**put_alert**](DatapointApi.md#put_alert) | **PUT** /v2/datapoint/alert/ | Edit an Alert.
[**put_datapoint_renaming**](DatapointApi.md#put_datapoint_renaming) | **PUT** /v2/datapoint/renaming/{id} | Change a renaming.
[**toggle_alert**](DatapointApi.md#toggle_alert) | **PUT** /v2/datapoint/alert_toggle/ | Enable or disable an alert.


# **delete_alert**
> Success delete_alert(data_point_id, project_id, name)

Delete an alert.

Delete an alert by name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
data_point_id = 'data_point_id_example' # str | The alphanumeric dataPointID for which to delete an alarm.
project_id = 789 # int | The numeric project id to which the specified data point belongs.
name = 'name_example' # str | The name of the alert to delete.

try:
    # Delete an alert.
    api_response = api_instance.delete_alert(data_point_id, project_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->delete_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_point_id** | **str**| The alphanumeric dataPointID for which to delete an alarm. | 
 **project_id** | **int**| The numeric project id to which the specified data point belongs. | 
 **name** | **str**| The name of the alert to delete. | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datapoint_favorite**
> Success delete_datapoint_favorite(data_point_id, project_id)

Remove a personal favorite data point.

Removes a data point from the personal favorites of the user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
data_point_id = 'data_point_id_example' # str | The dataPointID of the data point to unset as favorite
project_id = 789 # int | The numeric id of the project to which the data point identified by _dataPointID_ belongs

try:
    # Remove a personal favorite data point.
    api_response = api_instance.delete_datapoint_favorite(data_point_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->delete_datapoint_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_point_id** | **str**| The dataPointID of the data point to unset as favorite | 
 **project_id** | **int**| The numeric id of the project to which the data point identified by _dataPointID_ belongs | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datapoint_renaming**
> Success delete_datapoint_renaming(id)

Delete an alternative name for a given data point under a given data point key.

Deletes the alternative name for the data point referenced by its name/dataPointID under the specified dataPointKey.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the renaming to delete.

try:
    # Delete an alternative name for a given data point under a given data point key.
    api_response = api_instance.delete_datapoint_renaming(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->delete_datapoint_renaming: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the renaming to delete. | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datapoint_tag**
> Success delete_datapoint_tag(id, data_point_id, project_id)

Remove tag from data point.

Removes the tag identified by 'id' from the data point identified by 'dataPointID' and 'project_id'.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
id = 789 # int | The unique id of the tag to delete.
data_point_id = 'data_point_id_example' # str | The dataPointID of the data point from which the tag will be deleted.
project_id = 789 # int | The numeric id of the project to which the data point identified by 'dataPointID' belongs to.

try:
    # Remove tag from data point.
    api_response = api_instance.delete_datapoint_tag(id, data_point_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->delete_datapoint_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique id of the tag to delete. | 
 **data_point_id** | **str**| The dataPointID of the data point from which the tag will be deleted. | 
 **project_id** | **int**| The numeric id of the project to which the data point identified by &#39;dataPointID&#39; belongs to. | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert**
> Alert get_alert(data_point_id, project_id, name)

Get alert details.

Returns the details of the alert by name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
data_point_id = 'data_point_id_example' # str | The alphanumeric dataPointID for which to get an alarm.
project_id = 789 # int | The numeric project id to which the specified data point belongs.
name = 'name_example' # str | The name of the alert to retrieve.

try:
    # Get alert details.
    api_response = api_instance.get_alert(data_point_id, project_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->get_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_point_id** | **str**| The alphanumeric dataPointID for which to get an alarm. | 
 **project_id** | **int**| The numeric project id to which the specified data point belongs. | 
 **name** | **str**| The name of the alert to retrieve. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allalerts**
> Alerts get_allalerts(data_point_id, project_id)

Get all alerts on a datapoint.

Returns the details of all alerts on a datapoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
data_point_id = 'data_point_id_example' # str | The alphanumeric dataPointID for which to delete an alarm.
project_id = 789 # int | The numeric project id to which the specified data point belongs.

try:
    # Get all alerts on a datapoint.
    api_response = api_instance.get_allalerts(data_point_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->get_allalerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_point_id** | **str**| The alphanumeric dataPointID for which to delete an alarm. | 
 **project_id** | **int**| The numeric project id to which the specified data point belongs. | 

### Return type

[**Alerts**](Alerts.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datapoint**
> list[DataPointWithContext] get_datapoint(data_point_id, project_id)

Get details about data point.

Gets the data point including meta information, i.e., whether it is a user's favorite, its renamings and tags.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
data_point_id = 'data_point_id_example' # str | The dataPointID of the data point to retrieve.
project_id = 789 # int | The numeric id of the project to which the data point identified by _dataPointID_ belongs.

try:
    # Get details about data point.
    api_response = api_instance.get_datapoint(data_point_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->get_datapoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_point_id** | **str**| The dataPointID of the data point to retrieve. | 
 **project_id** | **int**| The numeric id of the project to which the data point identified by _dataPointID_ belongs. | 

### Return type

[**list[DataPointWithContext]**](DataPointWithContext.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datapoint_timeseries**
> TimeseriesWithContext get_datapoint_timeseries(project_id, data_point_id, start=start, end=end, max=max, samplerate=samplerate)

Get the time series data of a data point.

Returns the measured time series data for the specified data point referenced by its name/dataPointID for the time interval specified by **start** and **end**. Returns the last (or respectively next) **max** observations, if either **start** nor **end** are provided. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | The id of the project from which to query observations for a data point
data_point_id = 'data_point_id_example' # str | Name/ID of the data point, e.g., *bacnet100-4120-CO2*
start = '2013-10-20T19:20:30+01:00' # datetime | Return only observations *after* this date-time\"  If **start** is provided without **end**, the first **max** elements *after* **start** are returned.  (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | Return only observations *before* this date-time\".  If **end** is provided without **start**, the last **max** elements *before* **end** are returned.  (optional)
max = 1 # int | Maximum number of observations to return.  - This option is ignored when both **start** and **end** are provided.  - Setting **max** = 0 returns *all* available data points.  (optional) (default to 1)
samplerate = 'samplerate_example' # str | Desired sampling rate. The returned observations are sampled down to the specified interval. The down sampling will be done by calculating the arithmetic average on all observations made within an interval. The timestamp will represent the beginning of the interval the resampling average is estimated for. Allowed intervals are integers combined with durations, like seconds (s), minutes (m), hours (h), and days (d), e.g.  - \"10s\" specifies a sampling rate of \"once every 10 seconds\",  - \"1h\" specifies a sampling rate of \"once every (1) hour\",  - \"0s\", \"0m\", \"0h\", ... specify highest sampling rate available  (optional)

try:
    # Get the time series data of a data point.
    api_response = api_instance.get_datapoint_timeseries(project_id, data_point_id, start=start, end=end, max=max, samplerate=samplerate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->get_datapoint_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The id of the project from which to query observations for a data point | 
 **data_point_id** | **str**| Name/ID of the data point, e.g., *bacnet100-4120-CO2* | 
 **start** | **datetime**| Return only observations *after* this date-time\&quot;  If **start** is provided without **end**, the first **max** elements *after* **start** are returned.  | [optional] 
 **end** | **datetime**| Return only observations *before* this date-time\&quot;.  If **end** is provided without **start**, the last **max** elements *before* **end** are returned.  | [optional] 
 **max** | **int**| Maximum number of observations to return.  - This option is ignored when both **start** and **end** are provided.  - Setting **max** &#x3D; 0 returns *all* available data points.  | [optional] [default to 1]
 **samplerate** | **str**| Desired sampling rate. The returned observations are sampled down to the specified interval. The down sampling will be done by calculating the arithmetic average on all observations made within an interval. The timestamp will represent the beginning of the interval the resampling average is estimated for. Allowed intervals are integers combined with durations, like seconds (s), minutes (m), hours (h), and days (d), e.g.  - \&quot;10s\&quot; specifies a sampling rate of \&quot;once every 10 seconds\&quot;,  - \&quot;1h\&quot; specifies a sampling rate of \&quot;once every (1) hour\&quot;,  - \&quot;0s\&quot;, \&quot;0m\&quot;, \&quot;0h\&quot;, ... specify highest sampling rate available  | [optional] 

### Return type

[**TimeseriesWithContext**](TimeseriesWithContext.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_alert**
> Success post_alert(data_point_id, project_id, alert_type, alert)

Create a new alert.

Creates a new alert with the specified details. The following parameters can/must be provided:   - **alert_type** is mandatory. Choose from 'throughput' and 'threshold'. While 'throughput' will alarm on a lower limit of observations stored per time interval, 'threshold' will alarm on the measured values breaking the threshold limits. The alarm needs to be configured within the alert json string. Using the aedifion API/ui/ this means the json string needs to be reduced to the alert inputs needed (The lines \"JSON Example for [...]\" need to be erased. Please check consistency of brackets so that the outgoing json will be well defined.):         - **name** is mandatory, the name of the alert. The name needs to be unique. In case it is not, the error message will inform about it.   - **telegram_chatid** is optional, chat ID where you would like to recieve your alerts   - **email** is optional, email where you would like to recieve your alerts         - Mandatory for 'alert_type' = 'throughput':     - **threshold_crit**, the threshold above which the alert is fired     - **threshold_ok**, the threshold below which the alert is reset     - **period**, time period over which to measure the throughput (examples: \"1h\", \"30s\", \"10m\")    - Mandatory for 'alert_type' = 'threshold':     - **threshold_dead**, the threshold below which sensor is considered DEAD     - **threshold_info**, the threshold above which alert level is INFO (below resets to OK)     - **threshold_warn**, the threshold above which alert level is WARNING     - **threshold_crit**, the threshold above which alert level is CRITICAL     - **threshold_order**, order of the thresholds. 'asc' as described above, or 'desc' to reverse order of DEAD, OK, INFO, WARNING, and CRITICAL levels (basically, flips all comparisons from < to >= and <= to >)     - **period**, the time period after which an alert is resent (examples: \"1h\", \"30s\", \"10m\") 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
data_point_id = 'data_point_id_example' # str | The alphanumeric dataPointID of the datapoint upon which to set an alert.
project_id = 789 # int | The numeric project id to which the specified data point belongs.
alert_type = 'alert_type_example' # str | The type of the alert to create.
alert = swagger_client.NewAlert() # NewAlert | The details of the alert to create as documented in the description above.

try:
    # Create a new alert.
    api_response = api_instance.post_alert(data_point_id, project_id, alert_type, alert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->post_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_point_id** | **str**| The alphanumeric dataPointID of the datapoint upon which to set an alert. | 
 **project_id** | **int**| The numeric project id to which the specified data point belongs. | 
 **alert_type** | **str**| The type of the alert to create. | 
 **alert** | [**NewAlert**](NewAlert.md)| The details of the alert to create as documented in the description above. | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_datapoint_favorite**
> Success post_datapoint_favorite(data_point_id, project_id)

Set a data point as personal favorite.

Sets a data point referenced by its name/dataPointID as a favorite for the user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
data_point_id = 'data_point_id_example' # str | The dataPointID to to mark as favorite
project_id = 789 # int | The numeric id of the project to which the data point identified by _dataPointID_ belongs

try:
    # Set a data point as personal favorite.
    api_response = api_instance.post_datapoint_favorite(data_point_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->post_datapoint_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_point_id** | **str**| The dataPointID to to mark as favorite | 
 **project_id** | **int**| The numeric id of the project to which the data point identified by _dataPointID_ belongs | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_datapoint_renaming**
> Success post_datapoint_renaming(renaming)

Add an alternative name associated with a specific data point key for a data point.

Assigns an alternative name to a data point referenced by its name/dataPointID under the specified data point key id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
renaming = swagger_client.NewRenaming() # NewRenaming | The details of the datapoint renaming. - **renaming** is mandatory, the renaming for the datapoint referenced by the following parameters - **dataPointID** is mandatory, the name/ID of the datapoint to rename - **project_id** is mandatory, the numeric id of the project in which the datapoint referenced by _dataPointID_ must exist - **datapointkey_id** is mandatory, the numeric id of the datapointkey with which to associate the renaming\" 

try:
    # Add an alternative name associated with a specific data point key for a data point.
    api_response = api_instance.post_datapoint_renaming(renaming)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->post_datapoint_renaming: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **renaming** | [**NewRenaming**](NewRenaming.md)| The details of the datapoint renaming. - **renaming** is mandatory, the renaming for the datapoint referenced by the following parameters - **dataPointID** is mandatory, the name/ID of the datapoint to rename - **project_id** is mandatory, the numeric id of the project in which the datapoint referenced by _dataPointID_ must exist - **datapointkey_id** is mandatory, the numeric id of the datapointkey with which to associate the renaming\&quot;  | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_datapoint_tag**
> Success post_datapoint_tag(data_point_id, project_id, tag_id)

Add a tag.

Adds a tag to the specified data point.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
data_point_id = 'data_point_id_example' # str | The dataPointID of the data point to assign a tag to.
project_id = 789 # int | The numeric id of the project to which the data point identified by 'dataPointID' belongs to.
tag_id = 789 # int | The numeric id of the tag which will be assigned to the data point referenced to by 'dataPointID' and 'project_id'.

try:
    # Add a tag.
    api_response = api_instance.post_datapoint_tag(data_point_id, project_id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->post_datapoint_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_point_id** | **str**| The dataPointID of the data point to assign a tag to. | 
 **project_id** | **int**| The numeric id of the project to which the data point identified by &#39;dataPointID&#39; belongs to. | 
 **tag_id** | **int**| The numeric id of the tag which will be assigned to the data point referenced to by &#39;dataPointID&#39; and &#39;project_id&#39;. | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_alert**
> Success put_alert(data_point_id, project_id, name, param, value)

Edit an Alert.

Modify alert settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
data_point_id = 'data_point_id_example' # str | The alphanumeric dataPointID for which to delete an alarm.
project_id = 789 # int | The numeric project id to which the specified data point belongs.
name = 'name_example' # str | The name of the alert to modify.
param = 'param_example' # str | The name of the parameter to change. The available parameters can be viewed at the POST /v2/datapoint/alert endpoint, input example json.
value = 'value_example' # str | The new value for the specified parameter. Example acceptable values for period are 1s, 5m, 6h, 1w

try:
    # Edit an Alert.
    api_response = api_instance.put_alert(data_point_id, project_id, name, param, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->put_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_point_id** | **str**| The alphanumeric dataPointID for which to delete an alarm. | 
 **project_id** | **int**| The numeric project id to which the specified data point belongs. | 
 **name** | **str**| The name of the alert to modify. | 
 **param** | **str**| The name of the parameter to change. The available parameters can be viewed at the POST /v2/datapoint/alert endpoint, input example json. | 
 **value** | **str**| The new value for the specified parameter. Example acceptable values for period are 1s, 5m, 6h, 1w | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_datapoint_renaming**
> Success put_datapoint_renaming(id, renaming)

Change a renaming.

Changes the alternative name of a data point under a data point key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the data point renaming that should be updated.
renaming = swagger_client.UpdateRenaming() # UpdateRenaming | The details of the data point renaming. - **renaming** is optional, the updated renaming for the data point referenced by the following parameters 

try:
    # Change a renaming.
    api_response = api_instance.put_datapoint_renaming(id, renaming)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->put_datapoint_renaming: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the data point renaming that should be updated. | 
 **renaming** | [**UpdateRenaming**](UpdateRenaming.md)| The details of the data point renaming. - **renaming** is optional, the updated renaming for the data point referenced by the following parameters  | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_alert**
> Success toggle_alert(data_point_id, project_id, name)

Enable or disable an alert.

Enable or disable an alert.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DatapointApi(swagger_client.ApiClient(configuration))
data_point_id = 'data_point_id_example' # str | The alphanumeric dataPointID for which to delete an alarm.
project_id = 789 # int | The numeric project id to which the specified data point belongs.
name = 'name_example' # str | The name of the alert to toggle.

try:
    # Enable or disable an alert.
    api_response = api_instance.toggle_alert(data_point_id, project_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatapointApi->toggle_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_point_id** | **str**| The alphanumeric dataPointID for which to delete an alarm. | 
 **project_id** | **int**| The numeric project id to which the specified data point belongs. | 
 **name** | **str**| The name of the alert to toggle. | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

