import customtkinter as ctk
from tkinter import messagebox
from manager import GradeManager
from data_analysis import get_analysis_data

# --- GÖRSEL TEMA AYARLARI ---
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue") 

class ReportWindow(ctk.CTkToplevel):
    """Hizalanmış Akademik Analiz Raporu Penceresi"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("📊 Akademik Analiz Raporu")
        self.geometry("800x850")
        self.attributes("-topmost", True)

        data = get_analysis_data()
        if not data:
            ctk.CTkLabel(self, text="Görüntülenecek veri bulunamadı!", font=("Arial", 20)).pack(pady=100)
            return

        # 1. Dashboard (Üst Özet Paneli)
        stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        stats_frame.pack(pady=30, padx=40, fill="x")

        avg_card = ctk.CTkFrame(stats_frame, fg_color="#34495e", height=140)
        avg_card.grid(row=0, column=0, padx=15, sticky="nsew")
        ctk.CTkLabel(avg_card, text="Sınıf Ortalaması", font=("Arial", 18)).pack(pady=15)
        ctk.CTkLabel(avg_card, text=data['stats']['avg'], font=("Arial", 36, "bold"), text_color="#f1c40f").pack(pady=10)

        max_card = ctk.CTkFrame(stats_frame, fg_color="#34495e", height=140)
        max_card.grid(row=0, column=1, padx=15, sticky="nsew")
        ctk.CTkLabel(max_card, text="En Yüksek Not", font=("Arial", 18)).pack(pady=15)
        ctk.CTkLabel(max_card, text=data['stats']['max'], font=("Arial", 36, "bold"), text_color="#2ecc71").pack(pady=10)

        stats_frame.grid_columnconfigure((0, 1), weight=1)

        # 2. Liste ve Hizalı Tablo
        ctk.CTkLabel(self, text="Öğrenci Kayıtları", font=("Arial", 24, "bold")).pack(pady=(10, 5))

        self.scroll_frame = ctk.CTkScrollableFrame(self, width=700, height=450)
        self.scroll_frame.pack(padx=40, pady=20, fill="both", expand=True)

        id_w, name_w, gpa_w = 120, 380, 120

        header_frame = ctk.CTkFrame(self.scroll_frame, fg_color="#2c3e50", height=60)
        header_frame.pack(fill="x", pady=5)
        ctk.CTkLabel(header_frame, text="ID", width=id_w, font=("Arial", 15, "bold"), anchor="center").grid(row=0, column=0)
        ctk.CTkLabel(header_frame, text="Ad Soyad", width=name_w, font=("Arial", 15, "bold"), anchor="w", padx=30).grid(row=0, column=1)
        ctk.CTkLabel(header_frame, text="GPA", width=gpa_w, font=("Arial", 15, "bold"), anchor="center").grid(row=0, column=2)

        for _, row in data['df'].iterrows():
            row_frame = ctk.CTkFrame(self.scroll_frame, height=55)
            row_frame.pack(fill="x", pady=3)
            ctk.CTkLabel(row_frame, text=row['Student ID'], width=id_w, font=("Arial", 14), anchor="center").grid(row=0, column=0)
            ctk.CTkLabel(row_frame, text=row['Name'], width=name_w, font=("Arial", 14), anchor="w", padx=30).grid(row=0, column=1)
            ctk.CTkLabel(row_frame, text=f"{row['GPA']:.2f}", width=gpa_w, font=("Arial", 15, "bold"), anchor="center").grid(row=0, column=2)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.manager = GradeManager()
        
        self.title("Student Grade Management System v2.0")
        # Yüksekliği 950 yaparak her şeyin sığmasını sağlıyoruz
        self.geometry("1000x950") 
        self.resizable(False, False)

        # Ana Başlık
        self.label_title = ctk.CTkLabel(self, text="🎓 Öğrenci Yönetim Paneli", font=("Roboto", 42, "bold"))
        self.label_title.pack(pady=(30, 20))

        # 1. ÖĞRENCİ EKLEME BÖLÜMÜ
        self.frame_add = ctk.CTkFrame(self)
        self.frame_add.pack(padx=60, pady=10, fill="x")
        ctk.CTkLabel(self.frame_add, text="Yeni Öğrenci Kaydı", font=("Arial", 22, "bold")).pack(pady=(15, 10))
        
        self.entry_id = ctk.CTkEntry(self.frame_add, placeholder_text="Öğrenci ID", width=550, height=50, font=("Arial", 17))
        self.entry_id.pack(pady=5)
        self.entry_name = ctk.CTkEntry(self.frame_add, placeholder_text="Ad Soyad", width=550, height=50, font=("Arial", 17))
        self.entry_name.pack(pady=5)
        
        self.btn_add_student = ctk.CTkButton(self.frame_add, text="Sisteme Kaydet", command=self.add_student, 
                                             width=300, height=60, font=("Arial", 20, "bold"),
                                             fg_color="#2ecc71", hover_color="#27ae60")
        self.btn_add_student.pack(pady=15)

        # 2. NOT GİRİŞ BÖLÜMÜ
        self.frame_grade = ctk.CTkFrame(self)
        self.frame_grade.pack(padx=60, pady=10, fill="x")
        ctk.CTkLabel(self.frame_grade, text="Ders Notu Girişi", font=("Arial", 22, "bold")).pack(pady=(15, 10))

        input_grid = ctk.CTkFrame(self.frame_grade, fg_color="transparent")
        input_grid.pack(pady=5)
        self.entry_grade_id = ctk.CTkEntry(input_grid, placeholder_text="ID", width=120, height=50, font=("Arial", 17))
        self.entry_grade_id.grid(row=0, column=0, padx=10)
        self.entry_course = ctk.CTkEntry(input_grid, placeholder_text="Ders Adı", width=280, height=50, font=("Arial", 17))
        self.entry_course.grid(row=0, column=1, padx=10)
        self.entry_grade = ctk.CTkEntry(input_grid, placeholder_text="Not", width=100, height=50, font=("Arial", 17))
        self.entry_grade.grid(row=0, column=2, padx=10)

        self.btn_save_grade = ctk.CTkButton(self.frame_grade, text="Notu İşle", command=self.add_grade, 
                                            width=300, height=60, font=("Arial", 20, "bold"))
        self.btn_save_grade.pack(pady=15)

        # 3. ÖĞRENCİ SİLME BÖLÜMÜ
        self.frame_delete = ctk.CTkFrame(self)
        self.frame_delete.pack(padx=60, pady=10, fill="x")
        ctk.CTkLabel(self.frame_delete, text="Kayıt Silme", font=("Arial", 20, "bold"), text_color="#e74c3c").pack(pady=(10, 5))
        
        delete_inner = ctk.CTkFrame(self.frame_delete, fg_color="transparent")
        delete_inner.pack(pady=10)
        
        self.entry_delete_id = ctk.CTkEntry(delete_inner, placeholder_text="Öğrenci ID", width=250, height=50, font=("Arial", 17))
        self.entry_delete_id.grid(row=0, column=0, padx=10)

        self.btn_delete = ctk.CTkButton(delete_inner, text="Kayıttan Sil", command=self.confirm_delete, 
                                        width=200, height=50, font=("Arial", 18, "bold"),
                                        fg_color="#e74c3c", hover_color="#c0392b")
        self.btn_delete.grid(row=0, column=1, padx=10)

        # 4. BÜYÜK ANALİZ BUTONU (Geri Geldi!)
        self.btn_report = ctk.CTkButton(self, text="📊 Akademik Analiz Raporunu Görüntüle", 
                                        command=self.show_report, 
                                        width=700, height=80, 
                                        fg_color="#e67e22", hover_color="#d35400",
                                        font=("Arial", 24, "bold"))
        self.btn_report.pack(pady=(20, 30))

    def add_student(self):
        s_id, name = self.entry_id.get(), self.entry_name.get()
        if not s_id or not name:
            messagebox.showwarning("Hata", "Alanlar boş bırakılamaz!")
            return
        self.manager.add_student(s_id, name)
        messagebox.showinfo("Başarılı", f"{name} sisteme eklendi.")
        self.entry_id.delete(0, 'end'); self.entry_name.delete(0, 'end')

    def add_grade(self):
        s_id, course, grade = self.entry_grade_id.get(), self.entry_course.get(), self.entry_grade.get()
        try:
            self.manager.add_grade_to_student(s_id, course, float(grade))
            messagebox.showinfo("Başarılı", "Not kaydedildi.")
            self.entry_grade.delete(0, 'end')
        except:
            messagebox.showerror("Hata", "Giriş yapılamadı. Bilgileri kontrol edin.")

    def confirm_delete(self):
        s_id = self.entry_delete_id.get()
        if not s_id: return
        confirm = messagebox.askyesno("Onay", f"{s_id} ID'li öğrenci silinsin mi?")
        if confirm:
            if self.manager.delete_student(s_id):
                messagebox.showinfo("Başarılı", "Öğrenci silindi.")
                self.entry_delete_id.delete(0, 'end')
            else:
                messagebox.showerror("Hata", "ID bulunamadı.")

    def show_report(self):
        if hasattr(self, "report_win") and self.report_win.winfo_exists():
            self.report_win.focus()
        else:
            self.report_win = ReportWindow(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()