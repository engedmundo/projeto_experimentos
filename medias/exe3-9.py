"""
Exercício 3.9
Concentração verdadeira - 14.3%
Amostras = 13.7%, 14.0%, 13.9% e 14.1%
Confiabilidade de 95%
"""
# 1º passo - Calcular média, variância e desvio padrão
from equacoes.media import calcula_media
from equacoes.variancia import calcula_variancia
import math

dados_coletados = [13.7, 14.0, 13.9, 14.1]
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
valor_t = 3.182

# 4º passo -> calcular os limites do intervalo de confiança
termo_comum = valor_t * desvio_padrao / math.sqrt(qtd_elementos)
intervalo_inferior = media - termo_comum
intervalo_superior = media + termo_comum
print(f"Intervalo inferior -> {intervalo_inferior:.4f} %")
print(f"Intervalo superior -> {intervalo_superior:.4f} %")
"""
Verifica-se, com 95% de confiança, que a média da população
está representada entre 13.6533% e 14.1967%. Assim, sendo o valor
de referência igual a 14.3%, o método de medição NÃO consegue
reproduzir o processo de medição desejado.
"""