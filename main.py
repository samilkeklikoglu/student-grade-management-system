import customtkinter as ctk
from tkinter import messagebox
from manager import GradeManager
from data_analysis import get_analysis_data

# --- TEMA VE RENK AYARLARI ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ReportWindow(ctk.CTkToplevel):
    """Gelişmiş Akademik Analiz Raporu Penceresi"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("📊 Akademik Analiz Raporu")
        
        # Rapor penceresi boyutu
        self.geometry("850x800")
        self.attributes("-topmost", True)

        data = get_analysis_data()
        if not data:
            ctk.CTkLabel(self, text="Görüntülenecek veri bulunamadı!", font=("Arial", 18)).pack(pady=100)
            return

        # Üst İstatistik Paneli
        stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        stats_frame.pack(pady=20, padx=40, fill="x")

        # Ortalama Kartı
        avg_card = ctk.CTkFrame(stats_frame, fg_color="#34495e")
        avg_card.grid(row=0, column=0, padx=10, sticky="nsew")
        ctk.CTkLabel(avg_card, text="Sınıf Ortalaması", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(avg_card, text=data['stats']['avg'], font=("Arial", 30, "bold"), text_color="#f1c40f").pack(pady=5)

        # En Yüksek Not Kartı
        max_card = ctk.CTkFrame(stats_frame, fg_color="#34495e")
        max_card.grid(row=0, column=1, padx=10, sticky="nsew")
        ctk.CTkLabel(max_card, text="En Yüksek Not", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(max_card, text=data['stats']['max'], font=("Arial", 30, "bold"), text_color="#2ecc71").pack(pady=5)

        stats_frame.grid_columnconfigure((0, 1), weight=1)

        # Liste Bölümü
        ctk.CTkLabel(self, text="Öğrenci Kayıtları", font=("Arial", 22, "bold")).pack(pady=10)

        self.scroll_table = ctk.CTkScrollableFrame(self, width=750, height=450)
        self.scroll_table.pack(padx=30, pady=10, fill="both", expand=True)

        id_w, name_w, gpa_w = 100, 350, 100

        # Tablo Başlığı
        header = ctk.CTkFrame(self.scroll_table, fg_color="#2c3e50")
        header.pack(fill="x", pady=2)
        ctk.CTkLabel(header, text="ID", width=id_w, font=("Arial", 14, "bold")).grid(row=0, column=0)
        ctk.CTkLabel(header, text="Ad Soyad", width=name_w, font=("Arial", 14, "bold"), anchor="w", padx=20).grid(row=0, column=1)
        ctk.CTkLabel(header, text="GPA", width=gpa_w, font=("Arial", 14, "bold")).grid(row=0, column=2)

        # Veri Satırları
        for _, row in data['df'].iterrows():
            r_frame = ctk.CTkFrame(self.scroll_table)
            r_frame.pack(fill="x", pady=2)
            ctk.CTkLabel(r_frame, text=row['Student ID'], width=id_w).grid(row=0, column=0)
            ctk.CTkLabel(r_frame, text=row['Name'], width=name_w, anchor="w", padx=20).grid(row=0, column=1)
            ctk.CTkLabel(r_frame, text=f"{row['GPA']:.2f}", width=gpa_w, font=("Arial", 14, "bold")).grid(row=0, column=2)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.manager = GradeManager()
        
        # Dinamik Ekran Ölçeklendirme
        s_width = self.winfo_screenwidth()
        s_height = self.winfo_screenheight()
        
        # Pencere boyutlarını ekranın %85'ine göre ayarla (Maks 1000x900)
        w_width = min(1000, int(s_width * 0.85))
        w_height = min(900, int(s_height * 0.85))
        
        self.title("Student Grade Management System v2.0")
        self.geometry(f"{w_width}x{w_height}")
        
        # Ana Kaydırılabilir Konteynır (Her ekran boyutuna uyum için)
        self.main_container = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Başlık
        self.label_title = ctk.CTkLabel(self.main_container, text="🎓 Öğrenci Yönetim Paneli", font=("Roboto", 36, "bold"))
        self.label_title.pack(pady=(10, 30))

        # 1. ÖĞRENCİ EKLEME
        self.frame_add = ctk.CTkFrame(self.main_container)
        self.frame_add.pack(padx=40, pady=10, fill="x")
        ctk.CTkLabel(self.frame_add, text="Yeni Öğrenci Kaydı", font=("Arial", 20, "bold")).pack(pady=15)
        
        self.entry_id = ctk.CTkEntry(self.frame_add, placeholder_text="Öğrenci ID", width=400, height=45, font=("Arial", 16))
        self.entry_id.pack(pady=5)
        self.entry_name = ctk.CTkEntry(self.frame_add, placeholder_text="Ad Soyad", width=400, height=45, font=("Arial", 16))
        self.entry_name.pack(pady=5)
        
        self.btn_add_student = ctk.CTkButton(self.frame_add, text="Sisteme Kaydet", command=self.add_student, 
                                             width=250, height=55, font=("Arial", 18, "bold"),
                                             fg_color="#2ecc71", hover_color="#27ae60")
        self.btn_add_student.pack(pady=20)

        # 2. NOT GİRİŞİ
        self.frame_grade = ctk.CTkFrame(self.main_container)
        self.frame_grade.pack(padx=40, pady=10, fill="x")
        ctk.CTkLabel(self.frame_grade, text="Ders Notu Girişi", font=("Arial", 20, "bold")).pack(pady=15)

        g_grid = ctk.CTkFrame(self.frame_grade, fg_color="transparent")
        g_grid.pack(pady=5)
        self.entry_grade_id = ctk.CTkEntry(g_grid, placeholder_text="ID", width=100, height=45, font=("Arial", 16))
        self.entry_grade_id.grid(row=0, column=0, padx=10)
        self.entry_course = ctk.CTkEntry(g_grid, placeholder_text="Ders Adı", width=220, height=45, font=("Arial", 16))
        self.entry_course.grid(row=0, column=1, padx=10)
        self.entry_grade = ctk.CTkEntry(g_grid, placeholder_text="Not", width=80, height=45, font=("Arial", 16))
        self.entry_grade.grid(row=0, column=2, padx=10)

        self.btn_save_grade = ctk.CTkButton(self.frame_grade, text="Notu İşle", command=self.add_grade, 
                                            width=250, height=55, font=("Arial", 18, "bold"))
        self.btn_save_grade.pack(pady=20)

        # 3. KAYIT SİLME
        self.frame_delete = ctk.CTkFrame(self.main_container)
        self.frame_delete.pack(padx=40, pady=10, fill="x")
        ctk.CTkLabel(self.frame_delete, text="Kayıt Silme", font=("Arial", 18, "bold"), text_color="#e74c3c").pack(pady=10)
        
        d_inner = ctk.CTkFrame(self.frame_delete, fg_color="transparent")
        d_inner.pack(pady=10)
        self.entry_delete_id = ctk.CTkEntry(d_inner, placeholder_text="Öğrenci ID", width=200, height=45, font=("Arial", 16))
        self.entry_delete_id.grid(row=0, column=0, padx=10)
        self.btn_delete = ctk.CTkButton(d_inner, text="Kayıttan Sil", command=self.confirm_delete, 
                                        width=150, height=45, font=("Arial", 16, "bold"),
                                        fg_color="#e74c3c", hover_color="#c0392b")
        self.btn_delete.grid(row=0, column=1, padx=10)

        # 4. ANALİZ BUTONU
        self.btn_report = ctk.CTkButton(self.main_container, text="📊 Akademik Analiz Raporunu Görüntüle", 
                                        command=self.show_report, 
                                        width=500, height=75, 
                                        fg_color="#e67e22", hover_color="#d35400",
                                        font=("Arial", 22, "bold"))
        self.btn_report.pack(pady=40)

    # --- FONKSİYONLAR ---
    def add_student(self):
        s_id, name = self.entry_id.get(), self.entry_name.get()
        if not s_id or not name:
            messagebox.showwarning("Eksik Veri", "Lütfen tüm alanları doldurun.")
            return
        self.manager.add_student(s_id, name)
        messagebox.showinfo("Başarılı", f"{name} sisteme eklendi.")
        self.entry_id.delete(0, 'end'); self.entry_name.delete(0, 'end')

    def add_grade(self):
        s_id, crs, grd = self.entry_grade_id.get(), self.entry_course.get(), self.entry_grade.get()
        try:
            self.manager.add_grade_to_student(s_id, crs, float(grd))
            messagebox.showinfo("Başarılı", "Not başarıyla kaydedildi.")
            self.entry_grade.delete(0, 'end')
        except:
            messagebox.showerror("Hata", "Geçersiz giriş! ID ve Notu kontrol edin.")

    def confirm_delete(self):
        s_id = self.entry_delete_id.get()
        if not s_id: return
        if messagebox.askyesno("Onay", f"{s_id} ID'li kayıt kalıcı olarak silinecektir. Emin misiniz?"):
            if self.manager.delete_student(s_id):
                messagebox.showinfo("Başarılı", "Öğrenci silindi.")
                self.entry_delete_id.delete(0, 'end')
            else:
                messagebox.showerror("Hata", "Bu ID ile kayıtlı öğrenci bulunamadı.")

    def show_report(self):
        if hasattr(self, "report_win") and self.report_win.winfo_exists():
            self.report_win.focus()
        else:
            self.report_win = ReportWindow(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()