🤖 Ollama Chatbot with
Django Web Application
chatbot, built using Ollama for language modeling and Django for a seamless web experience. 
 AI chatbot built using the power of Ollama's local large language models and the robustness of the Django web framework.

</> Tech Stack
Ollama – Local LLM runtime engine
Django – Backend and web framework
HTML/CSS/JS – Frontend technologies
Python – Core scripting and backend logic


🌟 What's Special
⚝ Runs Locally: No API keys, no internet required — everything works right on your machine.
⚝ All conversations stay with you.
⚝ Built with Django


📂 Project Structure

CHATBOT/
├── chat/                         # Main Django app
│   ├── migrations/
│   ├── templates/chat/
│   │   └── index.html            # Chat UI
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py                  # Handles chat logic
│
├── chatbot_project/              # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Project configuration
│   ├── urls.py
│   └── wsgi.py
│
├── myvenv/                       # Virtual environment
├── db.sqlite3                    # SQLite database
└── manage.py                     # Django CLI utility

thanks


Prerequisites
Python 3.10+
Django (version used: 4.x recommended)
Ollama installed and running locally


