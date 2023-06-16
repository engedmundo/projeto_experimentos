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
pot_160 = [575, 542, 530, 539, 570]  # unidade - micrômetros
pot_180 = [565, 593, 590, 579, 610]  # unidade - micrômetros
pot_200 = [600, 651, 610, 637, 629]  # unidade - micrômetros
pot_220 = [725, 700, 715, 685, 710]  # unidade - micrômetros

### Calcular média, variancia e desvio padrão
# Potência de 160 W
media_160 = calcula_media(pot_160)
variancia_160 = calcula_variancia(pot_160)
desvio_padrao_160 = math.sqrt(variancia_160)

print("###### Potência 160 W ########")
print(f"Média: {media_160:.3f} um²")
print(f"Variância: {variancia_160:.4f} (um²)²")
print(f"Desvio Padrão: {desvio_padrao_160:.4f} um²")
print()

# Potência de 180 W
media_180 = calcula_media(pot_180)
variancia_180 = calcula_variancia(pot_180)
desvio_padrao_180 = math.sqrt(variancia_180)

print("###### Potência 180 W ########")
print(f"Média: {media_180:.3f} um²")
print(f"Variância: {variancia_180:.4f} (um²)²")
print(f"Desvio Padrão: {desvio_padrao_180:.4f} um²")
print()

# Potência de 200 W
media_200 = calcula_media(pot_200)
variancia_200 = calcula_variancia(pot_200)
desvio_padrao_200 = math.sqrt(variancia_200)

print("###### Potência 200 W ########")
print(f"Média: {media_200:.3f} um²")
print(f"Variância: {variancia_200:.4f} (um²)²")
print(f"Desvio Padrão: {desvio_padrao_200:.4f} um²")
print()

# Potência de 220 W
media_220 = calcula_media(pot_220)
variancia_220 = calcula_variancia(pot_220)
desvio_padrao_220 = math.sqrt(variancia_220)

print("###### Potência 220 W ########")
print(f"Média: {media_220:.3f} um²")
print(f"Variância: {variancia_220:.4f} (um²)²")
print(f"Desvio Padrão: {desvio_padrao_220:.4f} um²")
print()

# Calcular a média global
# colocar todos os dados dentro da mesma lista
todos_dados = [*pot_160, *pot_180, *pot_200, *pot_220]
media_global = calcula_media(todos_dados)
variancia_global = calcula_variancia(todos_dados)
desvio_padrao_global = math.sqrt(variancia_global)

print("###### Todos os dados ########")
print(f"Média: {media_global:.3f} um²")
print(f"Variância: {variancia_global:.4f} (um²)²")
print(f"Desvio Padrão: {desvio_padrao_global:.4f} um²")
print()

###  ANOVA ###
"""
SQtotal = SQpotencia + SQerros
SQtotal = soma(cada_valor - media_global)^2
SQtotal = (575 - 617.75)² + (542 - 617.75)² + ... 
"""
desvios_global = calcula_desvios(
    dados=todos_dados,
    media=media_global,
)
sq_total = calula_somatorio(desvios_global)  # Soma dos Quadrados total

"""
SQpotencia = 4 *[(551.2 - 617.75)² + (587.4 - 617.75)²+..]
"""
medias = [media_160, media_180, media_200, media_220]
desvios_potencia = calcula_desvios(
    dados=medias,
    media=media_global,
)
soma_potencia = calula_somatorio(desvios_potencia)
sq_potencia = len(medias) * soma_potencia
sq_erros = sq_total - sq_potencia

print(f"SQpotencia: {sq_potencia:.3f}")
print(f"SQerros:    {sq_erros:.3f}")
print(f"SQtotal:    {sq_total:.3f}")
print()


# Graus de liberdade:
niveis = 4
qtd_total = len(todos_dados)
gl_potencia = niveis - 1
gl_erro =  qtd_total - niveis
gl_total = qtd_total - 1
print(f"GL potencia: {gl_potencia:.3f}")
print(f"GL erros:    {gl_erro:.3f}")
print(f"GL total:    {gl_total:.3f}")
print()

# Media dos quadrados
mq_potencia = sq_potencia / gl_potencia
mq_erro = sq_erros / gl_erro
print(f"MQ potencia: {mq_potencia:.3f}")
print(f"MQ erros:    {mq_erro:.3f}")
print()

# estatistica F
valor_f = mq_potencia / mq_erro
print(f"Valor F: {valor_f:.3f}")

