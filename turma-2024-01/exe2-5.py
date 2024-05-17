import pandas as pd

empresa_a = [9.3, 6.8, 8.8, 8.7, 8.5, 6.7, 8.0, 6.5, 9.2, 7.0]
empresa_b = [11.0, 9.8, 9.9, 10.2, 10.1, 9.7, 11.0, 11.1, 10.2, 9.6]

dados = {
    "Empresa A": empresa_a,
    "Empresa B": empresa_b,
}
flexibilidade_df = pd.DataFrame(dados)
flexibilidade_df.head()

# medias
media_empresa_a = flexibilidade_df["Empresa A"].mean()
media_empresa_b = flexibilidade_df["Empresa B"].mean()

# medianas
mediana_empresa_a = flexibilidade_df["Empresa A"].median()
mediana_empresa_b = flexibilidade_df["Empresa B"].median()

print(f"Media Empresa A: {media_empresa_a}")
print(f"Media Empresa B: {media_empresa_b}")
print(f"Mediana Empresa A: {mediana_empresa_a}")
print(f"Mediana Empresa B: {mediana_empresa_b}")
