class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}  # Ders ve not eşleşmelerini tutacak sözlük (dictionary)

    def add_grade(self, course_name, grade):
        """Öğrenciye belirli bir ders için not ekler."""
        self.grades[course_name] = float(grade)

    def calculate_gpa(self):
        """Öğrencinin not ortalamasını otomatik hesaplar."""
        if not self.grades:
            return 0.0
        
        total_score = sum(self.grades.values())
        return round(total_score / len(self.grades), 2)

    def to_dict(self):
        """Verilerin JSON veya CSV'ye kolayca kaydedilmesi için sözlük formatına çevirir."""
        return {
            "Student ID": self.student_id,
            "Name": self.name,
            "Grades": self.grades,
            "GPA": self.calculate_gpa()
        }

# Test etmek için ufak bir kod bloğu
if __name__ == "__main__":
    test_student = Student("101", "Ahmet Yılmaz")
    test_student.add_grade("Math", 85)
    test_student.add_grade("Physics", 90)
    
    print(f"Öğrenci: {test_student.name}")
    print(f"Notlar: {test_student.grades}")
    print(f"Ortalama: {test_student.calculate_gpa()}")
    print(f"Kayıt Formatı: {test_student.to_dict()}")