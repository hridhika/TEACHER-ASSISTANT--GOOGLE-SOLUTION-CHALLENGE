
# 🎓 Teacher Assistant – Google Solution Challenge 2025

An AI-powered web platform built with Django and Google Generative AI to streamline exam evaluation — from uploading question papers to evaluating answer sheets and generating results. Developed as part of the **Google Solution Challenge 2025**.

🌐 **Live App**: [https://agreed-merna-hridhika-fcb1b031.koyeb.app](https://agreed-merna-hridhika-fcb1b031.koyeb.app)

---

## ✨ Features

- 🔐 **Role-Based Access** – Different interfaces for Teachers and Students
- 📄 **Question Paper Upload** – Teachers upload question keys
- 📸 **Answer Sheet Upload** –Students upload scanned sheets
- 🤖 **Auto Evaluation** – AI marks answers using Google GenAI
- 📥 **Result Download** – Download evaluated responses with marks
- 🧠 **Minimal UI** – Clean, user-friendly design

---

## 🛠️ Tech Stack

- **Backend:** Django (Python 3.12)
- **AI/ML:** Google Generative AI
- **Frontend:** Django Templates (HTML/CSS)
- **Image Processing:** Pillow
- **Database:** PostgreSQL
- **Deployment:** Koyeb + Gunicorn

---

## 💻 Local Setup

Follow the steps to run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/hridhika/TEACHER-ASSISTANT--GOOGLE-SOLUTION-CHALLENGE.git
cd TEACHER-ASSISTANT--GOOGLE-SOLUTION-CHALLENGE
```

### 2. Set Up Virtual Environment

Make sure [pipenv](https://pipenv.pypa.io/en/latest/) is installed:

```bash
pip install pipenv
pipenv shell
```

### 3. Install Dependencies

```bash
pipenv install
```

Or using pip directly:

```bash
pip install -r requirements.txt
```

### 4. Migrate the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 📦 Requirements (from `requirements.txt`)

```
Django
google-generativeai
pillow
psycopg2-binary
gunicorn
```

> 🔧 Python version: 3.12

---

## 📁 Project Structure

```
├── media/
├── Teacher/                 
├── teacherassist/          
├── templates/               
├── User/               
├── Pipfile / 
└── manage.py
```

---

## 🚀 Future Enhancements

-Manual Commenting Interface: Allow teachers to add notes/comments on specific student answers

-Analytics Dashboard: Visual insights like average scores, top performers, etc.

-Email Notifications: Notify students when results are published

---

## 🧑‍💻 Author

Made with ❤️ by **Anand, Hridhika, Raihan and Rishikesh** for Google Solution Challenge 2025

---

