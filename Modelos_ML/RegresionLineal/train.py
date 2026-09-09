import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

#Datos de entrenamiento (X) y etiquetas (y)
x = np.array([[50], [40], [70], [100], [60]])
y = np.array([6000000, 4500000, 8200000, 11000000, 7000000])

#Entrnar el modelo de regresion lineal

model = LinearRegression()
model.fit(x, y)

#Guardar el artefacto del modelo entrenado en un archivo
joblib.dump()