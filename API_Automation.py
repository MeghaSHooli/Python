import requests
import json

# api-endpoint
URL = "https://reqres.in/api/users?page=2"

r = requests.get(url = URL)

# extracting data in json format
data = r.json()

data_list = data['data']

for i in data_list:
  if i['id'] == 12:
    #From the response, verify id 12 is assigned to Rachel.
    assert i['first_name'] == 'Rachel', "id 12 is not assigned to Rachel"

  #From the response, verify the total number of users is 12
  if i == (len(data_list) -1):
    assert i['id'] == 12, "the total number of users is not 12"

  #From the response, verify id 8 is assigned to Lindsay
  if i['id'] == 8:
    assert i['first_name'] == 'Lindsay', "id 8 is assigned to not Lindsay"



URL = "https://reqres.in/api/users/2"

r = requests.get(url = URL)

# extracting data in json format
data = r.json()

#From the response, verify the company name “StatusCode Weekly” is associated with employee id 2.
if data['data']['id'] == 2:
  assert data['ad']['company'] == 'StatusCode Weekly', "company name is not StatusCode Weekly"
else:
  print("ID is not 2")

#From the response, verify HTTPS Status code 404 for user id 23
URL = "https://reqres.in/api/users/23"

response = requests.get(url = URL)
if response.status_code != 404:
  print("HTTPS respose is not 404 for user id 23")


""" From the response, if id 12 is not assigned rachel
 This is just error validation has been show 
 Error test script from the assignment 1 """

for i in data_list:
  if i['id'] == 12:
    #From the response, verify id 12 is assigned to Rachel.
    assert i['first_name'] == 'Priya', "id 12 is not assigned to Rachel"

