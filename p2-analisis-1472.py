# importar librerias
import pandas as pd
import numpy as np
print("Analisis De Desempeño Laboral Jose Solis NC 1472")
empleados = {
    "Empleado": ["Elena", "Sergio", "Lucia", "Gonzalo", "Valeria", "Diego"],
    "Departamento": ["Ventas", "IT", "HR", "IT", "Ventas", "Finanzas"],
    "Horas_Capacitacion": [40, 80, 25, 60, 90, 15],
    "Evaluacion_Desempeno": [8.5, 9.2, 7.0, 8.8, 9.6, 6.5]
}
df = pd.DataFrame(empleados)
print(df)
print("------Agrupar por una sola columna Departamento-------")
agrupado = df.groupby('Departamento')
print(agrupado)
print("------Promedio por Departamento-------")
# horas de capacitacion promedio por departamento
print(agrupado['Horas_Capacitacion'].mean())
print("------desempeño maximo en cada Departamento-------")
# Desempeño máximo en cada departamento
print(agrupado['Evaluacion_Desempeno'].max())

