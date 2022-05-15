import datetime
import time
import requests  

def dbquery(adress, query):

    response = requests.post(adress + '/api/v1/query',
      params={
        'query': query})

    results = response.json()['data']['result']
    return results
