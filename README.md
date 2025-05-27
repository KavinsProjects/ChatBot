# 🤖 Ollama Chatbot – Django Web Application

Welcome to the **Ollama Chatbot**, a private AI-powered chatbot built using **LLaMA 3.0** and Django. It runs fully offline using Ollama’s local LLM engine, making it fast, secure, and ideal for personal or experimental use.

---

## 🚀 Overview

This project combines:

- ⚙️ **Ollama (LLaMA 3.0)** – Local LLM runtime for intelligent text generation  
- 🌐 **Django** – Backend framework to manage logic and routes  
- 🎨 **HTML/CSS/JavaScript** – For a lightweight frontend chat interface  
- 🐍 **Python** – The programming core of both backend and integration

---

## 🌟 Key Features

- 📴 **Runs 100% Offline** – No API keys or internet required  
- 🔐 **Private by Design** – Your conversations never leave your device  
- ⚡ **Fast & Local** – Powered by LLaMA 3.0 via Ollama  
- 🧩 **Simple & Modular** – Easy to extend with new features

---

## 📂 Project Structure

```
CHATBOT/
├── chat/
│   ├── templates/chat/           # HTML for chat UI
│   │   └── index.html
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── chatbot_project/              # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3                    # SQLite database
├── manage.py                     # Django management tool
└── myvenv/                       # Virtual environment
```

---

## ⚙️ Prerequisites

### 🪟 Windows Setup

#### ✅ Install Python 3.10+
[Download from python.org](https://www.python.org/downloads/windows/)

#### ✅ Install Ollama with LLaMA 3.0
1. Visit [https://ollama.com](https://ollama.com) and download Ollama for Windows  
2. During setup, download the **LLaMA 3.0** model  
3. After installation, run the following in CMD/PowerShell:

```bash
ollama run llama3
```

---

## 🔧 Getting Started

1. **Open the project folder in VS Code**

2. **Create and activate a virtual environment**

```bash
python -m venv myvenv
myvenv\Scripts\activate
```

3. **Install Django**

```bash
pip install django
```

4. **Run database migrations**

```bash
python manage.py migrate
```

5. **Start the Django development server**

```bash
python manage.py runserver
```

6. **Run the LLaMA 3.0 model (in a separate terminal)**

```bash
ollama run llama3
```

7. Open your browser and go to:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧠 How It Works

- The user sends a message via the web chat interface  
- Django captures the message and sends it to the local Ollama API  
- LLaMA 3.0 processes the message and returns a response  
- The response is displayed back in the browser

---

## 💡 Tips & Improvements

- 💾 Save chat history using Django models  
- 🔐 Add authentication (login/signup)  
- 🎨 Style with Bootstrap or Tailwind CSS  
- 🎙️ Add voice input and output features  
- 🐳 Add Docker support for isolated deployments

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Author

Made with ❤️ by **Captain**  
Powered by [LLaMA 3.0](https://ollama.com/library/llama3) via [Ollama](https://ollama.com)
