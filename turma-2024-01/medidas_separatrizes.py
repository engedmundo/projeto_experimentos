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

# a função quantile faz a divisão percentual do 
# total da quantidade de dados
massa_df["Massa"].quantile(0.15)

# quartis - dividir os dados em 4 partes iguais
quartil_25 = massa_df["Massa"].quantile(0.25)
print(f"Quartil 25%: {quartil_25:.4f}")
quartil_50 = massa_df["Massa"].quantile(0.50)
print(f"Quartil 50%: {quartil_50:.4f}")
quartil_75 = massa_df["Massa"].quantile(0.75)
print(f"Quartil 75%: {quartil_75:.4f}")

# decis - dividir os dados em 10 partes iguais
# usar funções de repetição - loops
# for
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# para cada numero em números
for numero in numeros:
    print(f"O número é: {numero}")


quartis = [0.25, 0.50, 0.75]
for numero in quartis:
    valor_quartil = massa_df["Massa"].quantile(numero)
    print(f"Quartil {numero * 100}%: {valor_quartil:.4f}")

decis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for numero in decis:
    valor_decil = massa_df["Massa"].quantile(numero)
    print(f"Decil {numero * 100}%: {valor_decil:.4f}")

percentis = [numero / 100 for numero in range(1, 100)]
for numero in percentis:
    valor_percentil = massa_df["Massa"].quantile(numero)
    print(f"Percentil {numero * 100}%: {valor_percentil:.4f}")
# percentis - dividir os dados em 100 partes iguais


# boxplot
plt.figure(figsize=(8,6))
boxplot = sns.boxplot(
    x="Massa", # nome da coluna
    data=massa_df, # tabela
)
boxplot.set(xlabel="Massa (g)")
plt.title("Box Plot")
plt.show()
