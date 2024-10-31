import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",") #para cargar, importar una base da datos

health_data.dropna(axis=0,inplace=True) #dropna es para quitar todos los NaN(espacios en blanco) de la tabla

print(health_data)