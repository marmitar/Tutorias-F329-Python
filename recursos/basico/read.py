from libs import pd, plt

# -- bibliotecas e configurações -- #

dados = pd.read_csv('dados.csv', decimal=',')

# -- bibliotecas e configurações -- #

dados = pd.read_excel('dados.xlsx', sheet_name='Resistor')

# -- depois do gráfico pronto -- #

plt.savefig('grafico.png', dpi=200)

# -- depois do gráfico pronto -- #

plt.savefig('grafico.pdf')

# -- depois do gráfico pronto -- #

plt.savefig('grafico.svg')
# -- ou -- #
plt.savefig('grafico.pgf')


from glob import glob
import os

for file in glob('grafico.*'):
    os.remove(file)
