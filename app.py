import streamlit as st
from utils import parser, templates

from models.model import optimize_cv, api_query

api_key = 'AIzaSyB3YWa0LLWwymJtQWkvBc6kX0Ld7vYhGHc'

st.image("assets/Logo_gruppo.jpeg", width=150)
st.title("🧠 CV Agent")
st.subheader("Il tuo alleato per creare un curriculum perfetto, per il lavoro dei tuoi sogni!")

uploaded_cv = st.file_uploader("📄 Carica il tuo CV (PDF)", type=["pdf"])
job_description = st.text_area("💼 Inserisci la descrizione della posizione lavorativa")

if st.button("🚀 Ottimizza CV"):
    if uploaded_cv and job_description:
        #original_text = parser.extract_text(uploaded_cv)
        #optimized_cv = optimize_cv(original_text, job_description)
        response = api_query(api_key, "Crea un curriculum vitae ottimizzato per la posizione di Data Scientist con 5 anni di esperienza in Python e Machine Learning. Includi le competenze richieste e i risultati ottenuti in progetti precedenti.")
        st.success("✅ CV Ottimizzato!")
        st.download_button("📥 Scarica CV Ottimizzato", templates.generate_pdf(response), file_name="CV_Ottimizzato.pdf")
    else:
        st.error("Carica il CV e inserisci la descrizione del lavoro.")


