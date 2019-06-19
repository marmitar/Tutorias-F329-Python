from libs import pd, np, plt, read_tsv, write_table


dados = read_tsv('dados.tsv')

write_table(pd.DataFrame({
    'Tempo': dados['t'].apply(lambda x: f'{x:.1f} \si{{\ms}}'),
    '$V_1$': dados['V1'].apply(lambda x: f'{x:.1f} \si{{\\volt}}'),
    '$V_2$': dados['V2'].apply(lambda x: f'{x:.1f} \si{{\\volt}}'),
    'Corrente': dados['I'].apply(lambda x: f'{x:.0f} \si{{\mA}}')
}).head(6), 'dados.tex', column_format='cccc', escape=False)

# -- importa os dados antes -- #

# separando os dados
t = dados['t']
V1 = dados['V1']
V2 = dados['V2']
I = dados['I']

# desenha os gráficos
plt.plot(t, V1, color='red', alpha=0.6, label='Tensão de Entrada')
plt.plot(t, V2, color='blue', alpha=0.6, label='Tensão de Saída')

# coloca legenda e os textos
plt.legend()
plt.xlabel('Tempo [$ms$]')
plt.ylabel('Tensão [$V$]')
plt.title('Comportamento da Tensão em um Circuito RC')

# -- depois salva a figura -- #

plt.savefig('juntos.pgf')
plt.close()

# -- importa e separa os dados antes -- #

# criação dos eixos
eixo_esq = plt.subplot()
eixo_dir = eixo_esq.twinx()

# desenho e formatações do eixo esquerdo
eixo_esq.plot(t, V2, color='red', alpha=0.6, label='Tensão')
eixo_esq.set_ylabel('Tensão [$V$]')
eixo_esq.grid(False)

# mesmo para o eixo direito
eixo_dir.plot(t, I, color='blue', alpha=0.6, label='Corrente')
eixo_dir.set_ylabel('Corrente [$mA$]')
eixo_dir.grid(False)

# título r rótulo do eixo compartilhado
eixo_esq.set_title('Relação de Corrente e Tensão em um Capacitor')
eixo_esq.set_xlabel('Tempo [$ms$]')
# coluna do eixo da direita
eixo_dir.spines['right'].set_visible(True)
# e tira a coluna sobreposta
eixo_dir.spines['left'].set_visible(False)

# cores das colunas dos eixos
eixo_esq.spines['left'].set_color('red')
eixo_esq.spines['left'].set_alpha(0.6)
eixo_dir.spines['right'].set_color('blue')
eixo_dir.spines['right'].set_alpha(0.6)

# -- salva a figura -- #

plt.savefig('duplo.pgf')
plt.close()

# -- importa e separa os dados antes -- #

_, eixos = plt.subplots(nrows=2, ncols=1, sharex=True)
eixo_sup = eixos[0]
eixo_inf = eixos[1]

# eixo superior
eixo_sup.plot(t, V2, color='red', alpha=0.6)
eixo_sup.set_ylabel('Tensão [$V$]')

# eixo inferior
eixo_inf.plot(t, I, color='blue', alpha=0.6)
eixo_inf.set_ylabel('Corrente [$mA$]')

# formatações gerais
eixo_sup.set_title('Relação de Corrente e Tensão em um Capacitor')
eixo_inf.set_xlabel('Tempo [$ms$]')

# -- depois salva a figura -- #

plt.savefig('paineis.pgf')
