import bs4
import requests


#------------------------ # Functions # ---------------------------------------

def get_url_kwrd_from_user():
    
    url_in = input("Enter URL: ").strip().lower()
    kwrd_in = input("Enter Key-word: ").strip().lower()
    
    return url_in, kwrd_in

#-------------------------------------------------------

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
                all_links.append(u + _cur)
                latest_link = _cur
            
            else:
                all_links.append(_cur)
                latest_link = _cur

#---------------------------------------------------------

def queue_relevant_links_in_list():
    
    latest_link = ''

    for link in soup.find_all('a'):
    
        _cur = str(link.get('href'))
        
        if kwrd in link.get_text().lower():
    
            if _cur not in all_links:
        
                if _cur == ('/') or _cur.startswith('#') \
                or (link.get('href') is None) or _cur.startswith('javascript'):
                    continue
        
            if _cur != latest_link:    
        
                if not _cur.startswith('http'):
                    all_links.append(u + _cur)
                    latest_link = _cur
            
                else:
                    all_links.append(_cur)
                    latest_link = _cur
#-------------------------------------------------

def remove_duplicate(all_links):
    unq_links = []
    
    for link in all_links:
        if link not in unq_links:
            unq_links.append(link)
    
    return unq_links
      
#------------------------------
#------------------------------ # Main Code # --------------------------------------------

# Global variables
# all_links holds all the relevant links to the query
all_links = []

# get URL and Key-Word from user
u, kwrd = get_url_kwrd_from_user()

visted = []
# BeautifulSoup Setup
res = requests.get(u)
soup = bs4.BeautifulSoup(res.text,'lxml')
visted.append(u)


# Queue all links in all_links List
queue_relevant_links_in_list()
all_links = remove_duplicate(all_links)

print()
print('\n\n'.join(all_links))

#print(visted)
