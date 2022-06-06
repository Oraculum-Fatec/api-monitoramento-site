import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from matplotlib import pyplot as plt
from sklearn import metrics

import datetime
import time
import requests

from dataclasses import dataclass
@dataclass(frozen=True)
class ModelResult:
    n: int
    clf: DecisionTreeClassifier
    acc: float

def tree_model(max_depth: int):
    clf = DecisionTreeClassifier(max_depth=max_depth, criterion='entropy',  splitter='best') 
    clf.fit(train_x, train_y)

    pred_y = clf.predict(test_x)
    acc = metrics.accuracy_score(test_y, pred_y)
    return ModelResult(acc=acc, clf=clf, n=max_depth)

def SendResults(results):
    global clf, risk, alert
    W_test = pd.DataFrame(data = results)
    y_pred = clf.predict(W_test)
    if y_pred[0]:
        send_slack_message("Nos proximos 30 segundos, chance da aplicacao cair e de %s!" %alert[risk])
        risk+=1
    else:
        risk =0
    print(y_pred)

def send_slack_message(message):
    payload = '{"text":"%s"}' %message
    response = requests.post('https://hooks.slack.com/services/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',
                             data=payload)
    print(response.text)
    
def RequestQuery():
    global adress, query

    

    response = {"current_requests":0,
                "avg_response_time":0,
                "max_response_time":0}
    
    
    response["current_requests"] = [requests.post(adress + '/api/v1/query',
                                              params={'query': query[0]}).json()['data']['result'][0]['value'][1]]
    
    response["avg_response_time"] = [requests.post(adress + '/api/v1/query',
                                              params={'query': query[1]}).json()['data']['result'][0]['value'][1]]
    
    response["max_response_time"] = [requests.post(adress + '/api/v1/query',
                                              params={'query': query[2]}).json()['data']['result'][0]['value'][1]]
    
    return response

            
def PromQuery():
    errorFlag = 0
    while True:
        try:
            results = RequestQuery()
            
            SendResults(results)
            errorFlag = 0
            time.sleep(10)

        except Exception as e:
            errorFlag+=1
            if errorFlag >= 10:
                send_slack_message("Aplicacao caiu!")
                break
            else:
                time.sleep(5)
                continue

df = pd.read_csv("LoadTest.csv",sep=";")
df.rename(columns = {'max_users':'current_requests'}, inplace = True)

from sklearn.model_selection import train_test_split
train=df
test=df
train.reset_index(inplace=True)
test.reset_index(inplace=True)

def data_target_split(df: pd.DataFrame):
    target = df['dead'] # separa a coluna target (colunas com os dados das classes) => Y
    data = df.loc[:,'current_requests':'max_response_time'] # separa as colunas de features (colunas com os dados das features) => X
    return data, target
train_x, train_y = data_target_split(train)
test_x, test_y = data_target_split(test)

results = {n: tree_model(n) for n in range(1,4)}

clf = results[2].clf
f_names = test_x.columns
c_names = test_y.unique().astype(str)

adress = "http://localhost:9090"
query = ["sum(rate(http_server_requests_seconds_count[1m]))", # request
         "sum(rate(http_server_requests_seconds_sum[1m]))/sum(rate(http_server_requests_seconds_count[1m]))*2000", # tempo de resposta
         "max(http_server_requests_seconds_max)*1000"] # pico
risk = 0

alert = ['5%', '10%', '18%', '23%', '30%', '70%']

PromQuery()
