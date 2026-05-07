# 🏥 Clinical Trials Global Analysis

## 📊 Resumen Ejecutivo

Este proyecto analiza el panorama global de los ensayos clínicos utilizando datos en tiempo real de la API pública de ClinicalTrials.gov v2, que contiene más de 500.000 estudios registrados a nivel mundial.

A través de un pipeline completo de análisis de datos — que incluye extracción via API, limpieza de datos, análisis exploratorio (EDA) y visualizaciones en Python — identificamos patrones globales en la investigación clínica por fase de desarrollo, país de realización y tipo de patrocinador.

Los resultados muestran que Estados Unidos domina la investigación clínica global, que la mayoría de ensayos se concentran en fases tempranas de desarrollo, y que el COVID-19 disparó la actividad investigadora hasta niveles históricos en 2021.

Este proyecto combina habilidades de análisis de datos con conocimiento del dominio clínico — un perfil diferencial muy valorado en el sector farmacéutico, biotecnológico y de CROs.

---

## 📑 Tabla de Contenidos

- [Visualización principal](#visualización-principal)
- [Objetivo del proyecto](#objetivo-del-proyecto)
- [Dataset](#dataset)
- [Proceso de análisis](#proceso-de-análisis)
- [Resultados e Insights](#resultados-e-insights)
- [Próximos pasos](#próximos-pasos)
- [Cómo reproducir el análisis](#cómo-reproducir-el-análisis)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Resumen simple](#resumen-simple)

---

## 📈 Visualización Principal

**Evolución temporal de ensayos clínicos (2000-2024)**

Este gráfico muestra el crecimiento sostenido de la investigación clínica global, con un pico histórico en 2021 impulsado por la respuesta científica al COVID-19.

*(Ver notebooks/03_analysis.ipynb)*

---

## 🎯 Objetivo del Proyecto

El objetivo de este proyecto es analizar el panorama global de los ensayos clínicos para identificar tendencias por fase de desarrollo, país y tipo de patrocinador.

Las preguntas principales del análisis son:

- ¿Qué áreas terapéuticas concentran más ensayos clínicos activos a nivel global?
- ¿Qué países y regiones lideran la actividad de investigación clínica?
- ¿Cómo han evolucionado los ensayos clínicos por fase (I→IV) a lo largo del tiempo?
- ¿Qué relación existe entre el tipo de patrocinador y la fase del ensayo?

Este análisis busca entender mejor la estructura global de la investigación clínica y sus implicaciones para el sector farmacéutico y de salud.

---

## 🗂️ Dataset

El análisis utiliza datos extraídos de:

**ClinicalTrials.gov API v2**
- API pública sin registro ni API key requerida
- Más de 500.000 estudios clínicos registrados globalmente
- Actualización en tiempo real

**Variables principales**

| Variable | Descripción |
|----------|-------------|
| nct_id | Identificador único del ensayo |
| title | Título del estudio |
| status | Estado actual (Recruiting, Completed, etc.) |
| phase | Fase del ensayo (1, 2, 3, 4) |
| start_date | Fecha de inicio |
| enrollment | Número de participantes |
| sponsor | Nombre del patrocinador |
| sponsor_class | Tipo de patrocinador (Industry, NIH, Other) |
| conditions | Enfermedades estudiadas |
| countries | Países donde se realiza |
| primary_country | País principal |
| start_year | Año de inicio (derivado) |

**Áreas terapéuticas analizadas**
- Cancer
- Diabetes
- Cardiovascular
- Rare Disease

**Período analizado:** 2000 – 2024

---

## ⚙️ Proceso de Análisis

El proyecto sigue un pipeline completo de análisis de datos:

**1️⃣ Extracción de datos (API)**
- Conexión a ClinicalTrials.gov API v2
- Paginación automática con tokens
- Extracción de 4.000 ensayos clínicos
- Guardado en formato CSV

**2️⃣ Exploración inicial**
- Inspección del dataset
- Análisis de estructura y tipos de datos
- Identificación de valores nulos y duplicados

**3️⃣ Limpieza de datos (7 técnicas)**
- Eliminación de duplicados por NCT ID
- Tratamiento de valores nulos
- Estandarización de strings
- Normalización de fechas
- Tratamiento de outliers
- Extracción de país principal
- Limpieza de columnas

**4️⃣ Análisis Exploratorio (EDA)**
- Distribución por fase
- Rankings geográficos
- Evolución temporal
- Análisis por tipo de patrocinador

**5️⃣ Visualizaciones**
- Gráfico de distribución por fase
- Top 10 países con más ensayos
- Línea temporal 2000-2024
- Relación patrocinador vs fase

---

## 🔎 Resultados e Insights

**1️⃣ Distribución por fase — La pirámide de filtrado clínico**

La distribución confirma el alto nivel de exigencia del desarrollo de fármacos:
- Phase 2 → 1.036 ensayos (26%)
- Phase 1 → 816 ensayos (20%)
- Phase 3 → 327 ensayos (8%)
- Phase 4 → 85 ensayos (2%)

Cuanto más avanzada la fase, menos ensayos sobreviven.

**2️⃣ Países líderes — Concentración geográfica**

La investigación clínica está muy concentrada geográficamente:
- Estados Unidos → 1.487 ensayos (37%)
- China → 627 ensayos (16%)
- Francia → 305 ensayos (8%)

EEUU lidera con casi el doble de ensayos que China.

**3️⃣ Evolución temporal — El impacto del COVID-19**

- 2000-2015: crecimiento lento y estable
- 2015-2019: aceleración notable
- 2020: pequeña caída por interrupción de ensayos
- 2021: pico máximo histórico — boom post-COVID
- 2022-2024: estabilización en niveles altos

**4️⃣ Patrocinador vs Fase — Industria y academia**

Existe un patrón claro de especialización:
- Industry domina en fases avanzadas (retorno comercial)
- Other (universidades/hospitales) lidera en fases tempranas
- NIH presente principalmente en investigación básica

---

## 🚀 Próximos Pasos

Posibles extensiones del proyecto:

- Ampliar la extracción a 50.000 ensayos
- Análisis por enfermedad específica (oncología, neurología)
- Incorporar datos de resultados clínicos
- Análisis de tasas de éxito por área terapéutica
- Crear dashboards interactivos con Plotly/Streamlit
- Incorporar datos de inversión en I+D por país

---

## 🔁 Cómo Reproducir el Análisis

Este proyecto es completamente reproducible.

**Pasos para replicarlo**

1️⃣ Clonar el repositorio
```bash
git clone https://github.com/mssamaniegocarriel-ctrl/data-wrangling-project
cd data-wrangling-project
```

2️⃣ Instalar dependencias
```bash
pip install pandas numpy matplotlib seaborn requests jupyter
```

3️⃣ Extraer datos (sin API key necesaria)
```bash
python src/api_extraction.py
```

4️⃣ Limpiar datos
```bash
python src/cleaning.py
```

5️⃣ Abrir notebook de análisis
```bash
jupyter notebook notebooks/03_analysis.ipynb
```

---

## 🛠️ Tecnologías Utilizadas

- Python 3.10
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Requests
- Jupyter Notebook
- ClinicalTrials.gov API v2
- GitHub

---

## 📁 Estructura del Proyecto

```
data-wrangling-project/
│
├── data/
│   ├── raw/
│   │   └── trials_raw.csv
│   └── clean/
│       └── trials_clean.csv
│
├── notebooks/
│   ├── 01_extraction.ipynb
│   ├── 02_cleaning.ipynb
│   └── 03_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── api_extraction.py
│   └── cleaning.py
│
├── README.md
└── requirements.txt
```

---

## 📌 Resumen Simple

Este README responde a cinco preguntas clave:

**Qué hicimos**
Analizamos el panorama global de ensayos clínicos usando datos reales de ClinicalTrials.gov API v2.

**Con qué datos**
4.000 ensayos clínicos de 4 áreas terapéuticas (cancer, diabetes, cardiovascular, rare disease) del período 2000-2024.

**Qué proceso seguimos**
Extracción API → Limpieza de datos (7 técnicas) → EDA → Visualizaciones en Python.

**Qué descubrimos**
EEUU domina la investigación clínica global, la mayoría de ensayos están en fases tempranas, y el COVID-19 disparó la actividad investigadora a niveles históricos en 2021.

**Cómo reproducirlo**
Ejecutando el pipeline completo incluido en este repositorio — sin API key ni registro necesario.

---

##  Autora

**Mel Samaniego**
Data Analytics Bootcamp | Formación en Laboratorio Clínico y Biomédica


🔗 GitHub: [mssamaniegocarriel-ctrl](https://github.com/mssamaniegocarriel-ctrl)
📊 Presentación: https://docs.google.com/presentation/d/1o9TtduSCMLTt_iDc9HNEbdGFMNaZuAhkwXDPN0XlWbU/edit?usp=sharing

