from django.shortcuts import render, HttpResponse
from django.views import View
import pandas as pd
import time
import requests
from fake_useragent import UserAgent
import json
from .models import Floorsheet
import psycopg2

import os
from django.conf import settings
from sqlalchemy import create_engine

user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']
database_name = settings.DATABASES['default']['NAME']
host = settings.DATABASES['default']['HOST']

database_url = 'postgresql://{user}:{password}@{host}:5432/{database_name}'.format(
    user=user,
    password=password,
    database_name=database_name,
    host=host
)

def preprocess_df(df):
    df = df.drop(['id', 'contractType'], axis=1)
    df['tradeTime'] = pd.to_datetime(df['tradeTime']).astype(str)
    df = df.reset_index(drop=True)
    return df

def scrape(dev=True):
    start_time = time.time()
    i = 0
    df = pd.DataFrame()
    ua = UserAgent()
    while True:
        headers = {"User-Agent": ua.random}
        url = f'https://newweb.nepalstock.com.np/api/nots/nepse-data/floorsheet?page={i}&size=500&sort=contractId,desc'
        try:
            r = requests.get(url, allow_redirects=True,headers=headers)
            data = json.loads(r.content)
            floorsheet = data['floorsheets']['content']
            if len(floorsheet)==0:
                break
            df_i = pd.DataFrame(floorsheet)
            df = df.append(df_i)
            i+=1
            if dev:
                break
            time.sleep(0.2)
        except:
            time.sleep(1)
            continue
    
    print("--- %s seconds retrieved data ---" % (time.time() - start_time))
    return df

class ScrapeDailyDataView(View):
    def get(self, request):
        engine = create_engine(database_url)
        df = scrape(dev=False)
        df = preprocess_df(df)
        df.to_sql('collect_data_floorsheet', if_exists='replace', index=False, con=engine)
        # length = len(df)

        # model_instances = [Floorsheet(**df.loc[i].to_dict()) for i in range(length)]
        # Floorsheet.objects.bulk_create(model_instances)

        return HttpResponse('Sucessfully wrote to db')

