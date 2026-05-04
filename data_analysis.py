import pandas as pd
import json
import os

def analyze_student_data(file_path="students_data.json"):
    """JSON dosyasındaki verileri okur ve Pandas DataFrame kullanarak analiz eder."""
    
    if not os.path.exists(file_path):
        print("Hata: Veri dosyası bulunamadı. Lütfen önce sisteme öğrenci ekleyin.")
        return

    # 1. Veriyi JSON'dan Okuma
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Veri yoksa işlemi iptal et
    if not data:
        print("Analiz edilecek veri bulunmuyor.")
        return

    # 2. Sözlük (Dictionary) formatını Pandas DataFrame'e çevirme
    # data.values() içindeki her bir öğrenci sözlüğünü alıp listeye koyuyoruz
    student_list = list(data.values())
    df = pd.DataFrame(student_list)

    # 3. İstatistiksel Analizler ve Çıktılar
    print("\n" + "="*35)
    print("🎓 ÖĞRENCİ GENEL DURUM TABLOSU")
    print("="*35)
    # Sadece ID, İsim ve GPA sütunlarını temiz bir şekilde ekrana yazdırıyoruz
    print(df[['Student ID', 'Name', 'GPA']].to_string(index=False))
    
    print("\n" + "="*35)
    print("📊 SINIF İSTATİSTİKLERİ")
    print("="*35)
    
    # Pandas'ın hazır metotlarıyla tek satırda istatistik hesaplama
    print(f"Genel Not Ortalaması (GPA) : {df['GPA'].mean():.2f}")
    print(f"En Yüksek GPA            : {df['GPA'].max()}")
    print(f"En Düşük GPA             : {df['GPA'].min()}")
    print(f"Toplam Öğrenci Sayısı    : {len(df)}")
    print("="*35 + "\n")

# Test Bloğu
if __name__ == "__main__":
    analyze_student_data()