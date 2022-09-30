## 30/09/2022

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.title("Jogos vencidos na VNL 🏐")

st.text("Versão 0.1")



st.markdown("Entre maio e julho, o **Brasil** jogou com 10 seleções mundiais! Acompanhe quem venceu!")


jogos = pd.read_excel("data/jogos-vencidos-vnl.xlsx")

#st.table(jogos)

lista_dos_paises = jogos["País"].unique()

lista_dos_paises= np.append(lista_dos_paises, '')

lista_dos_paises.sort()



selecao = st.sidebar.selectbox('', lista_dos_paises)

#st.image("imagens/VNL-marca_bb.png", width=100)

gol, gol2 = st.beta_columns([5,20])
with gol:
    st.image("imagens/VNL-marca_bb.png")
with gol2:
    st.info("este é o logo da VNL!")

if selecao == "Brasil":

    st.header("A seleção feminina de vôlei ficou em 2 lugar!!")
    st.subheader("Ela perderam apenas para  Itália 😭")

if selecao == "Itália":
    st.header("A seleção feminina de vôlei ficou em 1 lugar!!")
    st.subheader("Elas jogaram contra o Brasil e ganharam")

    st.title("Acompanhe a quantidade de jogos vencidos por todas as seleções!")
    st.table(jogos)

    fig1=px.bar(jogos, x='Jogos_Vencidos', y='País', orientation='h')
    #fig1["data"][0]["marker"]["color"] = ["blue" if c == escolha_parlamentar_do_estado else "#C0C0C0" for c in fig1["data"][0]["y"]]
    fig1.update_layout(showlegend=False, yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig1, use_container_width=True)

    st.success("Observe que a Itália se destacou!")
    st.warning("Cuidado!!")
    st.error("Retorne")
