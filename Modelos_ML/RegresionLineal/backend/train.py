import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Datos de entrenamiento (X) y etiquetas (y)
x = np.array([[40], [50], [70], [100], [200]])
y = np.array([410000000,500000000,700000000,1000000000,2000000000])

#Entrnar el modelo de regresion lineal

model = LinearRegression()
model.fit(x, y)

# #Predicciones de prueba
# y_pred = model.predict(x)

# #Impremir los resultados de la informacion del modelo
# print("Coeficiente de regresion:", model.coef_[0])
# print("Interseccion:", model.intercept_)

# #Graficar los datos de entrenamiento
# plt.scatter(x, y, color='blue', label='Datos de entrenamiento')

# #Graficar la linea de regresion
# plt.plot(x, y_pred, color='red', label='Lineal de regresion')
# plt.xlabel('Superficie (m2)')
# plt.ylabel('Precio (COP)')
# plt.title('Regresion Lineal: Precio de vivienda segun su superficie')
# plt.legend()
# plt.grid(True)

# #Imprimir la grafica
# plt.show()

# Guardar el artefacto del modelo entrenado en un archivo
import os
os.makedirs('Models', exist_ok=True)
joblib.dump(model, 'Models/linear_regression_model.pkl')

