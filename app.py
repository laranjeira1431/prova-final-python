import pandas as pd
import plotly as px
import streamlit as st
import openpyxl 

df_ori = pd.read_excel('acidentes.xlsx')
#st.dataframe(df_ori)


df_cat = df_ori.groupby('dia_semana').sum()

st.set_page_config(
    page_title="Acidentes BH",
    page_icon="🚗",
    layout="wide"
)

st.title("Acidentes 🚗")
st.header("Acidentes em Belo Horizonte 2023 e 2024")

st.sidebar.header("🔍 Filtros")



modo_visualizacao = st.sidebar.radio(
    "Escolha o modo de visualização:",
    ["Tabelas", "Gráficos"]
)

dias_disp = sorted(df_ori["dia_semana"].unique(), reverse=True)

if modo_visualizacao == "Tabelas":
    dia_selecionado= st.sidebar.selectbox("Selecione o dia da semana:", dias_disp)
    df_quant = df_cat['ano'] / 2023
    st.dataframe(df_quant)
else:
    cidade_selecionada = None
    fig_bar = px.boxplot_frame(
        df_ori,
        x="Dias da semana",
        y="Quantidades de acidentes",
        color="",
        barmode="group",
        title=f"Acidentes por dia ({dia_selecionado})",
        color_discrete_sequence=["#1f77b4", "#e377c2"],
    )
    st.plotly_chart(fig_bar, use_container_width=True)

#grafico de baras: comparativo homem x mulher
#df_melted = df_ori.melt(
    #id_vars=["Dias semana"],
    #var_name="dias da semana",
    #value_name="dias"
#)
        
