import schedule
import time              
import os

def job():
    now1 = time.strftime("%Y-%m-%d %H:%M:%S")
    print (now1)
    os.system('Request_Proxies.py')
    print ("Request Proxies Fin")
    os.system('Remove_Proxies_Duplicates.py')
    print ("Duplicates Proxies Removed")
    os.system('Web_Scraping_Google_and_Bing_with_Concat_and_sorted_Random_Proxy.py')
    print ("Scraping Fin")
    now2 = time.strftime("%Y-%m-%d %H:%M:%S")
    print(now2)

schedule.every().day.at("11:00:00").do(job)

while True:
    schedule.run_pending()