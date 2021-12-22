#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:03:12 2021

@author: ella
"""
import pandas as pd
from bs4 import BeautifulSoup
import urllib

rank_lst=[]

df=pd.read_csv('movies2020.csv',encoding= 'unicode_escape')
df.to_csv('test.csv', index=False)
title_list=df['Title'].values

x=0
while x<= len(title_list)-1:
    print(x)
    frm_title=title_list[x].replace(":","")
    frm_title=frm_title.replace(" ","_")
    frm_title=frm_title.replace("!","")
    frm_title=frm_title.replace("&","and")
    frm_title=frm_title.replace(".","")
    
    try:
        with urllib.request.urlopen("https://www.rottentomatoes.com/m/"+frm_title) as url:
            soup = BeautifulSoup(url.read(), 'lxml')
            
            for link in soup.find_all('score-board',attrs={"class" :"scoreboard"}):
                try:
                    score=link.get("audiencescore")
                    rank_lst.append(score)
                    if score == '':
                        print("ERROR"+str(x))
                except Exception as e:
                    print(e)
                    print(frm_title)
                    rank_lst.append(None)
    except Exception as e:
        print(e)
        print(frm_title)
        rank_lst.append(None)
        

    x=x+1
    
print(rank_lst)
df['Rating'] = rank_lst
df.to_csv('movies2020_ratings.csv', index=False)



