import pandas as pd

diametro = [
    572,
    572,
    573,
    568,
    575,
    565,
    570,
    569,
]

dados = { "Diâmetro": diametro }
diametro_df = pd.DataFrame(dados)

media = diametro_df["Diâmetro"].mean()
mediana = diametro_df["Diâmetro"].median()
variancia = diametro_df["Diâmetro"].var()
desv_pad = diametro_df["Diâmetro"].std()
maximo = diametro_df["Diâmetro"].max()
minimo = diametro_df["Diâmetro"].min()
amplitude = maximo - minimo

print(f"Média: {media:.1f} mm")
print(f"Mediana: {mediana:.1f} mm")
print(f"Variância: {variancia:.1f} mm²")
print(f"Desvio Padrão: {desv_pad:.1f} mm")
print(f"Amplitude: {amplitude:.1f} mm")
