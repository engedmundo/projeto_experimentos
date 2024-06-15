import math
# para usar a tabela t-Student, altera a importação
from scipy.stats import t

media = 0.2024
desvio_padrao = 0.0363
qtd_amostras = 140
nivel_confiabilidade = 0.95

area = nivel_confiabilidade / 2 + 0.5
graus_liberdade = qtd_amostras - 1
valor_t = t.ppf(area, graus_liberdade)
margem_erro = valor_t * (desvio_padrao / math.sqrt(qtd_amostras))

print(f"Valor t: {valor_t}")
print(f"Margem de erro: {margem_erro:.4f}")

limite_inferior = media - margem_erro
limite_superior = media + margem_erro
print(f"Limite inferior: {limite_inferior:.4f} g")
print(f"Limite superior: {limite_superior:.4f} g")
