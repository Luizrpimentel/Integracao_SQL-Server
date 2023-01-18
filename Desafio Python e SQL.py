import pyodbc
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from IPython.display import display
dados_conexao = ("Driver={SQL Server};"
            "Server=DESKTOP-PCE1A1P;"
            "Database=ContosoRetailDW;")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()
print('Conexão Bem sucedida')

factSales_df = pd.read_sql('SELECT * FROM ContosoRetailDW.dbo.FactSales', conexao)
factSales_df = factSales_df[['DateKey','SalesAmount','TotalCost','DiscountAmount']]
profit_df = factSales_df.groupby('DateKey').sum()
profit_df['Profit'] = profit_df['SalesAmount'] - profit_df['TotalCost'] - profit_df['DiscountAmount']
display(profit_df)


grafic = profit_df['Profit'].plot(figsize=(15, 5))
grafic.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('${x:,.0f}'))
plt.show()