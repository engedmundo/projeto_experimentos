from equacoes.media import calcula_media
from equacoes.mediana import calcula_mediana

lista_dados = [
    3.4,
    2.5,
    4.8,
    2.9,
    3.6,
    2.8,
    3.3,
    5.6,
    3.7,
    2.8,
    4.4,
    4.0,
    5.2,
    3.0,
    4.8,
]

tamanho_amostra = len(lista_dados)
print(f"Tamanho da amostra: {tamanho_amostra}")

media = calcula_media(lista_dados)
print(f"Média: {media:.2f}")

mediana = calcula_mediana(lista_dados)
print(f"Mediana: {mediana:.2f}")
