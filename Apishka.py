import datetime
import time
from sqlalchemy import Column, Integer, Table, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, Query
from sqlalchemy import MetaData
import requests
import json
from pygame import mixer
mixer.init()
mixer.music.load('MS.mp3')
dom = 'zyrdu.cruisingsmallship.com'
def dnp_dev_calculate():
    url = "https://core-api-dev-dnprotect.wecandevelopit.com/api/v1/rate/calculate"

    payload = json.dumps({
        "domain_name": dom,
        'priority': '63'

    })
    headers = {
        'Content-Type': 'application/json'

    }
    i = 0
    response = requests.request("POST", url, headers=headers, data=payload)
    t = datetime.datetime.now()
    print("Start time:" + " " + str(t))
    print(response.text)
    print(response.status_code)
    while response.json()['status_value']!=2:
          response = requests.request("POST", url, headers=headers, data=payload)
          i=i+1
          t1 = datetime.datetime.now()
          t2 = t1 - t
          print(str(t2) + " " + str(i) + " " + "Due operation. Recent status is:" + " " + str(response.json()['status_value']))
    else:
        print("recalculated")
        mixer.music.play()

def dnp_dev_calculation_from_DB():
    engine = create_engine('sqlite:///C:/DB/test.db', echo=True)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)

    meta = MetaData()
    syu = Table('Domains', meta,
                Column('Domain', String),
                Column('id', Integer, primary_key=True)

                )
    meta.create_all(engine)
    url = "https://core-api-dev-dnprotect.wecandevelopit.com/api/v1/rate/calculate"

    headers = {
        'Content-Type': 'application/json'
    }
    connection = engine.connect()
    s = engine.execute('SELECT Domain FROM Domains limit 100')
    i = 0
    for rowitem in s:
        i = i+1
        rowitem = str(rowitem)
        rowitem = rowitem.replace("'","")
        rowitem = rowitem.replace(",","")
        rowitem = rowitem.replace("(","")
        rowitem = rowitem.replace(")", "")

        payload = json.dumps({
            "domain_name": rowitem
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        t = datetime.datetime.now()
        print("Start time:" + " " + str(t))
        print(response.text)
        print(response.status_code)
        while response.json()['status_value'] != 2:
            response = requests.request("POST", url, headers=headers, data=payload)
            i = i + 1
            t1 = datetime.datetime.now()
            t2 = t1 - t
            print(str(t2) + " " + str(i) + " " + "Due operation. Recent status is:" + " " + str(
                response.json()['status_value']))
        else:
            print("recalculated")

    mixer.music.play()

def dnp_dev_details():
    url = "https://core-api-dev-dnprotect.wecandevelopit.com/api/v1/rate/current/details"
    payload = json.dumps({
      "domain_name": dom
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    findvalue = data['marks']
    udrp = next((d for d in findvalue if d['key'] == 'udrp'),None)
    bing = next((d for d in findvalue if d['key'] == 'bing'), None)
    print(response.status_code)
    print(response.text)
    print(bing)