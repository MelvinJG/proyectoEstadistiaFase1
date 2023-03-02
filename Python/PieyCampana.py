
Grafica de PIE

import matplotlib
import matplotlib.pyplot as plt
import numpy as np




etnicos = 'Maya', 'Xinca', 'Garifuna', 'Ladino', 'Extranjero'
#Declaramos el tamaño de cada 'rebanada' y en sumatoria todos deben dar al 100%
sizes = [63, 65, 66, 62,67]
#En este punto señalamos que posicion debe 'resaltarse' y el valor, si se coloca 0, se omite
explode = (0.1, 0, 0, 0,0)  

fig1, ax1 = plt.subplots()
#Creamos el grafico, añadiendo los valores
ax1.pie(sizes, explode=explode, labels=etnicos, autopct='%1.1f%%',
        shadow=True, startangle=90)
#señalamos la forma, en este caso 'equal' es para dar forma circular
ax1.axis('equal')
plt.title("Grafica de Promedio de Notas x Grupo Etnico")
plt.legend()
plt.savefig('grafica_pastel.png')
plt.show()



CAMPANA DE GAUSS
# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

Extranjeros = [48.2,51.2,54.4,58,58.2,58.8,59.2,59.8,60.2,60.8,61.8,63,63.2,63.4,64.4,
            64.8,64.8,65,65.2,65.2,65.2,66,66.8,68.2,69,69.4,72.4,74.8,76.2,76.2,76.6]

Garifunas = [41.8,43.6,47.2,47.4,47.6,47.8,	50.6,51.8,52.6,	54.2,54.4,55,55.2,55.2,	55.4,56.2,56.2,	56.4,56.6,56.8,	57,57.2,57.2,57.2,
57.6,58,58.8,59,59.4,60.2,60.4,60.6,60.8,60.8,	61.2,61.2,61.6,	62,62.4,62.4,62.6,63.6,	63.8,63.8,64.2,	64.6,64.8,64.8,	65.4,
65.4,65.4,65.6,	65.8,66.4,66.6,	67,67.4,68,68.2,69,69.2,69.2,69.4,70.2,	70.4,70.8,70.8,	71.2,71.2,71.8,	71.8,72,72.2,72.4,
73.2,73.2,73.4,	74.2,76.4,76.4,	76.8,77,77.4,77.6,78.6,	78.6,80.2,81.8,	86.4,86.6,88,88.8,92.4,	92.4]  

Ladinos = [48,50.2,50.6,50.6,52.4,	52.6,52.6,52.6,	56.8,57,58,58.8,59.6,61.4,62.4,	65.4,65.4,66.2,	68,71,71,76.4,76.4,77.6,82.2]

Mayas = [48,50.2,50.6,50.6,52.4,52.6,52.6,52.6,	56.8,57,58,58.8,59.6,61.4,62.4,	65.4,65.4,66.2,	68,71,71,76.4,76.4,77.6,82.2]

Xinca = [
36.2,37,37,44.4,44.6,44.8,48.4,	48.8,48.8,50,50,53.4,53.4,54.8,	56.6,57.4,57.4,	57.8,57.8,57.8,	58.2,59.2,59.4,	
59.4,60,61,61.6,62.4,62.6,63.4,64.2,64.2,64.2,64.2,65.4,66.6,67.4,67.4,68.6,68.6,68.8,68.8,69.6,69.6,69.6,69.6,	
70.6,70.8,71.4,	71.4,71.4,71.6,	72,72,72.4,72.8,73,73.4,74,77.4,77.4,78,78,78.4,78.6,78.6,79.2,	80,80.6,81.8,81.8,83,86.4,95.4]

# A custom function to calculate
# probability distribution function
def pdf(x):
    
   mean = np.mean(x)
   std = np.std(x)
   CV = (std / mean) *100
   
   print (CV)
   
   
  # y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2))

   #return y_out
    
# To generate an array of x-values

x = Xinca 

# To generate an array of
# y-values using corresponding x-values
y = pdf(x)
  
# Plotting the bell-shaped curve



# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:42:56 2023

@author: dell
"""

# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

Extranjeros = [48.2,51.2,54.4,58,58.2,58.8,59.2,59.8,60.2,60.8,61.8,63,63.2,63.4,64.4,
            64.8,64.8,65,65.2,65.2,65.2,66,66.8,68.2,69,69.4,72.4,74.8,76.2,76.2,76.6]

Garifunas = [41.8,43.6,47.2,47.4,47.6,47.8,	50.6,51.8,52.6,	54.2,54.4,55,55.2,55.2,	55.4,56.2,56.2,	56.4,56.6,56.8,	57,57.2,57.2,57.2,
57.6,58,58.8,59,59.4,60.2,60.4,60.6,60.8,60.8,	61.2,61.2,61.6,	62,62.4,62.4,62.6,63.6,	63.8,63.8,64.2,	64.6,64.8,64.8,	65.4,
65.4,65.4,65.6,	65.8,66.4,66.6,	67,67.4,68,68.2,69,69.2,69.2,69.4,70.2,	70.4,70.8,70.8,	71.2,71.2,71.8,	71.8,72,72.2,72.4,
73.2,73.2,73.4,	74.2,76.4,76.4,	76.8,77,77.4,77.6,78.6,	78.6,80.2,81.8,	86.4,86.6,88,88.8,92.4,	92.4]  

Ladinos = [48,50.2,50.6,50.6,52.4,	52.6,52.6,52.6,	56.8,57,58,58.8,59.6,61.4,62.4,	65.4,65.4,66.2,	68,71,71,76.4,76.4,77.6,82.2]

Mayas = [48,50.2,50.6,50.6,52.4,52.6,52.6,52.6,	56.8,57,58,58.8,59.6,61.4,62.4,	65.4,65.4,66.2,	68,71,71,76.4,76.4,77.6,82.2]

Xinca = [
36.2,37,37,44.4,44.6,44.8,48.4,	48.8,48.8,50,50,53.4,53.4,54.8,	56.6,57.4,57.4,	57.8,57.8,57.8,	58.2,59.2,59.4,	
59.4,60,61,61.6,62.4,62.6,63.4,64.2,64.2,64.2,64.2,65.4,66.6,67.4,67.4,68.6,68.6,68.8,68.8,69.6,69.6,69.6,69.6,	
70.6,70.8,71.4,	71.4,71.4,71.6,	72,72,72.4,72.8,73,73.4,74,77.4,77.4,78,78,78.4,78.6,78.6,79.2,	80,80.6,81.8,81.8,83,86.4,95.4]

# A custom function to calculate
# probability distribution function
def pdf(x):
    
   mean = np.mean(x)
   std = np.std(x)

   
   
   y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2))

   return y_out
    
# To generate an array of x-values

x = Xinca 

# To generate an array of
# y-values using corresponding x-values
y = pdf(x)
  
# Plotting the bell-shaped curve

plt.style.use('seaborn')
plt.figure(figsize = (6, 6))
plt.plot(x, y, color = 'black',
         linestyle = 'dashed')
  
plt.scatter( x, y, marker = 'o', s = 25, color = 'red')
plt.show()
