# app.py
import streamlit as st
from backend import get_stock_price, ask_ollama

# Configuration de l'interface utilisateur
def main():
    st.title("📈 Assistant de marché avec LLM")
    st.markdown("""
    Ce projet utilise **Alpha Vantage** pour récupérer les données de marché et **Ollama** pour générer des analyses en langage naturel.
    """)

    # Zone pour renseigner la clé API Alpha Vantage
    api_key = st.text_input("Entrez votre clé API Alpha Vantage :", type="password")

    # Entrée utilisateur pour le symbole boursier
    symbol = st.text_input("Entrez le symbole boursier (exemple : AAPL, MSFT, BTCUSD) :", "AAPL").upper()

    if st.button("Obtenir le prix et l'analyse"):
        if api_key and symbol:
            with st.spinner("Récupération des données en cours..."):
                try:
                    # Obtenir le prix de l'action
                    price = get_stock_price(symbol, api_key)
                    st.success(f"Le dernier prix de {symbol} est **{price} USD**.")

                    # Générer une analyse avec Ollama
                    prompt = f"""
                    Analysez le prix de l'action {symbol} qui est actuellement à {price} USD. 
                    Prenez en compte les éléments suivants :
                    - **Tendance** : Quelle est la direction générale du prix (hausse, baisse, ou stable) ?
                    - **Résistance** : Y a-t-il un niveau de résistance clé où le prix pourrait rencontrer des difficultés à monter ?
                    - **Faiblesse** : Y a-t-il un niveau de support où le prix pourrait rencontrer des difficultés à baisser ?

                    Donnez une analyse technique en 3-4 phrases.
                    """
                    response = ask_ollama(prompt)

                    if response:
                        st.markdown("### Analyse du LLM")
                        st.write(response)
                    else:
                        st.error("Erreur lors de la génération de l'analyse.")
                except Exception as e:
                    st.error(str(e))
        else:
            if not api_key:
                st.warning("Veuillez entrer une clé API Alpha Vantage valide.")
            if not symbol:
                st.warning("Veuillez entrer un symbole boursier valide.")

    # Instructions pour l'utilisateur
    st.markdown("""
    ### Instructions :
    1. Obtenez une clé API gratuite sur [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
    2. Entrez votre clé API ci-dessus.
    3. Entrez un symbole boursier valide (exemple : AAPL pour Apple, MSFT pour Microsoft, BTCUSD pour Bitcoin).
    4. Cliquez sur "Obtenir le prix et l'analyse".
    5. Attendez que le système récupère le prix et génère une analyse.
    """)

    # Footer
    st.markdown("---")
    st.markdown("**Technologies utilisées :** Alpha Vantage, Ollama (Mistral/LLaMA), Streamlit")

# Point d'entrée de l'application
if __name__ == "__main__":
    main()