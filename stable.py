import requests
from bs4 import BeautifulSoup

links = set()

def check_relative_link(_cur):
    if _cur == ('/') or _cur.startswith('#') or _cur.startswith('javascript'):
        return False
    else: 
        return True

#or (link.get('href') is None)  _cur == ('/') or  or _cur.startswith('#') \

def spider(max_pages):
    
    url = input("URL: ").strip().lower()
    kwrd = input("kwrd: ").strip().lower()
    page = 1
    
    while page <= max_pages:
        
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'lxml')
        
        for link in soup.findAll('a'):
            hrf = link.get('href')
            
            if kwrd in link.get_text().lower():
                
                if check_relative_link(hrf):
                    links.add(hrf)
                    #print(hrf)
                    get_single_data(hrf, kwrd)
                
        page+=1
    
    
    #print('\n'.join(links))


def get_single_data(url,kwrd):
    
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')
    
    for link in soup.findAll('a'):       
        hrf = link.get('href')
        
        if kwrd in link.get_text().lower():
            
            if check_relative_link(hrf):
                links.add(hrf)
                #print(hrf)
                #and kwrd in link.get_text().lower()

    


#no_of_page = int(input("No. of pages: "))
spider(1)

print('---------------------------------')
print('\n'.join(links))
print('\n\n'+str(len(links)))