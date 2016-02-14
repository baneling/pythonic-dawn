#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import datetime

days = {0: "Maandag", 1:"Dinsdag", 2:"Woensdag", 3:"Donderdag", 4:"Vrijdag",
    5: "Zaterdag", 6: "Zondag"}
now = datetime.datetime.now()
date = now.isoformat()
day = days[now.weekday()]

url = "http://www.nu.nl/weer"
response = urlopen(url)
soup = bs(response)
maxtempRaw = soup.findAll("td", {"class": "max"})
mintempRaw = soup.findAll("td", {"class": "min"})
maxtemps, mintemps = [], []

for temp in maxtempRaw:
    maxtemps.append(temp.string)
for temp in mintempRaw:
    mintemps.append(temp.string)

def if7(number):
    """Zodat het niet alleen op maandag tot en met woensdag werkt."""
    if number > 6:
        number -= 7
    return number


for n in range (0, len(maxtemps)):
    print ("Op %s wordt het minimaal %s en maximaal %s." 
            % (     days[ if7( now.weekday()+n ) ],
                    mintemps[n],
                    maxtemps[n]  ))

#Omdat de datum niet van de site wordt geplukt.
# We vragen aan python hoeveelste dag van de week het is:
#> datetime.datetime.now().weekday()
# Wij hebben datetime.datetime.now() al afgekort met now:
#> now.weekday()

# Daar gaan we met n op itereren, van 0 tot 4.
# Het kan dus voorkomen (van donderdag tot en met zondag) dat onze index
# (now.weekday() + n) te hoog wordt voor de dictionary.
# Daarom is de functie "if7" gedefiniërd.
# Het nummer wat wordt teruggegeven door de functie "if7" wordt als index gebruikt in de dictionary.
# Met indexnummer n kunnen we vervolgens wel makkelijk bij de bijbehorende temperaturen.

