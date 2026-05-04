import json
import os
from student import Student

class GradeManager:
    def __init__(self, data_file="students_data.json"):
        self.data_file = data_file
        self.students = {}  # Öğrencileri ID'lerine göre burada tutacağız
        self.load_data()    # Program açıldığında eski verileri otomatik yükle

    def add_student(self, student_id, name):
        """Yeni öğrenci ekler ve kaydeder."""
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Başarılı: {name} (ID: {student_id}) sisteme eklendi.")
            self.save_data()
        else:
            print("Hata: Bu ID ile sisteme kayıtlı bir öğrenci zaten var!")

    def add_grade_to_student(self, student_id, course_name, grade):
        """Mevcut bir öğrenciye not ekler ve kaydeder."""
        if student_id in self.students:
            self.students[student_id].add_grade(course_name, grade)
            print(f"Not eklendi: {course_name} -> {grade}")
            self.save_data()
        else:
            print("Hata: Öğrenci bulunamadı!")

    def save_data(self):
        """Verileri JSON dosyasına kaydeder."""
        with open(self.data_file, 'w', encoding='utf-8') as file:
            # Tüm öğrenci nesnelerini to_dict() metoduyla sözlüğe çevirip JSON'a yazıyoruz
            data = {s_id: student.to_dict() for s_id, student in self.students.items()}
            json.dump(data, file, indent=4, ensure_ascii=False)

    def load_data(self):
        """JSON dosyasından eski verileri okur ve sisteme yükler."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for s_id, s_data in data.items():
                    # JSON'dan okunan verilerle Student nesnelerini tekrar oluştur
                    student = Student(s_id, s_data["Name"])
                    student.grades = s_data.get("Grades", {})
                    self.students[s_id] = student
            print("Sistem mesajı: Önceki kayıtlar başarıyla yüklendi.")

# Test Bloğu
if __name__ == "__main__":
    manager = GradeManager()
    
    # Sisteme yeni öğrenciler ekleyelim
    manager.add_student("101", "Ahmet Yılmaz")
    manager.add_student("102", "Ayşe Demir")
    
    # Not girelim
    manager.add_grade_to_student("101", "Advanced Python", 95)
    manager.add_grade_to_student("102", "Advanced Python", 88)