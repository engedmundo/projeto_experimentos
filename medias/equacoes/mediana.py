import math


def calcula_mediana(dados):
    lista_ordenada = sorted(dados)
    qtd_dados = len(dados)
    resto_divisao = qtd_dados % 2
    indice = math.floor(qtd_dados / 2)

    if resto_divisao == 0:  # par
        mediana = (lista_ordenada[indice] + lista_ordenada[indice - 1]) / 2
    else:  # se for impar
        mediana = lista_ordenada[indice]

    return mediana
