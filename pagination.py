#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


def get_user_input():
    return input("Enter Key-word: ").strip().lower().split(' ')


#------------ Main ------------

#kwrds = get_user_input()
url = 'https://talhatraining.com/video-course/1'
unq_links = {}
#----------------
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'lxml')

for li in soup.find_all(class_="pagination"):
    print(li.a.get('href'))















'''
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')

lll = ''
for ultag in soup.find_all('ul', {'class': 'pagiantion'}):
    #for litag in ultag.find_all('li'):
        #print(litag.text)
    lll+=ultag
print(lll)

list = soup.findAll('ul',{'class':'pagination'})

print(list.get_text())   


for link in soup.findAll('ul',{'class':'pagination'}):
    for pg in link.soup.findAll('a'):   
        hrf = link.get('href')
        print(hrf)
    
'''
