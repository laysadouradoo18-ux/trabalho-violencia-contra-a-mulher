import streamlit as st

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Landing Page - Violência Contra a Mulher",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# CSS PERSONALIZADO
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

/* HERO */

.hero {
    background: linear-gradient(135deg, #8e44ad, #e91e63);
    padding: 80px 40px;
    border-radius: 25px;
    text-align: center;
    color: white;
    margin-bottom: 50px;
}

.hero h1 {
    font-size: 60px;
    margin-bottom: 20px;
}

.hero p {
    font-size: 22px;
    max-width: 900px;
    margin: auto;
    line-height: 1.8;
}

/* BOTÃO */

div.stButton > button {
    background-color: white;
    color: #8e44ad;
    border: none;
    padding: 15px 35px;
    border-radius: 50px;
    font-size: 20px;
    font-weight: bold;
    transition: 0.3s;
}

div.stButton > button:hover {
    background-color: #f1f1f1;
    transform: scale(1.05);
}

/* CARDS */

.card {
    background-color: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    text-align: center;
    height: 100%;
}

.card h3 {
    color: #8e44ad;
    margin-bottom: 15px;
}

/* SEÇÕES */

.section-title {
    text-align: center;
    font-size: 38px;
    color: #8e44ad;
    margin-bottom: 40px;
    font-weight: bold;
}

/* FOOTER */

.footer {
    text-align: center;
    padding: 30px;
    margin-top: 50px;
    color: #777;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero">

    <h1>📊 Violência Contra a Mulher no Piauí</h1>

    <p>
        Plataforma interativa para análise de dados sobre violência doméstica,
        feminicídios, denúncias e medidas protetivas no estado do Piauí.
    </p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# BOTÃO DASHBOARD
# =========================================================

col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Acessar Dashboard"):

        st.switch_page("pages/dashboard.py")

# =========================================================
# SOBRE O PROJETO
# =========================================================

st.markdown(
    '<div class="section-title">📌 Sobre o Projeto</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="card">
        <h3>📈 Dados Estatísticos</h3>
        <p>
            Visualize informações sobre violência doméstica,
            feminicídios e denúncias registradas.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="card">
        <h3>🛡️ Medidas Protetivas</h3>
        <p>
            Acompanhe indicadores de proteção às mulheres
            em diferentes cidades do estado.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="card">
        <h3>📊 Dashboard Interativo</h3>
        <p>
            Explore gráficos dinâmicos desenvolvidos com
            Plotly, Python e Streamlit.
        </p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# OBJETIVO
# =========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">🎯 Objetivo da Plataforma</div>',
    unsafe_allow_html=True
)

st.info("""
Esta plataforma foi criada para transformar dados públicos em informações visuais,
facilitando análises, estudos acadêmicos e apoio à tomada de decisões relacionadas
ao combate à violência contra a mulher.
""")

# =========================================================
# TECNOLOGIAS
# =========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">⚙️ Tecnologias Utilizadas</div>',
    unsafe_allow_html=True
)

tec1, tec2, tec3, tec4 = st.columns(4)

with tec1:
    st.success("🐍 Python")

with tec2:
    st.success("⚡ Streamlit")

with tec3:
    st.success("📊 Plotly")

with tec4:
    st.success("📁 Excel")

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    <hr>

    <h4>Projeto • Violência Contra a Mulher no Piauí</h4>

    <p>
        Desenvolvido com Streamlit, Python e Plotly
    </p>

</div>
""", unsafe_allow_html=True)
