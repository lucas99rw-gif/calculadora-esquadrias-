import streamlit as st

st.set_page_config(page_title="Calculadora de Esquadrias", page_icon="window", layout="wide")

# CONFIGURACAO DE SEGURANCA
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

st.title("Sistema Personalizado de Esquadrias v9.0")
st.subheader("Calculos de Aluminios & Vidros Conforme Caderno de Fabrica")

# 1. PAINEL LATERAL
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

# 2. ENTRADA DE MEDIDAS
col_cli, col_num = st.columns(2)
with col_cli: nome_cliente = st.text_input("Nome do Cliente / Obra:", value="Geral")
with col_num: num_pedido = st.text_input("Numero do Pedido:", value="001")

col_larg, col_alt = st.columns(2)
with col_larg: largura = st.number_input("Largura (mm):", min_value=100.0, step=1.0, value=1200.0)
with col_alt: altura = st.number_input("Altura (mm):", min_value=100.0, step=1.0, value=1000.0)

st.divider()

if st.button("⚡ Calcular Aluminios e Vidros", type="primary"):
    itens_alum, itens_vidro, titulo_obra = [], [], ""

    # ==================== LINHA BELISSIMA / SUPREMA ====================
    if linha_principal == "Belissima / Suprema":
        if tipologia == "Janela de Correr - 2 Folhas":
            larg_trilho, alt_marco = largura - 32.0, altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 112.0) / 2 if versao_linha == "Belissima 40" else (larg_trilho - 153.0) / 2
            titulo_obra = f"Janela Belissima 2 Fls ({versao_linha})"
            itens_alum = [f"Trilhos (Largura): 2 pcs de {larg_trilho:.0f} mm", f"Marcos (Altura): 2 pcs de {alt_marco:.0f} mm", f"Altura das Folhas: 4 pcs de {alt_folha:.0f} mm", f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm", f"Largura da Folha: 4 pcs de {larg_folha:.0f} mm"]
            itens_vidro = [f"Vidro Janela: 2 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 112.0:.0f} mm"]

        elif tipologia == "Janela de Correr - 3 Folhas":
            larg_trilho, alt_marco = largura - 32.0, altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 128.0) / 3 if versao_linha == "Belissima 40" else (larg_trilho - 197.0) / 3
            titulo_obra = f"Janela Belissima 3 Fls ({versao_linha})"
            itens_alum = [f"Trilhos (Largura): 2 pcs de {larg_trilho:.0f} mm", f"Marcos (Altura): 2 pcs de {alt_marco:.0f} mm", f"Altura das Folhas: 6 pcs de {alt_folha:.0f} mm", f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm", f"Largura da Folha: 6 pcs de {larg_folha:.0f} mm"]
            itens_vidro = [f"Vidro Janela: 3 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 112.0:.0f} mm"]

        elif tipologia == "Janela Integrada - 2 Folhas":
            tubo_78, larg_trilho, alt_marco = largura - 86.0, largura - 40.0, altura - 3.0
            alt_folha = alt_marco - 208.0
            if var_integrada == "Padrao": f_desconto = 194.0
            elif var_integrada == "Belissima 40": f_desconto = 146.0
            elif var_integrada == "Dupla": f_desconto = 230.0
            elif var_integrada == "Belissima 40 Dupla": f_desconto = 184.0
            elif var_integrada == "Belissima 40 com Motor": f_desconto = 110.0
            else: f_desconto = 158.0
            larg_folha = (larg_trilho - f_desconto) / 2
            titulo_obra = f"Janela Integrada Belissima ({var_integrada})"
            itens_alum = [f"78-472 (Tubo): 1 pc de {tubo_78:.0f} mm", f"Trilhos: 2 pcs de {larg_trilho:.0f} mm", f"Marco (Altura): 2 pcs de {alt_marco:.0f} mm", f"IV014/IV015: {alt_marco - 187.0:.0f} mm", f"MN015 + Persiana: {largura - 129.0:.0f} mm", f"Altura da Folha: 4 pcs de {alt_folha:.0f} mm", f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm", f"Largura da Folha: 4 pcs de {larg_folha:.0f} mm"]
            itens_vidro = [f"Vidro Janela: 2 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 112.0:.0f} mm"]

        elif tipologia == "Porta de Giro - L.30":
            marco_30023 = largura - 4.0
            alt_30023 = altura - 4.0
            alt_folha = alt_30023 - 38.0
            if tipo_giro == "Folha Simples": larg_folha, qtd = marco_30023 - 63.0, 1
            elif tipo_giro == "Porta Dupla": larg_folha, qtd = (marco_30023 - 77.0) / 2, 2
            else: larg_folha, qtd = marco_30023 - 69.0, 1
            titulo_obra = f"Porta de Giro L.30 ({tipo_giro})"
            itens_alum = [f"30023 (Marco Largura): 1 pc de {marco_30023:.0f} mm", f"30023 (Marco Altura): 2 pcs de {alt_30023:.0f} mm", f"30026 (Montante Altura): {qtd*2} pcs de {alt_folha:.0f} mm", f"30026 (Montante Largura): {qtd*2} pcs de {larg_folha:.0f} mm"]
            itens_vidro = [f"Vidro Porta Giro: {qtd} chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 182.0:.0f} mm"]

        elif tipologia == "Porta de Correr - 2 Folhas":
            larg_trilho, alt_marco = largura - 32.0, altura - 3.0
            alt_folha = alt_marco - 39.0
            larg_folha = (larg_trilho - 112.0) / 2 if versao_linha == "Belissima 40" else (larg_trilho - 153.0) / 2
            titulo_obra = f"Porta Belissima 2 Fls ({versao_linha})"
            itens_alum = [f"Trilhos: 2 pcs de {larg_trilho:.0f} mm", f"Marcos: 2 pcs de {alt_marco:.0f} mm", f"Altura Folhas: 4 pcs de {alt_folha:.0f} mm", f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm", f"Largura Folha: 4 pcs de {larg_folha:.0f} mm"]
            itens_vidro = [f"Vidro Porta: 2 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 182.0:.0f} mm"]

        elif tipologia == "Porta de Correr - 3 Folhas":
            larg_trilho, alt_marco = largura - 32.0, altura - 3.0
            alt_folha = alt_marco - 39.0
            larg_folha = (larg_trilho - 128.0) / 3 if versao_linha == "Belissima 40" else (larg_trilho - 197.0) / 3
            titulo_obra = f"Porta Belissima 3 Fls ({versao_linha})"
            itens_alum = [f"Trilhos: 2 pcs de {larg_trilho:.0f} mm", f"Marcos: 2 pcs de {alt_marco:.0f} mm", f"Altura Folhas: 6 pcs de {alt_folha:.0f} mm", f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm", f"Largura Folha: 6 pcs de {larg_folha:.0f} mm"]
            itens_vidro = [f"Vidro Porta: 3 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 182.0:.0f} mm"]

        elif tipologia == "Porta de Correr - 4 Folhas":
            larg_trilho, alt_marco = largura - 32.0, altura - 3.0
            alt_folha = alt_marco - 39.0
            larg_folha = (larg_trilho - 149.0) / 4 if versao_linha == "Belissima 40" else (larg_trilho - 241.0) / 4
            titulo_obra = f"Porta Belissima 4 Fls ({versao_linha})"
            itens_alum = [f"Trilho: 2 pcs de {larg_trilho:.0f} mm", f"Altura/Marco: 2 pcs de {alt_marco:.0f} mm", f"Altura Folha: 8 pcs de {alt_folha:.0f} mm", f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm", f"Largura Folha: 8 pcs de {larg_folha:.0f} mm"]
            itens_vidro = [f"Vidro Porta: 4 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 182.0:.0f} mm"]

        elif tipologia == "Porta Integrada - 2 Folhas":
            tubo_78, larg_trilho, alt_marco = largura - 86.0, largura - 40.0, altura - 3.0
            alt_folha = alt_marco - 248.0
            if var_integrada == "Padrao": f_desconto = 194.0
            elif var_integrada == "Belissima 40": f_desconto = 146.0
            elif var_integrada == "Dupla": f_desconto = 230.0
            elif var_integrada == "Belissima 40 Dupla": f_desconto = 184.0
            elif var_integrada == "Belissima 40 com Motor": f_desconto = 110.0
            else: f_desconto = 158.0
            larg_folha = (larg_trilho - f_desconto) / 2
            titulo_obra = f"Porta Integrada Belissima ({var_integrada})"
