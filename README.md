# aedifion API tutorial

Welcome to the aedifion API example!

**Note:** Please contact support@aedifion.com for **demo login credentials** in order to use the aedifion API demo tutorial!

This tutorial demonstrates how you can use the aedifion http API within your programming environment. Since there are many ways how to interact with a http API, these are examples how to
- use the graphical aedifion API user interface
- use cURL
- export API clients for several programming environments form [Swagger Editor](https://swagger.io/swagger-editor/)
- include a Python client generated with [Swagger Codegen](https://swagger.io/swagger-codegen/)

among many other ways to interact with the aedifion API.

## Use the graphical aedifion API user interface
The graphical user interface is designed to give a fast introduction to the aedifion API.
1. Visit https://api.aedifion.io/ui/
2. Click `Authorize` at the right top and insert the demo user login credentials.
3. The aedifion API endpoints are sorted by the categories *Timeseries*, *Access Control* and *User Data*. A good starting point for first time users is to click on
*User Data* and try `/v1/getProjects`. After you chose the endpoint click the button *Try it out!*. The endpoint will show you the http request made
for querying the endpoint, the returned answer and a cURL request which could be used to query the API. If you are interested in cURL have a look at the following section.
4. Try as many endpoints as you like!

## Use cURL
[cURL](https://curl.haxx.se/) stands for "client for URL". It is a command line tool and library
for transferring data with URLs which allows to send individual http messages. Therefore any aedifion http API request can be made from cURL.
There are cURL libraries for many different operating systems available e.g. at the [cURL project website](https://curl.haxx.se/download.html).

### cURL with Windows

1. Downlaod cURL e.g. from the [cURL project website](https://curl.haxx.se/download.html) to your computer. The [download wizard](https://curl.haxx.se/dlwiz/) will help you to pick the right version for your Windows.
2. Unpack the .zip file.
3. Now there are two options how to run curl:
    1. Run curl directly form the folder you downloaded curl to:
        - Open the Windows command line
        - change the working directory to the path of `curl.exe`, e.g. to `D:<path>\bin\curl.exe` while `<path>` depends on curl distribution and storage path
            - First change to the correct harddrive partition: `D:`
            - Then `cd <path>\bin\`
            - Now try the aedifion API - **NOTE**: Please fill `<username>` and `<password>` with the demo login credentials:
                - getToken: `curl.exe -u <username>:<password> -X GET -H 'Content-Type:application/json' "https://api.aedifion.io/v1/getToken"`
                - getDatapointIDs - **NOTE**: Please *fill* <project> with the project name you want to query data from: `curl.exe -u <username>:<password> -X GET -H 'Content-Type:application/json' "https://api.aedifion.io/v1/getDatapointIDs?project=<project>"`
    2. Add an *environment variable* to the path of *curl.exe* in order to directly adress this executable by `curl` in the command line (e.g the path you saved curl to might be `C:\Program Files\curl\bin\curl.exe` - depends on curl distribution and storage path).
        - Open the Windows command line and try the aedifion API - **NOTE**: Please fill `<username>`and `<password>` with the demo login credentials:
            - getToken: `curl -u <username>:<password> -X GET -H 'Content-Type:application/json' "https://api.aedifion.io/v1/getToken"`
            - getDatapointIDs - **NOTE**: Please *fill* <project> with the project name you want to query data from: `curl -u <username>:<password> -X GET -H 'Content-Type:application/json' "https://api.aedifion.io/v1/getDatapointIDs?project=<project>"`

## Export API clients for several programming environments form [Swagger Editor](https://swagger.io/swagger-editor/)
There is an online version of the swagger editor as well as an downloadable one. This tutorial is using the [online editor](https://editor.swagger.io/).
1. Download `aedifion.yaml` file.
2. Go to https://editor.swagger.io/
3. Upload the `aedifion.yaml` by clicking on *File* -> *Import File* and insert the path to the `aedifion.yaml` file.
4. Now you can export an API client by *Generate Client* -> choose an export you prefer.
5. [Swagger Codegen](https://swagger.io/swagger-codegen/) will automaticly generate a API client. Download and safe the exported client. Please follow the instructions in `README.md` file, which is included in the downloaded folder, in order to embed the API client in your programming environment. The next section will explain how to include a Python API client.

## Include a Python client generated with [Swagger Codegen](https://swagger.io/swagger-codegen/)

This tutorial will explain how to include a Python client for the aedifion API which is generated using [Swagger Codegen](https://swagger.io/swagger-codegen/). 
1. Either download the aedifion API Python client at https://github.com/aedifion/aedifion-api-python-client **or** generate the client by following the steps in the previous section *"Export API clients for several programming environments form Swagger Editor"*. Note: This tutorial is based on a Swagger Codgen 2.2.3 Python client export.
2. The Swagger Codgen export will contain a generically generated `README.md`file. The further tutorial will be based on this and any manual commants, notations and hints are written in **_bold italics_**. 

### swagger-client
**_General information on the aedifion API from https://api.aedifion.io/ui/ :_**

Welcome to aedifion's http API! This graphical interface will give you a hands-on experience of the API.  In order to protect your privacy and security on the web, all of our API endpoints require a TLS encrypted connection. The aedifion server's certificate is using the GeoTrust Inc. CA, therefore the certificate is included in most programming and web environments by default.    All resources are access controlled using personal user accounts including individual access privileges. We implemented token-based authentication, so you do not have to bother to enter your username and password multiple times during a session or even saving this sensitive data within your programming environment. You can request a token at our API Endpoint \"/v1/getToken\" via basic http authentication.    We have prepared an example for you how to use our API in Python and cURL. The examples will provide you with an API client and a tutorial how to use it. In addition we gathered information how to generate API clients for other programming languages at https://github.com/aedifion/tutorial-api-client    Note: Currently the aedifion API does not support time zones. On data acquisition the time series will be time stamped with local time. Any information on the time zone will be ignored. On data export the time series will have the same time stamp as on data acquisition and the time zone information will be set to UTC+0. E.g. an observation made in Berlin (UTC+1) at 13:00:00 will have the time stamp 13:00:00 UTC+0 on data export. Please keep this in mind if you're application is time zone sensitve.    This API will grow along with the services of aedifion. For any further information, please contact support@aedifion.com 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
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

**_The Setuptool allows to install the Swagger Python client for the aedifion API from a local file folder. Therefore Setuptools can be used if you downloaded the aedifion API Python client form https://github.com/aedifion/aedifion-api-python-client to your local machine._**

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
api_instance = swagger_client.AccessControlApi()

try:
    # Query session access token.
    api_response = api_instance.get_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlApi->get_token: %s\n" % e)

```

#### Documentation for API Endpoints

All URIs are relative to *https://api.aedifion.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccessControlApi* | [**get_token**](docs/AccessControlApi.md#get_token) | **GET** /v1/getToken | Query session access token.
*TimeseriesApi* | [**get_first_after**](docs/TimeseriesApi.md#get_first_after) | **GET** /v1/getFirstAfter | Query first observation made after a certain point in time.
*TimeseriesApi* | [**get_last_before**](docs/TimeseriesApi.md#get_last_before) | **GET** /v1/getLastBefore | Query last observation made before a certain point in time.
*TimeseriesApi* | [**get_timeseries_by_id**](docs/TimeseriesApi.md#get_timeseries_by_id) | **GET** /v1/getTimeseriesByID | Query observations for datapoint Ids within time interval.
*UserDataApi* | [**get_datapoint_ids**](docs/UserDataApi.md#get_datapoint_ids) | **GET** /v1/getDatapointIDs | Query authorized datapoint IDs for a user within a project.
*UserDataApi* | [**get_projects**](docs/UserDataApi.md#get_projects) | **GET** /v1/getProjects | Query authorized projects for a user.


#### Documentation For Models
**_The models will be reviewed and changed very soon. Please do not mind the naming inconsistency._**

 - [ByBuilding](docs/ByBuilding.md)
 - [ByTag](docs/ByTag.md)
 - [NextLast](docs/NextLast.md)
 - [ResultsTimestamp](docs/ResultsTimestamp.md)
 - [Tags](docs/Tags.md)

#### Documentation For Authorization
**_Please contact support@aedifion.com to receive login credentials for demo purposes._**

#### basicAuth

- **Type**: HTTP basic authentication


#### Author

support@aedifion.com


### aedifion API Python client
The aedifion API Python client (`aedifion-api-client.py`) is an example how to use the generic Swagger Codegan code and add individual functionality e.g. asking for an input of login credentials as soon as a token is requested.
Several calls of the aedifion API are implemented including exemplarily API input parameters. In order to query every API endpoint one-by-one, some are commented out. They can be reactivated to try these endpoints. **Please feel free to give the aedifion-api-client.py a try!**

#### Code of `aedifion-api-client.py`

This script is designed for Python 3.4+.
To just view the code of `aedifion-api-client.py`, please have a look at the following lines of code:

```
# requirements: Python 3.4+

from __future__ import print_function
import time, json
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.by_building import ByBuilding
from swagger_client.models.tags import Tags
from swagger_client.models.by_tag import ByTag
from pprint import pprint


# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = input("Username: ")
swagger_client.configuration.password = input("Password: ")


# create an instance for each API class
api_instance_ACA = swagger_client.AccessControlApi()   
# get_token()

api_instance_UDA = swagger_client.UserDataApi()
#get_datapoint_ids(project)
#get_projects()

api_instance_TA = swagger_client.TimeseriesApi()
#get_first_after( project, timestamp, datapoint_id )
#get_last_before( project, timestamp, datapoint_id )
#get_timeseries_by_id( project, timestamp_start, timestamp_end, datapoint_id ):

try:

    # Query session access token.
    api_response = api_instance_ACA.get_token()
    
    #for demonstration purpose:
    print("\nToken:") 
    pprint(api_response)
    
    #Configure the client with username="TOKEN" and password='unused' 
    api_resp = api_response.replace('\'','"')
    obj = json.loads(api_resp)
    swagger_client.configuration.username = obj['token']
    swagger_client.configuration.password = 'unused'
     
    
    #get your data from server:    
    api_response = api_instance_UDA.get_projects()     
    
    #for demonstration purpose: json-format
    print("\nProject:")
    pprint(api_response)
    # extract all values from  response
    for item in api_response:
       print((item.to_dict())['building'])
    
    
    # example to extract the first result and use it to call another endpoint   
    project = (api_response[0].to_dict())['building']
    api_response = api_instance_UDA.get_datapoint_ids(project)
    
    #for demonstration purpose:
    print("\nDatapointIDs:")
    pprint(api_response)
    # extract all keys/values from  response
    for item in api_response:
       print((item.to_dict())['key'])
       print((item.to_dict())['value'])
    

    '''
    # please insert your parameters
    project="project-name"    
    timestamp_start = '2010-01-01T00:00:00Z'  
    timestamp_end   = '2020-01-01T00:00:00Z'
    datapoint_id = ["name=bacnet2001-Volumenstromanzeige-Abluftventilator"]
    
    print("\nTimeseriesByID:")
    api_response = api_instance_TA.get_timeseries_by_id( project, timestamp_start, timestamp_end, datapoint_id )
    pprint(api_response)
    '''
    # some advices how to extract the values from the api_response
    '''
    pprint(api_response[0].to_dict()['schema'])
    pprint(api_response[0].to_dict()['tagstring'])
    
    for item in api_response[0].to_dict()['schema']:
       pprint(item['time'])
       pprint(item['value'])
    '''
   
except ApiException as e:
    print("Exception when calling AccessControlApi->get_token: %s\n" % e)
```