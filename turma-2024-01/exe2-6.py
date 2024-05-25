import pandas as pd

concentracao = [
    3.91,
    4.01,
    3.61,
    3.83,
    3.75,
    3.91,
    3.82,
    3.70,
    3.50,
    3.77,
    3.96,
    3.85,
    3.67,
    3.83,
    3.77,
    3.51,
    3.85,
    4.04,
    3.74,
    3.97,
]

dados = { "Concentração": concentracao}
concentracao_df = pd.DataFrame(dados)

quartis = [0.25, 0.50, 0.75]
for numero in quartis:
    valor_quartil = concentracao_df["Concentração"].quantile(numero)
    print(f"Quartil {numero * 100}%: {valor_quartil:.2f}")

print("-" * 30)

decis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for numero in decis:
    valor_decil = concentracao_df["Concentração"].quantile(numero)
    print(f"Decil {numero * 100}%: {valor_decil:.2f}")

print("-" * 30)

media = concentracao_df["Concentração"].mean()
variancia = concentracao_df["Concentração"].var()
desvio_padrao = concentracao_df["Concentração"].std()

print(f"Média: {media:.2f} %")
print(f"Variância: {variancia:.2f} %²")
print(f"Desvio Padrão: {desvio_padrao:.2f} %")
