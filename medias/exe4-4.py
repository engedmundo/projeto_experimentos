import math

from equacoes.media import calcula_media
from equacoes.somatorio import calula_somatorio
from equacoes.variancia import calcula_variancia

"""
Deseja-se investigar a influência do material e da temperatura
na vida de baterias usadas em um determinado dispositivo. 
Serão investigados 2 materiais em 2 níveis de temperatura. 
A equipe decidiu usar utilizar 4 réplicas. Todos os demais 
fatores foram mantidos constantes.

"""
dados_litio_10 = [130, 155, 74, 180]
dados_litio_51 = [20, 70, 82, 58]
dados_niobio_10 = [138, 110, 168, 160]
dados_niobio_51 = [96, 104, 82, 60]

# Média, variância e desvio padrão
# Lítio - -10ºC
media_litio_10 = calcula_media(dados_litio_10)
variancia_litio_10 = calcula_variancia(dados_litio_10)
desvio_padrao_litio_10 = math.sqrt(variancia_litio_10)

print("### Litio - 10º C ###")
print(f"Média: {media_litio_10:.2f} horas")
print(f"Variância: {variancia_litio_10:.2f} horas²")
print(f"Desvio Padrão: {desvio_padrao_litio_10:.2f} horas")
print()

# Média, variância e desvio padrão
# Lítio - 51ºC
media_litio_51 = calcula_media(dados_litio_51)
variancia_litio_51 = calcula_variancia(dados_litio_51)
desvio_padrao_litio_51 = math.sqrt(variancia_litio_51)

print("### Litio - 51º C ###")
print(f"Média: {media_litio_51:.2f} horas")
print(f"Variância: {variancia_litio_51:.2f} horas²")
print(f"Desvio Padrão: {desvio_padrao_litio_51:.2f} horas")
print()

# Média, variância e desvio padrão
# Nióbio - -10ºC
media_niobio_10 = calcula_media(dados_niobio_10)
variancia_niobio_10 = calcula_variancia(dados_niobio_10)
desvio_padrao_niobio_10 = math.sqrt(variancia_niobio_10)

print("### Nióbio - 10º C ###")
print(f"Média: {media_niobio_10:.2f} horas")
print(f"Variância: {variancia_niobio_10:.2f} horas²")
print(f"Desvio Padrão: {desvio_padrao_niobio_10:.2f} horas")
print()

# Média, variância e desvio padrão
# Nióbio - 51ºC
media_niobio_51 = calcula_media(dados_niobio_51)
variancia_niobio_51 = calcula_variancia(dados_niobio_51)
desvio_padrao_niobio_51 = math.sqrt(variancia_niobio_51)

print("### Nióbio - 51º C ###")
print(f"Média: {media_niobio_51:.2f} horas")
print(f"Variância: {variancia_niobio_51:.2f} horas²")
print(f"Desvio Padrão: {desvio_padrao_niobio_51:.2f} horas")
print()


# Cálculo dos efeitos:
ab = media_litio_10
Ab = media_niobio_10
aB = media_litio_51
AB = media_niobio_51

# Efeito do material
efeito_material = (((Ab + AB) / 2) - ((ab + aB) / 2))

# Efeito da temperatura
efeito_temperatura = (((aB + AB) / 2) - ((ab + Ab) / 2))

# Efeito da interação
efeito_interacao = ((AB - aB) - (Ab - ab)) / 2

print(f"Efeito da temperatura: {efeito_temperatura:.2f} horas")
print(f"Efeito da material: {efeito_material:.2f} horas")
print(f"Efeito da interação: {efeito_interacao:.2f} horas")
print()

# todos os dados
todos_dados = [*dados_litio_10, *dados_litio_51, *dados_niobio_10, *dados_niobio_51]
media_geral = calcula_media(todos_dados)
print(f"Média geral: {media_geral:.2f} horas")
print()

"""
# Equação de efeitos:
tempo = media_geral + efeito_temperatura / 2 * nivel_temperatura +
efeito_material / 2 * nivel_material * efeito_interacao / 2 * nivel_material * nivel_temperatura
+ erro_aleatorio

niveis são -1 e 1 de cada fator

chega nos valores da media de cada combinação
"""
