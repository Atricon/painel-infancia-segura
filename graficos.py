import pandas as pd
import plotly.express as px
from import_data import *
import textwrap

# Configurando as cores
amarelo =  "#EDC40C" # "#E1C233"
laranja = "#E66C37"
cinza = "#EEE"
verde = "#58BDB6"
azul = "#1C6F9D"
sim = verde
nao = azul
nao_aplica = "#BBB"

# Configurando tamanho dos gráficos de pizza
width_pizza = 300
height_pizza = 300

# Função para quebrar o texto a cada 3 palavras
def quebrar_texto(texto, palavras_por_linha=3):
    palavras = texto.split()  # Divide o texto em palavras
    linhas = []
    
    # Quebra o texto em grupos de 3 palavras
    for i in range(0, len(palavras), palavras_por_linha):
        linha = ' '.join(palavras[i:i+palavras_por_linha])  # Pega 3 palavras de cada vez
        linhas.append(linha)
    
    return '<br>'.join(linhas)  # Junta as linhas com quebras de linha

######################################
# Função que cria gráfico de mapa do Brasil com respostas SIM e NÃO
######################################
def grafico_mapa_brasil(pergunta_id, df_entidades_levantamentos, title=None):
    filtro_pergunta = df_respostas[(df_respostas["pergunta_id"]==pergunta_id)][['resposta_levantamento_id','boolean_answer']]

    df_resposta = pd.merge(
        df_entidades_levantamentos, filtro_pergunta, left_on="id_x", right_on="resposta_levantamento_id", how="left"
        )[['uf', 'boolean_answer']]

    df_resposta["resposta_label"] = (
        df_resposta["boolean_answer"]
        .astype(str)
        .replace({
            "True": "Sim",
            "False": "Não",
            "true": "Sim",
            "false": "Não",
            "nao_aplica": "Não se aplica",
            "nan": "Não Respondeu"
        })
    )

    st.markdown(
        f"""
        <h3 style='font-size:16px;'>
            {title}
        </h3>
        """,
        unsafe_allow_html=True
    )

    # Gerar o mapa com Plotly Express
    fig_mapa = px.choropleth(
        df_resposta,
        geojson=geojson_url,
        locations="uf",
        featureidkey="properties.sigla",  # Códigos ISO no GeoJSON
        color="resposta_label",
        color_discrete_map={"Sim": sim, "Não": nao, "Não Respondeu": cinza, "Não se aplica": nao_aplica} ,
        labels={"resposta_label": "Resposta", "uf": "UF"},
        hover_name="uf",
    )

    fig_mapa.update_geos(
        fitbounds="locations",
        visible=False,
        resolution=50
    )

    fig_mapa.update_layout(
        height=800,
        paper_bgcolor="rgba(0,0,0,0)",
        geo=dict(bgcolor="rgba(0,0,0,0)")
    )

    return fig_mapa


######################################
# Função que cria gráfico de pizza 
######################################
def grafico_pizza(pergunta_id, df_entidades_levantamentos, title=None, hole=None):
    filtro_pergunta = df_respostas[(df_respostas["pergunta_id"]==pergunta_id)][['resposta_levantamento_id','boolean_answer']]

    df_resposta = pd.merge(
        df_entidades_levantamentos, filtro_pergunta, left_on="id_x", right_on="resposta_levantamento_id", how="inner"
    )

    dados = {
        'Sim': (
            (df_resposta['boolean_answer'] == True) |
            (df_resposta['boolean_answer'] == "true")
        ).sum(),

        'Não': (
            (df_resposta['boolean_answer'] == False) |
            (df_resposta['boolean_answer'] == "false")
        ).sum(),

        'Não se aplica': (
            df_resposta['boolean_answer'] == "nao_aplica"
        ).sum(),
    }

    # Remove categorias zeradas
    dados = {k: v for k, v in dados.items() if v > 0}

    pie_data = pd.DataFrame({
        'Resposta': list(dados.keys()),
        'Quantidade': list(dados.values())
    })

    st.markdown(
        f"""
        <h3 style='font-size:16px;'>
            {title}
        </h3>
        """,
        unsafe_allow_html=True
    )

    fig_resposta = px.pie(
        pie_data, 
        values='Quantidade', 
        names='Resposta',
        color='Resposta',
        color_discrete_map={'Sim': sim, 'Não': nao, 'Não se aplica': nao_aplica},
        hole=hole
    )
    fig_resposta.update_traces(textposition='inside', textinfo='percent+value')
    fig_resposta.update_layout(
        width=width_pizza,  # Largura em pixels
        height=height_pizza,  # Altura em pixels
    )

    return fig_resposta


def grafico_pizza_com_legenda(pergunta_id, df_entidades_levantamentos, title=None, hole=None):
    filtro_pergunta = df_respostas[(df_respostas["pergunta_id"]==pergunta_id)]

    df_resposta = pd.merge(
        df_entidades_levantamentos, filtro_pergunta, left_on="id_x", right_on="resposta_levantamento_id", how="inner"
    )[['id']]

    df_resposta = pd.merge(
        df_resposta, df_resposta_opcoes, left_on="id", right_on="respostapergunta_id", how="inner"
    )

    df_resposta = pd.merge(
        df_resposta, df_opcoes, left_on="opcao_id", right_on="id", how="inner"
    )

    count_df_resposta = df_resposta['texto'].value_counts().reset_index()
    count_df_resposta.columns = ['texto', 'total']

    baixo_risco = pd.DataFrame({'texto':['BAIXO RISCO'],
                                'total':[0]})
    
    # concateando com dataframe criado para exibir a legando de baixo risco que é zero
    count_df_resposta = pd.concat([count_df_resposta, baixo_risco], ignore_index=True)

    pie_data = pd.DataFrame({
        'Resposta': count_df_resposta['texto'],
        'Quantidade': count_df_resposta['total']
    })

    st.markdown(
        f"""
        <h3 style='font-size:16px;'>
            {title}
        </h3>
        """,
        unsafe_allow_html=True
    )

    fig_resposta = px.pie(
        pie_data, 
        values='Quantidade', 
        names='Resposta',
        color='Resposta',
        color_discrete_map={"ALTO RISCO": sim, "MÉDIO RISCO": nao, "BAIXO RISCO": cinza} ,
        hole=hole
    )
    fig_resposta.update_traces(textposition='inside', textinfo='percent+value')
    fig_resposta.update_layout(
        width=width_pizza,  # Largura em pixels
        height=height_pizza  # Altura em pixels
    )

    return fig_resposta


######################################
# Função que cria gráfico de barra horizontal
######################################
def grafico_barra_horizontal(pergunta_id, df_entidades_levantamentos, title=None, palavras=3, height=None):
    filtro_pergunta = df_respostas[(df_respostas["pergunta_id"]==pergunta_id)]

    df_resposta = pd.merge(
        df_entidades_levantamentos, filtro_pergunta, left_on="id_x", right_on="resposta_levantamento_id", how="inner"
    )[['id']]

    df_resposta = pd.merge(
        df_resposta, df_resposta_opcoes, left_on="id", right_on="respostapergunta_id", how="inner"
    )

    df_resposta = pd.merge(
        df_resposta, df_opcoes, left_on="opcao_id", right_on="id", how="inner"
    )

    # Aplicar quebra de linha nas categorias
    df_resposta['texto_quebrado'] = df_resposta['texto'].apply(lambda x: quebrar_texto(x, palavras))

    count_df_resposta = df_resposta['texto_quebrado'].value_counts().reset_index()

    count_df_resposta.columns = ['texto_quebrado', 'total']

    # Ordenar os dados pelo total
    count_df_resposta = count_df_resposta.sort_values('total', ascending=True)

    st.markdown(
        f"""
        <h3 style='font-size:16px;'>
            {title}
        </h3>
        """,
        unsafe_allow_html=True
    )

    # Criar gráfico de barras horizontais com Plotly
    fig_resposta = px.bar(
        count_df_resposta,
        x='total',
        y='texto_quebrado',
        orientation='h',
        text='total',
        color_discrete_sequence=[nao, sim],
        range_x=[0, 20],
        height=height
    )

    fig_resposta.update_layout(
        xaxis_title='',  # Sem título para o eixo X
        yaxis_title='',  # Sem título para o eixo Y
        showlegend=False,

    )

    fig_resposta.update_traces(
        textfont_size=14, 
        textangle=0, 
        cliponaxis=False,
        )

    return fig_resposta