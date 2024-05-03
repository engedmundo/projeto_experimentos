from equacoes.media import calcula_media
from equacoes.variancia import calcula_variancia
from equacoes.interpolacao import calcula_interpolacao
import math
""""
Um engenheiro está estudando o efeito de duas diferentes formulações de
polímero na sua resistência à tração. Cada formulação é um nível de um
fator ou tratamento. São fabricadas 10 amostras de cada tratamento
(10 réplicas)

A partir dos dados apresentados da tabela 1, efetue e responda:
a) Determine a média, variância e desvio padrão;
b) Há diferença significativa entre as duas amostras? (aplique o teste t)
"""
formulacao_01 = [
    16.85, 16.40, 17.21, 16.35, 16.52,
    17.04, 16.96, 17.15, 16.59, 16.57,
]

formulacao_02 = [
    16.62, 16.75, 17.37, 17.12, 16.98,
    16.87, 17.34, 17.02, 17.08, 17.27,
]

### Calcular média, variancia e desvio padrão
# Formulação 01
media_01 = calcula_media(formulacao_01)
variancia_01 = calcula_variancia(formulacao_01)
desvio_padrao_01 = math.sqrt(variancia_01)

print("###### Formulação 01 ########")
print(f"Média: {media_01:.3f} kgf m²")
print(f"Variância: {variancia_01:.4f} (kgf m²)²")
print(f"Desvio Padrão: {desvio_padrao_01:.4f} kgf m²")
print()

# Formulação 02
media_02 = calcula_media(formulacao_02)
variancia_02 = calcula_variancia(formulacao_02)
desvio_padrao_02 = math.sqrt(variancia_02)

print("###### Formulação 02 ########")
print(f"Média: {media_02:.3f} kgf m²")
print(f"Variância: {variancia_02:.4f} (kgf m²)²")
print(f"Desvio Padrão: {desvio_padrao_02:.4f} kgf m²")
print()

# Teste t-student, caso 2
# hipótese nula - médias iguais
# hipótese alternativa - médias diferentes

s_12 = math.sqrt((variancia_01 + variancia_02) / 2)  # desvio padrão combinado
replicas = len(formulacao_01)  # N
valor_t = (media_01 - media_02) / (s_12 * math.sqrt(2 / replicas))
graus_liberdade = 2 * replicas - 2

print("#######  Teste t-student  ########")
print(f"N: {replicas} replicas")
print(f"Graus de Liberdade: {graus_liberdade}")
print(f"Valor t: {valor_t:.3f}")
# com valor t, consultamos a tabela II pg 686/702 livro
"""
valor_t0=2.101
area_0=0.025
valor_t1=2.552
area_1=0.01
"""
valor_p_unicaudal = calcula_interpolacao(
    area_0=0.025,
    area_1=0.01,
    valor_t_0=2.101,
    valor_t_1=2.552,
    valor_t=abs(valor_t),
)
valor_p = valor_p_unicaudal * 2
print(f"Valor P: {valor_p:.4f}")
probabilidade = valor_p * 100
print(f"Probabilidade de {probabilidade:.2f}%")

"""
Ponto de corte geralmente 0.05
Se valor P for menor do 0.05 deve-se rejeitar a hipótese nula
h0 diz que as médias são iguais
Rejeitar a hipótese nula significa dizer que as médias
são DIFERENTES!!!!!

Se a diferença entre as médias é estatisticamente significativa
existe efeito da formulação na resistência a tração 
do material estudado.
"""