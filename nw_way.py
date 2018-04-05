import requests
from bs4 import BeautifulSoup


ulst = set()
#url = ''

def reshapeURL(u):
    #if str(u).startswith('/'):
    pass

def spider(url, kwrd):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')
    
    for link in soup.findAll('a'):       
        hrf = link.get('href')
        if kwrd in link.get_text() or kwrd in str(hrf):
            
            if not str(hrf).startswith('http'):
                ulst.add(url+hrf)
                single_list(url+hrf)
            else:
                ulst.add(hrf)
                single_list(url)
            


def single_list(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')
    
    for link in soup.findAll('a'):       
        hrf = link.get('href')
        
        ulst.add(hrf)
        print(hrf)




url = input("URL: ").strip()
kwrd = input("kwrd: ").strip()
spider(url,kwrd)

print('------------------------------------')
print('\n'.join(ulst))   