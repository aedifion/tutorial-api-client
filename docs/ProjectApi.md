# swagger_client.ProjectApi

All URIs are relative to *https://api.aedifion.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /v2/project/{id} | Delete project.
[**delete_project_datapointkey**](ProjectApi.md#delete_project_datapointkey) | **DELETE** /v2/project/{id}/datapointkey/{keyid} | Deletes a data point key associated with the project.
[**delete_project_tag**](ProjectApi.md#delete_project_tag) | **DELETE** /v2/project/{id}/tag/{tagid} | Delete a tag.
[**get_project**](ProjectApi.md#get_project) | **GET** /v2/project/{id} | Get project&#39;s details.
[**get_project_alerts**](ProjectApi.md#get_project_alerts) | **GET** /v2/project/{id}/alerts/ | Get all alerts in a project.
[**get_project_datapointkeys**](ProjectApi.md#get_project_datapointkeys) | **GET** /v2/project/{id}/datapointkeys | Get list of data point keys associated with project.
[**get_project_datapoints**](ProjectApi.md#get_project_datapoints) | **GET** /v2/project/{id}/datapoints | Get list of data points in this project.
[**get_project_roles**](ProjectApi.md#get_project_roles) | **GET** /v2/project/{id}/roles | Get all roles defined in the project.
[**get_project_tags**](ProjectApi.md#get_project_tags) | **GET** /v2/project/{id}/tags | Get all data point tags in this project.
[**post_project**](ProjectApi.md#post_project) | **POST** /v2/project | Create a new project.
[**post_project_datapointkey**](ProjectApi.md#post_project_datapointkey) | **POST** /v2/project/{id}/datapointkey | Create new data point key in project.
[**post_project_tag**](ProjectApi.md#post_project_tag) | **POST** /v2/project/{id}/tag | Createa new tag.
[**put_project**](ProjectApi.md#put_project) | **PUT** /v2/project/{id} | Update project&#39;s details.
[**put_project_datapointkey**](ProjectApi.md#put_project_datapointkey) | **PUT** /v2/project/{id}/datapointkey/{keyid} | Updates a data point key.
[**put_project_tag**](ProjectApi.md#put_project_tag) | **PUT** /v2/project/{id}/tag/{tagid} | Update an existing tag.


# **delete_project**
> Success delete_project(id)

Delete project.

Deletes the specified project and all its associated resources.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the project that should be deleted.

try:
    # Delete project.
    api_response = api_instance.delete_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project that should be deleted. | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_datapointkey**
> Success delete_project_datapointkey(id, keyid)

Deletes a data point key associated with the project.

Deletes the specified data point key from the list of data point keys available in this project.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the project.
keyid = 789 # int | The id of the data point key to remove.

try:
    # Deletes a data point key associated with the project.
    api_response = api_instance.delete_project_datapointkey(id, keyid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project_datapointkey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project. | 
 **keyid** | **int**| The id of the data point key to remove. | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_tag**
> Success delete_project_tag(id, tagid)

Delete a tag.

Deletes an existing tag associated with this project.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the project for which to delete a tags.
tagid = 789 # int | The id of the tag to delete.

try:
    # Delete a tag.
    api_response = api_instance.delete_project_tag(id, tagid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project for which to delete a tags. | 
 **tagid** | **int**| The id of the tag to delete. | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ProjectWithContext get_project(id)

Get project's details.

Returns the details of the queried project.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the project that should be retrieved.

try:
    # Get project's details.
    api_response = api_instance.get_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project that should be retrieved. | 

### Return type

[**ProjectWithContext**](ProjectWithContext.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_alerts**
> Alerts get_project_alerts(id)

Get all alerts in a project.

Returns the details of all alerts in a project.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the project for which alerts should be queried.

try:
    # Get all alerts in a project.
    api_response = api_instance.get_project_alerts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project for which alerts should be queried. | 

### Return type

[**Alerts**](Alerts.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_datapointkeys**
> list[DataPointKey] get_project_datapointkeys(id)

Get list of data point keys associated with project.

Returns a list of all data point keys that have been created in this project.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the project for which data point keys should be queried.

try:
    # Get list of data point keys associated with project.
    api_response = api_instance.get_project_datapointkeys(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_datapointkeys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project for which data point keys should be queried. | 

### Return type

[**list[DataPointKey]**](DataPointKey.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_datapoints**
> list[DataPointWithContext] get_project_datapoints(id)

Get list of data points in this project.

Returns a list of all data points that have been created in this project.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the project for which data points should be queried.

try:
    # Get list of data points in this project.
    api_response = api_instance.get_project_datapoints(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_datapoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project for which data points should be queried. | 

### Return type

[**list[DataPointWithContext]**](DataPointWithContext.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_roles**
> ListOfRoles get_project_roles(id)

Get all roles defined in the project.

Returns a list of roles defined for the queried project.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the project.

try:
    # Get all roles defined in the project.
    api_response = api_instance.get_project_roles(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project. | 

### Return type

[**ListOfRoles**](ListOfRoles.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tags**
> list[Tag] get_project_tags(id)

Get all data point tags in this project.

Returns a list of all data point tags that have been created in this project.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the project for which to query data point tags.

try:
    # Get all data point tags in this project.
    api_response = api_instance.get_project_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project for which to query data point tags. | 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project**
> Project post_project(project)

Create a new project.

Creates a new project with the specified details.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
project = swagger_client.NewProject() # NewProject | The details of the project to create\\n - **name** is mandatory - **description** is optional (default = \\\"\\\") - **comapny_id** is mandatory and the referenced company must exist 

try:
    # Create a new project.
    api_response = api_instance.post_project(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->post_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**NewProject**](NewProject.md)| The details of the project to create\\n - **name** is mandatory - **description** is optional (default &#x3D; \\\&quot;\\\&quot;) - **comapny_id** is mandatory and the referenced company must exist  | 

### Return type

[**Project**](Project.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_datapointkey**
> Success post_project_datapointkey(id, datapointkey)

Create new data point key in project.

Creates a new data point key in this project.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the project for which a new data point key should be created.
datapointkey = swagger_client.NewDataPointKey() # NewDataPointKey | The details of the new data point key. - **name** is mandatory, the name of the new data point key - **description** is optional, a textual description for the data point key (defaults to: \\\"\\\") 

try:
    # Create new data point key in project.
    api_response = api_instance.post_project_datapointkey(id, datapointkey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->post_project_datapointkey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project for which a new data point key should be created. | 
 **datapointkey** | [**NewDataPointKey**](NewDataPointKey.md)| The details of the new data point key. - **name** is mandatory, the name of the new data point key - **description** is optional, a textual description for the data point key (defaults to: \\\&quot;\\\&quot;)  | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_tag**
> Success post_project_tag(id, tag)

Createa new tag.

Creates a new tag that can then be assigned to data points in this project.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the project for which to add a data point tag.
tag = swagger_client.NewTag() # NewTag | The details of the tag. - **key** is mandatory, the key of the tag - **value** is mandatory, the value of the key 

try:
    # Createa new tag.
    api_response = api_instance.post_project_tag(id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->post_project_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project for which to add a data point tag. | 
 **tag** | [**NewTag**](NewTag.md)| The details of the tag. - **key** is mandatory, the key of the tag - **value** is mandatory, the value of the key  | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project**
> Success put_project(id, project)

Update project's details.

Updates the details of the specified project.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the project that should be updated.
project = swagger_client.UpdateProject() # UpdateProject | The details of the update to an existing project: - **name** is optional, a new name for the referenced project - **description** is optional, a new description for the referenced project 

try:
    # Update project's details.
    api_response = api_instance.put_project(id, project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->put_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project that should be updated. | 
 **project** | [**UpdateProject**](UpdateProject.md)| The details of the update to an existing project: - **name** is optional, a new name for the referenced project - **description** is optional, a new description for the referenced project  | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_datapointkey**
> Success put_project_datapointkey(id, keyid, datapointkey)

Updates a data point key.

Updates the specified data point key associated with the project.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the project.
keyid = 789 # int | The id of the data point key to update.
datapointkey = swagger_client.UpdateDataPointKey() # UpdateDataPointKey | The details of the updated data point key. - **name** is optional, the updated name for the data point key - **description** is optional, the updated description for the data point key 

try:
    # Updates a data point key.
    api_response = api_instance.put_project_datapointkey(id, keyid, datapointkey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->put_project_datapointkey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project. | 
 **keyid** | **int**| The id of the data point key to update. | 
 **datapointkey** | [**UpdateDataPointKey**](UpdateDataPointKey.md)| The details of the updated data point key. - **name** is optional, the updated name for the data point key - **description** is optional, the updated description for the data point key  | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_tag**
> Success put_project_tag(id, tagid, tag)

Update an existing tag.

Updates an existing tag associated with this project.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the project for which to update a tag.
tagid = 789 # int | The id of the tag to update.
tag = swagger_client.UpdateTag() # UpdateTag | The details of the updated tag. - **key** is optional, the tag's key - **value** is optional, the tag's key value 

try:
    # Update an existing tag.
    api_response = api_instance.put_project_tag(id, tagid, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->put_project_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the project for which to update a tag. | 
 **tagid** | **int**| The id of the tag to update. | 
 **tag** | [**UpdateTag**](UpdateTag.md)| The details of the updated tag. - **key** is optional, the tag&#39;s key - **value** is optional, the tag&#39;s key value  | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

