# aedifion API tutorial

Welcome to the aedifion API example!

**Note:** The tutorials are preconfigured to interact with the official API at api.aedifion.io. In case you want to interact with aedifion's development API, please change the URL accordingly to api-dev.aedifion.io.

Please contact support@aedifion.com for **personalized login credentials** in order to use the aedifion APIs!

This tutorial demonstrates how you can use the aedifion http API within your programming environment. Since there are many ways how to interact with a http API, these are examples how to
- use the aedifion Excel plug-in to import, resample and plot timeserieses to/within Microsoft Excel
- use the graphical aedifion API user interface
- use cURL
- use MATLAB `webread`
- use Python with `requests` library
- export API clients for several programming environments form [Swagger Editor](https://swagger.io/swagger-editor/)
- include a Python client generated with [Swagger Codegen](https://swagger.io/swagger-codegen/)

among many other ways to interact with the aedifion API.

## Use the aedifion Excel plug-in
The aedifion Excel plug-in can be downloaded at https://github.com/aedifion/aedifion-excel-plugin. Please follow the instructions provided in the download repository to install the plug-in to your Microsoft Excel. The aedifion plug-in will add a new ribbon to your Excel. Just click the ribbon and you can import timeseries data to your Excel sheets and own Excel tools right away.

## Use the graphical aedifion API user interface
The graphical user interface is designed to give a fast introduction to the aedifion API and give you a fast access to your data.
1. Visit https://api.aedifion.io/ui/
2. Click `Authorize` at the right top and insert your user login credentials. **Note:** Make sure you inserted the correct user credentials since the graphical interface will not check them and will give an `Basic authentication - authorized` feedback anyways. The easiest way to check if you inserted the correct data is trying the https://api.aedifion.io/ui/#!/User/get_token endpoint.
3. The aedifion API endpoints are sorted by the categories *User*, *Project* and *Datapoints*. A good starting point for first time users is to click on
*User* and try `/v2/user/projects`. After you chose the endpoint click the button *Try it out!*. The endpoint will show you the http request made
for querying the endpoint, the returned answer and a cURL request which could be used to query the API using cURL. If you are interested in cURL have a look at the following section.
4. Try as many endpoints as you like!

## Use cURL
[cURL](https://curl.haxx.se/) stands for "client for URL". It is a command line tool and library
for transferring data with URLs which allows to send individual http messages. Therefore any aedifion http API request can be made from cURL.
There are cURL libraries for many different operating systems available e.g. at the [cURL project website](https://curl.haxx.se/download.html).

### cURL with Windows

1. Download cURL e.g. from the [cURL project website](https://curl.haxx.se/download.html) to your computer. The [download wizard](https://curl.haxx.se/dlwiz/) will help you to pick the right version for your Windows.
2. Unpack the .zip file.
3. Now there are two options how to run curl:
    1. (recommended) Add an *environment variable* to the path of *curl.exe* in order to directly address this executable by `curl` in the command line (e.g the path you saved curl to might be `C:\Program Files\curl\bin\curl.exe` - depends on curl distribution and storage path).
        - In order to use cURL open the Windows command line and try the aedifion API with the examples below.
	2. Run curl directly form the folder you downloaded curl to:
        - Open the Windows command line
        - change the working directory to the path you saved cURL to, e.g. `C:\Program Files\<path>\bin\curl.exe` while `<path>` depends on cURL distribution and storage path.
            - First change to the correct hard drive partition: e.g. `D:`
            - Then `cd <path>\bin\`
		- When using the examples below, start the cURL commands with `curl.exe` instead of `curl`.
			
4. Try the aedifion API with cURL 
	Basic examples:
		- **NOTE:** Please fill `<username>` with your actual login username - after executing the cURL command you will be asked to insert your password:
		- token: `curl -u <username> -X GET --header "Accept: application/json" "https://api.aedifion.io/v2/token?validity=1&scope=full"`
		- project/{id}} 
			- Please *fill* <id> with the project ID of the project you want to query data from. If you are not aware of the project IDs your account is authorized for, either use graphical interface at `https://api.aedifion.io/ui/#!/User/get_user_projects` or in case you want to challenge yourself query `https://api.aedifion.io/v2/user/projects` by cURL.
			- `curl -u <username> -X GET --header "Accept: application/json" "https://api.aedifion.io/v2/project/<id>"`
	Using cURL commands form the graphical interface at `https://api.aedifion.io/ui/`:
		- By trying out any endpoint the graphical interface will provide an exemplary cURL command for the specific endpoint.
		- You can use these commands copy-paste. **NOTE:** On Windows you need to substitute the single quotes by double quotes. Your user credentials are included in the argument `--header 'Authorization: Basic <basic auth encrypted user credentials>'`.
	
## MATLAB `webread`
MATLAB contains the `webread` function which allows to interact with http APIs. This tutorial gives a functional example of how to use webread to import time series to MATLAB by interacting with the aedifion API.
1. Download the two MATLAB files (resample.m and queryTimeseriesAedifion.m).
2. Parametrize the variables in the resampling.m file. Example values are given in the comments of the script.
3. Run the script.
4. The MATLAB console will ask you to insert your user credentials.
5. MATLAB will automatically import the time series for the chosen data point within the interval and resample it to one second sample rate.
6. Try to interact with other aedifion endpoints from MATLAB by adding own implementations.

## Python with `requests` library
There are many ways to interact with http APIs from Python. One of them is by using the `requests` library.
1. Download the file `aedifion-python-api-example.py`.
2. Make sure `requests` is installed, e.g. by the `pip3 install requests`.
3. Run `aedifion-api-python-example.py`.
4. The script executes exemplary get/post/put/delete interactions with the aedifion API and prints the results to the python console.
5. Try to interact with other aedifion endpoints from Python by adding own implementations.
			
## Export API clients for several programming environments form [Swagger Editor](https://swagger.io/swagger-editor/)
There is an online version of the swagger editor as well as an downloadable one. This tutorial is using the [online editor](https://editor.swagger.io/).
1. Download `aedifion.yaml` file.
2. Go to https://editor.swagger.io/
3. Upload the `aedifion.yaml` by clicking on *File* -> *Import File* and insert the path to the `aedifion.yaml` file. In case you want to generate a client for the development API, please change `host:` to `api-dev.aedifion.io`.
4. Now you can export an API client by *Generate Client* -> choose an export you prefer.
5. [Swagger Codegen](https://swagger.io/swagger-codegen/) will automaticly generate a API client. Download and safe the exported client. Please follow the instructions in `README.md` file, which is included in the downloaded folder, in order to embed the API client in your programming environment. The next section will explain how to include a Python API client.

## Include a Python client generated with [Swagger Codegen](https://swagger.io/swagger-codegen/)

This tutorial will explain how to include a Python client for the aedifion API which is generated using [Swagger Codegen](https://swagger.io/swagger-codegen/). 
The Swagger Codgen export will contain a generically generated `README.md`file. The further tutorial will be based on this and any manual comments, notations and hints are written in **_bold italics_**.  In case you want to use the client for the development API, please follow the tutorial and install the regular client. Please change the `host` varibale in `configurations.py` to `api-dev.aedifion.io`. The file can be found at your Python installation path at `<Python path>/Lib/site-packages/swagger-client/`.

### swagger-client
**_General information on the aedifion API from https://api.aedifion.io/ui/ :_**

Welcome to the aedifion HTTP API! This user interface allows you to explore and test our API endpoints.  In order to protect your data, API endpoints are accessible only via HTTPS and require user authentication. Permissions to access critical endpoints, e.g. for creating new users, are under further role based access control.  We implemented token-based authentication for your convenience. You can request a token at our API Endpoint \"/v2/getToken\" (section \"User\") via HTTP basic auth. For more information on tokens please read the endpoint's description.  Furthermore we prepared different examples on how to use our API, e.g. from MatLab, Python or cURL at https://github.com/aedifion/tutorial-api-client. The examples will provide you with API clients and tutorials how to use them. In addition we gathered information on how to generate API clients for other programming languages.  Also the aedifion Excel plug-in makes use of the API. It enables you to one-click import, resample and plot timeseries data within your Microsoft Excel environment. Download it for free on https://github.com/aedifion/aedifion-excel-plugin.  *Note:* Currently the aedifion API exports time series data in the time zone that it was collected, meaning that on data export the time series will have the same time stamp as on data acquisition and the time zone information will be set to Zulu / UTC+0 irrespective of the actual time-zone. E.g. an observation made in Berlin (UTC+1) at 13:00:00 will have the time stamp 13:00:00Z on data export. Please keep this in mind if you're application is time zone sensitive. We will add proper support of time zones, soon.  This API has three sections:  - \"User\" comprises endpoints for managing users and their personal preferences such as favorites.  - \"Project\" comprises endpoints for managing projects and project-related resources such as data point keys.  - \"Datapoint\" comprises endpoints for managing single data points and querying their time-series data.   This API will grow along with the services of aedifion.  For any further information or feedback, please contact us or sign up to one of our webinares at support@aedifion.com

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

#### Requirements.

Python 2.7 and 3.4+

#### Installation & Usage
**_Using pip or Setuptools to install the aedifion API swagger client means it will be added to your system Python packages. This means all Python users will be able to import the API library by including `import swagger_client` in their python script. If you do not want to install the client system-wide make use of the pip and Setuptools option `--user` option or download the aedifion API client. In this case you will need to manage the installation folder so that it is readable by the Python code in which you wish to include the `swagger_client` package. You will also need to change the line 'import swagger_client' so that swagger_client contains the path to the library relative to your Python code. Also you need to install the required Python packages by `pip install -r <path>/swagger-client/requirements.txt`, where `<path>` has to be replaced by the actual path to the aedifion API Python client on your computer._**


##### pip install

**_More information on pip: https://pip.pypa.io/en/stable/user_guide/_**

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/aedifion/aedifion-api-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/aedifion/aedifion-api-python-client.git`)

Then import the package:
```python
import swagger_client 
```

##### Setuptools

**_The Setuptool allows to install the Swagger Python client for the aedifion API from a local file folder. Therefore Setuptools can be used if you downloaded the aedifion API Python client form https://github.com/aedifion/aedifion-api-python-client to your local machine or generate the client yourself by following the steps in the previous section *"Export API clients for several programming environments form Swagger Editor"*._**

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

#### Getting Started
**_This is a minimal example on how to include the swagger client, which was generated by Swagger Codegen. There is a more complete example in the file `aedifion-api-client.py`. It is presented in the subsection `aedifion API Python client`. If you are using the minimal example, saving your login credentials in plain text could present a security risk. Have a look at `aedifion-api-client.py` for another solution for managing credentials._**

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = swagger_client.DatapointApi()
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

## Documentation for API Endpoints

All URIs are relative to *https://api.aedifion.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DatapointApi* | [**delete_alert**](docs/DatapointApi.md#delete_alert) | **DELETE** /v2/datapoint/alert/ | Delete an alert.
*DatapointApi* | [**delete_datapoint_favorite**](docs/DatapointApi.md#delete_datapoint_favorite) | **DELETE** /v2/datapoint/favorite | Remove a personal favorite data point.
*DatapointApi* | [**delete_datapoint_renaming**](docs/DatapointApi.md#delete_datapoint_renaming) | **DELETE** /v2/datapoint/renaming/{id} | Delete an alternative name for a given data point under a given data point key.
*DatapointApi* | [**delete_datapoint_tag**](docs/DatapointApi.md#delete_datapoint_tag) | **DELETE** /v2/datapoint/tag/{id} | Remove tag from data point.
*DatapointApi* | [**get_alert**](docs/DatapointApi.md#get_alert) | **GET** /v2/datapoint/alert/ | Get alert details.
*DatapointApi* | [**get_allalerts**](docs/DatapointApi.md#get_allalerts) | **GET** /v2/datapoint/allalerts/ | Get all alerts on a datapoint.
*DatapointApi* | [**get_datapoint**](docs/DatapointApi.md#get_datapoint) | **GET** /v2/datapoint | Get details about data point.
*DatapointApi* | [**get_datapoint_timeseries**](docs/DatapointApi.md#get_datapoint_timeseries) | **GET** /v2/datapoint/timeseries | Get the time series data of a data point.
*DatapointApi* | [**post_alert**](docs/DatapointApi.md#post_alert) | **POST** /v2/datapoint/alert | Create a new alert.
*DatapointApi* | [**post_datapoint_favorite**](docs/DatapointApi.md#post_datapoint_favorite) | **POST** /v2/datapoint/favorite | Set a data point as personal favorite.
*DatapointApi* | [**post_datapoint_renaming**](docs/DatapointApi.md#post_datapoint_renaming) | **POST** /v2/datapoint/renaming | Add an alternative name associated with a specific data point key for a data point.
*DatapointApi* | [**post_datapoint_tag**](docs/DatapointApi.md#post_datapoint_tag) | **POST** /v2/datapoint/tag | Add a tag.
*DatapointApi* | [**put_alert**](docs/DatapointApi.md#put_alert) | **PUT** /v2/datapoint/alert/ | Edit an Alert.
*DatapointApi* | [**put_datapoint_renaming**](docs/DatapointApi.md#put_datapoint_renaming) | **PUT** /v2/datapoint/renaming/{id} | Change a renaming.
*DatapointApi* | [**toggle_alert**](docs/DatapointApi.md#toggle_alert) | **PUT** /v2/datapoint/alert_toggle/ | Enable or disable an alert.
*ProjectApi* | [**delete_project**](docs/ProjectApi.md#delete_project) | **DELETE** /v2/project/{id} | Delete project.
*ProjectApi* | [**delete_project_datapointkey**](docs/ProjectApi.md#delete_project_datapointkey) | **DELETE** /v2/project/{id}/datapointkey/{keyid} | Deletes a data point key associated with the project.
*ProjectApi* | [**delete_project_tag**](docs/ProjectApi.md#delete_project_tag) | **DELETE** /v2/project/{id}/tag/{tagid} | Delete a tag.
*ProjectApi* | [**get_project**](docs/ProjectApi.md#get_project) | **GET** /v2/project/{id} | Get project&#39;s details.
*ProjectApi* | [**get_project_alerts**](docs/ProjectApi.md#get_project_alerts) | **GET** /v2/project/{id}/alerts/ | Get all alerts in a project.
*ProjectApi* | [**get_project_datapointkeys**](docs/ProjectApi.md#get_project_datapointkeys) | **GET** /v2/project/{id}/datapointkeys | Get list of data point keys associated with project.
*ProjectApi* | [**get_project_datapoints**](docs/ProjectApi.md#get_project_datapoints) | **GET** /v2/project/{id}/datapoints | Get list of data points in this project.
*ProjectApi* | [**get_project_roles**](docs/ProjectApi.md#get_project_roles) | **GET** /v2/project/{id}/roles | Get all roles defined in the project.
*ProjectApi* | [**get_project_tags**](docs/ProjectApi.md#get_project_tags) | **GET** /v2/project/{id}/tags | Get all data point tags in this project.
*ProjectApi* | [**post_project**](docs/ProjectApi.md#post_project) | **POST** /v2/project | Create a new project.
*ProjectApi* | [**post_project_datapointkey**](docs/ProjectApi.md#post_project_datapointkey) | **POST** /v2/project/{id}/datapointkey | Create new data point key in project.
*ProjectApi* | [**post_project_tag**](docs/ProjectApi.md#post_project_tag) | **POST** /v2/project/{id}/tag | Createa new tag.
*ProjectApi* | [**put_project**](docs/ProjectApi.md#put_project) | **PUT** /v2/project/{id} | Update project&#39;s details.
*ProjectApi* | [**put_project_datapointkey**](docs/ProjectApi.md#put_project_datapointkey) | **PUT** /v2/project/{id}/datapointkey/{keyid} | Updates a data point key.
*ProjectApi* | [**put_project_tag**](docs/ProjectApi.md#put_project_tag) | **PUT** /v2/project/{id}/tag/{tagid} | Update an existing tag.
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /v2/user | CAUTION: Delete logged in user.
*UserApi* | [**delete_user_plotview**](docs/UserApi.md#delete_user_plotview) | **DELETE** /v2/user/plotview/{id} | Delete a plotview.
*UserApi* | [**delete_user_role**](docs/UserApi.md#delete_user_role) | **DELETE** /v2/user/{id}/role/{roleid} | Removes a role from a user.
*UserApi* | [**get_token**](docs/UserApi.md#get_token) | **GET** /v2/token | Get authentication token.
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /v2/user | Get logged in user&#39;s details.
*UserApi* | [**get_user_favorites**](docs/UserApi.md#get_user_favorites) | **GET** /v2/user/favorites | Get user&#39;s favorite data points.
*UserApi* | [**get_user_plotviews**](docs/UserApi.md#get_user_plotviews) | **GET** /v2/user/plotviews | Get user&#39;s plotviews.
*UserApi* | [**get_user_projects**](docs/UserApi.md#get_user_projects) | **GET** /v2/user/projects | Get user&#39;s projects.
*UserApi* | [**get_user_reset_password**](docs/UserApi.md#get_user_reset_password) | **GET** /v2/user/resetPassword | Resets user&#39;s password.
*UserApi* | [**post_user**](docs/UserApi.md#post_user) | **POST** /v2/user | Create a new user.
*UserApi* | [**post_user_plotview**](docs/UserApi.md#post_user_plotview) | **POST** /v2/user/plotview | Add a plotview.
*UserApi* | [**post_user_role**](docs/UserApi.md#post_user_role) | **POST** /v2/user/{id}/role/{roleid} | Assign a role to a user.
*UserApi* | [**put_user**](docs/UserApi.md#put_user) | **PUT** /v2/user | Update the details of the logged in user.
*UserApi* | [**put_user_plotview**](docs/UserApi.md#put_user_plotview) | **PUT** /v2/user/plotview/{id} | Update a plotview.


#### Documentation For Models
**_The models will be reviewed and changed very soon. Please do not mind the naming inconsistency._**

 - [Alert](docs/Alert.md)
 - [Alerts](docs/Alerts.md)
 - [AuthTag](docs/AuthTag.md)
 - [AuthToken](docs/AuthToken.md)
 - [Company](docs/Company.md)
 - [DataPoint](docs/DataPoint.md)
 - [DataPointKey](docs/DataPointKey.md)
 - [DataPointWithContext](docs/DataPointWithContext.md)
 - [Error](docs/Error.md)
 - [ListOfRoles](docs/ListOfRoles.md)
 - [NewAlert](docs/NewAlert.md)
 - [NewDataPointKey](docs/NewDataPointKey.md)
 - [NewPlotView](docs/NewPlotView.md)
 - [NewProject](docs/NewProject.md)
 - [NewRenaming](docs/NewRenaming.md)
 - [NewRole](docs/NewRole.md)
 - [NewTag](docs/NewTag.md)
 - [NewUser](docs/NewUser.md)
 - [Observation](docs/Observation.md)
 - [PlotView](docs/PlotView.md)
 - [Project](docs/Project.md)
 - [ProjectWithContext](docs/ProjectWithContext.md)
 - [Renaming](docs/Renaming.md)
 - [Role](docs/Role.md)
 - [Success](docs/Success.md)
 - [Tag](docs/Tag.md)
 - [Timeseries](docs/Timeseries.md)
 - [TimeseriesWithContext](docs/TimeseriesWithContext.md)
 - [UpdateDataPointKey](docs/UpdateDataPointKey.md)
 - [UpdatePlotView](docs/UpdatePlotView.md)
 - [UpdateProject](docs/UpdateProject.md)
 - [UpdateRenaming](docs/UpdateRenaming.md)
 - [UpdateRole](docs/UpdateRole.md)
 - [UpdateTag](docs/UpdateTag.md)
 - [UpdateUser](docs/UpdateUser.md)
 - [User](docs/User.md)
 - [UserWithContext](docs/UserWithContext.md)

#### Documentation For Authorization
**_Please contact support@aedifion.com to receive login credentials._**

#### basicAuth

- **Type**: HTTP basic authentication


#### Author

support@aedifion.com


### aedifion API Python client
The aedifion API Python client (`aedifion-api-client.py`) is an example how to use the generic Swagger Codegan code and add individual functionality e.g. asking for an input of login credentials as soon as a token is requested. **Please install the aedifion API client first!**
Several calls of the aedifion API are implemented including exemplary API input parameters. In order to query every API endpoint one-by-one, some are commented out. They can be reactivated to try these endpoints. **Please feel free to give the aedifion-api-client.py a try!**
