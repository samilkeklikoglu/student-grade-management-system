import tkinter as tk
from tkinter import messagebox
from manager import GradeManager
from data_analysis import analyze_student_data

class App:
    def __init__(self, root):
        # Arka planda çalışacak veri yöneticimizi başlatıyoruz
        self.manager = GradeManager()
        
        # Arayüzün temel ayarları
        self.root = root
        self.root.title("Student Grade Management System")
        self.root.geometry("350x450")
        self.root.resizable(False, False)

        # --- 1. ÖĞRENCİ EKLEME BÖLÜMÜ ---
        frame_student = tk.LabelFrame(root, text="Yeni Öğrenci Ekle", padx=10, pady=10)
        frame_student.pack(padx=20, pady=10, fill="x")

        tk.Label(frame_student, text="Öğrenci ID:").grid(row=0, column=0, sticky="w")
        self.entry_id = tk.Entry(frame_student)
        self.entry_id.grid(row=0, column=1, pady=5)

        tk.Label(frame_student, text="Ad Soyad:").grid(row=1, column=0, sticky="w")
        self.entry_name = tk.Entry(frame_student)
        self.entry_name.grid(row=1, column=1, pady=5)

        tk.Button(frame_student, text="Öğrenci Ekle", command=self.add_student, bg="#4CAF50", fg="white").grid(row=2, columnspan=2, pady=10)

        # --- 2. NOT EKLEME BÖLÜMÜ ---
        frame_grade = tk.LabelFrame(root, text="Not Ekle", padx=10, pady=10)
        frame_grade.pack(padx=20, pady=10, fill="x")

        tk.Label(frame_grade, text="Öğrenci ID:").grid(row=0, column=0, sticky="w")
        self.entry_grade_id = tk.Entry(frame_grade)
        self.entry_grade_id.grid(row=0, column=1, pady=5)

        tk.Label(frame_grade, text="Ders Adı:").grid(row=1, column=0, sticky="w")
        self.entry_course = tk.Entry(frame_grade)
        self.entry_course.grid(row=1, column=1, pady=5)

        tk.Label(frame_grade, text="Not (0-100):").grid(row=2, column=0, sticky="w")
        self.entry_grade = tk.Entry(frame_grade)
        self.entry_grade.grid(row=2, column=1, pady=5)

        tk.Button(frame_grade, text="Notu Kaydet", command=self.add_grade, bg="#2196F3", fg="white").grid(row=3, columnspan=2, pady=10)
        tk.Button(root, text="Sınıf İstatistiklerini Göster", command=self.show_report, bg="#FF9800", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

    # --- BUTONLARIN YAPACAĞI İŞLEMLER ---
    def add_student(self):
        s_id = self.entry_id.get().strip()
        name = self.entry_name.get().strip()
        
        if not s_id or not name:
            messagebox.showerror("Hata", "Lütfen ID ve İsim alanlarını doldurun.")
            return
            
        if s_id in self.manager.students:
            messagebox.showerror("Hata", "Bu ID ile kayıtlı bir öğrenci zaten var!")
        else:
            self.manager.add_student(s_id, name)
            messagebox.showinfo("Başarılı", f"{name} sisteme başarıyla eklendi.")
            self.entry_id.delete(0, tk.END)
            self.entry_name.delete(0, tk.END)

    def add_grade(self):
        s_id = self.entry_grade_id.get().strip()
        course = self.entry_course.get().strip()
        grade_str = self.entry_grade.get().strip()
        
        if not s_id or not course or not grade_str:
            messagebox.showerror("Hata", "Lütfen tüm not alanlarını doldurun.")
            return

        try:
            grade = float(grade_str)
            if grade < 0 or grade > 100:
                raise ValueError
        except ValueError:
            messagebox.showerror("Hata", "Lütfen 0 ile 100 arasında geçerli bir sayı girin.")
            return

        if s_id not in self.manager.students:
            messagebox.showerror("Hata", "Sistemde böyle bir Öğrenci ID bulunamadı! Önce öğrenciyi ekleyin.")
            return

        self.manager.add_grade_to_student(s_id, course, grade)
        messagebox.showinfo("Başarılı", f"{course} notu sisteme işlendi!")
        self.entry_course.delete(0, tk.END)
        self.entry_grade.delete(0, tk.END)

    def show_report(self):
        # Analiz modülünden rapor metnini al
        report_text = analyze_student_data()
        # Bu metni yeni bir bilgi penceresinde göster
        messagebox.showinfo("Sınıf Analiz Raporu", report_text)    

# Programı Çalıştıran Ana Döngü
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()