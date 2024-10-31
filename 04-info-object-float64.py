import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")

print(health_data.info()) 

# te dara el la informacion de la tabla hay object y float pero tenemos q trabajar con float unicamente


#########################################
import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")
health_data.dropna(axis=0,inplace=True) #como vimos anteriormente es para quitar las NaN de la tabla (limpiar)

health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float) #codigo para transformar en object en float
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)

print(health_data.info()) ##Proporciona información estructural del DataFrame. como el object o float
