import pandas as pd
import json
import os

def analyze_student_data(file_path="students_data.json"):
    if not os.path.exists(file_path):
        return "Hata: Veri dosyası bulunamadı."

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if not data:
        return "Analiz edilecek veri bulunmuyor."

    student_list = list(data.values())
    df = pd.DataFrame(student_list)

    # Çıktıyı bir metin değişkeninde topluyoruz
    report = "="*35 + "\n"
    report += "🎓 ÖĞRENCİ GENEL DURUMU\n"
    report += "="*35 + "\n"
    report += df[['Student ID', 'Name', 'GPA']].to_string(index=False) + "\n\n"
    
    report += "="*35 + "\n"
    report += "📊 SINIF İSTATİSTİKLERİ\n"
    report += "="*35 + "\n"
    report += f"Ortalama GPA: {df['GPA'].mean():.2f}\n"
    report += f"En Yüksek: {df['GPA'].max()}\n"
    report += f"En Düşük: {df['GPA'].min()}\n"
    report += f"Toplam Öğrenci: {len(df)}\n"
    
    return report # Metni geri döndür