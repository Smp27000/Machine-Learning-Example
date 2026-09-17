# 🧠 Taller 3: Fundamentos de Machine Learning y Visión Artificial con Python

Este repositorio contiene una colección práctica y didáctica de proyectos, modelos y técnicas desarrolladas para el aprendizaje de **Machine Learning**, **Carga y Procesamiento de Datos** y **Visión Artificial** en Python.

---

## 📁 Estructura del Proyecto

```text
├── Carga_datos/                   # Extracción, transformación y lectura de datos
│   ├── 1.csv_carga_datos.ipynb    # Carga y manipulación de archivos CSV
│   ├── 2.excel_carga_datos.ipynb  # Procesamiento de hojas de cálculo Excel (.xlsx)
│   ├── 3.api_carga_datos.ipynb    # Consumo de datos desde APIs REST
│   ├── 4.webscraping_carga_datos.ipynb # Extracción web con BeautifulSoup
│   └── dataset_ventas.*           # Datasets de ejemplo (CSV / Excel)
│
├── Modelos_ML/                    # Implementación de algoritmos de Machine Learning
│   │
│   ├── RegresionLineal/           # Predicción del valor de inmuebles según área (m²)
│   │   ├── backend/               # Entrenamiento (train.py) y API de predicción
│   │   └── front/                 # Interfaz de usuario para realizar consultas
│   │
│   ├── RandomForest/              # Clasificación y diagnóstico con Random Forest
│   │   ├── 1.Crear_dataset.py     # Generación y preparación de datos sintéticos
│   │   ├── 2.Entrenar_modelo.py   # Entrenamiento del clasificador Random Forest
│   │   └── 3.Predecir_enefermedad.py # Interfaz/Script interactivo de inferencia
│   │
│   ├── VisionArtificial/          # Pruebas y procesamiento en Jupyter Notebooks
│   │   ├── haarcascade_frontalface_default.xml # Clasificador en cascada
│   │   └── index.ipynb            # Detección de rostros en imágenes estáticas
│   │
│   └── Captura de video/          # Aplicación Web Full-Stack de Visión Artificial
│       └── py_img/
│           ├── api/index.py       # API Flask con OpenCV (detección Haar Cascade)
│           ├── public/            # Frontend Glassmorphism (HTML5, CSS3, JS)
│           └── requirements.txt   # Dependencias específicas de la app web
│
├── requirements.txt               # Dependencias globales del repositorio
└── README.md                      # Documentación general del taller
```

---

## 🚀 Módulos y Proyectos Incluidos

### 1. 📊 Ingesta y Carga de Datos (`Carga_datos/`)
Cuadernos interactivos de Jupyter que cubren las fuentes de datos más utilizadas en la industria:
- **Archivos planos (CSV)** y **Hojas de cálculo (Excel)** usando `pandas` y `openpyxl`.
- **APIs REST** mediante la librería `requests`.
- **Web Scraping** extrayendo información estructurada con `beautifulsoup4`.

### 2. 📈 Regresión Lineal (`Modelos_ML/RegresionLineal/`)
- Modelo supervisado que predice el precio estimado de una propiedad según su superficie en metros cuadrados ($m^2$).
- Serialización y persistencia del modelo entrenado usando `joblib`.
- Arquitectura cliente-servidor con integración Backend (API) y Frontend interactivo.

### 3. 🌲 Random Forest Classifier (`Modelos_ML/RandomForest/`)
- Generación de dataset médico/sintético de síntomas.
- Entrenamiento de un ensamble multivariable de árboles de decisión (`RandomForestClassifier`) con métricas de rendimiento y validación.
- Diagnóstico predictivo de enfermedades según el cuadro sintomático ingresado.

### 4. 👁️ Visión Artificial y Detección de Rostros (`Captura de video/py_img` & `VisionArtificial/`)
- Detección facial en tiempo real usando **OpenCV** y el modelo **Haar Cascade**.
- **Servidor Flask:** Endpoint `/api/detect` que decodifica frames en Base64, localiza rostros y dibuja coordenadas delimitadoras.
- **Frontend Moderno:** Interfaz responsiva con soporte para arrastrar y soltar imágenes (Drag & Drop) y captura continua vía cámara web (Webcam).

---

## 🛠️ Requisitos e Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/Smp27000/Machine-Learning-Example.git
cd Machine-Learning-Example
```

### 2. Crear y activar entorno virtual (Recomendado)
```bash
# En Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

> **Nota:** Para ejecutar la aplicación web de detección facial en `Captura de video/py_img`, asegúrate de instalar las dependencias de su carpeta:
> ```bash
> cd "Modelos_ML/Captura de video/py_img"
> pip install -r requirements.txt
> ```

---

## ▶️ Guía de Ejecución

### Ejecutar la Aplicación Web de Visión Facial:
```powershell
cd "Modelos_ML/Captura de video/py_img"
python -m flask --app api.index run --debug --port 8000
```
Luego abre tu navegador en `http://127.0.0.1:8000`.

### Ejecutar los Notebooks de Análisis de Datos:
```powershell
jupyter lab
# o también:
jupyter notebook
```

### Entrenar el Modelo de Random Forest:
```powershell
cd "Modelos_ML/RandomForest"
python "1.Crear_dataset.py"
python "2.Entrenar_modelo.py"
python "3.Predecir_enefermedad.py"
```

---

## 💻 Tecnologías Utilizadas

- **Lenguaje:** Python 3.10+ / 3.13
- **Machine Learning & Datos:** `scikit-learn`, `numpy`, `pandas`, `joblib`
- **Visión Artificial:** `OpenCV` (`opencv-python-headless`)
- **Visualización & Notebooks:** `matplotlib`, `plotly`, `jupyter`
- **Desarrollo Web & APIs:** `Flask`, `HTML5`, `CSS3 (Glassmorphism)`, `JavaScript Vanilla`, `Bootstrap 5`

---

## Links
- Pagina web de la Captura de video/py_img: https://machine-learning-example-tawny.vercel.app/
- Backend de RegresionLineal: https://machine-learning-example-production.up.railway.app/
- Frontend de RegresionLineal: https://stunning-enjoyment-production-a00f.up.railway.app/
- streamlit de Random Forest: https://machine-learning-example-68os9qtqktiy8jyyucflsn.streamlit.app/
