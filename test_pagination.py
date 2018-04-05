from bs4 import BeautifulSoup
import requests


url = "https://talhatraining.com/video-course"
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
items = soup.find_all('a', class_='pagination')

for item in items:
    print(str(item.get('href')))