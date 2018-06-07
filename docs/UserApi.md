# swagger_client.UserApi

All URIs are relative to *https://api.aedifion.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user**](UserApi.md#delete_user) | **DELETE** /v2/user | CAUTION: Deletes logged in user.
[**delete_user_plotview**](UserApi.md#delete_user_plotview) | **DELETE** /v2/user/plotview/{id} | Delete a plotview.
[**delete_user_role**](UserApi.md#delete_user_role) | **DELETE** /v2/user/{id}/role/{roleid} | Removes a role from a user.
[**get_token**](UserApi.md#get_token) | **GET** /v2/token | Get authentication token.
[**get_user**](UserApi.md#get_user) | **GET** /v2/user | Get logged in user&#39;s details.
[**get_user_favorites**](UserApi.md#get_user_favorites) | **GET** /v2/user/favorites | Get user&#39;s favorite data points.
[**get_user_plotviews**](UserApi.md#get_user_plotviews) | **GET** /v2/user/plotviews | Get user&#39;s plotviews.
[**get_user_projects**](UserApi.md#get_user_projects) | **GET** /v2/user/projects | Get user&#39;s projects.
[**get_user_reset_password**](UserApi.md#get_user_reset_password) | **GET** /v2/user/resetPassword | Resets user&#39;s password.
[**post_user**](UserApi.md#post_user) | **POST** /v2/user | Create a new user.
[**post_user_plotview**](UserApi.md#post_user_plotview) | **POST** /v2/user/plotview | Add a plotview.
[**post_user_role**](UserApi.md#post_user_role) | **POST** /v2/user/{id}/role/{roleid} | Assign a role to a user.
[**put_user**](UserApi.md#put_user) | **PUT** /v2/user | Update the details of the logged in user.
[**put_user_plotview**](UserApi.md#put_user_plotview) | **PUT** /v2/user/plotview/{id} | Update a plotview.


# **delete_user**
> Success delete_user()

CAUTION: Deletes logged in user.

Deletes the logged in user and all his/her resources - DANGER to suspend important accounts!

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # CAUTION: Deletes logged in user.
    api_response = api_instance.delete_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_plotview**
> Success delete_user_plotview(id)

Delete a plotview.

Deletes a plotview for this user.

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the plotview to delete.

try:
    # Delete a plotview.
    api_response = api_instance.delete_user_plotview(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_plotview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the plotview to delete. | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_role**
> Success delete_user_role(id, roleid)

Removes a role from a user.

Removes role with id 'role_id' from user with id 'id'.

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
id = 789 # int | The unique id of the user
roleid = 789 # int | The unique id of the role

try:
    # Removes a role from a user.
    api_response = api_instance.delete_user_role(id, roleid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique id of the user | 
 **roleid** | **int**| The unique id of the role | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> AuthToken get_token(validity=validity, scope=scope)

Get authentication token.

Returns an authentication token which contains the encrypted user name and password. The token can be used instead of HTTP basic auth by using the token as user name and leaving the password field empty.

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
validity = 24 # float | The validity for the requested token in hours. (optional) (default to 24)
scope = 'full' # str | The scope of the requested token. (optional) (default to full)

try:
    # Get authentication token.
    api_response = api_instance.get_token(validity=validity, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validity** | **float**| The validity for the requested token in hours. | [optional] [default to 24]
 **scope** | **str**| The scope of the requested token. | [optional] [default to full]

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserWithContext get_user()

Get logged in user's details.

Returns the details of the logged in user.

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # Get logged in user's details.
    api_response = api_instance.get_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserWithContext**](UserWithContext.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_favorites**
> list[DataPoint] get_user_favorites()

Get user's favorite data points.

Returns a list of data points that the user marked as his/her favorites.

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # Get user's favorite data points.
    api_response = api_instance.get_user_favorites()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_favorites: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DataPoint]**](DataPoint.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_plotviews**
> list[PlotView] get_user_plotviews()

Get user's plotviews.

Returns a list of all plotviews that the user has specified or shared.

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # Get user's plotviews.
    api_response = api_instance.get_user_plotviews()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_plotviews: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PlotView]**](PlotView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_projects**
> list[ProjectWithContext] get_user_projects()

Get user's projects.

Returns a list of all projects that the user is authorized for.

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # Get user's projects.
    api_response = api_instance.get_user_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProjectWithContext]**](ProjectWithContext.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_reset_password**
> Success get_user_reset_password(email)

Resets user's password.

Triggers a confirmation mail to the given email address that allows to reset user's password.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
email = 'email_example' # str | The user's email address.

try:
    # Resets user's password.
    api_response = api_instance.get_user_reset_password(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The user&#39;s email address. | 

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user**
> Success post_user(user)

Create a new user.

Creates a new user with the specified details.

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user = swagger_client.NewUser() # NewUser | The details of the user to create\\n - **firstName** is mandatory, the first name of the new user - **lastName**  is mandatory, the last name of the new user - **email** is mandatory, must be unique among all users - **password** is mandatory, the initial password for the new user - **comapny_id** is mandatory, the referenced company must exist\" 

try:
    # Create a new user.
    api_response = api_instance.post_user(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->post_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**NewUser**](NewUser.md)| The details of the user to create\\n - **firstName** is mandatory, the first name of the new user - **lastName**  is mandatory, the last name of the new user - **email** is mandatory, must be unique among all users - **password** is mandatory, the initial password for the new user - **comapny_id** is mandatory, the referenced company must exist\&quot;  | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_plotview**
> Success post_user_plotview(plotview)

Add a plotview.

Creates a new plotview and adds it to the list of plotviews for this user.

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
plotview = swagger_client.NewPlotView() # NewPlotView | The details of the plotview to create. - **name** is mandatory, the name of the new plotView - **plotViewJson** is mandatory, a JSON with the detailed specification of this plotview\" 

try:
    # Add a plotview.
    api_response = api_instance.post_user_plotview(plotview)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->post_user_plotview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plotview** | [**NewPlotView**](NewPlotView.md)| The details of the plotview to create. - **name** is mandatory, the name of the new plotView - **plotViewJson** is mandatory, a JSON with the detailed specification of this plotview\&quot;  | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_role**
> Success post_user_role(id, roleid)

Assign a role to a user.

Assigns role with its id 'role_id' to user with her/his id 'id'.

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
id = 789 # int | The unique id of the user
roleid = 789 # int | The unique id of the role

try:
    # Assign a role to a user.
    api_response = api_instance.post_user_role(id, roleid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->post_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique id of the user | 
 **roleid** | **int**| The unique id of the role | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_user**
> Success put_user(user)

Update the details of the logged in user.

Updates the details of the specified user (specification by authentication credentials).

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user = swagger_client.UpdateUser() # UpdateUser | The details of the updated user:   - **firstName** is optional, the new first name of the updated user   - **lastName** is optional, the new last name of the updated user   - **email** is optional, the new email address of the updated user   - **password** is optional, the new password for the updated user 

try:
    # Update the details of the logged in user.
    api_response = api_instance.put_user(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->put_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UpdateUser**](UpdateUser.md)| The details of the updated user:   - **firstName** is optional, the new first name of the updated user   - **lastName** is optional, the new last name of the updated user   - **email** is optional, the new email address of the updated user   - **password** is optional, the new password for the updated user  | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_user_plotview**
> Success put_user_plotview(id, plotview)

Update a plotview.

Updates a plotview for this user.

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
id = 789 # int | The id of the plotview to delete
plotview = swagger_client.UpdatePlotView() # UpdatePlotView | The details of the plotview update - **name** is optional, the new name of the plotview - **plotViewJson** is optional, the updated JSON specifications for the specified plotview 

try:
    # Update a plotview.
    api_response = api_instance.put_user_plotview(id, plotview)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->put_user_plotview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the plotview to delete | 
 **plotview** | [**UpdatePlotView**](UpdatePlotView.md)| The details of the plotview update - **name** is optional, the new name of the plotview - **plotViewJson** is optional, the updated JSON specifications for the specified plotview  | 

### Return type

[**Success**](Success.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

