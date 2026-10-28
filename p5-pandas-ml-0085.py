import numpy as np
import pandas as pd

# Lopez Ricardo NC = 0085
## datos matriz 4
datos_alumno=[
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnas
# y almacenar la tabla en la variable df DataFrame
print("----------datos a partir de una matriz---------")
df=pd.DataFrame(datos_alumno,columns=['ci','marcas','paquete'])

# CORRECCIÓN: Imprime la variable df, no la librería pd
print(df)
# datos a partir de diccionario
print("----------datos a partir de un diccionario---------")
alumno_diccionario={"nombre":["alan","johan","ricardo","scarlett","christian","iker"],
"califa":[59,67,60,90,100,98],
"edad":[64,15,26,16,18,14]
}
estudiantes=pd.DataFrame(alumno_diccionario)
print(estudiantes)
print("Ricardo Lopez Nc 0085")