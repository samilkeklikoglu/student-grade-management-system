import pandas as pd
import json
import os

def get_analysis_data(file_path="students_data.json"):
    """JSON verilerini Pandas ile analiz eder ve UI için hazırlar."""
    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if not data or len(data) == 0:
        return None

    # Verileri tablo yapısına (DataFrame) döküyoruz
    df = pd.DataFrame(list(data.values()))
    
    # İstatistiksel özetler
    stats = {
        "avg": round(df['GPA'].mean(), 2) if 'GPA' in df.columns else 0,
        "max": df['GPA'].max() if 'GPA' in df.columns else 0,
        "min": df['GPA'].min() if 'GPA' in df.columns else 0,
        "total": len(df)
    }
    
    return {"df": df, "stats": stats}