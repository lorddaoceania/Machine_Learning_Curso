import pandas as pd

# Leia o arquivo CSV ou crie o DataFrame com seus dados
data = pd.read_csv('seuarquivo.csv')

# Selecione uma coluna específica por nome
coluna_desejada = data['NomeDaColuna']

# Crie uma máscara booleana com base em uma condição (exemplo: idade maior que 30)
mascara = data['Idade'] > 30

# Aplique a máscara para filtrar as linhas do DataFrame
linhas_filtradas = data[mascara]

# Exiba o resultado
print(coluna_desejada)
print(linhas_filtradas)
