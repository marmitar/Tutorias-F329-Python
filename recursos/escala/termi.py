from libs import pd, np, plt, read_tsv, write_table
from scipy import odr

dados = read_tsv('termi.tsv')


def pontos(dados):

    # -- recupera os dados antes -- #

    T, dT = dados['T'], dados['dT']
    y, dy = dados['R'], dados['dR']

    # transformação do eixo x
    x = 1/T
    dx = dT/T**2

    plt.errorbar(
        x, y, xerr=dx, yerr=dy,
        fmt='o', elinewidth=2/3, capsize=2, capthick=2/3,
        color='black', zorder=10,
    )

    # escala logarítmica
    plt.yscale('log')

    # linhas de grid internas no eixo y
    plt.grid(True, which='minor', axis='y', color='0.9')

    # -- depois completa os textos e salva a imagem -- #

    textos(True)
    return x, y, dx, dy


def textos(inv):
    plt.xlabel('Temperatura [$K$]' if not inv else '1/T [$K^{-1}$]')
    plt.ylabel('Resistência [$\Omega$]')
    plt.title(f'''Relação da Resistência pel{"""a
    """ if not inv else """o Inverso
    da"""} Temperatura em um Termistor''')



pontos(dados)
plt.savefig('semilog.pgf')


fig = plt.figure(figsize=[3.6, 2.8])
x, dx = dados['T'], dados['dT']
y, dy = dados['R'], dados['dR']

ax = fig.add_subplot()
ax.errorbar(
    x, y, xerr=dx, yerr=dy,
    fmt='o', elinewidth=2/3, capsize=2, capthick=2/3, color='black',
    zorder=10, label='Dados Coletados'
)

textos(False)

fig.savefig('tdados.pgf')
