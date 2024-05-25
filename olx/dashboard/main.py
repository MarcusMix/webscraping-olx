import pandas as pd
from sqlalchemy import create_engine
import streamlit as st
import plotly.express as px

# conexao com o banco
engine = create_engine('mysql://root:root@localhost/rents')

tabela = 'rent_table'

query_sql = f"SELECT * FROM {tabela}"

df = pd.read_sql_query(query_sql, engine)

# tratamento
df['neighbourhood'] = df['neighbourhood'].replace('', 'Sem informação')

st.title("Dados Aluguéis na Grande Florianópolis")

# colunas
col1, col2, col3, col4 = st.columns(4)

# média (removendo valores acima de 100k, pq geralmente é venda não aluguel)
filtered_data = df[(df["price"] <= 100000) & (df["price"] != 0)]

if not filtered_data.empty:
    average_price = filtered_data["price"].mean().round(2)

col1.metric(label="Valor Médio Aluguel", value=average_price)

# quantidade total
total_rents = df.shape[0]
col2.metric(label="Quantidade de Imóveis", value=total_rents)

# quantidade cidades
total_cities = len(df["city"].unique())
col3.metric(label="Quantidade de Cidades", value=total_cities)

# quantidade bairros
total_neighbourhood = len(df["neighbourhood"].unique())
col4.metric(label="Quantidade de Bairros", value=total_neighbourhood)

# quantidade por cidade
st.subheader("Quantidade de aluguéis por Cidade")
most_popular_city = df["city"].value_counts().sort_values(ascending=False)
top_10_cities = most_popular_city.head(10).reset_index()
top_10_cities.columns = ['Cidade', 'Quantidade']

# grafico com plotly
fig = px.bar(top_10_cities, x='Quantidade', y='Cidade')
fig.update_traces(marker_color='#ffaa00', text=top_10_cities['Quantidade'])
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.update_layout(yaxis={'categoryorder':'total ascending'})

st.plotly_chart(fig, use_container_width=True)

# valor médio por cidade
st.subheader("Valor médio por Cidade (até 10k)")
filtered_df = df[df["price"] <= 10000]
average_price_per_city = filtered_df.groupby("city")["price"].mean().sort_values(ascending=False).reset_index().round(2)
average_price_per_city.columns = ['Cidade', 'Valor']

# grafico com plotly
fig2 = px.pie(average_price_per_city, values='Valor', names='Cidade')
fig2.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig2, use_container_width=True)

# valor médio por cidade
st.subheader("Valor médio por Bairro (até 10k)")
col10, col20 = st.columns([4, 2])

# opcao todos, retorna tudo
city_options = ['Todos'] + list(df['city'].sort_values(ascending=True).dropna().unique())
neighbourhood_options = ['Todos'] + list(df['neighbourhood'].sort_values(ascending=True).dropna().unique())

# dropdowns 
selected_city = col20.selectbox('Selecione a cidade:', city_options)
selected_neighbourhood = col20.selectbox('Selecione o bairro:', neighbourhood_options)

filtered_df_neighbourhood = df[(df["price"] <= 10000) & (df["neighbourhood"] != "")]

# filtrando cidade
if selected_city != "Todos":
    filtered_df_neighbourhood = filtered_df_neighbourhood[df['city'] == selected_city]

# filtrando bairro
if selected_neighbourhood != "Todos":
   filtered_df_neighbourhood = filtered_df_neighbourhood[df['neighbourhood'] == selected_neighbourhood]

# agrupando por bairro e cidade e pegando a média
# average_price_per_neighbourhood = filtered_df_neighbourhood.groupby(["neighbourhood", "city"])["price"].mean().sort_values(ascending=True).reset_index()
average_price_per_neighbourhood = filtered_df_neighbourhood.groupby(["neighbourhood", "city"])["price"].mean().sort_values(ascending=True).reset_index()
average_price_per_neighbourhood.columns = ['Bairro', 'Cidade', 'Valor']

# plotando tabela
col10.table(average_price_per_neighbourhood)