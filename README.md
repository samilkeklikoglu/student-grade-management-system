🎓 Student Grade Management System

Overview

A modern and robust desktop application for managing student records and academic performance. This project integrates graphical user interface design with data analysis to provide a professional educational tool.

🚀 Key Features

    Modern Interface: Built with CustomTkinter, offering a high-DPI, Dark Mode dashboard for a premium user experience.

    Data Analysis: Real-time statistics (Class Average, Max/Min grades) using the Pandas library.

    Data Persistence: Automatic synchronization with a JSON database—data is never lost when the app closes.

    Student Management: Complete control with the ability to Register, Add Grades, and Delete students securely.

📂 Project Architecture

    main.py: The GUI and main dashboard logic.

    manager.py: Business logic for managing student data and file I/O.

    data_analysis.py: Data processing engine for academic reporting.

    student.py: The core Object-Oriented model.

🛠️ Installation & Setup

To run this project locally, follow these steps:

    Install Python: Make sure you have Python 3.x installed on your system.

    Install Dependencies: pip install customtkinter pandas

    Run the Application: python main.py

📚 Tech Stack & Citations

    Language: Python 3.x

    UI: CustomTkinter (Modernized Tkinter elements)

    Analysis: Pandas (Data manipulation)

    Storage: JSON (Lightweight data persistence)