"""
Verifique se o lote de uma produção cervejeira atende 
a porcentagem mínima de 4% de alcool. Considere a 
seguinte amostra:
3.91%, 4.01%, 3.61%, 3.83%, 3.75%.
Faça suas conclusões com base em uma probabilidade mínima
de 95%
"""
# 1º passo - Calcular média, variância e desvio padrão
from equacoes.media import calcula_media
from equacoes.variancia import calcula_variancia
import math

dados_coletados = [3.91, 4.01, 3.61, 3.83, 3.75]
media = calcula_media(dados_coletados)
variancia = calcula_variancia(dados_coletados)
desvio_padrao = math.sqrt(variancia)

print(f"Média -> {media:.2f} %")
print(f"Variância -> {variancia:.4f} %^2")
print(f"Desvio padrão -> {desvio_padrao:.4f} %")

# 2º passo -> determinar número de elementos (N) e graus de liberdade
qtd_elementos = len(dados_coletados)
graus_liberdade = qtd_elementos - 1
print(f"N -> {qtd_elementos}")
print(f"Graus de liberdade (v) -> {graus_liberdade}")

# 3º passo -> consultar o valor t na tabela t-Student
valor_t = 2.776

# 4º passo -> calcular os limites do intervalo de confiança
termo_comum = valor_t * desvio_padrao / math.sqrt(qtd_elementos)
intervalo_inferior = media - termo_comum
intervalo_superior = media + termo_comum
print(f"Intervalo inferior -> {intervalo_inferior:.4f} %")
print(f"Intervalo superior -> {intervalo_superior:.4f} %")
"""
Conclusão - sendo o valor mínimo admissível igual a 4%, o lote cervejeiro
deve ser recusado, uma vez que a média do lote pode ser de, no máximo,
4.01% de alcool, com confiança de 95%
A média é maior do que 3.6324% e menor do que 4.0116%.
"""

# Descobrindo o número de amostras para uma precisão de 0.1%
precisao = 0.15

tamanho_amostra = (valor_t * desvio_padrao / precisao) ** 2
print(f"Tamanho mínimo da amostra -> {tamanho_amostra:.2f} elementos")

