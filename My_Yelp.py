import requests

api_key = "WwnFNTOLh59acC69ySVCT6owelmI991pFRM1Uju2RwJCZyL2TaGKS7FV5EEo4HJ3mlGSk9ljujJt-SkTwrefSYZyqL6QGYlbym9mdgI3KhU2yh4haUH4BLZPgmt_W3Yx"

url= "https://api.yelp.com/v3/businesses/search"

my_headers = {
    "Authorization":"Bearer %s" % api_key
}

my_params = {
    "term": "restaurants",
    "location": "chicago",
    "limit": 3,
}

businesses_object = requests.get(url, headers=my_headers, params=my_params)

businesses_dict= businesses_object.text

print(businesses_dict)

##print(businesses.text)
