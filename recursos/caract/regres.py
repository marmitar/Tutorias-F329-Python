from libs import pd, np, plt, read_tsv, write_table
from scipy import odr

dados = read_tsv('termistor.tsv')

T, dT = dados['T'], dados['dT']
y, dy = dados['R'], dados['dR']

x, dx = 1/T, dT/T**2

plt.errorbar(
    x, y, xerr=dx, yerr=dy,
    fmt='o', elinewidth=2/3, capsize=2, capthick=2/3, color='black',
    zorder=10, label='Dados Coletados'
)

plt.yscale('log')
plt.grid(True, which='minor', axis='y', color='0.9')

logy, dlogy = np.log(y), dy / y

data = odr.RealData(x, logy, sx=dx, sy=dlogy)
odreg = odr.ODR(data, odr.models.unilinear)
ans = odreg.run()

a, b = ans.beta
da, db = np.sqrt(np.diag(ans.cov_beta))

rotulo = f'''Regressão Linearizada:
$\ln y = ({a:.0f} \pm {da:.0f}) \\times x^{{-1}} + ({b:.1f} \pm {db:.1f})$'''

X = np.linspace(min(x), max(x), num=200)
Y =  np.exp(a*X + b)
plt.plot(X, Y, color='red', alpha=0.4, label=rotulo)

plt.xlabel('Temperatura [$K$]')
plt.ylabel('Resistência [$\Omega$]')
plt.title(f'''Relação da Resistência pelo Inverso
da Temperatura em um Termistor''')
plt.legend()

plt.savefig('regres.pgf')