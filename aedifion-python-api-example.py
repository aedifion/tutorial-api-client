import sys

"""
If script throws a 'ModuleNotFound' error, install the requests module via
  >> pip3 install requests
""" 
import requests

"""
Please configure which API to use.
 - https://api-dev.aedifion.io - aedifion's development API with the latest features but possibly unstable 
 - https://api.aedifion.io - aedifion's production API stable but possibly missing some of the latest features
 
Note: You can explore and try out the API's via the User Interface at https://api-dev.aedifion.io/ui/ and https://api.aedifion.io/ui/
"""
api_base_url = 'https://api-dev.aedifion.io'

"""
Please configure your crededentials for the selected API here.
 - *username* is your email address
 - *password* is the password you received
 
Note: Credentials are *per API*, i.e. credentials for the development API do not necessarily work for the production API and vice versa.
"""
username = ''
password = ''

if username == '' or password == '':
    print("Error: Please configure username and password in the script.")
    sys.exit(-1)

"""
    Example 1 (GET Request): Retrieve, parse and print user's details.
"""
print("(1) Retrieving user's credentials")

# Prepare the request
url = "{}/v2/user".format(api_base_url)
auth = (username, password)

# Make the request
r = requests.get(url, auth=auth)

# Process the response
if r.status_code == 200:
    print("- Request to {} successful: {}, {}".format(url, r.status_code, r.text))
    print("- Parsed response contents: ")
    userjson = r.json()
    for key,value in sorted(userjson.items()):
        print("   - {:20s} -> {}".format(key, value))
else:
    print("- Request to {} unsuccessful: {}, {}".format(url, r.status_code. r.text))
    print("- Please check your access credentials")
    sys.exit(-1)
print()

"""
    Example 2 (PUT Request): Changing user's name.
"""
print("(2) Changing user's name")

# Prepare the request
url = "{}/v2/user".format(api_base_url)
firstName = userjson['user']['firstName']#
lastName = userjson['user']['lastName']
params = {'firstName':firstName.upper(), 'lastName':lastName.upper()} # Change firstName and lastName to Capitals

 # Make the GET request
r = requests.put(url, auth=auth, json=params)

# Process the response
if r.status_code == 200:
    print("- Request to {} successful: {}, {}".format(url, r.status_code, r.text))
    json = r.json()
    print("   - firstName was {} now is {}".format(firstName, json['resource']['firstName']))
    print("   - lastName was {} now is {}".format(lastName, json['resource']['lastName']))
else:
    print("Request to {} unsuccessful: {}, {}".format(url, r.status_code, r.text))
    print("- Please check your access credentials")
    sys.exit(-1)    

# Change firstName and lastName back
params = {'firstName':firstName, 'lastName':lastName}
r = requests.put(url, auth=auth, json=params)
print()
print("(2.1) YOUR USER'S CREDENTIALS WERE SET BACK TO THE INITIAL STATE!")
print()

"""
    Example 3 (POST Request): Creating another user.
    
    Note: A user can only create other users for his/her own company.
"""
print("(3) Creating another user")

# Prepare the request
url = "{}/v2/user".format(api_base_url)
newuser = {'firstName':'Max', 
           'lastName':'Mustermann', 
           'email':'max@some-company.com', 
           'company_id':userjson['user']['company_id'],
           'password':'asecretpw'}

# Make the POST request
r = requests.post(url, auth=auth, json=newuser)

# Process the response
if r.status_code == 200:
    print("- Request to {} successful: {}, {}".format(url, r.status_code, r.text))
else:
    print("- Request to {} unsuccessful: {}, {}".format(url, r.status_code, r.text))
print()

"""
    Example 4 (DELETE Request): Creating another user.
    
    Note: A user can only create other users for his/her own company.
"""
print("(4) Delete a user")

# Prepare the request
url = "{}/v2/user".format(api_base_url)
auth_newuser = ("max@some-company.com", "asecretpw")

# Make the DELETE request
r = requests.delete(url, auth=auth_newuser)

# Process the response
if r.status_code == 200:
    print("- Request to {} successful: {}, {}".format(url, r.status_code, r.text))
else:
    print("- Request to {} unsuccessful: {}, {}".format(url, r.status_code, r.text))
