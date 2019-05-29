from libs import pd, read_tsv, write_table, plt

dados = read_tsv('dados.tsv')

write_table(pd.DataFrame({
        k: dados[k].apply(lambda x: f'{x:.2f} {u}')
        for k, u in zip(dados.columns, ['V', 'mA'])
    }), 'dados.tex', column_format='rr')


# -- recupera os dados antes -- #

plt.scatter(dados['Tensão'], dados['Corrente'])

# -- depois salva o gráfico -- #

plt.savefig('dados.pgf')

# -- desenha os dados no gráfico antes -- #

plt.xlabel('Tensão [V]')
plt.ylabel('Corrente [mA]')
plt.title('''Relação da Corrente pela Tensão em um Resistor''')

# -- depois salva o gráfico -- #

plt.savefig('resultado.pgf')
plt.savefig('resultado.png')
