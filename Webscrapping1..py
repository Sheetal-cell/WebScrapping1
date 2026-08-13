import requests
from bs4 import BeautifulSoup, Comment
web=requests.get("https://portfoliosheetal.vercel.app/")
print(web)

#output: <Response [200]>
#print(web.content)  #gives html code of that file
print(web.url)
print(web.status_code)

soup=BeautifulSoup(web.content,"html.parser")
#print(soup.prettify())
#print(soup.p)
#print(soup.title)
#print(soup.a)

tag=soup.html  
#print(type(tag))

#print(soup.a) - 1st anchor element
#print(soup.p) #-1st para element
#print(soup.h1) #-1st h1 element
#print(soup.img)  -1st image element

#print(soup.p.string)# only gives op if there is string without any other used tags
#print(soup.title.string)

#print(soup.p.get_text())

#print(soup.find("p"))
#print(soup.find_all("p"))

#print(soup.find_all(string=lambda text: isinstance(text, Comment)))

#print(soup.prettify())
"""class_data=soup.find("div",class_="dashboard-tab-content")
print(class_data)


print(class_data.find("span"))
print(class_data.find_all("span"))"""

'''id_data=soup.find("div",id="admin-login-modal")
print(id_data)


print(id_data.find("h3"))
print(id_data.find_all("h3"))'''

'''lines=soup.find_all("p")
for line in lines:
    print(line.text)'''
