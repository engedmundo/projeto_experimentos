soma = 12.6 + 12.9 + 13.4 + 12.3 + 13.6 + 13.5 + 12.6 + 13.1
media = soma / 8
print(f"Média: {media}")

import pandas as pd

dados_resistencia = [12.6, 12.9, 13.4, 12.3, 13.6, 13.5, 12.6, 13.1]
dados = { "Resistência": dados_resistencia }
dados_resistencia_df = pd.DataFrame(dados)
media = dados_resistencia_df["Resistência"].mean()
print(f"Média: {media}")

mediana = dados_resistencia_df["Resistência"].median()
mediana
