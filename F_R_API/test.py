import requests

base= "http://127.0.0.1:5000/"#base url of api

#usage of json is to make the output not look like a object but to rather look like some info

data=[{"Likes":2090,"name":"Sumukh","Views":2120000},
        {"Likes":203,"name":"Flasky","Views":1230000},
        {"Likes":2000,"name":"Iron man","Views":200000000}]

for i in range(len(data)):
    response=requests.put(base+ "video/"+str(i),data[i] )#put request
    print(response.json())

input()

response=requests.get(base+ "video/1" )#get request
print(response.json())

"""
#patch/update query
response=requests.patch(base+ "video/2",{"views":99,"likes":109} )#get request
print(response.json())
"""