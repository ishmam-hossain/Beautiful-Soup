from bs4 import BeautifulSoup
import urllib3
from django.template.context_processors import request
def recursiveUrl(url,depth):

    if depth == 5:
        return url
    else:
        page=request.get(url)
        soup = BeautifulSoup(page.read())
        newlink = soup.find('a') #find just the first one
        if len(newlink) == 0:
            return url
        else:
            return url, recursiveUrl(newlink,depth+1)


def getLinks(url):
    page=request.get(url)
    soup = BeautifulSoup(page.read())
    links = soup.find_all('a', {'class':'institution'})
    for link in links:
        links.append(recursiveUrl(link,0))
    return links