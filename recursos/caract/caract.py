from libs import pd, np, plt, read_tsv, write_table
from scipy import odr

# -- importa as bibliotecas -- #

# coletando os dados
dados = pd.read_csv('termistor.tsv', decimal=',', sep='\t')

T, dT = dados['T'], dados['dT']
R, dR = dados['R'], dados['dR']

# valores medidos
plt.errorbar(
    R, T, xerr=dR, yerr=dT,
    fmt='o', elinewidth=2/3, capsize=2, capthick=2/3, color='black',
    zorder=10, label='Dados Coletados'
)

# transformação dos eixos
logR = np.log(R)
dlogR = dR / R

Tinv = 1/T      # inverso da temperatura
dTinv = dT/T**2

# regressão linear com incertezas
data = odr.RealData(Tinv, logR, sx=dTinv, sy=dlogR)
odreg = odr.ODR(data, odr.models.unilinear)
ans = odreg.run()

# coeficientes: lnR = a T^-1 + b
a, b = ans.beta
da, db = ans.sd_beta

# transforma para R = A e^(B/T)
A = np.exp(b)
dA = db * np.exp(b)

B = a
dB = da

# mostra os coeficientes da eq. característica
print(f'valor inicial   = {A}+-{dA}')
print(f'fator de cresc. = {B}+-{dB}')

# desenha a eq. característica
rotulo = f'''Equação Característica:
$T = \\frac{{({B:.0f} \pm {dB:.0f})}}{{\ln(R) - \ln({A:.4f} \pm {dA:.4f})}}$'''

Rs = np.linspace(min(R) - 2*min(dR), max(R) + 2*max(dR), num=200)
# então T = B/ln(R/A) = B/(lnR-lnA)
Ts = B/(np.log(Rs) - np.log(A))
plt.plot(Rs, Ts, color='red', alpha=0.4, label=rotulo)

# formatações do gráfico
plt.xlabel('Resistência [$\Omega$]')
plt.ylabel('Temperatura [$K$]')
plt.title(f'''Relação da Temperatura pela
Resistência em um Termistor''')
plt.legend()

# -- salva o gráfico -- #

if __name__ == "__main__":
    plt.savefig('caract.pgf')
