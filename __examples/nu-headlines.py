#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup as Bs
import time, datetime

url         = "http://www.nu.nl"

# Vrij standaard
response    = urlopen( url )
soup        = Bs( response )

# Niet altijd hetzelfde
captions    = soup.find_all("span", {"class": "title"})

# Output 
print ("De nu.nl headlines van %s" % 
        datetime.date.isoformat(datetime.datetime.now()))
for i in captions:
    print ("#%d: %s" % (captions.index(i), i.string))
    time.sleep(0.5)






