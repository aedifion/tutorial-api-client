# swagger_client.UserDataApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_datapoint_ids**](UserDataApi.md#get_datapoint_ids) | **GET** /v1/getDatapointIDs | Query authorized datapoint IDs for a user within a project.
[**get_projects**](UserDataApi.md#get_projects) | **GET** /v1/getProjects | Query authorized projects for a user.


# **get_datapoint_ids**
> list[Tags] get_datapoint_ids(project)

Query authorized datapoint IDs for a user within a project.

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
api_instance = swagger_client.UserDataApi()
project = 'project_example' # str | Name of the project where data will be queried from.

try: 
    # Query authorized datapoint IDs for a user within a project.
    api_response = api_instance.get_datapoint_ids(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserDataApi->get_datapoint_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Name of the project where data will be queried from. | 

### Return type

[**list[Tags]**](Tags.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> list[ByBuilding] get_projects()

Query authorized projects for a user.

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
api_instance = swagger_client.UserDataApi()

try: 
    # Query authorized projects for a user.
    api_response = api_instance.get_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserDataApi->get_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ByBuilding]**](ByBuilding.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

