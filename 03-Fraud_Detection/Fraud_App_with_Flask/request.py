
   
import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json ={'V3':1.116,'V4':-0.052	,'V7': 0.749,'V10':0.073,'V11': 0.058,'V12': 0.640,'V14': -0.830,'V16': 0.279,'V17': -0.084	,'amount':1.980})

print(r.json())