from sys import displayhook
import pandas as pd

#importando dados de um outro arquivo
vendas_df = pd.read_excel(r"C:\Users\Giovani\Desktop\Repositorio\Python_Exercises\Biblioteca_pandas\csv\Vendas.xlsx")
#displayhook(vendas_df)

#Visualizar os dados: head, shape e describe
#.head()-> melhor caminho para ver o começo da tabela
#displayhook(vendas_df.head())

#.shape -> mostra quantas linhas e quantas colunas tem a sua tabela
#print(vendas_df.shape)

#describe() -> resume a tabela e devolve a média de todas os dados númericos
#displayhook(vendas_df.describe())

#Selecionando colunas separadas
produtos = vendas_df[['Produto', 'Valor Unitário']]
#displayhook(produtos)

#método .loc -> pega linhas de acordo com algumas condições

#pegar uma linha especifica
