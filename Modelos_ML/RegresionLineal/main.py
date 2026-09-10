import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title='API de predicción de precio',
    description='API para predecir el precio de una casa segun su tamaño en m2',
    version='1.0.0'
)

try:
    #Cargar el modelo entrenado
    model = joblib.load('Modelos_ML/RegresionLineal/Models/linear_regression_model.pkl')

except Exception:
    model = None

class House_m2(BaseModel):
    area_m2 : float = Field(..., example = 82.5, description="Area de la casa en m2", gt=0)

@app.get("/")
def health_check():
    return {
        "message": "API de prediccion de precios de viviendas en funcionamiento",
        "Status" : "OK",
        "model" : "Regresion Lineal",
        "version" : "1.0.0",
        "model_loaded" : model is not None
    }

@app.post("/predict")
def prdict_price_m2(data:House_m2): 
    if not model:
        raise HTTPException(status_code=500, detail="Model not found or not loaded")
    
    prediction = model.predict([[data.area_m2]])[0]
    return {
        "area_m2" : data.area_m2,
        "predicted_price" : round(prediction, 2)
    }
    
