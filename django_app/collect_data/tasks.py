from __future__ import absolute_import, unicode_literals
from celery import shared_task

# For scrape task
# import pandas as pd
# import time
# import requests
# from fake_useragent import UserAgent
# import json

# @shared_task
# def scrape_task(self):
#     start_time = time.time()
#     i = 0
#     df = pd.DataFrame()


#     while True:
#         headers = {"User-Agent": ua.random}
#         url = f'https://newweb.nepalstock.com.np/api/nots/nepse-data/floorsheet?page={i}&size=500&sort=contractId,desc'
#         try:
#             r = requests.get(url, allow_redirects=True,headers=headers)
#             data = json.loads(r.content)
#             floorsheet = data['floorsheets']['content']
#             if len(floorsheet)==0:
#                 break
#             df_i = pd.DataFrame(floorsheet)
#             df = df.append(df_i)
#             i+=1
#             time.sleep(0.2)
#         except:
#             time.sleep(1)
#             continue
            
#     print("--- %s seconds ---" % (time.time() - start_time))

@shared_task
def sample_task():
    print("The sample task just ran.")