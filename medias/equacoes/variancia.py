from .media import calcula_media


def calcula_variancia(dados):
    media = calcula_media(dados)
    soma_desvios = 0

    for valor in dados:
        resultado_parcial = (valor - media) ** 2
        soma_desvios += resultado_parcial

    qtd_elementos = len(dados)
    termo_graus_liberdade = 1 / (qtd_elementos - 1)
    variancia = termo_graus_liberdade * soma_desvios

    return variancia
