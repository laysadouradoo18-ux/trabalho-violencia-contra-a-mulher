import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================================

st.set_page_config(
    page_title="Violência Contra a Mulher no Piauí",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# ESTILO CSS
# =====================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.hero {
    background: linear-gradient(135deg, #8e44ad, #e91e63);
    padding: 50px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 48px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 20px;
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    text-align: center;
}

.section-title {
    font-size: 30px;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 20px;
    color: #8e44ad;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="hero">
    <h1>📊 Violência Contra a Mulher no Piauí</h1>
    <p>
        Dashboard interativo para análise de feminicídios,
        violência doméstica, denúncias e medidas protetivas.
    </p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# LEITURA DOS DADOS
# =====================================================

try:
    df = pd.read_excel("violencia_mulher_piaui.xlsx")

    # AJUSTAR NOMES DAS COLUNAS
    df.columns = [
        "Ano",
        "Cidade",
        "Feminicidios",
        "Violencia_Domestica",
        "Medidas_Protetivas",
        "Denuncias_180",
        "BO_Registrados"
    ]

except Exception as e:
    st.error(f"Erro ao carregar o arquivo Excel: {e}")
    st.stop()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🔎 Filtros")

anos = st.sidebar.multiselect(
    "Selecione o Ano",
    options=df["Ano"].unique(),
    default=df["Ano"].unique()
)

df_filtrado = df[df["Ano"].isin(anos)]

# =====================================================
# MÉTRICAS
# =====================================================

st.markdown(
    '<div class="section-title">📌 Indicadores Gerais</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Violência Doméstica",
        int(df_filtrado["Violencia_Domestica"].sum())
    )

with col2:
    st.metric(
        "Feminicídios",
        int(df_filtrado["Feminicidios"].sum())
    )

with col3:
    st.metric(
        "Denúncias 180",
        int(df_filtrado["Denuncias_180"].sum())
    )

with col4:
    st.metric(
        "BO Registrados",
        int(df_filtrado["BO_Registrados"].sum())
    )

# =====================================================
# GRÁFICO 1
# =====================================================

st.markdown(
    '<div class="section-title">📈 Violência Doméstica por Cidade</div>',
    unsafe_allow_html=True
)

grafico1 = px.bar(
    df_filtrado,
    x="Cidade",
    y="Violencia_Domestica",
    color="Cidade",
    text_auto=True
)

st.plotly_chart(grafico1, use_container_width=True)

# =====================================================
# GRÁFICO 2
# =====================================================

st.markdown(
    '<div class="section-title">⚠️ Feminicídios por Cidade</div>',
    unsafe_allow_html=True
)

grafico2 = px.pie(
    df_filtrado,
    names="Cidade",
    values="Feminicidios",
    hole=0.5
)

st.plotly_chart(grafico2, use_container_width=True)

# =====================================================
# GRÁFICO 3
# =====================================================

st.markdown(
    '<div class="section-title">📞 Denúncias 180 por Ano</div>',
    unsafe_allow_html=True
)

grafico3 = px.line(
    df_filtrado,
    x="Ano",
    y="Denuncias_180",
    markers=True
)

st.plotly_chart(grafico3, use_container_width=True)

# =====================================================
# TABELA
# =====================================================

st.markdown(
    '<div class="section-title">📋 Base de Dados</div>',
    unsafe_allow_html=True
)

st.dataframe(df_filtrado, use_container_width=True)

# =====================================================
# RODAPÉ
# =====================================================

st.markdown("""
<hr>

<center>
    <h4>Projeto Streamlit • Violência Contra a Mulher no Piauí</h4>
    <p>Desenvolvido com Python, Plotly e Streamlit</p>
</center>
""", unsafe_allow_html=True)
