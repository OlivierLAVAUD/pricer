# backend.py
import requests
import subprocess

# Fonction pour obtenir le dernier prix d'une action
def get_stock_price(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if "Global Quote" in data and "05. price" in data["Global Quote"]:
        price = data["Global Quote"]["05. price"]
        return price
    else:
        raise ValueError(f"Impossible de récupérer le prix pour {symbol}. Vérifiez le symbole ou votre clé API.")

# Fonction pour interroger Ollama
def ask_ollama(prompt, model="llama3.2"):
    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],  # Utilisez le modèle de votre choix (mistral, llama3.2, etc.)
            capture_output=True, text=True, encoding="utf-8"
        )
        return result.stdout
    except Exception as e:
        raise RuntimeError(f"Erreur lors de l'interrogation du modèle Ollama : {e}")