import requests
from bs4 import BeautifulSoup

url = "https://seo.wizard.id/domain-age-checker/output"
s = open("list.txt", "r").readlines()

banner = """
--------Info--------
"""
b = """
--------------------
"""
info = """
==========================
Created By HexaKun
Whatsapp : 082335757008
Facebook : Daffa (Hexa Kun)
Email : hexa_kun@yahoo.com
==========================
"""

print info
for l in s:
   site = l.strip()
   req = requests.post(url, data={"url":site, "submit":"Get+Domain+Age"})
   soup = BeautifulSoup(req.content, "html.parser")
   domain = soup.find_all("strong")[0].get_text()
   age = soup.find_all("strong")[1].get_text()
   dibuat = soup.find_all("strong")[2].get_text()
   update = soup.find_all("strong")[3].get_text()
   expiry = soup.find_all("strong")[4].get_text()
   opn = open("finish.txt", "a")
   format = "Domain : {}\nAge : {}\nCreated : {}\nUpdated : {}\nExpired : {}\n\n".format(domain,age,dibuat,update,expiry)
   opn.write(format)
   print banner
   print "Domain : ",domain
   print "Age :",age
   print "Created :",dibuat
   print "Updated : ",update
   print "Expired : ",expiry
   print b,"\n"
