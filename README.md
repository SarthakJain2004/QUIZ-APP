# 🎯 Django Quiz App

A web-based **Quiz Application** built with **Django**.  
This app allows users to attempt quizzes, view results, and manage questions via the Django admin panel.  

---

## 📑 Table of Contents
- [About](#-about)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Contributing](#-contributing)

---

## 📖 About

The **Django Quiz App** is designed for students and educators.  
It allows:
- Admins to create and manage quizzes
- Users to attempt quizzes with multiple-choice questions
- Instant score calculation  

This project is perfect for learning Django fundamentals like **models, views, templates, static files, and authentication**.

---

## 🚀 Features

- 🔐 User authentication (Login, Logout, Signup if enabled)  
- 📝 Admin can add quizzes & questions via **Django Admin Panel**  
- 🎮 Users can attempt quizzes with MCQs  
- 📊 Auto-calculated results and score tracking  
- 🎨 Responsive UI with static files (CSS, JS)  
- 🛠️ Easy customization and scalability  

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, JS (Bootstrap) 
- **Database:** SQLite (default)   
- **Environment:** Virtualenv  

---

## 📂 Project Structure
```
QUIZ_APP/
│── core/ # Main app (quiz logic)
│ ├── init.py
│ ├── admin.py # Admin configurations
│ ├── apps.py # App configuration
│ ├── migrations/ # Database migrations
│ ├── models.py # Database models
│ ├── tests.py # Test cases
│ └── views.py # Views (Quiz rendering, results, etc.)
│
│── quiz_project/ # Project settings
│ ├── init.py
│ ├── asgi.py # ASGI entry point
│ ├── settings.py # Project settings
│ ├── urls.py # URL routing
│ └── wsgi.py # WSGI entry point
│
│── static/ # Static files (CSS, JS)
│ └── core/
│ ├── css/
│ └── js/
│
│── templates/ # HTML templates
│ └── core/
│ └── base.html
│
│── .gitignore # Git ignore file
│── db.sqlite3 # SQLite database
│── manage.py # Django management file

```
---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-quiz-app.git
   cd django-quiz-app
2. **Create and activate virtual environment**
   ```bash
    python -m venv venv
   source venv/bin/activate    # On Mac/Linux
   venv\Scripts\activate       # On Windows
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
4. **Apply migrations**
   python manage.py migrate
5. **Create superuser (for admin access)**
    ```bash
    python manage.py migrate
6. **Run development server**
    ```bash
    python manage.py createsuperuser
7. **Open in browser** → http://127.0.0.1:8000/

---

## ▶️ Usage
- Visit /admin/ → login with superuser → create quizzes & questions
- Visit / → take quizzes as a user
- Results appear instantly after submission

---

## 🤝 Contributing
Pull requests are welcome!
If you’d like to contribute, fork this repo and create a feature branch.
