# Importe o módulo Streamlit e subprocess
import streamlit as st
import pandas as pd

# Pré-configurações
st.set_page_config(page_title = "Projeto 2 - Modelagem", page_icon = "🚩", layout = "wide")

# Configurando o título & subtítulo
st.markdown("<h1 style ='text-align: center; color: white;'>🤖 Automação na Decisão: Modelagem Preditiva 🤖</h1>", unsafe_allow_html = True)
st.markdown("<h2 style='text-align: center; color: green;'>- Análise de Crédito via Crisp-DM -</h2>", unsafe_allow_html = True)

# Breve introdução
st.markdown("<p style='text-align: center; color: white;'>O projeto desenvolve habilidades em diferentes aspectos da Ciência de Dados. Cada etapa do framework demanda e explora um saber distinto. Cada ideia e passo esta devidamente documentado, com intuito de ser inteligível a qualquer pessoa. O objetivo principal é a construção de um Score de Crédito através de Média Ponderada pelo desempenhos dos modelos frente a acertividade na simulação, para que o mutuário receba uma indicação de automatizada para auxiliar em sua tomada de decisões.</p>", unsafe_allow_html=True)

# Apresentação
st.subheader(":copyright: Registros do Projeto:")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🌞 Heatmap", "🌟 Bivariadas - Renda", "🎎 Bivariadas - Explicativas", "🧭 Análise Outliers", "🤹 TOP 3 Influências", "🎯 Dispersão de Previsões"])

with tab1:
   st.header("Heatmap de Correlações das Variáveis do Conjunto de Dados Inicial")
   st.image("Heatmap.png")

with tab2:
   st.header("Bivariadas - Renda vs. Explicativas")
   st.image("BivariadasRenda.png")

with tab3:
   st.header("Bivariadas - Relações entre Explicativas")
   st.image("RelacoesBivariadas.png")

with tab4:
   st.header("Comparação entre Conjuntos de Dados Inicial vs. Sem Outliers")
   st.image("ComXsemOutliers.png")

with tab5:
   st.header("Ranking TOP 3 - Influenciadores & Coeficientes de Aprendizado dos Modelos")
   st.image("TOP3influenciadores.png")

with tab6:
   st.header("Dispersão das Estimativas dos Modelos durante o Teste")
   st.image("DispersaoModelos.png", width = 900)

st.markdown("<hr style='border: 1px solid white;'>", unsafe_allow_html = True)

# URL do arquivo
pdf_url = "https://drive.google.com/file/d/1oPyK4fOOMTF_y2Y4YqOKm4NQ0RZTDyiR/view?usp=drive_link"

st.markdown(
    "<div style='text-align: center;'><h3 style='color: white;'>👇 Download do PDF Completo do Projeto (.HTML):</h3>"
    f'<a href="{pdf_url}" download="arquivo.pdf"><button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Baixar ☑️ (1005 KB)</button></a></div>',
    unsafe_allow_html=True
)

# Criandos as tabelas laterais
modelos = {"-": ["RF", "LR", "DT", "SVM", "KNN"], "Ensemble do Modelos": ["Random Forest", "Linear Regression", "Decision Tree", "SVM (Support Vector Machine)", "K-NN (K-Nearest Neighbors)"],}
parametros = {"-": ["R²", "RMSE", "MAE"], "Parâmetros de Desempenho": ["Coeficiente de Determinação", "Raiz do Erro Quadrático Médio", "Erro Médio Absoluto"]}
performance = {"-": ["RF", "LR", "DT", "SVM", "KNN"], "R² (%)": ["98,7", "93,2", "92,4", "74,1", "82,1"], "Peso no Score": ["0,893", "0,794", "0,811", "0,453", "0,620"]}
modelos_df = pd.DataFrame(modelos)
parametros_df = pd.DataFrame(parametros)
desempenho_df = pd.DataFrame(performance)

# Adicionando a barra lateral e preenchendo-a
st.sidebar.markdown("<p style='text-align: center; color: white;'><em>Este é um projeto com propósitos estritamente educacionais</em> 📓</p>", unsafe_allow_html = True)
st.sidebar.markdown("<h1 style='text-align: left; color: white;'><strong>Informações Adicionais:</strong></h3>", unsafe_allow_html = True)
st.sidebar.table(modelos_df.set_index('-').style.set_properties(**{'text-align': 'left', 'color': 'white'}))
st.sidebar.table(parametros_df.set_index('-').style.set_properties(**{'text-align': 'left', 'color': 'white'}))
st.sidebar.table(desempenho_df.set_index('-').style.set_properties(**{'text-align': 'left', 'color': 'white'}))
st.sidebar.markdown("<hr style='border: 1px solid white;'>", unsafe_allow_html = True)
st.sidebar.markdown("<ul style='text-align: left; color: white; list-style-type: square; padding-left: 20px;'><li>Desenvolvido por: Victor Lovato de Abreu</li><li>Data de Início: 03/11/2023</li><li>Versão do App: 2.0</li></ul>", unsafe_allow_html = True)
st.sidebar.markdown("<hr style='border: 1px solid white;'>", unsafe_allow_html = True)