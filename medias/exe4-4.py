import math

from equacoes.interpolacao import calcula_interpolacao
from equacoes.media import calcula_media
from equacoes.somatorio import calula_somatorio
from equacoes.teste_t import desvio_padrao_combinado
from equacoes.variancia import calcula_variancia
from equacoes.desvios import calcula_desvios

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