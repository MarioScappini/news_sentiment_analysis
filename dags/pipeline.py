import requests
from bs4 import BeautifulSoup
import csv
   
URL = "https://www.ultimahora.com/contenidos/nacional.html"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
   
quotes=[]  # a list to store quotes
   


for article in soup.findAll('article', attrs = {'class':'article'}):
    title = article.find('h2',attrs={'class':'article-title'})
    summary = article.find('h4',attrs={'class':'article-excerpt'})
    print(title, summary)
                                          

