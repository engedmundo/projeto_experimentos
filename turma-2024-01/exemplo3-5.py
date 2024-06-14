media = 0.2024
desvio_padrao = 0.0363

# intervalo que contenha 95% dos dados
# olhar na tabela - valor de z padronizado para 95%

z_maior = 1.96
z_menor = -1.96

x_maior = z_maior * desvio_padrao + media
x_menor = z_menor * desvio_padrao + media
print(f"Limite superior: {x_maior:.4f} g")
print(f"Limite inferior: {x_menor:.4f} g")
