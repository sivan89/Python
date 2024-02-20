import requests


""" #api_url = "https://reqres.in/api/users?page=2"
api_url = "https://reqres.in/api/users/2"
#api_url = "https://reqres.in/api/users/23"
#api_url = "https://reqres.in/api/unknown"

print(requests.get(api_url)) #,auth = HTTPBasicAuth('user', 'pass')

data = requests.get(api_url)

print(data.status_code) #filter only the code
print(data.json()) """

""" print("****************************************")

api_url = "https://reqres.in/api/users"
update = {"name" : "Smart" , "last_name": "hel"}
respo = requests.post(api_url, json = update)
print(respo.status_code)
print(respo.json()) """

""" print("****************************************")

api_url = "https://reqres.in/api/users/1"
update = {"id": 1, "name" : "Smart" , "last_name": "hel"}
updated = requests.put(api_url, json = update)
print(updated.status_code)
print(updated.json()) """

print("****************************************")

api_url = "https://reqres.in/api/users/2"
response = requests.delete(api_url)
print(response.status_code)