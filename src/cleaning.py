import pandas as pd
import numpy as np
import os
from datetime import datetime

BASE_PATH = r"C:\Users\MEL\Downloads\DATA\SEMANA 4\Proyect_Lab\Proyecto_lab"

def load_raw_data():
    filepath = f"{BASE_PATH}\\data\\raw\\trials_raw.csv"
    df = pd.read_csv(filepath)
    print(f"Datos cargados: {df.shape}")
    return df

def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates(subset=["nct_id"], keep="first")
    print(f"Duplicados eliminados: {before - len(df)}")
    return df

def handle_nulls(df):
    df["enrollment"] = df["enrollment"].fillna(df["enrollment"].median())
    for col in ["phase", "sponsor_class", "conditions", "countries"]:
        df[col] = df[col].fillna("Unknown")
    print("Nulos tratados")
    return df

def clean_strings(df):
    phase_map = {
        "PHASE1": "Phase 1", "PHASE2": "Phase 2",
        "PHASE3": "Phase 3", "PHASE4": "Phase 4",
        "EARLY_PHASE1": "Phase 1 (Early)", "NA": "Not Applicable"
    }
    status_map = {
        "RECRUITING": "Recruiting", "COMPLETED": "Completed",
        "TERMINATED": "Terminated", "NOT_YET_RECRUITING": "Not Yet Recruiting",
        "ACTIVE_NOT_RECRUITING": "Active, Not Recruiting",
        "WITHDRAWN": "Withdrawn"
    }
    df["phase"] = df["phase"].map(phase_map).fillna(df["phase"])
    df["status"] = df["status"].map(status_map).fillna(df["status"])
    df["title"] = df["title"].str.strip()
    df["sponsor"] = df["sponsor"].str.strip()
    print("Strings estandarizados")
    return df

def clean_dates(df):
    df["start_date"] = pd.to_datetime(df["start_date"], errors="coerce")
    df["start_year"] = df["start_date"].dt.year
    df.loc[df["start_year"] < 1990, "start_year"] = np.nan
    df.loc[df["start_year"] > 2025, "start_year"] = np.nan
    print("Fechas normalizadas")
    return df

def clean_enrollment(df):
    df.loc[df["enrollment"] > 1_000_000, "enrollment"] = np.nan
    df["enrollment"] = df["enrollment"].fillna(df["enrollment"].median())
    df["enrollment"] = df["enrollment"].astype(int)
    print("Outliers tratados")
    return df

def extract_primary_country(df):
    df["primary_country"] = df["countries"].str.split(";").str[0].str.strip()
    df["primary_country"] = df["primary_country"].replace("", "Unknown")
    print("Pais principal extraido"