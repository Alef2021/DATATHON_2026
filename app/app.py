import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Previsão de Risco Educacional", layout="centered")

st.title("📊 Modelo de Previsão de Risco Educacional")
st.write("Sistema preditivo para identificar alunos com risco de defasagem escolar.")

# carregar modelo
model = joblib.load("modelo_risco_random.pkl")

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
    
    probs = model.predict_proba(input_df)[0]
    prob_em_fase = probs[0]
    prob_moderado = probs[1]
    prob_severo = probs[2]

    pred = model.predict(input_df)[0]

    st.subheader("Resultado da previsão")

    if pred == 2:
        st.metric("Probabilidade de risco alto", f"{prob_severo*100:.1f}%")
    elif pred == 1:
        st.metric("Probabilidade de risco moderado", f"{prob_moderado*100:.1f}%")
    else:
        st.metric("Probabilidade de estar em fase", f"{prob_em_fase*100:.1f}%")

    if pred == 2:
        st.error("Aluno com ALTO risco de defasagem")
        st.write("👉 Recomenda-se acompanhamento pedagógico e psicossocial.")
    elif pred == 1:
        st.warning("Aluno com risco MODERADO de defasagem")
        st.write("👉 Recomenda-se acompanhamento regular.")
    else:
        st.success("Aluno fora da zona de risco de defasagem")
        st.write("👉 Manter acompanhamento regular.")