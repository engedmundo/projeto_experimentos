def calcula_desvios(dados, media):
    quadrado_dos_desvios = list()
    for valor in dados:
        desvio = (valor - media) ** 2
        quadrado_dos_desvios.append(desvio)

    return quadrado_dos_desvios
