from equacoes.media import calcula_media
from equacoes.mediana import calcula_mediana


# endereço=    0    1    2     3     4     5     6    ....
lista_dados = [1.7, 2.2, 3.9, 3.11, 14.7]
media = calcula_media(lista_dados)
print(f"Média -> {media:.2f}")
mediana = calcula_mediana(lista_dados)
print(f"Mediana -> {mediana}")
