import random
import threading
import datetime
import time
import csv
from sqlalchemy import Column, Integer, Table, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, Query
from sqlalchemy import MetaData
import requests
import json
from pygame import mixer
mixer.init()
mixer.music.load('Finita.mp3')




def evaluationfromDB():


    url1 = "https://core-api.trustratings.com/api/v1/rate/current/details"
    url = "https://core-api.trustratings.com/api/v1/rate/calculate"
    engine = create_engine('sqlite:///C:/DB/test.db', echo=True)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)

    meta = MetaData()
    syu = Table('Domains', meta,
                Column('Domain', String),
                Column('id', Integer, primary_key=True)

                )
    meta.create_all(engine)

    headers = {
        'Content-Type': 'application/json'
    }
    connection = engine.connect()
    s = engine.execute('SELECT Domain FROM Domains Where id>31543 limit 144')

    for rowitem in s:

        rowitem = str(rowitem)
        rowitem = rowitem.replace("'", "")
        rowitem = rowitem.replace(",", "")
        rowitem = rowitem.replace("(", "")
        rowitem = rowitem.replace(")", "")

        payload = json.dumps({
            "domain_name": rowitem,
            "priority_value": -1

        })
        headers = {
            'Content-Type': 'application/json'

        }
        i = 0
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except requests.exceptions.RequestException:
            print(response)
        t = datetime.datetime.now()
        print("Start time:" + " " + str(t))
        print(response.text)
        print(response.status_code)
        if response.ok:
            while response.json()['status_value'] != 2:
                try:
                    response = requests.request("POST", url, headers=headers, data=payload)
                except requests.exceptions.RequestException:
                    print(response)
                i = i + 1
                t1 = datetime.datetime.now()
                t2 = t1 - t
                print(time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime("%S") + " " + str(
                    i) + " " + "Domain is:" + " " + rowitem + " " + ". Recent status is:" + " " +
                    str(response.json()['status_value']))
            else:
                print("recalculated")
                try:
                    response = requests.request("POST", url1, headers=headers, data=payload)
                except requests.exceptions.RequestException:
                    print(response)
                data = response.json()
                t = datetime.datetime.now()
                print("Start time:" + " " + str(t))
                print(response.text)
                print(response.status_code)
                findvalue = data['marks']

                malwarelist = next((d for d in findvalue if d['key'] == 'blacklist_bing' and d['points'] != 0), None)
                if malwarelist is not None:
                    print(str(rowitem))
                    print(malwarelist)


def evaluationfromFile():
    url1 = "https://core-api.trustratings.com/api/v1/rate/current/details"
    url = "https://core-api.trustratings.com/api/v1/rate/calculate"
    engine = create_engine('sqlite:///C:/DB/test.db', echo=True)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)

    meta = MetaData()
    syu = Table('Domains', meta,
                Column('Domain', String),
                Column('id', Integer, primary_key=True)

                )
    meta.create_all(engine)

    headers = {
        'Content-Type': 'application/json'
    }
    connection = engine.connect()
    s = engine.execute('SELECT Domain FROM Domains where id>7 LIMIT 200')

    for rowitem in s:

        rowitem = str(rowitem)
        rowitem = rowitem.replace("'", "")
        rowitem = rowitem.replace(",", "")
        rowitem = rowitem.replace("(", "")
        rowitem = rowitem.replace(")", "")

        payload = json.dumps({
            "domain_name": rowitem,
            "priority_value": -1

        })
        headers = {
            'Content-Type': 'application/json'

        }
        i = 0
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except requests.exceptions.RequestException:
            print(response)
        t = datetime.datetime.now()
        print("Start time:" + " " + str(t))
        print(response.text)
        print(response.status_code)
        if response.ok:
            while response.json()['status_value'] != 2:
                try:
                    response = requests.request("POST", url, headers=headers, data=payload)
                except requests.exceptions.RequestException:
                    print(response)
                i = i + 1
                t1 = datetime.datetime.now()
                t2 = t1 - t
                print(time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime("%S") + " " + str(
                    i) + " " + "Domain is:" + " " + rowitem + " " + ". Recent status is:" + " " +
                      str(response.json()['status_value']))
            else:
                print("recalculated")
                try:
                    response = requests.request("POST", url1, headers=headers, data=payload)
                except requests.exceptions.RequestException:
                    print(response)
                data = response.json()
                t = datetime.datetime.now()
                print("Start time:" + " " + str(t))
                print(response.text)
                print(response.status_code)
                findvalue = data['marks']

                malwarelist = next((d for d in findvalue if d['key'] == 'blacklist_bing' and d['points'] != 0), None)
                if malwarelist is not None:
                    print(str(rowitem))
                    print(malwarelist)

def calc_s():
    t1=[]
    t2 = []
    mass = []
    mass1 = []
    thresds = 100
# init threads
    for i in range(thresds):
        t1.append(i)
        t2.append(i)
        t1[i] = threading.Thread(target=evaluationfromDB(), args=(0))
        t2[i] = threading.Thread(target=evaluationfromFile(), args=(1))

        t1[i].start()
        t2[i].start()
        mass.append(t1[i])
        mass1.append(t2[i])
# # join threads to the main thread
    for threadkill in mass:
        threadkill = t1[i].join()
    for threadkill in mass1:
        threadkill = t2[i].join()
        mixer.music.play()
