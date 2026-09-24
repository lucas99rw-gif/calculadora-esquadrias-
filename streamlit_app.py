import streamlit as st

st.set_page_config(page_title="Calculadora de Esquadrias", page_icon="window", layout="wide")

# =========================================================================
# CONFIGURACAO DE SEGURANCA: SUA SENHA DEFINITIVA
# =========================================================================
SENHA_CORRETA = "1122"

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

st.title("Sistema Personalizado de Esquadrias v8.0")
st.subheader("Calculos de Aluminios & Vidros Conforme Caderno de Fabrica")

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

    # Variacoes baseadas nos arquivos enviados
    versao_linha = "Belissima 40"
    if linha_principal == "Belissima / Suprema":
        if tipologia in ["Janela de Correr - 2 Folhas", "Janela de Correr - 3 Folhas", "Porta de Correr - 2 Folhas", "Porta de Correr - 3 Folhas", "Porta de Correr - 4 Folhas", "Janela Sanfonada / Italiana / Veneziana"]:
            versao_linha = st.radio("Variacao da Linha:", ["Belissima 40", "Belissima 65"])
        
    var_integrada = "Simples"
    if "Integrada" in tipologia:
        var_integrada = st.radio("Configuracao do Fechamento:", ["Simples", "Dupla"])
        
    tipo_giro = "Folha Simples"
    if tipologia == "Porta de Giro - L.30":
        tipo_giro = st.radio("Configuracao da Porta:", ["Folha Simples", "Porta Dupla", "Abertura para Fora"])

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
if st.button("⚡ Calcular Aluminios e Vidros", type="primary"):
    
    itens_alum = []
    itens_vidro = []
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
            
            itens_alum = [
                f"Trilhos (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos / Altura: 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas: 4 pcs de {alt_folha:.0f} mm",
                f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha (R/2): 4 pcs de {larg_folha:.0f} mm"
            ]
            itens_vidro = [
                f"Vidro Janela: 2 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 112.0:.0f} mm"
            ]

        elif tipologia == "Janela de Correr - 3 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 128.0) / 3 if versao_linha == "Belissima 40" else (larg_trilho - 197.0) / 3
            titulo_obra = f"Janela Belissima 3 Fls ({versao_linha})"
            
            itens_alum = [
                f"Trilhos (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos / Altura: 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas: 6 pcs de {alt_folha:.0f} mm",
                f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha (R/3): 6 pcs de {larg_folha:.0f} mm"
            ]
            itens_vidro = [
                f"Vidro Janela: 3 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 112.0:.0f} mm"
            ]

        elif tipologia == "Janela Integrada - 2 Folhas":
            tubo_78 = largura - 86.0
            larg_trilho = largura - 40.0
            alt_marco = altura - 3.0
            alt_folha = altura - 208.0
            
            if var_integrada == "Simples":
                larg_folha = (larg_trilho - 146.0) / 2 if versao_linha == "Belissima 40" else (larg_trilho - 194.0) / 2
            else: # Dupla
                larg_folha = (larg_trilho - 184.0) / 2 if versao_linha == "Belissima 40" else (larg_trilho - 230.0) / 2
                
            titulo_obra = f"Janela Integrada Belissima ({var_integrada})"
            itens_alum = [
                f"78-472 (Tubo/Largura): 1 pc de {tubo_78:.0f} mm",
                f"Trilhos (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Altura / Marco: 2 pcs de {alt_marco:.0f} mm",
                f"IV014 / IV015 (Altura): {alt_marco - 187.0:.0f} mm",
                f"MN015 + Persiana (Largura): {largura - 129.0:.0f} mm",
                f"Altura da Folha: 4 pcs de {alt_folha:.0f} mm",
                f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha (R/2): 4 pcs de {larg_folha:.0f} mm"
            ]
            itens_vidro = [
                f"Vidro Janela: 2 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 112.0:.0f} mm"
            ]

        elif tipologia == "Porta de Giro - L.30":
            marco_30023 = largura - 4.0
            alt_marco_30023 = altura - 4.0
            alt_folha = alt_marco_30023 - 38.0
            
            if tipo_giro == "Folha Simples":
                larg_folha = marco_30023 - 63.0
                qtd_folhas = 1
            elif tipo_giro == "Porta Dupla":
                larg_folha = (marco_30023 - 77.0) / 2
                qtd_folhas = 2
            else: # Abertura para Fora
                larg_folha = marco_30023 - 69.0
                qtd_folhas = 1
                
            titulo_obra = f"Porta de Giro L.30 ({tipo_giro})"
            itens_alum = [
                f"30023 (Marco - Largura): 1 pc de {marco_30023:.0f} mm",
                f"30023 (Marco - Altura): 2 pcs de {alt_marco_30023:.0f} mm",
                f"30026 (Montante Porta - Altura): {qtd_folhas * 2} pcs de {alt_folha:.0f} mm",
                f"30026 (Montante Porta - Largura): {qtd_folhas * 2} pcs de {larg_folha:.0f} mm"
            ]
            itens_vidro = [
                f"Vidro Porta Giro: {qtd_folhas} chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 182.0:.0f} mm"
            ]
        elif tipologia == "Porta de Correr - 2 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 39.0
            larg_folha = (larg_trilho - 112.0) / 2 if versao_linha == "Belissima 40" else (larg_trilho - 153.0) / 2
            titulo_obra = f"Porta Belissima 2 Fls ({versao_linha})"
            
            itens_alum = [
                f"Trilhos (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos / Altura: 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas: 4 pcs de {alt_folha:.0f} mm",
                f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha (R/2): 4 pcs de {larg_folha:.0f} mm"
            ]
            itens_vidro = [
                f"Vidro Porta: 2 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 182.0:.0f} mm"
            ]

        elif tipologia == "Porta de Correr - 3 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 39.0
            larg_folha = (larg_trilho - 128.0) / 3 if versao_linha == "Belissima 40" else (larg_trilho - 197.0) / 3
            titulo_obra = f"Porta Belissima 3 Fls ({versao_linha})"
            
            itens_alum = [
                f"Trilhos (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos / Altura: 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas: 6 pcs de {alt_folha:.0f} mm",
                f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha (R/3): 6 pcs de {larg_folha:.0f} mm"
            ]
            itens_vidro = [
                f"Vidro Porta: 3 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 182.0:.0f} mm"
            ]

        elif tipologia == "Porta de Correr - 4 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 39.0
            larg_folha = (larg_trilho - 149.0) / 4 if versao_linha == "Belissima 40" else (larg_trilho - 241.0) / 4
            titulo_obra = f"Porta Belissima 4 Fls ({versao_linha})"
            
            itens_alum = [
                f"Trilho (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Altura / Marco: 2 pcs de {alt_marco:.0f} mm",
                f"Altura da Folha: 8 pcs de {alt_folha:.0f} mm",
                f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha (R/4): 8 pcs de {larg_folha:.0f} mm"
            ]
            itens_vidro = [
                f"Vidro Porta: 4 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 182.0:.0f} mm"
            ]

        elif tipologia == "Porta Integrada - 2 Folhas":
            tubo_78 = largura - 86.0
            larg_trilho = largura - 40.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 248.0
            larg_folha = (larg_trilho - 146.0) / 2 if var_integrada == "Simples" else (larg_trilho - 184.0) / 2
            titulo_obra = f"Porta Integrada Belissima ({var_integrada})"
            
            itens_alum = [
                f"78-472 (Tubo/Largura): 1 pc de {tubo_78:.0f} mm",
                f"Trilhos (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Altura / Marco: 2 pcs de {alt_marco:.0f} mm",
                f"IV013 / IV015 (Altura): {alt_marco - 226.0:.0f} mm",
                f"MN015 + Persiana (Largura): {largura - 129.0:.0f} mm",
                f"Altura da Folha: 4 pcs de {alt_folha:.0f} mm",
                f"SU008 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha (R/2): 4 pcs de {larg_folha:.0f} mm"
            ]
            itens_vidro = [
                f"Vidro Porta: 2 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 182.0:.0f} mm"
            ]

        elif tipologia == "Janela Sanfonada / Italiana / Veneziana":
            larg_trilho = largura - 40.0
            alt_marco = altura - 3.0
            alt_porta_dobradica = altura - 52.0
            alt_su008 = altura - 39.0
            alt_folhas_geral = altura - 60.0
            larg_folhas_geral = (larg_trilho - 155.0) / 2 if versao_linha == "Belissima 65" else (larg_trilho - 110.0) / 2
            
            alt_veneziana = altura - 61.0
            larg_r1 = (larg_trilho - 428.0) / 4.0
            larg_r2 = larg_r1 - 35.0
            comp_vra009 = (alt_veneziana - 57.0) / 2.0
            qtd_vz500_por_folha = int((alt_veneziana - 140.0) / 74.0)
            qtd_vz500_total = qtd_vz500_por_folha * 4
            
            titulo_obra = f"Janela Sanfonada Italiana 2 Fls ({versao_linha})"
            itens_alum = [
                f"Trilho (Largura): 1 pc de {larg_trilho:.0f} mm",
                f"Marco (Altura): 2 pcs de {alt_marco:.0f} mm",
                f"Porta Dobradica (Altura): 2 pcs de {alt_porta_dobradica:.0f} mm",
                f"SU008 (Batente): 2 pcs de {alt_su008:.0f} mm",
                f"Altura das Folhas Gerais: 2 pcs de {alt_folhas_geral:.0f} mm",
                f"Largura das Folhas Gerais: 2 pcs de {larg_folhas_geral:.0f} mm",
                f"Altura das Folhas de Veneziana (Todas): 4 pcs de {alt_veneziana:.0f} mm",
                f"Largura da Veneziana TAMANHO 1 (R1): 4 pcs de {larg_r1:.0f} mm",
                f"Largura da Veneziana TAMANHO 2 (R2): 4 pcs de {larg_r2:.0f} mm",
                f"VRA009 (Eixo Articulador Interno): 2 pcs de {comp_vra009:.0f} mm",
                f"Quantidade Total de Palhetas VZ500 (Para as 4 Fls): {qtd_vz500_total} pcs"
            ]
            itens_vidro = [
                "Esta tipologia utiliza venezianas em aluminio (Palhetas VZ500)"
            ]

    # =========================================================================
    # SECAO 2: LINHA ROMANA (CONFORME ARQUIVOS OFICIAIS)
    # =========================================================================
    elif linha_principal == "Linha Romana":
        
        if tipologia == "Janela Romana - 2 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 146.0) / 2
            titulo_obra = "Janela Romana - 2 Folhas"
            
            itens_alum = [
                f"Trilhos RO (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos RO (Altura): 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas RO: 4 pcs de {alt_folha:.0f} mm",
                f"Largura da Folha RO (R/2): 4 pcs de {larg_folha:.0f} mm"
            ]
            itens_vidro = [
                f"Vidro Janela Romana: 2 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 90.0:.0f} mm"
            ]

        elif tipologia == "Janela Romana - 3 Folhas":
            larg_trilho = largura - 34.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 187.0) / 3
            titulo_obra = "Janela Romana - 3 Folhas"
            
            itens_alum = [
                f"Trilhos RO (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos RO (Altura): 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas RO: 6 pcs de {alt_folha:.0f} mm",
                f"LG028 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha RO (R/3): 6 pcs de {larg_folha:.0f} mm"
            ]
            itens_vidro = [
                f"Vidro Janela Romana: 3 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 90.0:.0f} mm"
            ]

        elif tipologia == "Janela Romana - 4 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 215.0) / 4
            titulo_obra = "Janela Romana - 4 Folhas"
            
            itens_alum = [
                f"Trilhos RO (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos RO (Altura): 2 pcs de {alt_marco:.0f} mm",
                f"Altura das Folhas RO: 8 pcs de {alt_folha:.0f} mm",
                f"LG028 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha RO (R/4): 8 pcs de {larg_folha:.0f} mm"
            ]
            itens_vidro = [
                f"Vidro Janela Romana: 4 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 90.0:.0f} mm"
            ]

        elif tipologia == "Janela Romana Integrada - 2 Folhas":
            tubo_78 = largura - 86.0
            larg_trilho = largura - 40.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 209.0
            larg_folha = (larg_trilho - 228.0) / 2 if var_integrada == "Dupla" else (larg_trilho - 194.0) / 2
            titulo_obra = f"Janela Romana Integrada ({var_integrada})"
            
            itens_alum = [
                f"78472 (Tubo/Largura): 1 pc de {tubo_78:.0f} mm",
                f"Trilhos RO (Largura): 2 pcs de {larg_trilho:.0f} mm",
                f"Marcos RO (Altura): 2 pcs de {alt_marco:.0f} mm",
                f"IV013 / IV015 (Altura): {alt_marco - 184.0:.0f} mm",
                f"MN055 + Persiana (Largura): {largura - 129.0:.0f} mm",
                f"Altura das Folhas RO: 4 pcs de {alt_folha:.0f} mm",
                f"LG028 (Batente): 2 pcs de {alt_folha + 16.0:.0f} mm",
                f"Largura da Folha RO (R/2): 4 pcs de {larg_folha:.0f} mm"
            ]
            itens_vidro = [
                f"Vidro Janela Romana: 2 chapas de {larg_folha - 6.0:.0f} mm x {alt_folha - 90.0:.0f} mm"
            ]

        elif tipologia == "Porta Romana - 2 Folhas":
            larg_trilho = largura - 32.0
            alt_marco = altura - 3.0
            alt_folha = alt_marco - 49.0
            larg_folha = (larg_trilho - 146.0) / 2
            titulo_obra = "Porta Romana - 2 Folhas"
            
            itens_alum = [
                f"Trilhos RO (Largura): 2 pcs de {larg_trilho:.0f} mm",
