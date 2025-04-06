

```markdown
# 🎓 Teacher Assistant – Google Solution Challenge 2024

An AI-powered web platform built with Django and Google Generative AI to streamline exam evaluation — from uploading question papers to evaluating answer sheets and generating results. Developed as part of the **Google Solution Challenge 2024**.

🌐 **Live App**: [https://agreed-merna-hridhika-fcb1b031.koyeb.app](https://agreed-merna-hridhika-fcb1b031.koyeb.app)

---

## ✨ Features

- 🔐 **Role-Based Access** – Different interfaces for Teachers, Evaluators, and Students
- 📄 **Question Paper Upload** – Teachers upload question files and keys
- 📸 **Answer Sheet Upload** – Evaluators upload scanned sheets
- 🤖 **Auto Evaluation** – AI marks answers using Google GenAI and Sentence Transformers
- 📥 **Result Download** – Download evaluated responses with marks
- 🧠 **Minimal UI** – Clean, user-friendly design

---

## 🛠️ Tech Stack

- **Backend:** Django (Python 3.12)
- **AI/ML:** Google Generative AI, Sentence Transformers
- **Frontend:** Django Templates (HTML/CSS)
- **Image Processing:** Pillow
- **Database:** SQLite / PostgreSQL
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
sentence-transformers
psycopg2-binary
gunicorn
```

> 🔧 Python version: 3.12

---

## 📁 Project Structure

```
├── core/                 # Django app logic
├── templates/            # HTML template files
├── media/                # Uploaded answer sheets/results
├── static/               # CSS/JS assets
├── Pipfile / requirements.txt
└── manage.py
```

---

## 🚀 Future Enhancements

- 🧑‍🎓 Student dashboard for results
- 📊 Analytics for teachers
- 📎 PDF export of reports
- ✏️ AI feedback on answers

---

## 🧑‍💻 Author

Made with ❤️ by **Hridhika** for Google Solution Challenge 2024  
GitHub: [@hridhika](https://github.com/hridhika)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
```

---

Let me know if you want to include screenshots, badges, or contributor credits! We can make this README even more aesthetic and impactful 🌟
