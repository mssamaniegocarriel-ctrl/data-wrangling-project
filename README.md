# 🏥 Clinical Trials Global Analysis

> **Data Analytics Bootcamp — Individual Project | Module 1**

## 📋 Project Overview

This project analyzes the global landscape of clinical trials using real-time data from the **ClinicalTrials.gov public API v2** (500,000+ studies worldwide).

As a data analyst with a background in Clinical Laboratory and Biomedical Science, this project bridges data analytics with domain expertise — a combination highly valued in pharma, biotech, and CRO sectors.

---

## ❓ Research Questions

1. **Which therapeutic areas** concentrate the most active clinical trials globally?
2. **Which countries and regions** lead clinical research activity?
3. **How have clinical trials evolved** by phase (I → IV) over time (2010–2024)?
4. **What is the relationship** between sponsor type (Industry vs. Government) and trial phase?

---

## 🗂️ Data Sources

| Source | Type | Description |
|--------|------|-------------|
| [ClinicalTrials.gov API v2](https://clinicaltrials.gov/data-api/api) | REST API (public, no key required) | 500,000+ clinical studies worldwide |
| [Kaggle — Clinical Trials Dataset](https://www.kaggle.com/) | CSV Dataset | Historical clinical trial data for EDA enrichment |

---

## ⚙️ Methodology

### Pipeline
```
API Extraction → Raw Data → Cleaning (7 techniques) → EDA → Visualizations → Insights
```

### Data Cleaning Techniques Applied
1. **Duplicate removal** — deduplicated by NCT ID
2. **Null handling** — median imputation for numerical, 'Unknown' for categorical
3. **String standardization** — phase/status/sponsor_class normalization
4. **Date normalization** — mixed format parsing, year extraction, duration calculation
5. **Outlier treatment** — enrollment_count capping at 1M
6. **Feature engineering** — primary_country extraction, duration_months
7. **Column cleanup** — removing redundant processed columns

---

## 📊 Key Findings

_(To be completed after analysis)_

---

## 🛠️ Technologies

- **Python 3.9+** — pandas, numpy, matplotlib, seaborn, requests
- **Jupyter Notebook**
- **ClinicalTrials.gov API v2**

---

## 📁 Project Structure

```
data-wrangling-project/
├── data/
│   ├── raw/            ← Datos extraídos de la API
│   └── clean/          ← Datos después de limpieza
├── notebooks/
│   ├── 01_extraction_exploration.ipynb
│   ├── 02_cleaning.ipynb
│   └── 03_analysis_report.ipynb
├── src/
│   ├── api_extraction.py   ← Extracción via API
│   └── cleaning.py         ← Pipeline de limpieza
└── README.md
```

---

## 🚀 How to Reproduce

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/data-wrangling-project
cd data-wrangling-project

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn requests jupyter

# 3. Extract data (no API key needed)
python src/api_extraction.py

# 4. Clean data
python src/cleaning.py

# 5. Open analysis notebook
jupyter notebook notebooks/03_analysis_report.ipynb
```

---

## 👤 Author

**Mel Samaniego**  
Data Analytics Bootcamp | Background in Clinical Laboratory & Biomedical Science  
_Building a portfolio at the intersection of data analytics and life sciences._

---

## 🔗 Links

- 📊 [Presentation Slides](#) _(add link)_
- 📁 [Data Source — ClinicalTrials.gov](https://clinicaltrials.gov)
- 📋 [Project Board — Trello](#) _(add link)_
