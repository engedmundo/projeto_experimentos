# Calcule a média aritmética do seguinte conjunto de dados
# referente a ensaios de resistência à tração de um material polimérico:
# x1=12.6
# x2=12.9
# x3=13.4
# x4=12.3
# x5=13.6
# x6=13.5
# x7=12.6
# x8=13.1

"""
# Solução 1
x1 = 12.6
x2 = 12.9
x3 = 13.4
x4 = 12.3
x5 = 13.6
x6 = 13.5
x7 = 12.6
x8 = 13.1
x9 = 12.8

soma = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9
print(f"Soma: -> {soma:.1f}")
media = (1 / 9) * soma
print(f"Média: -> {media:.1f}")
"""


import time


# criar função para somar registros
def calula_somatorio(dados):
    soma = 0
    for valor in dados:
        soma = soma + valor
        # print(valor, soma)
        # time.sleep(5)
    return soma


def calcula_media(dados):
    somatorio = calula_somatorio(dados)
    qtd_dados = len(dados)
    media = somatorio / qtd_dados
    return media


lista_dados = [12.6, 12.9, 13.4, 12.3, 13.6, 13.5, 12.6, 13.1]
media = calcula_media(lista_dados)
print(f"Média -> {media:.2f}")
