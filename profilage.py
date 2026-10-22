#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#python3 profilage.py pour le lancer

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# partie à adapter
FILE          = "communication_long_distance.xlsx"  #le nom du fichier
X_LABEL       = "vitesse données (kbps)" # le nom de x axis
Y_LABEL       = "Consommation moyenne (mW)" # le nom de y axis
X_MIN, X_MAX  = 1, 20 #plage de fonctionnement
WORKING_POINT = 10  #point de fonctionnement souhaiter

def model(x, a, b):          # l'equation pour relier les 2  colones Excels (à adapter par cas)
    return b + a/x

#pour cette exemple a = (Ptransmission - Psleep)*nombre des bits/(1000*Le temps)
#                   b = Psleep
#ref: https://www.ti.com/document-viewer/lit/html/SNAA352?utm

df = pd.read_excel(FILE)  # lire le fichier 
print(df.columns.tolist())
x = np.linspace(X_MIN, X_MAX, 500) # le pas de chaque points entre x_min et x_max


#lire le fichier ligne par ligne

for _, row in df.iterrows():   
    params = row.drop("name").to_dict()
    line, = plt.plot(x, model(x, **params), label=row["name"])
    y_wp = model(WORKING_POINT, **params)
    plt.plot(WORKING_POINT, y_wp, "o", color=line.get_color())
   # print(f"{row['name']:15s} -> {y_wp:.4g}") #print sur le terminal si on veut

plt.axvline(WORKING_POINT, color="gray", linestyle="--")
plt.xlabel(X_LABEL)
plt.ylabel(Y_LABEL)
#plt.xscale("log") #echelle logarithmique (optionnel)
plt.yscale("log")  #echelle logarithmique (optionnel)
plt.grid(True, which="both", alpha=0.3)
plt.legend()
plt.show()