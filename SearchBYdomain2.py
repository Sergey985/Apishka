import datetime
from sqlalchemy import Column, Integer, Table, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, Query
from sqlalchemy import MetaData
import requests
import json
from pygame import mixer
mixer.init()

engine = create_engine('sqlite:///C:/DB/test.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

meta = MetaData()
syu = Table('Domains', meta,
      Column('Domain', String),
        Column('id', Integer, primary_key = True )

)
meta.create_all(engine)
url2 = "https://core-api-dev-dnprotect.wecandevelopit.com/api/v1/rate/current/details"
url1 = "https://core-api-dev-dnprotect.wecandevelopit.com/api/v1/rate/calculate"

headers = {
            'Content-Type': 'application/json'
        }
connection = engine.connect()

def search_malware_domains():
    s = engine.execute('SELECT Domain FROM Domains WHERE id>9 ')
    i = 0
    for rowitem in s:
        i = i+1
        rowitem = str(rowitem)
        rowitem = rowitem.replace("'","")
        rowitem = rowitem.replace(",","")
        rowitem = rowitem.replace("(","")
        rowitem = rowitem.replace(")", "")

        payload = json.dumps({
            "domain_name": rowitem,
            "priority_value": -1

        })



        try:
            response = requests.request("POST", url1, headers=headers, data=payload)
        except requests.exceptions.RequestException:
            print(response)
        # t = datetime.datetime.now()
        # print("Start time:" + " " + str(t))
        # print(response.text)
        # print(response.status_code)
        while response.json()['status_value'] != 2:

            # i = i + 1
            # t1 = datetime.datetime.now()
            # t2 = t1 - t
            # print(str(t2) + " " + str(i) + " " + "Due operation. Recent status is:" + " " + str(
            #     response.json()['status_value']))
            try:
                response = requests.request("POST", url1, headers=headers, data=payload)
            except requests.exceptions.RequestException:
                print(response)
        else:
            print(str(rowitem) + "recalculated")
            try:
                response = requests.request("POST", url2, headers=headers, data=payload)
            except requests.exceptions.RequestException:
                print(response)
            data = response.json()
            mixer.music.load('MS.mp3')
            mixer.music.play()

            findvalue = data['marks']

            malwarelist = next((d for d in findvalue if d['key'] == 'blacklist_bing' and d['points'] != 0), None)
            if malwarelist is not None:
                print(str(rowitem))
                print(malwarelist)
                mixer.music.load('SV.mp3')
                mixer.music.play()

    #
    #
    #
    #
    # mixer.music.play()




