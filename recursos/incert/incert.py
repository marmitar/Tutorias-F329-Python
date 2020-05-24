from libs import pd, np, plt, read_tsv, write_table
from scipy import odr

dados = read_tsv('dados.tsv')

k, c, u = 0, 0, 0
write_table(pd.DataFrame({
        k: dados.apply(lambda x: f'${x[c]:.2f} \\pm {x["d"+str(c)]:.2f}$', axis=1)
        for k, c in zip(['Tensão [V]', 'Corrente [mA]'], ['V', 'I'])
    }), 'dados.tex', column_format='rr', escape=False)

# -- recupera os dados antes -- #

# guarda as colunas em variáveis novas
x, dx = dados['V'], dados['dV']
y, dy = dados['I'], dados['dI']

# e coloca os dados pontuais com barras de incerteza
plt.errorbar(
    x, y, xerr=dx, yerr=dy,
    fmt='o', elinewidth=2/3, capsize=2, capthick=2/3, color='black',
    zorder=10, label='Dados Coletados'
)

# -- para fazer a regressão depois -- #

# regressão linear com incertezas
data = odr.RealData(x, y, sx=dx, sy=dy)
odreg = odr.ODR(data, odr.models.unilinear)
#odreg.set_job(fit_type=2)  # mínimos quadrados não suporta incertezas em x
ans = odreg.run()

a, b = ans.beta                         # y = ax + b
da, db = np.sqrt(np.diag(ans.cov_beta)) # incertezas de a e b

# mostrando os coeficientes e suas incertezas
print(f'coef. angular = ({a}+-{da}) [mA/V -> kOhm^-1 -> kS]')
print(f'coef. linear  = ({b}+-{db}) [mA]')

# -- desenha a reta resultante da regressão e completa o gráfico -- #

rotulo = f'Regressão: $y = ({a:.1f} \pm {da:.1f})~x + ({b:.1f} \pm {db:.1f})$'

# monta os limites para desenho da reta
X = np.linspace(min(x), max(x), num=200)
Y =  a * X + b
# e faz o gráfico dela atrá dos pontos
plt.plot(X, Y, color='red', alpha=0.4, label=rotulo)

# para exibir as legendas do gráfico
plt.legend()

plt.xlabel('Tensão [V]')
plt.ylabel('Corrente [mA]')
plt.title('Regressão Linear da Corrente pela Tensão em um Resistor')

plt.savefig('resultado.pgf')
