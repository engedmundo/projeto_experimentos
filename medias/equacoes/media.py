from .somatorio import calula_somatorio


def calcula_media(dados):
    somatorio = calula_somatorio(dados)
    qtd_dados = len(dados)
    media = somatorio / qtd_dados
    return media
