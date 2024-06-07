# pip install scipy

import pandas as pd
import numpy as np
from scipy.stats import norm

tabela_normal_padronizada = pd.DataFrame(
    list(),
    index=["{0:0.2f}".format(i/100) for i in range(0, 400, 10)],
    columns=["{0:0.2f}".format(i/100) for i in range(0,10)],
)
for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        value_z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(value_z))

tabela_normal_padronizada.rename_axis("Z",axis="columns", inplace=True)
tabela_normal_padronizada
