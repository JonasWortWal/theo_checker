import requests
from config import KI_PROVIDER, API_KEY

def run_ki_analysis(transcript):
    prompt = f"Analysiere folgenden theologischen Text nach biblischer Wahrheit: {transcript}"
    try:
        if KI_PROVIDER == "openrouter":
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {API_KEY}"},
                json={
                    "model": "deepseek-chat",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 600
                }
            )
            return response.json()['choices'][0]['message']['content']
        else:
            return "Kein unterstützter KI-Anbieter konfiguriert."
    except Exception as e:
        return "Fehler bei der KI-Anfrage."