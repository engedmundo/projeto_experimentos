import math
from scipy.stats import norm

# definir variáveis
desvio_padrao = 6
nivel_confianca = 0.95 
qtd_amostras = 50

# encontrar valor z
area = nivel_confianca / 2 + 0.5
valor_z = norm.ppf(area)
print(f"Valor Z: {valor_z}")

# encontrar margem de erro
erro = valor_z * (desvio_padrao / math.sqrt(qtd_amostras))
print(f"Margem de erro: R$ {erro:.2f}")
