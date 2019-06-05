import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# -- configurações e o resto do código -- #

# -- bibliotecas -- #

config = {
    'axes.spines.right': False,
    'axes.spines.top':   False,
    'axes.edgecolor':  '.4',
    'axes.labelcolor': '.0',
    'axes.titlesize': 'large',
    'axes.labelsize': 'medium',
    'figure.autolayout': True,
    'figure.figsize': (4.5, 3.5),
    'font.family': ['serif'],
    'font.size': 10.0,
    'grid.linestyle': '--',
    'legend.frameon': True,
    'text.color': '.0',
    'xtick.labelsize': 'small',
    'ytick.labelsize': 'small',
}
plt.style.use(['seaborn-whitegrid', 'seaborn-paper', 'seaborn-muted', config])

# -- resto do código -- #

plt.rcParams['text.usetex'] = True
plt.rcParams['pgf.preamble'] = r"""
    \usepackage[portuguese]{babel}
    \usepackage[T1]{fontenc}
    \usepackage[utf8]{inputenc}
"""
plt.rcParams['pgf.rcfonts'] = False

def read_tsv(arq, decimal=',', **kwargs) -> pd.DataFrame:
    try:
        return pd.read_csv(arq, sep='\t', decimal=decimal, **kwargs)
    except RuntimeError:
        return pd.read_csv(arq, sep='\t', decimal=decimal, **kwargs)


def write_table(df: pd.DataFrame, arq_nome: str, index=False, **kwargs):
    with open(arq_nome, 'w') as arq:
        arq.write(df.to_latex(index=index, **kwargs))
