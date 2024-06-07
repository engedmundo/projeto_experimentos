import math

n = 4 # quantidade total de cores
k = 2 # Quantidade de elementos de cada combinação - pares

combinacoes = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

print(f"Total de combinações: {combinacoes}")
