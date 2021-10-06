import datetime
import time
from sqlalchemy import Column, Integer, Table, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, Query
from sqlalchemy import MetaData
import requests
import json
from pygame import mixer
import threading
mixer.init()
mixer.music.load('MS.mp3')
dom = 'Wikipedia.org'



def live_calculate():
    url = "https://core-api.trustratings.com/api/v1/rate/calculate"

    payload = json.dumps({
        "domain_name": dom,
        "priority_value":-1

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
    if not response:
        print(response.status_code)

    else:
        while response.json()['status_value']!=2:
           response = requests.request("POST", url, headers=headers, data=payload)
           i=i+1
           t1 = datetime.datetime.now()
           t2 = t1 - t
           print(str(t2) + " " + str(i) + " " + "Due operation. Recent status is:" + " " + str(response.json()['status_value']))
        else:
            print("recalculated")
            mixer.music.play()

def tr_demo_calculate():
    url = "https://demo-core-api-trustratings.wecandevelopit.com/api/v1/rate/calculate"

    payload = json.dumps({
        "domain_name": dom,
        "priority_value": -1

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
                i) + " " + "Domain is:" + " " + dom + " " + ". Recent status is:" + " " +
                  str(response.json()['status_value']))
        else:
            print("recalculated")

    else:
        print("Calculation for domain: " + str(dom) + " " + "wrong" + " " + str(response))
mixer.music.play()


def dnp_dev_calculate():
    url = "https://core-api-dev-dnprotect.wecandevelopit.com/api/v1/rate/calculate"

    payload = json.dumps({
        "domain_name": dom,
        "priority_value":-1

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
                i) + " " + "Domain is:" + " " + dom + " " + ". Recent status is:" + " " +
                  str(response.json()['status_value']))
        else:
            print("recalculated")
            mixer.music.play()
    else:
        print("Calculation for domain: " + str(dom) + " " + "wrong" + " " + str(response))
def tr_demo_details():
    url = "https://demo-core-api-trustratings.wecandevelopit.com/api/v1/rate/current/details"
    payload = json.dumps({
        "domain_name": dom
    })
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
    except requests.exceptions.RequestException:
        print(response)
    if response.ok:
        data = response.json()
        findvalue = data['marks']
        udrp = next((d for d in findvalue if d['key'] == 'udrp'), None)
        bing = next((d for d in findvalue if d['key'] == 'bing'), None)
        print(response.status_code)
        print(response.text)
        print(bing)
    else:
        print("Details for domain: " + str(dom) + " " + "wrong" + " " + str(response))

def dnp_dev_details():
    url = "https://core-api-dev-dnprotect.wecandevelopit.com/api/v1/rate/current/details"
    payload = json.dumps({
      "domain_name": dom
    })
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
    except requests.exceptions.RequestException:
        print(response)
    if response.ok:
        data = response.json()
        findvalue = data['marks']
        udrp = next((d for d in findvalue if d['key'] == 'udrp'), None)
        bing = next((d for d in findvalue if d['key'] == 'bing'), None)
        print(response.status_code)
        print(response.text)
        print(bing)
    else:
        print("Details for domain: " + str(dom) + " " + "wrong" + " " + str(response))


def dnp_dev_mass_calculation_from_DB():
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
    s = engine.execute('SELECT Domain FROM Domains  limit 100')
    url = "https://core-api-dev-dnprotect.wecandevelopit.com/api/v1/rate/calculate"
    i = 0
    rnd = []
    rndS=[]
    for rowitem in s:
        i = i+1
        rowitem = str(rowitem)
        rowitem = rowitem.replace("'","")
        rowitem = rowitem.replace(",","")
        rowitem = rowitem.replace("(","")
        rowitem = rowitem.replace(")", "")

        payload = json.dumps({
            "domain_name": rowitem,
            "priority_value":-1
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        t = datetime.datetime.now()
        print("Start time:" + " " + str(t))
        print(response.text)
        print(response.status_code)
        while response.json()['status_value']!=2:
            #rnd.append(rowitem)
            print(" " + str(i) + " " + rowitem + " " + "Recent status is:" + " " + str(
                response.json()['status_value']))
            response = requests.request("POST", url, headers=headers, data=payload)


        else:
            print(rowitem + " " + "recalculated")
        #print(rnd)
            rndS.append(rowitem)
 #   for ar in rnd:
 #        while response.json()['status_value'] != 2:
 #         i = i + 1
 #         t1 = datetime.datetime.now()
 #         t2 = t1 - t
 #         print(str(t2) + " " + str(i) + " " + rowitem + " " + "Recent status is:" + " " + str(
 #             response.json()['status_value']))
 #         response = requests.request("POST", url, headers=headers, data=payload)
 #        else:
 #            rnd.remove(rowitem)
 #        next: ar
    print(rndS)
        # while response.json()['status_value'] != 2:
        #     response = requests.request("POST", url, headers=headers, data=payload)
        #     i = i + 1
        #     t1 = datetime.datetime.now()
        #     t2 = t1 - t
        #     print(str(t2) + " " + str(i) + " " + rowitem + " " + "Recent status is:" + " " + str(
        #         response.json()['status_value']))
        # else:
        #     print("recalculated")

    mixer.music.play()

#
#
# threads = []
# for t in range(20):
#     t = threading.Thread(target=dnp_dev_mass_calculation_from_DB, args=(0))
#     t.start()
#     threads.append(t)
# for t in threads:
#     t.join()


