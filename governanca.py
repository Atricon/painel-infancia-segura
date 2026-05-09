import streamlit as st
from import_data import *
from graficos import *
import textwrap

# Título da Página
st.title("📋 Governança")

st.sidebar.header("Filtros")
uf_selecao = st.sidebar.selectbox(
    "Estado", 
    estados["uf"],
    index=None,
    placeholder="Selecione um Estado...",
)

if uf_selecao:
    df_entidades_levantamentos = df_entidades_levantamentos[(df_entidades_levantamentos["uf"]==uf_selecao)]

######################################
# Gráficos da faixa 1
######################################
titulo_1 = "Estados que possuem Plano Estadual para o enfrentamento à violência contra crianças e adolescentes ou instrumento similar"
st.plotly_chart(grafico_mapa_brasil(1, df_entidades_levantamentos, titulo_1), key="resposta_1", width='stretch')

col1, col2 = st.columns(2, gap="large", vertical_alignment="top")

with col1:
        titulo_2 = "Estados que possuem Plano Estadual ancorado em alguminstrumento normativo"
        st.plotly_chart(grafico_pizza(2, df_entidades_levantamentos, titulo_2), key="resposta_2", width='stretch')

        titulo_4 = "Estados com plano publicado em veículo oficial e disponível para sociedade"
        st.plotly_chart(grafico_pizza(4, df_entidades_levantamentos, titulo_4, .4), key="resposta_4", width='stretch')

with col2:
        titulo_3 = "Estados com Plano Estadual alinhado com o Plano Nacional de enfrentamento da violência contra crianças e adolescentes"
        st.plotly_chart(grafico_pizza(3, df_entidades_levantamentos, titulo_3, .4), key="resposta_3", width='stretch')

        titulo_7 = "Estados nos quais houve a instituição de ciclos periódicos de avaliação e monitoramento do plano estadual"
        st.plotly_chart(grafico_pizza(7, df_entidades_levantamentos, titulo_7), key="resposta_7", width='stretch')

col3, col4 = st.columns(2, gap="large", vertical_alignment="top")

with col3:
    titulo_5 = "Ações realizadas no processo de construção dos planos nos Estados<br>que possuem Plano Estadual"
    st.plotly_chart(grafico_barra_horizontal(5, df_entidades_levantamentos, titulo_5), key="resposta_5", use_container_width=True)

with col4:
    titulo_6 = "Nos planos estaduais existentes foram estabelecidos:"
    st.plotly_chart(grafico_barra_horizontal(6, df_entidades_levantamentos, titulo_6), key="resposta_6", use_container_width=True)


######################################
# Gráficos da faixa 2
######################################
titulo_13 = "Estados que estabeleceram normas sobre o sistema de garantia de direitos da criança e do adolescente vítima ou testemunha de violência"
st.plotly_chart(grafico_mapa_brasil(13, df_entidades_levantamentos, titulo_13), key="resposta_13", use_container_width=True)

col5, col6, col7 = st.columns(3, gap="large", vertical_alignment="top")

with col5:
    titulo_8 = "Estados que possuem Comitê Intersetorial de políticas públicas para a primeira infância?"
    st.plotly_chart(grafico_pizza(8, df_entidades_levantamentos, titulo_8), key="resposta_8", use_container_width=True)

    titulo_22 = "Estados que receberam do MJSP orientação sobre programa ou ação na temática da violência contra a criança e o adolescente ou da implementação da lei da escuta especializada"
    st.plotly_chart(grafico_pizza(22, df_entidades_levantamentos, titulo_22), key="resposta_22", use_container_width=True)

with col6:
    titulo_9 = "Estados nos quais o Comitê Intersetorial de políticas públicas para a primeira infância está em efetivo funcionamento"
    st.plotly_chart(grafico_pizza(9, df_entidades_levantamentos, titulo_9, 0.4), key="resposta_9", use_container_width=True)

    titulo_9 = "Estados nos instituiram Comitê de gestão colegiada da rede de cuidado e de proteção social das crianças e dos adolescentes vítimas ou testemunhas de violência"
    st.plotly_chart(grafico_pizza(14,df_entidades_levantamentos, titulo_9, 0.4), key="resposta_14", use_container_width=True)

with col7:
    titulo_10 = "Estados nos quais existe uma articulação permanente entre os órgãos responsáveis pela coordenação do comitê intersetorial no âmbito federal e estadual"
    st.plotly_chart(grafico_pizza(10, df_entidades_levantamentos, titulo_10), key="resposta_10", use_container_width=True)

    titulo_15 = "Estados nos quais o Comitê de gestão colegiada da rede de cuidado está em efetivo funcionamento"
    st.plotly_chart(grafico_pizza(15, df_entidades_levantamentos, titulo_15), key="resposta_15", use_container_width=True)


######################################
# Gráficos da faixa 3
######################################
titulo_17 = "Estados que estabeleceram dotações orçamentárias específicas, em de 2024, para a implementação de ações específicas do sistema de garantias de direitos da criança e do adolescente vítima ou testemunha de violência?"
st.plotly_chart(grafico_mapa_brasil(17, df_entidades_levantamentos, titulo_17), key="resposta_17", use_container_width=True)

col8, col9 = st.columns(2, gap="large", vertical_alignment="top")

with col8:
    titulo_11 = "Estados nos quais a União ofereceu assistência técnica na elaboração de planos estaduais para a primeira infância que articulem os diferentes setores, com vistas a uma abordagem multi e intersetorial"
    st.plotly_chart(grafico_pizza(11, df_entidades_levantamentos, titulo_11), key="resposta_11", use_container_width=True)
with col9:
    titulo_16 = "Estados que estabeleceram as diretrizes para que os municípios<br>definam o fluxo de atendimento das crianças e adolescentes vítimas ou testemunhas de violência, conforme art. 9°, Il do Decreto 9.603/2018"
    st.plotly_chart(grafico_pizza(16, df_entidades_levantamentos, titulo_16, .4), key="resposta_16", use_container_width=True)