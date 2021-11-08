import requests
from datetime import datetime
import os
import socket
from bs4 import BeautifulSoup
from selenium import webdriver
from bs4.element import Tag
from selenium.webdriver.chrome.options import Options
import csv
import time
import random
import urllib.request
import urllib.error
from pathlib import Path
F="附曲甲繁宇君睡塞敬緡班靄洪描忙哥擺簷燈迫偷違瓦昏呀升掩緩賊賢軾筍朧搓踱熙茜坤袍櫥淪犧勳擲庸喚釉疏徽瑩侃逢鯉袱揀巾榜懊侈渴贍龕竣蒜淶杷驍獰藶矜噫潦蜒噗閽輜虼娌斫捎悚鎘烽贄瑋婁噩萃珞殫揶桉漵冪飴鞽笱嗌鉬湫鶘邨堀魺緶鞫蜍肟嵬刖紕傈旮櫪魍齶搿驃碓痍"
proxyList = []

def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('http://www.example.com')  # change the URL to test here
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print("ERROR:", detail)
        return True
    return False
    
def Scraping_Google (soup_G,filename_G,key_2):
    Result_2 = soup_G.find(id='result-stats')
    Result_S_2=""
    if Result_2:
        Result_S_2 = Result_2.text
        Result_S_2 = Result_S_2.replace(" ","").replace("\n","").replace("\r","").replace("\t","")
    #saving the total number of results as csv file 
    f=open ("Total_Number_results_Random_Proxy\\Google_{}_results.csv".format(datetime.now().strftime("%Y_%m_%d")),"a", encoding='utf-8',newline ='')
    writer_G1 = csv.writer(f)
    writer_G1.writerow([key_2,Result_S_2])
    f.close
    #saving the sorted raw data as csv file  
    f=open ("Google_Raw_Data_with_Sorted_Random_Proxy\\{}_sorted.csv".format(filename_G),"w", encoding="utf-8",newline ='')
    writer_G2 = csv.writer(f)
    writer_G2.writerow(["Title", "URL", "description"])
    for hit in soup_G.find_all("div", class_='g'):
        Hit_title = hit.find('h3')
        if hit.find('div', attrs={'role':'heading'}):
            title = hit.find('div', attrs={'role':'heading'}).text  
            pass          
        elif hit.find('div', class_='I6TXqe osrp-blk'):
            title = hit.find('h2', class_='qrShPb kno-ecr-pt PZPZlf mfMhoc').text
            pass
        else: 
            if  Hit_title :
                title = Hit_title.text 
            else:   
                title = 'N/A'
        title = title.replace("\n","").replace("\r","").replace("\t","").replace(" ","")    
        URL=hit.find('a', href=True)
        URL_Link=URL.attrs['href']
        description = hit.find(class_='aCOpRe') or hit.find(class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc')
        if hit.find('div', attrs={'role':'heading'}):
            description_S = title
            pass
        
        else:
            if description:
                description_S = description.text      
            else:
                description_S= "N/A"
        description_S = description_S.replace(" ","").replace("\n","").replace("\t","").replace("\r","")    
        writer_G2.writerow([title,URL_Link,description_S])
    f.close

def Scraping_Bing (soup_B,filename_B,key_1):
    Result_1 = soup_B.find(class_='sb_count')
    Result_S_1=""
    if Result_1:
        Result_S_1 = Result_1.text
        Result_S_1 = Result_S_1.replace(" ","").replace("\n","").replace("\r","").replace("\t","")
    #saving the total number of results in csv format
    f=open ("Total_Number_results_Random_Proxy\\Bing_{}_results.csv".format(datetime.now().strftime("%Y_%m_%d")),"a", encoding='utf-8',newline ='')
    writer_B1 = csv.writer(f)
    writer_B1.writerow([key_1,Result_S_1])
    f.close
    #saving the sorted raw data in csv format 
    f=open ("Bing_Raw_Data_with_Sorted_Random_Proxy\\{}_sorted.csv".format(filename_B),"w", encoding="utf-8",newline ='')
    writer_B2 = csv.writer(f)
    writer_B2.writerow(["Title", "URL", "description"])
    iB = 0
    for hit in soup_B.find_all(class_='b_algo'):
        hitf = hit.find('h2')
        if iB>50 : 
            break
        elif hitf is None:
            pass
        elif hit.find('h2').find('a', href=True) is not None and iB<50: 
            Hit_title = hit.find('h2').find('a', href=True)
            URL=Hit_title['href']
            description = hit.find(class_='b_caption').find(['p', 'dir'])
            if description:
                description_S = description.text
                description_S = description_S.replace(" ","")
                description_S = description_S.replace("\n","")
                description_S = description_S.replace("\t","")
                description_S = description_S.replace("\r","")
            else:
                description_S= "N/A"
            title = Hit_title.next
            writer_B2.writerow([title,URL,description_S])
        else:
            break
        iB = iB + 1
    f.close 
    
def Web_Scraping(f,CurrP):
    fB = f
    fG = f
    user_input_1 = f.encode("utf-8")
    user_input_2 = user_input_1.decode("utf-8")
    user_input_1 = str(user_input_1)
    user_input_1_1 = user_input_1 [4:-9]
    user_input_1_1 = user_input_1_1.upper()
    user_input_1_2 = user_input_1 [8:-5]
    user_input_1_2 = user_input_1_2.upper()
    user_input_1_3 = user_input_1 [12:-1]
    user_input_1_3 = user_input_1_3.upper()
    user_input_1 = ('%' + user_input_1_1 + '%' + user_input_1_2 + '%' + user_input_1_3)
    headers_B = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Accept-Language": "zh-HK,zh;q=0.9,en-GB;q=0.8,en;q=0.7,zh-TW;q=0.6,en-US;q=0.5","Dnt": "1",  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0","cookie":""}
    headers_G = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Accept-Language": "zh-HK,zh;q=0.9,en-GB;q=0.8,en;q=0.7,zh-TW;q=0.6,en-US;q=0.5","Dnt": "1",  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0","cookie":""}
    proxies_R = {'http':CurrP}
    #Requesting Google
    html2 = requests.get("https://www.google.com.hk/search?q=" + user_input_1 + "&num=100&lr=lang_zh-TW&filter=0", headers=headers_G,  proxies=proxies_R)
    html2.encoding = 'utf-8' 
    soup2=BeautifulSoup(html2.text, "html.parser")    
    soup2.encoding = 'utf-8'
    #copy the requested data to avoid the confusion of the requested data
    soup6=soup2
    #save the soup result (Raw Data) as html file
    
    filename2 = ("Google_{}-{}".format(datetime.now().strftime("%Y_%m_%d"),user_input_2))
    f=open ('Html_Google_Raw_Data_Random_Proxy\\{}.html'.format(filename2),"w", encoding="utf-8")
    f.writelines(soup2.prettify())
    f.close
    Gi=0
    while Path('Html_Google_Raw_Data_Random_Proxy\\{}.html'.format(filename2)).stat().st_size< 10000 :
        Gi = Gi +1
        print ("The "+ str(Gi) +" times for requesting Google fail due to unusual traffice block" )
        print ("Waiting for unusual traffic block unlock")
        time.sleep(300)
        html2 = requests.get("https://www.google.com.hk/search?q=" + user_input_1 + "&num=100&lr=lang_zh-TW&filter=0", headers=headers_G,  proxies=proxies_R)
        html2.encoding = 'utf-8' 
        soup2=BeautifulSoup(html2.text, "html.parser")    
        soup2.encoding = 'utf-8'
        #copy the requested data to avoid the confusion of the requested data
        soup6=soup2
        #save the soup result (Raw Data) as html file
        filename2 = ("Google_{}-{}".format(datetime.now().strftime("%Y_%m_%d"),user_input_2))
        f=open ('Html_Google_Raw_Data_Random_Proxy\\{}.html'.format(filename2),"w", encoding="utf-8")
        f.writelines(soup2.prettify())
        f.close
    Scraping_Google(soup6,filename2,fG)
    print("Google with Random Proxy finished")
    #Requesting Bing
    html1 = requests.get("https://www.bing.com/search?q=" + user_input_1 + "&search=&form=QBLH&sp=-1&pq=" + user_input_1 + "&sc=0-1&qs=n&sk=&cvid=806A089094614DB4A35C3AA9C1BF0B0F&rdr=1&rdrig=1D4E40D8DC974355B82EC83112EA3E2A&count=50&setLang=zh-hant&cc=hk", headers=headers_B,proxies=proxies_R)
    html1.encoding = 'utf-8' 
    soup1=BeautifulSoup(html1.text, "html.parser")
    soup1.encoding = 'utf-8'
    #copy the requested data to avoid the confusion of the requested data
    soup5=soup1
    #save the soup result (Raw Data) as html file
    filename1 = ("Bing_{}-{}".format(datetime.now().strftime("%Y_%m_%d"),user_input_2))
    f=open ('Html_Bing_Raw_Data_Random_Proxy\\{}.html'.format(filename1),"w", encoding="utf-8")
    f.writelines(soup1.prettify())
    f.close
    #call the upper function with the requested data for Scraping
    Scraping_Bing (soup5,filename1,fB)
    print("Bing with Random Proxy finished")
        
#counter for avoiding too much request in one second
start_time = time.time()
i=0
j=0
R_Break=random.randint(4,7)
R_Break_Time=random.randint(90,250)
R_Wait_Time = random.randint(15,25)
Proxies_ST = time.time()
CP = ""
with open('online_proxies\\online_proxies_of_{}_without_Repeat.csv'.format(datetime.now().strftime("%Y_%m_%d")), 'r') as f_proxy:
    reader = csv.reader(f_proxy)
    for row in reader:
        proxyList.append(row[0])
random.shuffle(proxyList)
print(proxyList)
for f in F:
    socket.setdefaulttimeout(60)
    while True:
        if j>= len(proxyList):
            j=j%len(proxyList)
            print("Proxy reuse")
            Proxies_T = time.time()
            Proxies_T_D = int(Proxies_T - Proxies_ST)
            if Proxies_T_D > 600:
                print("no wait")
                Proxies_ST=time.time()
            else:
                Proxies_T_W = 600 - Proxies_T_D
                print ("wait " + str(Proxies_T_W) + " seconds")
                time.sleep(Proxies_T_W)
                Proxies_ST=time.time()
        CP = proxyList[j]
        if is_bad_proxy(CP):
            print("Bad Proxy:" + CP)
            pass
        else:
            print (CP + " is working")
            print (f)
            Web_Scraping(f,CP)
            i=i+1
            print ("wait " + str(R_Wait_Time) + "s")
            time.sleep(R_Wait_Time)
            R_Wait_Time = random.randint(15,25)
            j=j+1
            break
        j=j+1
    if i>R_Break:
        print ("Random Break for " +str(R_Break_Time) +" seconds")
        time.sleep(R_Break_Time)
        R_Break=random.randint(4,7)
        R_Break_Time=random.randint(90,250)
        i = 0                