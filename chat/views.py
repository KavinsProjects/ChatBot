import requests
import json
from django.shortcuts import render

def chat_view(request):
    user_message = ""
    bot_reply = ""

    if request.method == "POST":
        user_message = request.POST.get("message")

        # Setup Ollama chat endpoint
        url = "http://localhost:11434/api/chat"
        payload = {
            "model": "mistral",  # You can change this to llama3, etc.
            "messages": [{"role": "user", "content": user_message}]
        }

        try:
            response = requests.post(url, json=payload, stream=True)
            if response.status_code == 200:
                bot_reply_parts = []
                for line in response.iter_lines(decode_unicode=True):
                    if line:
                        try:
                            json_data = json.loads(line)
                            if "message" in json_data and "content" in json_data["message"]:
                                bot_reply_parts.append(json_data["message"]["content"])
                        except json.JSONDecodeError:
                            pass
                bot_reply = ''.join(bot_reply_parts)
            else:
                bot_reply = f"⚠️ Error: {response.status_code}"
        except requests.exceptions.RequestException as e:
            bot_reply = f"⚠️ Connection error: {str(e)}"

    return render(request, "chat/index.html", {
        "user_message": user_message,
        "bot_reply": bot_reply
    })
