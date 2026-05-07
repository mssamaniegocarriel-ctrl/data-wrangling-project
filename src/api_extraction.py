import requests
import pandas as pd
import time
import os

BASE_URL = "https://clinicaltrials.gov/api/v2/studies"
BASE_PATH = r"C:\Users\MEL\Downloads\DATA\SEMANA 4\Proyect_Lab\Proyecto_lab"

def fetch_page(condition=None, page_size=1000, page_token=None):
    params = {"format": "json", "pageSize": page_size, "countTotal": "true"}
    if condition:
        params["query.cond"] = condition
    if page_token:
        params["pageToken"] = page_token
    r = requests.get(BASE_URL, params=params, timeout=30)
    return r.json() if r.status_code == 200 else {}

def parse_study(study):
    p = study.get("protocolSection", {})
    id_ = p.get("identificationModule", {})
    st = p.get("statusModule", {})
    d = p.get("designModule", {})
    sp = p.get("sponsorCollaboratorsModule", {})
    locs = p.get("contactsLocationsModule", {}).get("locations", [])
    conds = p.get("conditionsModule", {}).get("conditions", [])
    return {
        "nct_id": id_.get("nctId", ""),
        "title": id_.get("briefTitle", ""),
        "status": st.get("overallStatus", ""),
        "phase": d.get("phases", [None])[0] if d.get("phases") else None,
        "start_date": st.get("startDateStruct", {}).get("date", ""),
        "enrollment": d.get("enrollmentInfo", {}).get("count", None),
        "sponsor": sp.get("leadSponsor", {}).get("name", ""),
        "sponsor_class": sp.get("leadSponsor", {}).get("class", ""),
        "conditions": "; ".join(conds[:3]),
        "countries": "; ".join({l.get("country","") for l in locs if l.get("country")}),
    }

def fetch_all(conditions, max_studies=5000):
    records = []
    for term in conditions:
        print(f"Extrayendo: {term}...")
        page_token = None
        while len(records) < max_studies:
            data = fetch_page(condition=term, page_token=page_token)
            studies = data.get("studies", [])
            if not studies:
                break
            for s in studies:
                records.append(parse_study(s))
            page_token = data.get("nextPageToken")
            if not page_token:
                break
            time.sleep(1.2)
        print(f"  Total acumulado: {len(records)}")
    return pd.DataFrame(records)

def save_raw_data(df):
    filepath = f"{BASE_PATH}\\data\\raw\\trials_raw.csv"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"Datos guardados: {filepath}")

if __name__ == "__main__":
    CONDITIONS = ["cancer", "diabetes", "cardiovascular", "rare disease"]
    df = fetch_all(CONDITIONS, max_studies=4000)
    save_raw_data(df)