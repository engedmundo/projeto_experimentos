import math

from equacoes.media import calcula_media
from equacoes.somatorio import calula_somatorio
from equacoes.variancia import calcula_variancia
from equacoes.desvios import calcula_desvios

""""
Deseja-se investigar a relação entre a potência do equipamento e quantidade de
recobrimento depositado em um processo de revestimento para proteção.
Planejou-se executar experimentos em quatro níveis de potência: 160W, 180W,
200W e 220W. A equipe decidiu usar utilizar 5 réplicas. Todos os demais
fatores foram mantidos constantes.
"""
dados_pot_160 = [575, 542, 530, 539, 570]
dados_pot_180 = [565, 593, 590, 579, 610]
dados_pot_200 = [600, 651, 610, 637, 629]
dados_pot_220 = [725, 700, 715, 685, 710]