import math


def calcula_mediana(dados):
    lista_ordenada = sorted(dados)
    qtd_dados = len(dados)
    resto_divisao = qtd_dados % 2
    indice = math.floor(qtd_dados / 2)
    mediana = lista_ordenada[indice]
    return mediana
