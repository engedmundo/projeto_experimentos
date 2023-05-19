"""
Exemplo 3.2 - Qual a probabilidade de se retirar ao acaso um 
grão de feijão que:
a) pese mais de 0.18g?
b) Quais os pesos máximo e mínimos para uma probabilidade de 95%?
Considere:
- média populacional de 0.2024g
- desvio padrão populacional de 0.0363g
"""
# a)
media_pop = 0.2024
desv_padrao_pop = 0.0363
peso = 0.18
peso_padronizado = (peso - media_pop) / desv_padrao_pop

area_cauda = 0.2676  # Veio da tabela A1
probabilidade = (1 - area_cauda) * 100
print(f"Probabilidade de retirar um grão de feijão maior do que {peso}g")
print(f"é de {probabilidade:.2f}%")


# b)
peso_padronizado_minimo = -1.96  # sai da tabela A1
peso_padronizado_maximo = 1.96  # sai da tabela A1
peso_minimo = peso_padronizado_minimo * desv_padrao_pop + media_pop
peso_maximo = peso_padronizado_maximo * desv_padrao_pop + media_pop
print(f"Resposta B:")
print(f"Para uma probabilidade de 95%, os valores do intervalo são:")
print(f"Peso mínimo: {peso_minimo:.2f}g")
print(f"Peso máximo: {peso_maximo:.2f}g")
