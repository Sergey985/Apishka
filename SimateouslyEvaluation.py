import threading
from Apishka import dnp_dev_calculation_from_DB
import datetime
import time
import csv
from sqlalchemy import Column, Integer, Table, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, Query
from sqlalchemy import MetaData
import requests
import json

url = "https://core-api-dev-dnprotect.wecandevelopit.com/api/v1/rate/current/details"


def evaluationfromDB():
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
            "domain_name": rowitem
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        t = datetime.datetime.now()
        print("Start time:" + " " + str(t))
        print(response.text)
        print(response.status_code)


def evaluationfromFile():
    with open('US.csv', 'rU') as f:
        # read the file as a dictionary for each row ({header : value})
        reader = csv.DictReader(f)
        data = {}
        for row in reader:
            for header, value in row.items():
                try:
                    data[header].append(value)
                except KeyError:
                    data[header] = [value]
    names = data['domain_name']

    payload = json.dumps({
        "domain_name": names
    })
    headers = {
        'Content-Type': 'application/json'
    }

    tryam = 1
    for i in names:
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        t = datetime.datetime.now()
        print("Start time:" + " " + str(t))
        print(response.text)
        print(response.status_code)
        tryam = tryam + 1
        if tryam > 100:
            exit()

def start_evaluation():

# init threads
    t1 = threading.Thread(target=start_evaluation(), args=(0))
    t2 = threading.Thread(target=start_evaluation(), args=(1))
#
# # start threads
    t1.start()
    t2.start()


# # join threads to the main thread
    t1.join()
    t2.join()