from libs import pd, np, plt, read_tsv, write_table
from scipy import odr

dados = read_tsv('wheat.tsv')


def pontos(dados):

    # -- recupera os dados antes -- #

    x, dx = dados['Rx'], dados['dRx']
    y, dy = dados['Rd'], dados['dRd']

    plt.errorbar(
        x, y, xerr=dx, yerr=dy,
        fmt='o', elinewidth=2/3, capsize=2, capthick=2/3, color='black',
        zorder=10, label='Dados Coletados'
    )

    # escala log-log
    plt.xscale('log')
    plt.yscale('log')

    # linhas de grid internas
    plt.grid(True, which='minor', axis='both', color='0.9')

    # -- depois completa os textos e salva a imagem -- #

    textos()
    return x, y, dx, dy


def regres(dados):
    x, y, dx, dy = pontos(dados)

    # transforma os dados para a linearização
    logx = np.log10(x)
    logy = np.log10(y)

    dlogx = dx / (x * np.log(10))
    dlogy = dy / (y * np.log(10))

    # regressão linear com incertezas
    data = odr.RealData(logx, logy, sx=dlogx, sy=dlogy)
    odreg = odr.ODR(data, odr.models.unilinear)
    ans = odreg.run()

    a, b = ans.beta                         # logy = a logx + b
    da, db = np.sqrt(np.diag(ans.cov_beta)) # incertezas de a e b

    # mostrando os coeficientes e suas incertezas
    print(f'coef. angular = {a}+-{da}')
    print(f'coef. linear  = {b}+-{db}')

    # -- desenha a reta resultante da regressão e completa o gráfico -- #

    rotulo = 'Regressão Linearizada'

    rotulo = f'''Regressão Linearizada:
    $\log_{{10}}y = ({a:.1f} \pm {da:.1f}) \\times \log_{{10}}x + ({b:.1f} \pm {db:.1f})$'''

    # monta os limites para desenho da reta
    X = np.logspace(min(logx), max(logx), num=200)
    Y =  10 ** (a*np.log10(X) + b)
    # e faz o gráfico dela atrá dos pontos
    plt.plot(X, Y, color='red', alpha=0.4, label=rotulo)

    # para exibir as legendas do gráfico
    plt.legend()

    textos()


def textos():
    plt.xlabel('Resistência Desconhecida [$\Omega$]')
    plt.ylabel('Resistência da Década [$\Omega$]')
    plt.title('''Relação das Resistências em uma
    Ponte de Wheatstone Equilibrada''')



pontos(dados)
plt.savefig('loglog.pgf')


plt.close()
regres(dados)
plt.savefig('regres.pgf')


fig = plt.figure(figsize=[3.6, 2.8])
x, dx = dados['Rx'], dados['dRx']
y, dy = dados['Rd'], dados['dRd']

ax = fig.add_subplot()
ax.errorbar(
    x, y, xerr=dx, yerr=dy,
    fmt='o', elinewidth=2/3, capsize=2, capthick=2/3, color='black',
    zorder=10, label='Dados Coletados'
)

textos()

fig.savefig('wdados.pgf')
