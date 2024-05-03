def calcula_interpolacao(
    area_0,
    area_1,
    valor_t_0,
    valor_t_1,
    valor_t,
):
    termo_parcial_t = (valor_t - valor_t_0) / (valor_t_1 - valor_t_0)
    valor_p = area_0 + (area_1 - area_0) * termo_parcial_t
    return valor_p
