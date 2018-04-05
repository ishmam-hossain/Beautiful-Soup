#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import bs4


def queue_links_in_list(u,soup,kwrd):
    
    latest_link = ''

    for link in soup.find_all('a'):
        
        if link not in visited:
            
            if kwrd in link.get_text().lower():
    
                _cur = str(link.get('href'))
    
                if _cur not in all_links:
        
                    if _cur == ('/') or _cur.startswith('#') \
                    or (link.get('href') is None) or _cur.startswith('javascript'):
                        continue
                    '''
                    else:
                        all_links.append(_cur)
                        visited.append(_cur)
                    '''
                
        
                if _cur != latest_link:    
        
                    if not _cur.startswith('http'):
                        all_links.append(u + _cur)
                        visited.append(u + _cur)
                        latest_link = _cur
            
                    else:
                        all_links.append(_cur)
                        visited.append(_cur)
                        latest_link = _cur
                    


def remove_duplicate(all_links):
    unq_links = []
    
    for link in all_links:
        if link not in unq_links:
            unq_links.append(link)
            print(link)
    
    return unq_links

#------------------------------------------------------------------------------

all_links = []
visited = []

u = input("Enter URL: ").strip()
kwrd = input("Enter keyword: ").strip().lower()
    
res = requests.get(u)
sp = bs4.BeautifulSoup(res.text,'lxml')
    
queue_links_in_list(u, sp, kwrd)
    
all_links = remove_duplicate(all_links)
#visited = all_links


for itm in all_links:
    
    u = itm
        
    res = requests.get(u)
    sp = bs4.BeautifulSoup(res.text,'lxml')
    
    queue_links_in_list(u, sp, kwrd)
    
    all_links = remove_duplicate(all_links)
    #visited = all_links

print(len(all_links))
#print('\n'.join(visited))
    