import streamlit as st
from utils import parser, templates

from models.model import optimize_cv

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


st.image("assets/Logo_gruppo.jpeg", width=150)
st.title("🧠 CV Agent")
st.subheader("Il tuo alleato per creare un curriculum perfetto, per il lavoro dei tuoi sogni!")

uploaded_cv = st.file_uploader("📄 Carica il tuo CV (PDF)", type=["pdf"])
job_description = st.text_area("💼 Inserisci la descrizione della posizione lavorativa")

if st.button("🚀 Ottimizza CV"):
    if uploaded_cv and job_description:
        original_text = parser.extract_text(uploaded_cv)
        optimized_cv = optimize_cv(original_text, job_description, api_key)      
        st.success("✅ CV Ottimizzato!")
        st.download_button("📥 Scarica CV Ottimizzato", templates.generate_txt(optimized_cv), file_name="CV_Ottimizzato.pdf", mime="application/pdf")
    else:
        st.error("Carica il CV e inserisci la descrizione del lavoro.")


