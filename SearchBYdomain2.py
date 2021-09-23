from sqlalchemy import Column, Integer, Table, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, Query
from sqlalchemy import MetaData
import requests
import json
from pygame import mixer
mixer.init()
mixer.music.load('MS.mp3')
engine = create_engine('sqlite:///C:/DB/test.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

meta = MetaData()
syu = Table('Domains', meta,
      Column('Domain', String),
        Column('id', Integer, primary_key = True )

)
meta.create_all(engine)
url = "https://core-api-dev-dnprotect.wecandevelopit.com/api/v1/rate/current/details"

headers = {
            'Content-Type': 'application/json'
        }
connection = engine.connect()

def search_malware_domains():
    s = engine.execute('SELECT Domain FROM Domains')
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
        findvalue = data['marks']

        malwarelist = next((d for d in findvalue if d['key'] == 'blacklist_bing' and d['points'] != 0), None)
        if malwarelist is not None:
            print(str(rowitem))
            print(malwarelist)
        else:
            print(rowitem + str(i))
    mixer.music.play()




