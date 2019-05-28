from .libs import pd

dados = pd.read_csv('dados.csv', decimal=',')

dados = pd.read_excel('dados.xlsx', sheet_name='Resistor')
