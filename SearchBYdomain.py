import csv
import datetime
import requests
from sqlalchemy import Column, Integer, Table, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, Query
from sqlalchemy import MetaData
from pygame import mixer
import json
mixer.init()
mixer.music.load('MS.mp3')
engine = create_engine('sqlite:///C:/DB/test1.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

meta = MetaData()
syu = Table(
   'DomainsX', meta,
   Column('id', Integer, primary_key = True),
   Column('Domain', String),
   # Column('Date', String),


        )
meta.create_all(engine)

def add_domains_to_db():
    mass = []
    #adding from csv file
    #colnames = ["num","domain_name","query_time","create_date","update_date","expiry_date","domain_registrar_id","domain_registrar_name","domain_registrar_whois","domain_registrar_url","registrant_name","registrant_company","registrant_address","registrant_city","registrant_state","registrant_zip","registrant_country","registrant_email","registrant_phone","registrant_fax","administrative_name","administrative_company","administrative_address","administrative_city","administrative_state","administrative_zip","administrative_country","administrative_email","administrative_phone","administrative_fax","technical_name","technical_company","technical_address","technical_city","technical_state","technical_zip","technical_country","technical_email","technical_phone","technical_fax","billing_name","billing_company","billing_address","billing_city","billing_state","billing_zip","billing_country","billing_email","billing_phone","billing_fax","name_server_1","name_server_2","name_server_3","name_server_4","domain_status_1","domain_status_2","domain_status_3","domain_status_4"]
    # with open('US.csv', 'rU') as f:
    #     # read the file as a dictionary for each row ({header : value})
    #     reader = csv.DictReader(f)
    #     data = {}
    #     for row in reader:
    #         for header, value in row.items():
    #             try:
    #                 data[header].append(value)
    #             except KeyError:
    #                 data[header] = [value]
    # names = data['domain_name']
    #
    # print(names)



    f = open('Domainlist.txt')
    connection = engine.connect()

    for line in f:
        line = line.replace("\n", "")
        result = connection.execute(syu.insert().values(Domain = line))
        tr = datetime.datetime.now()
        print(tr)
        connection = engine.connect()
        mass = []
        s = engine.execute('SELECT Domain FROM Domains')
        mass.append(s)
        f = open('Domainlist.txt')
        for line in f:
            line = line.replace("\n", "")
            meta.create_all(engine)
            for j in mass:
                if line != j:
                    ins = syu.insert().values(Domain = line)
            con = engine.connect()
            result = con.execute(ins)
            con.close()
        mixer.music.play()
def look_at_db():

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
    s = engine.execute("SELECT * FROM Domains")

    for rowitem in s:
        print(rowitem)

def check_api_code_request():
    url = "https://demo-core-api-trustratings.wecandevelopit.com/api/v1/rate/current/details"
    f = open('Domainlist.txt')
    for rowitem in f:
        rowitem = rowitem.replace("\n", "")

        rowitem = rowitem.replace("'", "")
        rowitem = rowitem.replace(",", "")
        rowitem = rowitem.replace("(", "")
        rowitem = rowitem.replace(")", "")

        payload = json.dumps({
        "domain_name": rowitem

        })
        headers = {
            'Content-Type': 'application/json'

        }
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except requests.exceptions.RequestException:
            if response.status_code!=200:
                print(response)
            else:
                print(str(rowitem) + " " + "ok")
