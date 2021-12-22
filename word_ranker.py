#video_response=youtube.commentThreads().list(part='snippet,replies',videoId="Enter Video ID").execute()
import pandas as pd
from bs4 import BeautifulSoup
import urllib
import ast
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import re

def video_comments(video_id,vid_tit):
    x=0
    
    strarray=[]
    while x<=len(video_id)-1:
        y=0
        print(x)
        res = ast.literal_eval(video_id[x])
        totStr=vid_tit[x]+" "
        Stp=0
        
        while y<= len(res)-1:
            code=res[y]
           
            s = Service('/home/ella/Desktop/PROJECT/chromedriver')
            driver = webdriver.Chrome(service=s)
            
            if Stp==2:
                strarray.append([totStr])
                break
            elif y==len(res)-1:
                strarray.append([totStr])
                break
            else:
                try:
                    driver.get("https://www.youtube.com/watch?v="+code)
                except Exception as e:
                    print(e)
                    y=y+1
                    totStr=totStr+'None'
                    continue
                    
                driver.execute_script('window.scrollTo(1, 500);')
                
                n=0
                while n<=170:
                    #now wait let load the comments
                    time.sleep(.05)            
                    scroll_val=n*500
                    driver.execute_script('window.scrollTo(1, '+str(scroll_val)+');')
                    n=n+1
                try:
                    comments=driver.find_elements(By.XPATH,'//*[@id="content-text"]')
                except Exception as e:
                    print(e)
                    y=y+1
                    totStr=totStr+'None'
                    continue
                
                if len(comments)==0:
                    y=y+1
                    totStr=totStr+'None'
                    continue
                else:
                    for comment in comments:
                        totStr=totStr+comment.text+' '  
                    Stp=Stp+1

            y=y+1
        x=x+1
    return(strarray)


def applyranking(df_ranking,word_arr):
    rank_lst=[]
    key_words=df_ranking['key'].values.tolist()
    x=0
    
    while x<= len(word_arr)-1:
        sel_movie_words=word_arr[x]
        op_string = re.sub(r'[^\w\s]','',sel_movie_words[0])
        
        patts = re.compile("|".join(r"\b{}\b".format(s) for s in key_words), re.I)
        flt_words=patts.findall(op_string.lower())
        rnk_word=[]
        for item in flt_words:
            rnk_val=df_ranking[df_ranking['key'].str.match(item)]
            try:
                rnk_word.append(rnk_val['rank'].values[0])
            except Exception as e:
                print(x)
                print(e)
                print(item)
                print(rnk_val)
                rank_lst.append([None])
                break
        rank_lst.append(rnk_word)
        x=x+1
    return rank_lst

df=pd.read_csv('good_movies2022_codes.csv',encoding= 'unicode_escape')

code_list = df['YT_codes'].values
vid_tit = df['Title'].values

commArray=video_comments(code_list,vid_tit)
ranking_df=pd.read_csv('key_words.csv',encoding= 'unicode_escape')
rank_array=applyranking(ranking_df,commArray)

df['yt comments'] = commArray
df['word rating'] = rank_array
df.to_csv('bad_word_rating.csv', index=False)

df=pd.read_csv('Bad_movies2022_codes.csv',encoding= 'unicode_escape')

code_list = df['YT_codes'].values
vid_tit = df['Title'].values

commArray=video_comments(code_list,vid_tit)
rank_array=applyranking(ranking_df,commArray)

df['yt comments'] = commArray
df['word rating'] = rank_array
df.to_csv('good_word_rating.csv', index=False)

df=pd.read_csv('movies2020_codes.csv',encoding= 'unicode_escape')

code_list = df['YT_codes'].values
vid_tit = df['Title'].values

commArray=video_comments(code_list,vid_tit)
rank_array=applyranking(ranking_df,commArray)

df['yt comments'] = commArray
df['word rating'] = rank_array
df.to_csv('word_rating.csv', index=False)
