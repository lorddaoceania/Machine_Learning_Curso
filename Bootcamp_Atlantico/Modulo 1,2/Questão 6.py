import pandas as pd

# Lê o arquivo CSV e cria um DataFrame
data = pd.read_csv('seuarquivo.csv')

# Exibe as primeiras 5 linhas do DataFrame
print(data.head())
