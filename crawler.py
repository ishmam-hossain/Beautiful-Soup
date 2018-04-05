import bs4
import requests
import os


#------------------------ # Functions # ---------------------------------------

def get_url_kwrd_from_user():
    
    url_in = input("Enter URL: ").strip()
    kwrd_in = input("Enter Key-word: ").strip().replace(' ','-')
    
    if not url_in.startswith('http://www.'):
        url_in = 'http://www.' + url_in
    
    elif not url_in.startswith('http://'):
        url_in = 'http://' + url_in
            
    
    return url_in, kwrd_in



def queue_links_in_list():
    
    latest_link = ''

    for link in soup.find_all('a'):
    
        _cur = str(link.get('href'))
    
        if _cur not in all_links:
        
            if _cur == ('/') or _cur.startswith('#') \
            or (link.get('href') is None) or _cur.startswith('javascript'):
                continue
        
        if _cur != latest_link:    
        
            if not _cur.startswith('http'):
                all_links.append(url + _cur)
                latest_link = _cur
            
            else:
                all_links.append(_cur)
                latest_link = _cur


#------------------------------ # Main Code # --------------------------------------------

# Global variables
all_links = []

# get URL and Key-Word from user
url, kwrd = get_url_kwrd_from_user()

# BeautifulSoup Setup
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text,'lxml')

# Queue all links in all_links List
queue_links_in_list()

        
print('\n\n'.join(all_links))


