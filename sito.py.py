import streamlit as st
#1.  st.title("Benvenuto nel mio primo sito web")
#2.  campi di input grafici (caselle di testo e numeri)
nome_utente = st.text_input("Nome utente")
# 3.  Usiamo un selettore numerico così l'utente non sbaglia a scrivere
età_utente = st.number_input("età utente", min_value=0, max_value=100, value=18)
# 4. Bottone per inviare i dati
if st.button ("verifica accesso"):
    if età_utente >= 18:
        st.success(f"Benvenuto {nome_utente}, puoi accedere al sito!")
    else:
        st.error(f"Mi dispiace {nome_utente}, devi avere almeno 18 anni per accedere al sito.")