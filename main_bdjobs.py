from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def get_user_input():
    return input("Enter Key-word: ").strip().lower().split(' ')


#------------ Main ------------

kwrds = get_user_input()
#url = 'http://jobs.bdjobs.com/jobsearch.asp?fcatId=8&icatId='
#url = 'http://jobs.bdjobs.com/jobsearch.asp?fcatId=8'
url = 'http://hckrnews.com/'
unq_links = {}
#----------------

source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')


for link in soup.findAll('a'):       
    
    hrf = link.get('href')
    
    if any(kwrd in link.get_text().lower() for kwrd in kwrds):
        if str(hrf).startswith('jobdetails'):
            unq_links[link.get_text().strip()] = urljoin(url,hrf)



print()
for key,val in unq_links.items():
    print(key +'\n'+ val + '\n')
print('\nTotal results: ' + str(len(unq_links)))

