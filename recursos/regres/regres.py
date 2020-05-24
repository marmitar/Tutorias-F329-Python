from libs import pd, np, plt, read_tsv
# -- outras bibliotecas -- #
from scipy import odr

# -- resto do código -- #

arq = '../reta/dados.tsv'
dados = read_tsv(arq)

# -- recupera os dados antes -- #

# guarda as colunas em variáveis novas
x, y = dados['Tensão'], dados['Corrente']

# e coloca os dados pontuais no gráfico
plt.scatter(x, y, zorder=10, label='Dados Coletados')

# -- para fazer a regressão depois -- #

# regressão linear
data = odr.RealData(x, y)
odreg = odr.ODR(data, odr.models.unilinear)
odreg.set_job(fit_type=2)  # muda para mínimos quadrados
ans = odreg.run()

a, b = ans.beta                         # y = ax + b
da, db = np.sqrt(np.diag(ans.cov_beta)) # incertezas de a e b

# mostrando os coeficientes e suas incertezas
print(f'coef. angular = ({a}+-{da}) [mA/V -> kOhm^-1 -> kS]')
print(f'coef. linear  = ({b}+-{db}) [mA]')

# -- desenha a reta resultante da regressão e completa o gráfico -- #

# -- depois da regressão -- #

rotulo = 'Regressão Linear'
# ou
rotulo = f'Regressão: $y = ({a:.1f} \pm {da:.1f})~x + ({b:.1f} \pm {db:.1f})$'

# monta os limites para desenho da reta
X = np.linspace(min(x), max(x), num=200)
Y =  a * X + b
# e faz o gráfico dela atrá dos pontos
plt.plot(X, Y, color='red', alpha=0.4, label=rotulo)

# para exibir as legendas do gráfico
plt.legend()

# -- depois completa a formatação do gráfico e salva em uma imagem -- #

plt.xlabel('Tensão [V]')
plt.ylabel('Corrente [mA]')
plt.title('Regressão Linear da Corrente pela Tensão em um Resistor')

plt.savefig('resultado.pgf')
