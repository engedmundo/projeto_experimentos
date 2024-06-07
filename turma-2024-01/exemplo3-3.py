import math

qtd_questoes_n = 10 # número de questoes -> n - total de eventos
# quantas alternativas por questao?
alternativas = 5
# Específica do evento 
probabilidade_sucesso_p = 1 / alternativas # acertar uma questao isolada
probabilidade_fracasso_q = 1 - probabilidade_sucesso_p

print(f"Probabilidade sucesso: {probabilidade_sucesso_p}")
print(f"Probabilidade fracasso: {probabilidade_fracasso_q}")

# quantidade de questoes que devo acertar
eventos_sucesso_k = 7

# determinar numero de combinações
combinacoes = math.factorial(qtd_questoes_n) / (math.factorial(eventos_sucesso_k) * math.factorial(qtd_questoes_n - eventos_sucesso_k))

print(f"Combinações: {combinacoes}")

# probabilidade de acertar 7 questoes em 10
probabilidade = combinacoes * (probabilidade_sucesso_p ** eventos_sucesso_k) * (probabilidade_fracasso_q ** (qtd_questoes_n - eventos_sucesso_k))

print(f"Probabilidade de acertar 7 questões: {probabilidade * 100:.6f} %")
