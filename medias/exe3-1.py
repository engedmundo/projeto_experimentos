"""
Exemplo 3.1 - Qual a probabilidade de se retirar ao acaso um 
grão de feijão que pese entre 0.18g e 0.25g?
Considere:
- média populacional de 0.2024g
- desvio padrão populacional de 0.0363g
"""
media_pop = 0.2024
desv_padrao_pop = 0.0363
peso_minimo = 0.18
peso_maximo = 0.25

# Z - peso padronizado (qualquer variável padronizada)
peso_minimo_padronizado = (peso_minimo - media_pop) / desv_padrao_pop
peso_maximo_padronizado = (peso_maximo - media_pop) / desv_padrao_pop
print(f"Peso mínimo padronizado-> {peso_minimo_padronizado:.2f}")
print(f"Peso máximo padronizado-> {peso_maximo_padronizado:.2f}")
area_cauda_inferior = 0.2676  # Veio da tabela A1
area_cauda_superior = 0.0951  # Veio da tabela A1

area_central = 1 - area_cauda_inferior - area_cauda_superior
probabilidade = area_central * 100
print(
    f"Probabilidade de retirar um grao de feijão entre {peso_minimo}g e {peso_maximo}g"
)
print(f"Probabilidade {probabilidade:.2f}%")
