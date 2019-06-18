from caract import np, plt, Rs, Ts, A, dA, B, dB

# -- funções de cálculo de incerteza -- #

def resolucao(R):
    if      0 <= R <= 600:
        return 0.1
    elif   600 < R <= 6_000:
        return 1
    elif 6_000 < R <= 60_000:
        return 10
    else:
        raise ValueError


def dR_calibracao(R):
    d = resolucao(R)
    if    0 <= R <= 600:
        return 0.010 * R + 3 * d
    elif 600 < R <= 60_000:
        return 0.005 * R + 2 * d
    else:
        raise ValueError


def dist_retangular(a):
    return a / (2 * np.sqrt(3))


@np.vectorize
def dR_total(R):
    dR_calib = dist_retangular(2 * dR_calibracao(R))
    dR_leitura = dist_retangular(resolucao(R))

    return np.sqrt(dR_calib**2 + dR_leitura**2)

# -- #

# -- depois de mostrar a eq. característica -- #

# incerteza de cada R mostrado na reta
dRs = dR_total(Rs)

# e a inceteza de cada T
lnRmlnA = np.log(Rs) - np.log(A)
dTs = np.sqrt((lnRmlnA * dB)**2 + (dA/A)**2 + (dRs/Rs)**2)/lnRmlnA**2

# desenho da banda de incerteza
plt.fill_between(
    Rs, Ts-dTs, Ts+dTs,
    color='red', alpha=0.15,
    label='Faixa de Incerteza'
)

# -- coloca os textos e a legenda, depois salva o gráfico -- #

plt.legend()
plt.savefig('incert.pgf')
