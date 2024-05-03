import math


def desvio_padrao_combinado(desvio_01, desvio_02):
    desvio_combinado = math.sqrt((desvio_01**2 + desvio_02**2) / 2)
    return desvio_combinado
