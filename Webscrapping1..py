import requests
from bs4 import BeautifulSoup
web=requests.get("https://portfoliosheetal.vercel.app/")
print(web)

#output: <Response [200]>
#print(web.content)  #gives html code of that file
print(web.url)
print(web.status_code)

soup=BeautifulSoup(web.content,"html.parser")
print(soup.prettify)