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
    s = engine.execute('SELECT Domain FROM Domains limit 100')

    for rowitem in s:

        rowitem = str(rowitem)
        rowitem = rowitem.replace("'", "")
        rowitem = rowitem.replace(",", "")
        rowitem = rowitem.replace("(", "")
        rowitem = rowitem.replace(")", "")

        payload = json.dumps({
            "domain_name": rowitem,
            "priority_value": 63

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
    s = engine.execute('SELECT Domain FROM Domains WHERE id>1097 LIMIT 100')

    for rowitem in s:

        rowitem = str(rowitem)
        rowitem = rowitem.replace("'", "")
        rowitem = rowitem.replace(",", "")
        rowitem = rowitem.replace("(", "")
        rowitem = rowitem.replace(")", "")

        payload = json.dumps({
            "domain_name": rowitem,
            "priority_value": 63

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







def calc_s():
    mass = []
    mass1 = []
    thresds = 100
# init threads
    for i in range(thresds):
        t1 = "t1" + str(i)
        t2 = "t2"+str(i)
        t1 = threading.Thread(target=evaluationfromDB(), args=(0))
        t2 = threading.Thread(target=evaluationfromFile(), args=(1))

        t1.start()
        t2.start()
        mass.append(t1)
        mass1.append(t2)
# # join threads to the main thread
    for threadkill in mass:
        threadkill = t1.join()
    for threadkill in mass1:
        threadkill = t2.join()
        mixer.music.play()
