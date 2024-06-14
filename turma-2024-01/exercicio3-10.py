import math
from scipy.stats import norm

# variáveis
qtd_amostras = 1976
desvio_padrao = 11
media = 28
nivel_confiabilidade = 0.9

# Para determinar intervalo de confiança para a média
# primeiro devemos calcular a margem de erro
area = nivel_confiabilidade / 2 + 0.5
valor_z = norm.ppf(area)
margem_erro = valor_z * (desvio_padrao / math.sqrt(qtd_amostras))
print(f"Valor de Z: {valor_z}")
print(f"Margem de erro: {margem_erro}")
# intervalo de confiança para 90%
media_inferior = media - margem_erro
media_superior = media + margem_erro
print(f"Limite superior: {media_superior:.2f}")
print(f"Limite inferior: {media_inferior:.2f}")
