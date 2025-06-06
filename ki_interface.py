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
                    "model": "openrouter/deepseek-chat",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 600
                }
            )
            data = response.json()
            if "error" in data:
                return f"[KI-Fehler: {data['error']['message']}]"
            return data['choices'][0]['message']['content']
        else:
            return "Kein unterstützter KI-Anbieter konfiguriert."
    except Exception as e:
        return f"[Technischer Fehler bei KI-Abfrage: {str(e)}]"
