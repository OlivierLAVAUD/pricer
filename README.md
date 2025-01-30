# 📈 Assistant de marché avec LLM

Ce projet est une application Streamlit qui utilise **Alpha Vantage** pour récupérer les données de marché et **Ollama** (avec des modèles comme Mistral ou LLaMA) pour générer des analyses en langage naturel. L'application permet aux utilisateurs de saisir un symbole boursier et d'obtenir le dernier prix ainsi qu'une analyse technique.

![Assistant de marché avecLLM](image.png)

## Fonctionnalités

- **Récupération des prix de marché** : Utilise l'API Alpha Vantage pour obtenir les derniers prix des actions.
- **Analyse en langage naturel** : Utilise Ollama pour générer des analyses techniques basées sur les prix de marché.
- **Interface conviviale** : Une interface simple et intuitive construite avec Streamlit.


## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

1. **Python 3.8 ou supérieur** : Installé sur votre machine.
2. **Clé API Alpha Vantage** : Obtenez une clé API gratuite sur [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
3. **Ollama** : Installé et configuré sur votre machine. Téléchargez-le depuis [ollama.ai](https://ollama.ai).
4. **Modèle de langage** : Téléchargez un modèle compatible avec Ollama, comme Mistral ou LLaMA :
   ```bash
   ollama pull mistral

5. Clonez le dépôt :
    ```bash
    git clone https://github.com/OlivierLAVAUD/pricer.git
    cd pricer

6. Créez un environnement virtuel (optionnel mais recommandé) :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate

7. Installez les dépendances
    ```bash
    pip install -r requirements.txt


## Configuration
1.Configurez la clé API Alpha Vantage :

    Lorsque vous exécutez l'application, une zone de texte vous permettra de saisir votre clé API Alpha Vantage. (https://www.alphavantage.co/)

    Vous pouvez également définir la clé API dans un fichier .env (optionnel) :
    echo "ALPHA_VANTAGE_API_KEY=VOTRE_CLE_API" > .env

## Utilisation

1. Lancez l'application Streamlit :
     ```bash
    streamlit run app.py

2. Utilisez l'interface :

    Entrez votre clé API Alpha Vantage dans la zone prévue.

    Saisissez un symbole boursier (exemple : AAPL pour Apple, MSFT pour Microsoft, BTCUSD pour Bitcoin).

    Cliquez sur "Obtenir le prix et l'analyse".

    L'application affichera le dernier prix de l'action et une analyse générée par le LLM