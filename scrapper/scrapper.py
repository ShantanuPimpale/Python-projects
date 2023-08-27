import requests
from bs4 import BeautifulSoup

req=requests.get("https://www.geeksforgeeks.org/")

soup=BeautifulSoup(req.content,"html.parser")

#print(soup.prettify()) #print html code
#print(soup.get_text()) #print text

res=soup.title
print(res.prettify()) # print title in html