import csv
from datetime import datetime

with open("online_proxies\\online_proxies_of_{}.csv".format(datetime.now().strftime("%Y_%m_%d")), 'r', newline='') as in_file, open("online_proxies\\online_proxies_of_{}_without_Repeat.csv".format(datetime.now().strftime("%Y_%m_%d")), 'w', newline='') as out_file:
    reader = csv.reader(in_file)    
    writer = csv.writer(out_file)
    seen = set() # set for fast O(1) amortized lookup
    for row in reader:
        row = tuple(row)
        if row in seen: continue # skip duplicate
        seen.add(row)
        writer.writerow(row)