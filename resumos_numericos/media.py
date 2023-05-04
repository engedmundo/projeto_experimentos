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
