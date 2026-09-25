import streamlit as st
st.set_page_config(page_title="Calculadora de Esquadrias", page_icon="window", layout="wide")
SENHA_CORRETA = "1122"
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False
if not st.session_state["autenticado"]:
    st.title("Sistema Privado de Esquadrias")
    senha_digitada = st.text_input("Digite a senha para liberar o painel:", type="password")
    if st.button("Liberar Sistema", type="primary"):
        if senha_digitada == SENHA_CORRETA:
            st.session_state["autenticado"] = True
            st.rerun()
        else:
            st.error("Senha incorreta!")
    st.stop()
st.title("Sistema Personalizado de Esquadrias v9.1")
st.subheader("Calculos de Aluminios & Vidros Conforme Caderno de Fabrica")
with st.sidebar:
    st.header("Configuracoes")
    linha_principal = st.selectbox("Selecione a Linha:", ["Belissima / Suprema", "Linha Romana"])
    if linha_principal == "Belissima / Suprema":
        tipologias = ["Janela de Correr - 2 Folhas", "Janela de Correr - 3 Folhas", "Janela Integrada - 2 Folhas", "Porta de Giro - L.30", "Porta de Correr - 2 Folhas", "Porta de Correr - 3 Folhas", "Porta de Correr - 4 Folhas", "Porta Integrada - 2 Folhas", "Janela Sanfonada / Italiana / Veneziana"]
    else:
        tipologias = ["Janela Romana - 2 Folhas", "Janela Romana - 3 Folhas", "Janela Romana - 4 Folhas", "Janela Romana Integrada - 2 Folhas", "Porta Romana - 2 Folhas", "Porta Romana - 3 Folhas", "Porta Romana - 4 Folhas", "Porta Romana Integrada - 2 Folhas"]
    tipologia = st.selectbox("Selecione a Estrutura:", tipologias)
    versao_linha = "Belissima 40"
    if linha_principal == "Belissima / Suprema" and tipologia in ["Janela de Correr - 2 Folhas", "Janela de Correr - 3 Folhas", "Porta de Correr - 2 Folhas", "Porta de Correr - 3 Folhas", "Porta de Correr - 4 Folhas", "Janela Sanfonada / Italiana / Veneziana"]:
        versao_linha = st.radio("Variacao da Linha:", ["Belissima 40", "Belissima 65"])
    var_integrada = "Padrao"
    if "Integrada" in tipologia:
        if linha_principal == "Belissima / Suprema":
            var_integrada = st.selectbox("Variacao da Integrada:", ["Padrao", "Belissima 40", "Dupla", "Belissima 40 Dupla", "Belissima 40 com Motor", "Dupla com Motor"])
        else:
            var_integrada = st.radio("Configuracao do Fechamento RO:", ["Simples", "Dupla"])
    tipo_giro = "Folha Simples"
    if tipologia == "Porta de Giro - L.30":
        tipo_giro = st.radio("Configuracao da Porta:", ["Folha Simples", "Porta Dupla", "Abertura para Fora"])
col_cli, col_num = st.columns(2)
with col_cli: nome_cliente = st.text_input("Nome do Cliente / Obra:", value="Geral")
with col_num: num_pedido = st.text_input("Numero do Pedido:", value="001")
col_larg, col_alt = st.columns(2)
with col_larg: largura = st.number_input("Largura (mm):", min_value=100.0, step=1.0, value=1200.0)
with col_alt: altura = st.number_input("Altura (mm):", min_value=100.0, step=1.0, value=1000.0)
st.divider()
