import pandas as pd
import requests , json
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Bensin1.csv', sep=';')
#data.set_index('län')
år = data[['Sthlm','Uppsala','Södmln','Jkpg','Kalmar','Gotlands','Blekinge','Skåne','Örebro','Dalarna','Jämtlands','Västerbtn','Norrbtn']]
lan = data['år']
plt.plot(lan,år)
plt.ylabel('Bensinbilar')
plt.xlabel('Län')
plt.show()
#print(data)