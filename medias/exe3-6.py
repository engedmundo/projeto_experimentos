from equacoes.media import calcula_media
from equacoes.variancia import calcula_variancia
import math

"""
3-6 - Determine, com 95% de confiança, o intervalo de confiança
para o número de grãos de feijão em um pacote de 1kg de feijão
a partir de uma lista com 10 valores.
"""
valores = [
    0.1188,
    0.2673,
    0.1795,
    0.2369,
    0.1826,
    0.1860,
    0.2045,
    0.1795,
    0.1910,
    0.1409,
]
# calcular a média, desvio padrão
media = calcula_media(valores)  # x barra
variancia = calcula_variancia(valores)  # s^2
desvio_padrao = math.sqrt(variancia)  # s
print(f"Média -> {media:.4f}g")
print(f"Desvio padrão -> {desvio_padrao:.4f}g")

# calcular quantidade de elementos, graus de liberdade
qtd_elementos = len(valores)  # N
graus_liberdade = qtd_elementos - 1  # v (ní)
print(f"Quantidade de elementos -> {qtd_elementos}")
print(f"Graus de liberdade -> {graus_liberdade}")

# encontrar valor t na tabela A2 (95% de probabilidade)
valor_t = 2.262
# calcular valor do termo em comum
termo_comum = valor_t * desvio_padrao / math.sqrt(qtd_elementos)

# calcular os valores de limite inferior e superior
limite_inferior = media - termo_comum
limite_superior = media + termo_comum

# primeira conclusão
# Probabilidade da média:
print(f"95% de probabilidade que o peso médio do grão do pacote")
print(f"esteja entre {limite_inferior:.4f}g e {limite_superior:.4f}g")

# segunda conclusão
qtd_minima = int(1000 / limite_superior)
qtd_maxima = int(1000 / limite_inferior)
print(f"95% de probabilidade que existam entre")
print(f"{qtd_minima} e {qtd_maxima} grãos no pacote.")
