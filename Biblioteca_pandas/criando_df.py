#as pd -> faz com que precise escrever apenas o pd parausar o pandas
from sys import displayhook
import pandas as pd

#Dataframe -> tabelas no python, usado para usar dados no python
# datafrave = pd.DataFrame()
venda = {'data': ['15/02/2021', '16/02/2021'],
         'valor': [500, 300],
         'produto': ['feijao', 'arroz'],
         'qtde': [50, 70],
        }
vendas_df = pd.DataFrame(venda) 

#visualizar o Datafrave criado: print e display
#print(vendas_df)
#displayhook(vendas_df)