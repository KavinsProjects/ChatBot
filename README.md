# 🤖 Ollama Chatbot – Django Web Application

Welcome to the **Ollama Chatbot**, a locally-running AI chatbot powered by **Ollama's LLM engine** and the **Django web framework**. This project is designed to provide a seamless, private, and interactive conversational experience—right from your machine, without needing the internet or API keys.

---

## 🚀 Overview

This chatbot combines:

 **Ollama (LLaMA 3.0)** – Local LLM runtime for intelligent text generation.
- 🌐 **Django** – A robust backend framework for building dynamic web apps.
- 💡 **HTML/CSS/JS** – Clean, responsive UI for user interaction.
- 🐍 **Python** – The brain behind backend logic and integration.

---

## 🌟 Key Features

- 🔒 **Runs Locally** – No API keys or cloud models needed.
- 🛡️ **Private by Design** – All conversations stay on your device.
- ⚡ **Fast & Responsive** – Powered by Django and efficient model serving.
- 🧩 **Modular Codebase** – Easy to extend or plug into larger projects.

---

## 📂 Project Structure

CHATBOT/
├── chat/                          # Main app
│   ├── migrations/                # DB migrations
│   ├── templates/chat/           # HTML templates
│   │   └── index.html             # Chat UI page
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── chatbot_project/              # Django project config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Main settings file
│   ├── urls.py                   # Project URL config
│   └── wsgi.py
│
├── db.sqlite3                    # SQLite database
├── manage.py                     # Django management CLI
└── myvenv/                       # Python virtual environment



![Screenshot](https://github.com/user-attachments/assets/03c4599e-afcb-4512-b742-e2b573aa0450)

---

⚙️ Prerequisites

### 🪟 For Windows:

1. **Install Python 3.10+**  
   [Download Python for Windows](https://www.python.org/downloads/windows/)

2. **Install Ollama (Windows)**  
   Download from the official site: [https://ollama.com](https://ollama.com)

   After installation:
   - Open **Ollama app** 
   - Open terminal (PowerShell/CMD) and run:
   - type ollama
        

![WhatsApp Image 2025-05-27 at 12 59 05_a9d161c4](https://github.com/user-attachments/assets/b5e9dd4f-43a3-41ac-8316-1ffe86ee6161)

-Type ollama list
![image](https://github.com/user-attachments/assets/5cda1319-2364-48e2-9f88-88a29915d0e9)

🔧 Getting Started
Open the project folder in VS Code

Create and activate a virtual environment

bash
Copy
Edit
python -m venv myvenv
myvenv\Scripts\activate
Install Django

bash
Copy
Edit
pip install django
Run migrations

bash
Copy
Edit
python manage.py migrate
Start the development server

bash
Copy
Edit
python manage.py runserver
Start LLaMA 3.0 in a separate terminal

bash
Copy
Edit
ollama run llama3
Open your browser and go to:
👉 http://127.0.0.1:8000

