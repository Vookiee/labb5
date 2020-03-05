import pandas as pd
import requests , json
import numpy as np
from numpy import percentile
import matplotlib.pyplot as plt
import csv, sys

data = pd.read_csv('Bensin1.csv', sep=';')
#data.set_index('län')
lan = data[['Sthlm','Uppsala','Södmln','Jkpg','Kalmar','Gotlands','Blekinge','Skåne','Örebro','Dalarna','Jämtlands','Västerbtn','Norrbtn']]
year = data['år']
plt.plot(year,lan)
plt.ylabel('Bensinbilar')
plt.xlabel('År')
plt.title('Bensinbilar i olika län under åren')
plt.legend(lan, loc='upper right')
plt.show()

procentYear = percentile(lan, [25, 50, 75])
print(f"median : ",(procentYear),"procentenheter")
minst = percentile(lan, [0])
högst = percentile(lan, [100])
print(f"minst antal bensinbilar", minst)
print(f"högst antal bensinbilar", högst)

#bensinbilar i kalmar
lan = data[['Kalmar']]
year = data[['år']]

plt.plot(year,lan)
plt.ylabel('benisbilar')
plt.xlabel('År')
plt.legend(lan)
plt.tight_layout()
plt.show()

#jämför två län
lan = data[['Sthlm','Uppsala']]
year = data[['år']]

plt.scatter(year,data['Sthlm'])
plt.scatter(year,data['Uppsala'])
plt.ylabel('bensinbilar')
plt.xlabel('År')
plt.legend(lan)
plt.tight_layout()
plt.show()

#jämför Stockholm och Dalarna ökning/minskning
lan = data[['Sthlm','Dalarna']]
year = data[['år']]

plt.plot(year,lan)
plt.ylabel('bensinbilar')
plt.xlabel('År')
plt.legend(lan)
plt.tight_layout()
plt.show()

#Jämför mellan skåne o jkpg
lan = data[['Skåne','Jkpg']]
year = data[['år']]

plt.plot(year,lan)
plt.ylabel('bensinbilar')
plt.xlabel('År')
plt.legend(lan)
plt.tight_layout()
plt.show()

#Jämför mellan sthlm o uppsala
lan = data[['Sthlm','Uppsala']]
year = data[['år']]

plt.scatter(year,data['Sthlm'])
plt.scatter(year,data['Uppsala'])
plt.ylabel('bensinbilar')
plt.xlabel('År')
plt.legend(lan)
plt.tight_layout()
plt.show()

