import math


def calula_somatorio(dados):
    soma = 0
    for valor in dados:
        soma = soma + valor
    return soma


def calcula_media(dados):
    somatorio = calula_somatorio(dados)
    qtd_dados = len(dados)
    media = somatorio / qtd_dados
    return media


def calcula_mediana(dados):
    # ordena uma lista em ordem crescente
    lista_ordenada = sorted(dados)
    # retorna a quantidade de elementos da lista
    qtd_dados = len(dados)
    # % retorna o resto da divisão entre dois números
    resto_divisao = qtd_dados % 2
    # math.floor() arredonda um valor para baixo
    indice = math.floor(qtd_dados / 2)
    # lista[indice] retorna o elemento no endereço indice
    mediana = lista_ordenada[indice]
    return mediana


# endereço=    0    1    2     3     4     5     6    ....
lista_dados = [1.7, 2.2, 3.9, 3.11, 14.7]
media = calcula_media(lista_dados)
print(f"Média -> {media:.2f}")
mediana = calcula_mediana(lista_dados)
print(f"Mediana -> {mediana}")
