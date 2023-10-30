import pandas as pd
import numpy as np

# Criar um DataFrame com valores ausentes (NaN)
data = pd.DataFrame({'A': [1, 2, np.nan, 4, 5],
                     'B': [np.nan, 2, 3, 4, 5]})

# Verificar valores ausentes
print(data.isna())

# Remover linhas com pelo menos um valor nulo
data_sem_nan = data.dropna()

# Preencher valores nulos com um valor específico (por exemplo, zero)
data_preenchido = data.fillna(0)

# Preencher valores nulos com a média da coluna
media_A = data['A'].mean()
data['A'] = data['A'].fillna(media_A)

# Preencher valores nulos com o valor anterior
data_preenchido_anterior = data.fillna(method='ffill')

# Preencher valores nulos com o valor seguinte
data_preenchido_seguinte = data.fillna(method='bfill')

# Exibir o resultado
print(data_sem_nan)
print(data_preenchido)
print(data_preenchido_anterior)
print(data_preenchido_seguinte)
