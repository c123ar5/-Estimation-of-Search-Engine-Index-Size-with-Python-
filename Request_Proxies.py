import requests
from datetime import datetime
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from bs4.element import Tag
from selenium.webdriver.chrome.options import Options
import csv
import time
import random
import re
from pathlib import Path
import numpy as np

proxies_IP = ''
proxies_Port=''
P_IP = []
P_Port = []
P_combine=[]
Proxies=[]
f=open("online_proxies\\online_proxies_of_{}.csv".format(datetime.now().strftime("%Y_%m_%d")),"w", encoding='utf-8',newline ='')
writer = csv.writer(f)
def getProxiesFromProxyNova():
    global proxies_IP
    global proxies_Port
    countries = ['tw','jp','kr','id','my','th','vn','ph','hk','us']
    pattern = re.compile(r"document\.write\('\n?([^']*?)(?:\n\s*)?'\);")
    for country in countries:
        html = requests.get("https://www.proxynova.com/proxy-server-list/country-" + country + "/")
        soup=BeautifulSoup(html.text, "html.parser")
        table = soup.find('table', {'class': 'table'})
        for row in table.findAll('tr'):
            if row.find_all('td', {'align': 'left'}):
                ip = row.find_all('td')[0].find('abbr').find('script')
                ip = str(ip)
                ip = pattern.sub('\g<1>',ip)
                ip = ip.replace("'","").replace("<script>","").replace("</script>","").replace('<script async="" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">','').replace('(adsbygoogle = window.adsbygoogle || []).push({})','').replace('[','').replace('\n','').replace(']','').replace(' ','').replace(';','')
                proxies_IP = proxies_IP + ip + ","
                proxies_IP = proxies_IP.replace(" ","").replace("\n","").replace("\r","").replace("\t","")
        else:
            pass 
        for row in table.findAll('tr'):
            if row.find_all('td', {'align': 'left'}):
                port = row.find_all('td')[1].text
                port = str(port)
                port = port.replace('<td align="left">','').replace('</td>','').replace("\n","").replace("\r","").replace("\t","").replace(" ","")
                proxies_Port = proxies_Port + port + ","
            else :
                break
    P_IP = [x.strip() for x in proxies_IP.split(',')]
    P_Port = [y.strip() for y in proxies_Port.split(',')]
    P_IP.pop()
    P_Port.pop()
    for i,j in zip(P_IP,P_Port):
        writer.writerow([i + ":" + j])
    time.sleep(1)    

def getProxiesFromFreeProxyList():
    global Proxies
    html = requests.get("https://free-proxy-list.net/")
    soup=BeautifulSoup(html.text, "html.parser")
    textarea = soup.find('div',{'id':'raw'}).find('div',{'class':'modal-dialog'}).find('div',{'class':'modal-content'}).find('div',{'class':'modal-body'}).text
    textarea = textarea.replace('\n',',').replace('\r\n',',')
    Proxies=[x.strip() for x in textarea.split(',')]
    Proxies.pop()
    del Proxies[0:3]
   
getProxiesFromProxyNova()
getProxiesFromFreeProxyList()
for i in Proxies:
    writer.writerow([i])
f.close