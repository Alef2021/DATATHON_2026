import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Previsão de Risco Educacional", layout="centered")

st.title("📊 Modelo de Previsão de Risco Educacional")
st.write("Sistema preditivo para identificar alunos com risco de defasagem escolar.")

# carregar modelo
model = joblib.load(r"C:\Users\Igor\Documents\GitHub\DATATHON_2026\DATATHON_2026\app\modelo_risco_random.pkl")

st.header("📥 Inserir dados do aluno")

col1, col2 = st.columns(2)

with col1:
    IDA = st.number_input("IDA - Desempenho Acadêmico", 0.0, 10.0, 5.0)
    IEG = st.number_input("IEG - Engajamento", 0.0, 10.0, 5.0)
    IPS = st.number_input("IPS - Psicossocial", 0.0, 10.0, 5.0)
    IPP = st.number_input("IPP - Psicopedagógico", 0.0, 10.0, 5.0)

with col2:
    IAA = st.number_input("IAA - Autoavaliação", 0.0, 10.0, 5.0)
    IPV = st.number_input("IPV - Ponto de Virada", 0.0, 10.0, 5.0)
    Idade = st.number_input("Idade", 6, 25, 12)

input_df = pd.DataFrame({
    'IDA':[IDA],
    'IEG':[IEG],
    'IPS':[IPS],
    'IPP':[IPP],
    'IAA':[IAA],
    'IPV':[IPV],
    'Idade':[Idade]
})

st.divider()

if st.button("🔎 Calcular risco"):
    
    prob = model.predict_proba(input_df)[0][1]
    pred = model.predict(input_df)[0]

    st.subheader("Resultado da previsão")

    st.metric("Probabilidade de risco", f"{prob*100:.1f}%")

    if pred == 1:
        st.error("Aluno com ALTO risco de defasagem")
        st.write("👉 Recomenda-se acompanhamento pedagógico e psicossocial.")
    else:
        st.success("Aluno fora da zona de risco")
        st.write("👉 Manter acompanhamento regular.")