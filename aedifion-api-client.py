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

