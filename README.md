# 📊 DATATHON 2026 – Previsão de Risco Educacional  
### Case: Associação Passos Mágicos

Este projeto foi desenvolvido como parte do Datathon 2026 da Postech, utilizando dados reais da Associação Passos Mágicos, organização social que atua há mais de 30 anos na transformação da vida de crianças e jovens em vulnerabilidade por meio da educação.

O objetivo da solução é utilizar **Data Analytics e Machine Learning** para apoiar decisões pedagógicas e identificar precocemente alunos em risco de defasagem escolar.

---

## 🎯 Problema de Negócio

A Associação Passos Mágicos acompanha o desenvolvimento educacional de seus alunos por meio de indicadores multidimensionais, incluindo:

- Desempenho acadêmico  
- Engajamento escolar  
- Aspectos psicossociais  
- Avaliações psicopedagógicas  
- Percepção do próprio aluno  

O desafio do Datathon consiste em transformar esses dados em **insights acionáveis e soluções preditivas** que permitam:

- Identificar alunos em risco antes da queda de desempenho  
- Compreender fatores que influenciam a defasagem  
- Apoiar intervenções educacionais precoces  

---

## 🧠 Abordagem da Solução

A solução foi dividida em três etapas principais:

### 🔹 1. Engenharia e Limpeza de Dados

- União das bases históricas de 2022, 2023 e 2024  
- Padronização de indicadores educacionais  
- Tratamento de inconsistências  
- Seleção de variáveis relevantes  
- Normalização dos indicadores  

Essa etapa garantiu uma base consolidada e confiável para análise.

---

### 🔹 2. Modelagem Preditiva

#### 🎯 Definição da variável alvo

Foi criado um indicador de risco educacional:

Risco = 1 quando Defasagem < 0

Risco = 0 caso contrário


Ou seja, alunos com atraso educacional são classificados como risco.

---

#### 🔹 Indicadores utilizados no modelo

- **IDA** → desempenho acadêmico  
- **IEG** → engajamento escolar  
- **IPS** → contexto psicossocial  
- **IPP** → avaliação psicopedagógica  
- **IAA** → autoavaliação do aluno  
- **IPV** → ponto de virada educacional  
- **Idade** → fator demográfico  

Essas variáveis representam dimensões pedagógicas, emocionais e comportamentais do aluno.

---

#### 🔹 Modelos testados

Foram avaliados:

- Random Forest  
- XGBoost  
- Gradient Boosting  

O modelo **Random Forest** foi escolhido por apresentar:

- Melhor equilíbrio entre precisão e recall  
- Maior robustez a ruídos nos dados  
- Melhor identificação da classe de risco  

O modelo final foi serializado para uso em produção.

---

### 🔹 3. Aplicação Preditiva (Streamlit)

Foi desenvolvida uma aplicação interativa que permite:

- Inserir indicadores de um aluno manualmente  
- Calcular a probabilidade de risco educacional  
- Classificar automaticamente o aluno  
- Sugerir ações pedagógicas  

Isso transforma o modelo em uma ferramenta prática de apoio educacional.

---

## 🏗️ Arquitetura da Solução

Dados educacionais históricos
↓
Limpeza e padronização
↓
Feature Engineering
↓
Treinamento de modelos
↓
Escolha do melhor modelo
↓
Serialização do modelo
↓
Aplicação Streamlit
↓
Previsão de risco em tempo real


---

## 📊 Impacto Esperado

A solução permite:

- Identificação precoce de alunos em risco  
- Priorização de acompanhamento pedagógico  
- Apoio a decisões baseadas em dados  
- Redução de evasão e defasagem escolar  
- Maior eficiência do programa educacional  

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/Alef2021/DATATHON_2026.git
cd DATATHON_2026
```

### 2️⃣ Instalar dependências

- pip install -r requirements.txt

### 3️⃣ Executar aplicação

- streamlit run app/app.py

### 🛠️ Tecnologias Utilizadas

- Python

- Pandas

- Scikit-learn

- XGBoost

- Streamlit

- Joblib

- Jupyter Notebook

### 👨‍💻 Autor

- Projeto desenvolvido para o Datathon 2026 – Postech
- Case: Associação Passos Mágicos

- Solução focada em Data Science aplicada à educação e impacto social.