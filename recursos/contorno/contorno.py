from libs import read_tsv, write_table, pd, plt, np
from matplotlib import tri

def encerra(nome, salvar=True):
    if salvar:
        plt.savefig(nome)
    else:
        plt.show()
    plt.close()

dx = 0.5

dados = read_tsv('dados.tsv')

def get_key(df: pd.DataFrame, key: str, d=1):
    x, dx = key, f'd{key}'
    return df.apply(lambda row: f'${row[x]:.{d}f} \pm {row[dx]:.{d}f}$', axis=1)

write_table(pd.DataFrame({
    'Posição $X$ [\si{\cm}]': get_key(dados, 'x', d=1),
    'Posição $Y$ [\si{\cm}]': get_key(dados, 'y', d=1),
    'Tensão [\si{\\volt}]': get_key(dados, 'V', d=3)
}).head(10), 'dados.tex', dots=True, column_format='ccc', escape=False)

plt.figure(figsize=[3.6, 2.8])


# separando os dados
x, dx = dados['x'], dados['dx']
y, dy = dados['y'], dados['dy']
V, dV = dados['V'], dados['dV']

# faz o contorno
plt.tricontour(x, y, V)


encerra('base.pgf')

plt.figure(figsize=[3.6, 2.8])


# curvas de nível
plt.tricontour(x, y, V, cmap='winter_r')
# barra de cores
plt.colorbar()


encerra('cmap.pgf')

plt.figure(figsize=[3.6, 2.8])


# niveis a serem desenhados
niveis = [0.34, 0.66, 1.00, 1.33, 1.65]

# curvas de nível
plt.tricontour(x, y, V, niveis, cmap='winter_r')
# barra de cores
plt.colorbar()


encerra('niveis.pgf')
plt.figure(figsize=[3.15, 2.45])

niveis = [0.33, 0.66, 1.00, 1.33, 1.66]
plt.tricontour(x, y, V, niveis, cmap='winter_r')
plt.colorbar()
encerra('problema.pgf')

# -- depois de separar os dados -- #

# niveis a serem desenhados
niveis = [0.34, 0.66, 1.00, 1.33, 1.65]

# curvas de nível e escala de cores
plt.tricontour(x, y, V, niveis, cmap='winter_r', extend='both')
escala_de_cores = plt.colorbar()

# textos
escala_de_cores.set_label('Tensão [$V$]')
plt.xlabel('Posição X [$cm$]')
plt.ylabel('Posição Y [$cm$]')
plt.title('Potencial na Cuba com uma Ponta em uma das Placas')

# -- salva a figura -- #

encerra('completo.pgf')
