# 📊 DATATHON 2026 --- Previsão de Risco Educacional

### Case: Associação Passos Mágicos

Este projeto foi desenvolvido como parte do Datathon 2026 da Postech,
com o objetivo de utilizar dados educacionais reais para identificar
alunos em risco de defasagem e apoiar decisões pedagógicas baseadas em
dados.

A solução combina análise exploratória, modelagem preditiva e uma
aplicação interativa para uso prático pela instituição.

------------------------------------------------------------------------

# 🌐 Aplicação Online

A solução completa de **Machine Learning** foi implantada e está disponível para uso imediato através do link abaixo:

👉 **[Acessar Plataforma de Previsão de Risco – Datathon 2026](https://alefdatathon2026.streamlit.app/)**


### 📋 Passo a Passo para Uso:

1.  **Acesso ao App:** Clique no link acima. Caso a aplicação esteja em **modo de hibernação** (comum em hospedagens gratuitas após inatividade), basta clicar no botão de confirmação (**"Yes, get this app back up!"**) e aguardar cerca de 30 segundos para o carregamento do ambiente e do modelo.
2.  **Inserção de Indicadores:** No painel lateral ou central, preencha os dados multidimensionais do aluno:
    * **IDA:** Desempenho Acadêmico.
    * **IEG:** Engajamento Escolar.
    * **IPS:** Contexto Psicossocial.
    * **IPP:** Avaliação Psicopedagógica.
    * **IAA:** Autoavaliação do Aluno.
    * **IPV:** Ponto de Virada.
    * **IDADE:** Idade.
3.  **Processamento:** O modelo **Random Forest** analisará os dados em tempo real, cruzando os indicadores comportamentais e pedagógicos para identificar padrões de risco.
4.  **Resultado e Insights:** A aplicação retornará a **Probabilidade de Risco (0-100%)** e uma classificação sugerindo o nível de intervenção pedagógica necessária.

------------------------------------------------------------------------

# 🎯 Objetivo do Projeto

-   Identificar alunos em risco de defasagem educacional
-   Entender fatores que influenciam desempenho e engajamento
-   Apoiar intervenções pedagógicas antecipadas
-   Transformar dados educacionais em ações concretas

------------------------------------------------------------------------

# 🧠 Abordagem da Solução

## 🔹 Preparação dos Dados

-   Consolidação das bases de 2022, 2023 e 2024\
-   Padronização de indicadores educacionais\
-   Tratamento de valores ausentes\
-   Seleção de variáveis relevantes

------------------------------------------------------------------------

## 🔹 Modelagem Preditiva

O problema foi tratado como uma classificação multiclasses:

-   0 → Em fase (sem risco)\
-   1 → Risco moderado\
-   2 → Risco severo

Foram testados três algoritmos principais.

------------------------------------------------------------------------

# 📈 Resultados dos Modelos

## 🌲 Random Forest

Accuracy: **0.74**\
Macro F1: **0.65**

Modelo equilibrado entre classes e com melhor capacidade de
identificação de alunos em risco.

## ⚡ XGBoost

Accuracy: **0.76**\
Macro F1: **0.56**

Apesar da maior acurácia, apresentou baixa capacidade de identificar
alunos em risco severo.

## 📊 Gradient Boosting

Accuracy: **0.74**\
Macro F1: **0.50**

Desempenho inferior na generalização entre classes.

------------------------------------------------------------------------

# 🏆 Modelo Escolhido

O **Random Forest** foi selecionado para produção por apresentar melhor
desempenho no contexto do problema educacional e das características da
base de dados.

Apesar de o XGBoost apresentar acurácia global ligeiramente superior, a
decisão considerou critérios mais relevantes para o impacto educacional
da solução.

O dataset possui **forte desbalanceamento entre classes**, com poucos
registros de alunos em risco severo. Nesse cenário, métricas globais
como acurácia podem mascarar falhas na identificação dos casos mais
críticos.

O Random Forest demonstrou:

-   Melhor equilíbrio entre classes\
-   Maior capacidade de identificar alunos em risco educacional\
-   Maior robustez frente a dados desbalanceados\
-   Menor tendência a ignorar classes raras\
-   Melhor interpretabilidade para uso pedagógico

Considerando que o objetivo principal da solução é detectar precocemente
alunos que necessitam de intervenção, o Random Forest mostrou-se mais
adequado para uso prático pela instituição.


------------------------------------------------------------------------

# 📊 Impacto Esperado

-   Identificação precoce de alunos em risco\
-   Priorização de acompanhamento pedagógico\
-   Decisões educacionais baseadas em dados\
-   Maior eficiência do programa social



------------------------------------------------------------------------

# 👨‍🎓 Autor

**Alef Souza Pereira**\
Pós-Tech em Data Analytics --- POSTECH

