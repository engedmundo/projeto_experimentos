import pandas as pd

tempo_secagem = [
    3.4, 2.5, 4.8, 2.9, 3.6, 
    2.8, 3.3, 5.6, 3.7, 2.8, 
    4.4, 4.0, 5.2, 3.0, 4.8,
]
dados = { "Tempo": tempo_secagem }

# criar tabela:
tempo_df = pd.DataFrame(dados)
tempo_df.head()

# contar os valores
quantidade_valores = tempo_df["Tempo"].count()
# calcular a média
media = tempo_df["Tempo"].mean()
# calcular a mediana
mediana = tempo_df["Tempo"].median()

# mostrar resultado:
print(f"Quantidade de valores: {quantidade_valores}")
print(f"Média: {media:.4f}")
print(f"Mediana: {mediana}")
# print(tempo_df)
