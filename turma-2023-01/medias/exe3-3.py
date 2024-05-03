from equacoes.media import calcula_media
import math

"""
3-4 - Determine, com 95% de confiança, o intervalo de confiança
para o número de grãos de feijão em um pacote de 1kg de feijão
a partir de uma unidade com massa de 0.1795g.
Considere o desvio padrão populacional de 0.0363g
peso_grao = 0.1795
z = 1.96
desvio_padrao = 0.0363

limite_inferior = peso_grao - z * desvio_padrao  # subtrair
limite_superior = peso_grao + z * desvio_padrao  # somar
print(f"Limite inferior da média -> {limite_inferior:.4f}g")
print(f"Limite superior da média -> {limite_superior:.4f}g")

qtd_maxima_graos = int(1000 / limite_inferior)
qtd_minima_graos = int(1000 / limite_superior)

print("Pode-se dizer, com 95% de certeza, que existem entre")
print(f"{qtd_minima_graos} e {qtd_maxima_graos} grãos em um pacote de 1kg de feijão")
"""

#### Usando a média para calcular os intervalos de confiança
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
    0.1733,
]
media = calcula_media(valores)
desvio_padrao = 0.0363
z = 1.96  # para 95%
qtd_elementos = len(valores)  # N

termo_igual = z * desvio_padrao / math.sqrt(qtd_elementos)
intervalo_inferior = media - termo_igual
intervalo_superior = media + termo_igual

print(f"Limite inferior da média -> {intervalo_inferior:.4f}g")
print(f"Limite superior da média -> {intervalo_superior:.4f}g")

qtd_maxima_graos = int(1000 / intervalo_inferior)
qtd_minima_graos = int(1000 / intervalo_superior)

print("Pode-se dizer, com 95% de certeza, que existem entre")
print(f"{qtd_minima_graos} e {qtd_maxima_graos} grãos em um pacote de 1kg de feijão")