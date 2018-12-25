#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 17:26:00 2018

@author: fiftycentsjj
"""

import requests
from bs4 import BeautifulSoup

res = requests.get('https://movies.yahoo.com.tw/movie_thisweek.html')
soup = BeautifulSoup(res.text.strip())

for item in soup.select('.release_info'):
    print (item.select('.btn_s_introduction')[0].text.strip()) #上映日期
    print (item.select('.gabtn')[0].text.strip()) #中文片名
    print (item.select('.release_movie_time')[0].text.strip()) #期待度
    print (item.select('.leveltext')[0].text.strip()) #網友想看
    
for cover in soup.select('img'): #電影封面網址
    print(cover)
    

