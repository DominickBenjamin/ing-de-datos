import pandas as pd
import numpy as np

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

Max_Pulse= full_health_data["Max_Pulse"] ##se crea la variable max_pulse para usarla luego en el percentile10
percentile10 = np.percentile(Max_Pulse, 10) ##crea la variable percentile10, y usa la variable max_pulse, y el numero que sera el porcentaje

print(percentile10) ## se lee