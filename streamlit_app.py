import streamlit as st

st.set_page_config(page_title="Calculadora de Esquadrias", page_icon="window", layout="wide")

# =========================================================================
# CONFIGURACAO DE SEGURANCA: SUA SENHA DEFINITIVA
# =========================================================================
SENHA_CORRETA = "1122"

# CONTROLE DE ACESSO POR SENHA
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    st.title("Sistema Privado de Esquadrias")
    st.subheader("Digite a sua senha de acesso para liberar o painel")
    
    senha_digitada = st.text_input("Senha de Acesso:", type="password")
    if st.button("Liberar Sistema", type="primary"):
        if senha_digitada == SENHA_CORRETA:
            st.session_state["autenticado"] = True
            st.rerun()
        else:
            st.error("Senha incorreta! Tente novamente.")
    st.stop()

# =========================================================================
# O SISTEMA SO RODA SE PASSAREM DA SENHA ACIMA
# =========================================================================

st.title("Sistema Personalizado de Esquadrias v7.0")
st.subheader("Calculos Diretos de Fabrica (Valores Arredondados)")

# 1. PAINEL LATERAL DE CONFIGURACAO (TIPOLOGIAS)
with st.sidebar:
    st.header("Linha de Perfis")
    linha_principal = st.selectbox("Selecione a Linha:", ["Belissima / Suprema", "Linha Romana"])
    
    st.header("Tipologia da Obra")
    if linha_principal == "Belissima / Suprema":
        tipologias_disponiveis = [
            "Janela de Correr - 2 Folhas", 
            "Janela de Correr - 3 Folhas",
            "Janela Integrada - 2 Folhas",
            "Porta de Giro - L.30",
            "Porta de Correr - 2 Folhas",
            "Porta de Correr - 3 Folhas",
            "Porta de Correr - 4 Folhas",
            "Porta Integrada - 2 Folhas",
            "Janela Sanfonada / Italiana / Veneziana"
        ]
    else:
        tipologias_disponiveis = [
            "Janela Romana - 2 Folhas",
            "Janela Romana - 3 Folhas",
            "Janela Romana - 4 Folhas",
            "Janela Romana Integrada - 2 Folhas",
            "Porta Romana - 2 Folhas",
            "Porta Romana - 3 Folhas",
            "Porta Romana - 4 Folhas",
            "Porta Romana Integrada - 2 Folhas"
        ]
        
    tipologia = st.selectbox("Selecione a Estrutura:", tipologias_disponiveis)

    versao_linha = "Belissima 40"
    if linha_principal == "Belissima / Suprema" and tipologia in ["Janela de Correr - 2 Folhas", "Janela de Correr - 3 Folhas", "Porta de Correr - 2 Folhas", "Porta de Correr - 3 Folhas", "Porta de Correr - 4 Folhas"]:
        versao_linha = st.radio("Variacao da Linha:", ["Belissima 40", "Belissima 65"])
    elif linha_principal == "Belissima / Suprema" and tipologia == "Janela Sanfonada / Italiana / Veneziana":
        versao_linha = st.radio("Variacao da Linha:", ["Belissima 40", "Belissima 65"])
        
    var_integrada = "Simples"
    if "Integrada" in tipologia:
        var_integrada = st.radio("Configuracao do Fechamento:", ["Simples", "Dupla"])
        
    tipo_giro = "Folha Simples"
    if tipologia == "Porta de Giro - L.30":
        tipo_giro = st.radio("Configuracao da Porta:", ["Folha Simples", "Porta Dupla"])

st.markdown("---")

# 2. ENTRADA DIRETA DE MEDIDAS E IDENTIFICACAO
st.markdown("### Identificacao e Medidas do Vao")
col_cli, col_num = st.columns(2)
with col_cli:
    nome_cliente = st.text_input("Nome do Cliente / Identificacao da Obra:", value="Geral")
with col_num:
    num_pedido = st.text_input("Numero do Pedido / Codigo:", value="001")

col_larg, col_alt = st.columns(2)
with col_larg:
    largura = st.number_input("Largura (mm):", min_value=100.0, step=1.0, value=1200.0)
with col_alt:
    altura = st.number_input("Altura (mm):", min_value=100.0, step=1.0, value=1000.0)

st.divider()

# 3. BOTAO FIXO PARA ACIONAR O CALCULO
if st.button("⚡ Calcular Lista de Corte", type="primary"):
    
    itens_para_tela = []
    titulo_obra = ""

    # =========================================================================
    # MOTOR DE CALCULO - SECAO 1: LINHA BELISSIMA / SUPREMA
    # =========================================================================
    if linha_principal == "Belissima / Suprema":
        if tipologia == "Janela de Correr - 2 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 112.0) / 2 if versao_linha == "Belissima 40" else (larg_trilho - 153.0) / 2
            titulo_obra = f"Janela Belissima 2 Fls ({versao_linha})"
            itens_para_tela = [
                f"Trilhos (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos / Altura: 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas: 4 pcs de {alt_folha:.0f} mm",
                f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha (R/2): 4 pcs de {larg_folha:.0f} mm"
            ]

        elif tipologia == "Janela de Correr - 3 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 128.0) / 3 if versao_linha == "Belissima 40" else (larg_trilho - 197.0) / 3
            titulo_obra = f"Janela Belissima 3 Fls ({versao_linha})"
            itens_para_tela = [
                f"Trilhos (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos / Altura: 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas: 6 pcs de {alt_folha:.0f} mm",
                f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha (R/3): 6 pcs de {larg_folha:.0f} mm"
            ]

        elif tipologia == "Janela Integrada - 2 Folhas":
            tubo_78 = largura - 86.0
            larg_trilho = largura - 40.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 208.0
            larg_folha = (larg_trilho - 146.0) / 2 if var_integrada == "Simples" else (larg_trilho - 184.0) / 2
            titulo_obra = f"Janela Integrada Belissima ({var_integrada})"
            itens_para_tela = [
                f"78-472 (Tubo/Largura): 1 pc de {tubo_78:.0f} mm",
                f"Trilhos (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Altura / Marco: 2 pcs de {alt_marco:.0f} mm",
                f"IV014 / IV015 (Altura): {alt_marco - 187.0:.0f} mm",
                f"MN015 + Persiana (Largura): {largura - 129.0:.0f} mm",
                f"Altura da Folha: 4 pcs de {alt_folha:.0f} mm",
                f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha (R/2): 4 pcs de {larg_folha:.0f} mm"
            ]

        elif tipologia == "Porta de Giro - L.30":
            marco_30023 = largura - 4.0
            alt_30023 = altura - 4.0
            alt_folha = alt_30023 - 38.0
            larg_folha_giro = marco_30023 - 63.0 if tipo_giro == "Folha Simples" else (marco_30023 - 77.0) / 2
            titulo_obra = f"Porta de Giro L.30 ({tipo_giro})"
            itens_para_tela = [
                f"30023 (Marco - Largura): 1 pc de {marco_30023:.0f} mm",
                f"30023 (Marco - Altura): 2 pcs de {alt_30023:.0f} mm",
                f"30026 (Montante Porta - Altura): 2 pcs de {alt_folha:.0f} mm",
                f"30026 (Montante Porta - Largura): {'2 pcs' if tipo_giro=='Folha Simples' else '4 pcs'} de {larg_folha_giro:.0f} mm"
            ]

        elif tipologia == "Porta de Correr - 2 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 39.0
            larg_folha = (larg_trilho - 112.0) / 2 if versao_linha == "Belissima 40" else (larg_trilho - 153.0) / 2
            titulo_obra = f"Porta Belissima 2 Fls ({versao_linha})"
            itens_para_tela = [
                f"Trilhos (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos / Altura: 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas: 4 pcs de {alt_folha:.0f} mm",
                f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha (R/2): 4 pcs de {larg_folha:.0f} mm"
            ]

        elif tipologia == "Porta de Correr - 3 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 39.0
            larg_folha = (larg_trilho - 128.0) / 3 if versao_linha == "Belissima 40" else (larg_trilho - 197.0) / 3
            titulo_obra = f"Porta Belissima 3 Fls ({versao_linha})"
            itens_para_tela = [
                f"Trilhos (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos / Altura: 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas: 6 pcs de {alt_folha:.0f} mm",
                f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha (R/3): 6 pcs de {larg_folha:.0f} mm"
            ]

        elif tipologia == "Porta de Correr - 4 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 39.0
            larg_folha = (larg_trilho - 149.0) / 4 if versao_linha == "Belissima 40" else (larg_trilho - 241.0) / 4
            titulo_obra = f"Porta Belissima 4 Fls ({versao_linha})"
            itens_para_tela = [
                f"Trilho (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Altura / Marco: 2 pcs de {alt_marco:.0f} mm",
                f"Altura da Folha: 8 pcs de {alt_folha:.0f} mm",
                f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha (R/4): 8 pcs de {larg_folha:.0f} mm"
            ]

        elif tipologia == "Porta Integrada - 2 Folhas":
            tubo_78 = largura - 86.0
    # =========================================================================
    # MOTOR DE CALCULO - SECAO 2: LINHA ROMANA (CONFORME NOVO CADERNO)
    # =========================================================================
    elif linha_principal == "Linha Romana":
        
        # --- JANELA 02 FOLHAS CORRER (ROMANA) ---
        if tipologia == "Janela Romana - 2 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 146.0) / 2
            titulo_obra = "Janela Romana - 2 Folhas"
            itens_para_tela = [
                f"Trilhos RO (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos RO (Altura): 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas RO: 4 pcs de {alt_folha:.0f} mm",
                f"Largura da Folha RO (R/2): 4 pcs de {larg_folha:.0f} mm"
            ]

        # --- JANELA 03 FOLHAS CORRER (ROMANA) ---
        elif tipologia == "Janela Romana - 3 Folhas":
            larg_trilho = largura - 34.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 187.0) / 3
            titulo_obra = "Janela Romana - 3 Folhas"
            itens_para_tela = [
                f"Trilhos RO (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos RO (Altura): 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas RO: 6 pcs de {alt_folha:.0f} mm",
                f"LG028 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha RO (R/3): 6 pcs de {larg_folha:.0f} mm"
            ]

        # --- JANELA ROMANA INTEGRADA 2 FOLHAS ---
        elif tipologia == "Janela Romana Integrada - 2 Folhas":
            tubo_78 = largura - 86.0
            larg_trilho = largura - 40.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 209.0
            larg_folha = (larg_trilho - 228.0) / 2 if var_integrada == "Dupla" else (larg_trilho - 194.0) / 2
            titulo_obra = f"Janela Romana Integrada ({var_integrada})"
            itens_para_tela = [
                f"78472 (Tubo/Largura): 1 pc de {tubo_78:.0f} mm",
                f"Trilhos RO (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos RO (Altura): 2 pcs de {alt_marco:.0f} mm",
                f"IV013 / IV015 (Altura): {alt_marco - 184.0:.0f} mm",
                f"MN055 + Persiana (Largura): {largura - 129.0:.0f} mm",
                f"Altura das Folhas RO: 4 pcs de {alt_folha:.0f} mm",
                f"LG028 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha RO (R/2): 4 pcs de {larg_folha:.0f} mm"
            ]

        # --- PORTA 03 FOLHAS CORRER (ROMANA) ---
        elif tipologia == "Porta Romana - 3 Folhas":
            larg_trilho = largura - 34.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 187.0) / 3
            titulo_obra = "Porta Romana - 3 Folhas"
            itens_para_tela = [
                f"Trilhos RO (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos RO (Altura): 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas RO: 6 pcs de {alt_folha:.0f} mm",
                f"LG028 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha RO (R/3): 6 pcs de {larg_folha:.0f} mm"
            ]

        # --- PORTA 04 FOLHAS DE CORRER (ROMANA) ---
        elif tipologia == "Porta Romana - 4 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 214.0) / 4
            titulo_obra = "Porta Romana - 4 Folhas"
            itens_para_tela = [
                f"Trilhos RO (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos RO (Altura): 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas RO: 8 pcs de {alt_folha:.0f} mm",
                f"LG028 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha RO (R/4): 8 pcs de {larg_folha:.0f} mm"
            ]

        # --- PORTA ROMANA INTEGRADA 2 FOLHAS ---
        elif tipologia == "Porta Romana Integrada - 2 Folhas":
            tubo_78 = largura - 86.0
            larg_trilho = largura - 40.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 248.0
            larg_folha = (larg_trilho - 228.0) / 2 if var_integrada == "Dupla" else (larg_trilho - 194.0) / 2
            titulo_obra = f"Porta Romana Integrada ({var_integrada})"
            itens_para_tela = [
                f"78472 (Tubo/Largura): 1 pc de {tubo_78:.0f} mm",
                f"Trilhos RO (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos RO (Altura): 2 pcs de {alt_marco:.0f} mm",
                f"IV013 / IV015 (Altura): {alt_marco - 220.0:.0f} mm",
                f"MN055 + Persiana (Largura): {largura - 129.0:.0f} mm",
                f"Altura das Folhas RO: 4 pcs de {alt_folha:.0f} mm",
                f"LG028 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha RO (R/2): 4 pcs de {larg_folha:.0f} mm"
            ]

        # --- ADAPTACAO RECORRENTE PARA ESTRUTURAS RO DE 2 FLS TRADICIONAIS ---
        elif tipologia == "Porta Romana - 2 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 146.0) / 2
            titulo_obra = "Porta Romana - 2 Folhas"
            itens_para_tela = [
                f"Trilhos RO (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos RO (Altura): 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas RO: 4 pcs de {alt_folha:.0f} mm",
                f"Largura da Folha RO (R/2): 4 pcs de {larg_folha:.0f} mm"
            ]
        elif tipologia == "Janela Romana - 4 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 214.0) / 4
            titulo_obra = "Janela Romana - 4 Folhas"
            itens_para_tela = [
                f"Trilhos RO (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos RO (Altura): 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas RO: 8 pcs de {alt_folha:.0f} mm",
                f"LG028 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha RO (R/4): 8 pcs de {larg_folha:.0f} mm"
            ]

    # EXIBICAO DOS RESULTADOS NA TELA
    st.success(f"### Resultado do Calculo: {titulo_obra}")
    st.markdown(f"**Cliente / Obra:** {nome_cliente} | **Pedido:** {num_pedido}")
    for item in itens_para_tela:
        st.markdown(f"* {item}")
