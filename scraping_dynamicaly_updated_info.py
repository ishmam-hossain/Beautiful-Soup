from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def get_user_input():
    return input("Enter Key-word: ").strip().lower()

kwrd = get_user_input()
url = 'http://hckrnews.com/'


source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')
cn =0

for link in soup.findAll('a'):       
    
    hrf = link.get('href')
    
    if kwrd in link.get_text():
        print(hrf)
        cn +=1

print(cn)