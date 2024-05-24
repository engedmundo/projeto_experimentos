import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

massa_dos_graos = [
    0.1188,	0.2673,	0.1795,	0.2369,	0.1826,	0.1860,	0.2045, 0.1795,	0.1910,	0.1409,
    0.1733,	0.2146,	0.1965,	0.2326, 0.2382,	0.2091,	0.2660,	0.2126,	0.2048,	0.2058,
    0.1666, 0.2505,	0.1823,	0.1590,	0.1722,	0.1462,	0.1985,	0.1769, 0.1810,	0.2126,
    0.1596,	0.2504,	0.2285,	0.3043,	0.1683, 0.2833,	0.2380,	0.1930,	0.1980,	0.1402,
    0.2060,	0.2097, 0.2309,	0.2458,	0.1496,	0.1865,	0.2087,	0.2335,	0.2173, 0.1746,
    0.1677,	0.2456,	0.1828,	0.1663,	0.1971,	0.2341, 0.2327,	0.2137,	0.1793,	0.2423,
    0.2012,	0.1968,	0.2433, 0.2311,	0.1902,	0.1970,	0.1644,	0.1935,	0.1421,	0.1202,
    0.2459,	0.2098,	0.1817,	0.1736,	0.2296,	0.2200,	0.2025, 0.1996,	0.1995,	0.1732,
    0.1987,	0.2482,	0.1708,	0.2465, 0.2096,	0.2054,	0.1561,	0.1766,	0.2620,	0.1642,
    0.2507, 0.1814,	0.1340,	0.2051,	0.2455,	0.2008,	0.1740,	0.2089, 0.2595,	0.1470,
    0.2674,	0.1701,	0.2055,	0.2215,	0.2080, 0.1848,	0.2184,	0.2254,	0.1573,	0.1696,
    0.2262,	0.1950, 0.1965,	0.1773,	0.1340,	0.2237,	0.1996,	0.1463,	0.1917, 0.2593,
    0.1799,	0.2585,	0.2153,	0.2365,	0.1629,	0.1875, 0.2657,	0.2666,	0.2535,	0.1874,
    0.1869,	0.2266,	0.2143, 0.1399,	0.2790,	0.1988,	0.1904,	0.1911,	0.2186,	0.1606, 
]

dados = { "Massa": massa_dos_graos }
massa_df = pd.DataFrame(dados)
massa_df.head()

# calcular a amplitude
massa_max = massa_df["Massa"].max()
massa_min = massa_df["Massa"].min()
amplitude_amostral = massa_max - massa_min
print(f"Amplitude amostral: {amplitude_amostral:.4f} g")

# calcular o desvio
media = massa_df["Massa"].mean()
print(f"Média: {media:.4f}")
massa_df["Desvio"] = massa_df["Massa"] - media
soma_dos_desvios = massa_df["Desvio"].sum()
print(f"Soma dos desvios: {soma_dos_desvios:.4f}")
# calcular o quadrado dos desvios
massa_df["Quadrado Desvio"] = massa_df["Desvio"] ** 2
soma_quadrado_desvios = massa_df["Quadrado Desvio"].sum()
print(f"Soma quadrado desvios: {soma_quadrado_desvios:.4f} g²")

# calcular a variância
qtd_valores = massa_df["Massa"].count() # N da equação
variancia = (1 / (qtd_valores - 1)) * soma_quadrado_desvios
print(f"Variância: {variancia:.6f}")

variancia_2 = massa_df["Massa"].var()
print(f"Variância 2: {variancia_2:.6f} g²")

# calcular o desvio padrão
desvio_padrao = massa_df["Massa"].std()
print(f"Desvio padrão: {desvio_padrao:.4f} g")
massa_df
