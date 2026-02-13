# 🔐 Secure Login System with Password Hashing

## 📌 Project Overview
This project is a Secure Login System developed using Flask and SQLite.  
It demonstrates important cybersecurity concepts like password hashing and brute-force attack prevention.

---

## 🚀 Features
- User Registration System
- Secure Password Hashing using bcrypt
- Login Authentication
- Brute Force Protection (Account locks after 3 failed attempts)
- Secure Session Handling
- Modern User Interface

---

## 🛠 Technologies Used
- Frontend: HTML, CSS
- Backend: Python (Flask)
- Database: SQLite
- Security: bcrypt password hashing

---

## 🔐 Cybersecurity Concepts Implemented
- Password Hashing
- Authentication & Authorization
- Brute Force Attack Prevention
- Secure Data Storage
- Session Management

---

## ⚙️ Installation & Setup

1. Clone or download the project.
2. Install dependencies:
pip install -r requirements.txt
3. Run the application:
python app.py or py app.py
4. Open in browser:
http://127.0.0.1:5000

---

## 🧪 How It Works
- User registers with username and password.
- Password is hashed using bcrypt before storing in database.
- During login, hashed password is verified.
- After 3 failed login attempts, account gets locked.

---

## 📈 Future Enhancements
- Two-Factor Authentication (2FA)
- CAPTCHA integration
- Email alerts on suspicious login
- Password reset system
- Admin monitoring panel

---

## 🎯 Conclusion
This project demonstrates practical implementation of cybersecurity fundamentals in a web authentication system. It provides a foundation for building secure web applications.
