#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:03:12 2021

@author: ella
"""
import pandas as pd
from bs4 import BeautifulSoup
import urllib
import requests
from googleapiclient.discovery import build

rank_lst=[]

api_key='AIzaSyA3OyB4JRFOnCkczCCbRsUno4F6jLydc5g'

df=pd.read_csv('Bad_movies_2022.csv',encoding= 'unicode_escape')
df.to_csv('test.csv', index=False)
title_list=df['Title'].values



# creating youtube resource object
service = build('youtube','v3',developerKey=api_key)


x=0
Vid_lst=[]
while x<= len(title_list)-1:
    print(x)
    frm_title=title_list[x].replace("&","and")
    frm_title=frm_title.replace(" ","+")
    
    search_response = service.search().list(q=frm_title+"+trailer+official+2020",part="id",type="video",fields="items/id").execute()

    videos = []

    for search_result in search_response.get("items", []):
        videos.append("%s" % (search_result["id"]["videoId"]))

    print("Videos:\n", "\n".join(videos), "\n")
    
    Vid_lst.append(videos)
    print(Vid_lst)

    x=x+1

df['YT_codes'] = Vid_lst
df.to_csv('Bad_movies2022_codes.csv', index=False)


