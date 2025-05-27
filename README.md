# 🤖 Ollama Chatbot – Django Web Application

Welcome to the **Ollama Chatbot**, a locally-running AI chatbot powered by **Ollama's LLM engine** and the **Django web framework**. This project is designed to provide a seamless, private, and interactive conversational experience—right from your machine, without needing the internet or API keys.

---

## 🚀 Overview

This chatbot combines:

- ⚙️ **Ollama** – A local LLM runtime to process natural language.
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

## ⚙️ Prerequisites

Before you begin, ensure the following are installed:

- ✅ Python 3.10+
- ✅ Django 4.x (recommended)
- ✅ Ollama (installed and running locally)

---
