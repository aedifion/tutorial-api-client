# -*- coding: utf-8 -*-

from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException


# Definition of API input parameter
project_id = 42   # int - A project ID can be fetched by using the graphical interface at https://api.aedifion.io/ui/#!/User/get_user_projects
data_point_id = ''   # string - A datapoint ID can be fetched by using the graphical interface at https://api.aedifion.io/ui/#!/Project/get_project_datapoints
start = ''   # string - datetime e.g. '2018-06-02 16:00:00'
end = ''   # string - datetime e.g. '2018-06-02 18:00:00'

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()

# Configure HTTP basic authorization: basicAuth
configuration.username = input("Username: ")
configuration.password = input("Password: ")


"""
    Example 1 (GET Request): Retrieve, parse and print timeseries data details.
"""

# create an API instance
api_instance = swagger_client.ApiClient(configuration=configuration)
DatapointApi = swagger_client.DatapointApi(api_client=api_instance)
UserApi = swagger_client.UserApi(api_client=api_instance)
        
try:
    # Get a timeseries.
    timeseries = DatapointApi.get_datapoint_timeseries(project_id=project_id,data_point_id=data_point_id,start=start,end=end)
    timeseries_dict = timeseries.to_dict()
    print('Timeseries data in dict data structur:')
    print(timeseries_dict)
except ApiException as e:
    print("Exception when calling DatapointApi -> get_datapoint_timeseries: %s\n" % e)

"""
    Example 2 (GET Request): Retrieve, parse and print user's details.
"""    

try:    
    #get user
    user = UserApi.get_user()
    user_dict = user.to_dict()
    print()
    print('Current username:')
    print(user_dict['user']['first_name'] + ' ' + user_dict['user']['last_name'])
except ApiException as e:
    print("Exception when calling UserApi -> get_user: %s\n" % e)   
    
"""
    Example 3 (PUT Request): Changing user's name to all upper case and back.
"""
try:
    user_obj = swagger_client.User(first_name = user_dict['user']['first_name'].upper(), last_name = user_dict['user']['last_name'].upper())
    update_user_obj = swagger_client.UpdateUser(first_name = user_dict['user']['first_name'].upper(), last_name = user_dict['user']['last_name'].upper())
    user_upper = UserApi.put_user(update_user_obj)
    print()
    print('Username is updated to:')
    print(user_upper.resource['firstName'] + ' ' + user_upper.resource['lastName'])
    
    #put user back to initial state
    update_user_obj = swagger_client.UpdateUser(first_name = user_dict['user']['first_name'], last_name = user_dict['user']['last_name'])
    user_restore = UserApi.put_user(update_user_obj)
    print()
    print('Username is restored to:')
    print(user_restore.resource['firstName'] + ' ' + user_restore.resource['lastName'])
except Exception as e:
    print(e)
    
"""
    Example 4 (POST Request): Creating another user.
    
    Note: A user can only create other users for his/her own company.
"""
try:
    auth_jdoe = ('jdoe@aedifion.com','superSecurePW')
    post_user_obj = swagger_client.NewUser(first_name='John',last_name='Doe',email=auth_jdoe[0],password=auth_jdoe[1],company_id=user_dict['company']['id'])
    post_user = UserApi.post_user(post_user_obj)
    post_user = post_user.to_dict
    print()
    print('New user created:')
    print(post_user)
except ApiException as e:
    print("Exception when calling UserApi -> post_user: %s\n" % e)
    

"""
    Example 5 (DELETE Request): Creating another user.
    
    Note: A user can only create other users for his/her own company.
"""

try:
    configuration_jdoe = swagger_client.Configuration()
    configuration_jdoe.username = auth_jdoe[0]
    configuration_jdoe.password = auth_jdoe[1]

    # create an API instance
    api_instance_jdoe = swagger_client.ApiClient(configuration=configuration_jdoe)
    UserApi_jdoe = swagger_client.UserApi(api_client=api_instance_jdoe)
    
    delete_user = UserApi_jdoe.delete_user()
    print()
    print('John Doe deleted:')
    print(delete_user)
except ApiException as e:
    print("Exception when calling UserApi -> delete_user: %s\n" % e)