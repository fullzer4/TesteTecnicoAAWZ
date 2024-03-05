import pandas as pd

def clean(value) -> float:
    return float(value.replace('R$ ', '').replace('.', '').replace(',', '.'))

vendas = pd.read_csv('./data/vendas.csv')
pagamentos = pd.read_csv('./data/pagamentos.csv')

# ------- Tarefa 1 -------

vendas['Comissao'] = vendas['Valor da Venda'].apply(lambda x: clean(x) * 0.1)
vendas.loc[vendas['Canal de Venda'] == 'Online', 'Comissao'] *= 0.8
vendas['Comissao_gerente'] = 0
vendas.loc[vendas['Comissao'] >= 1500, 'Comissao_gerente'] = vendas['Comissao'] * 0.1
vendas['Comissao_final'] = vendas['Comissao'] - vendas['Comissao_gerente']

saida_esperada = vendas[['Nome do Vendedor', 'Comissao', 'Comissao_final']]
print("Saída Esperada - Cálculo de Comissões:")
print(saida_esperada)

# ------- Tarefa 2 ------

pagamentos['Comissão'] = pagamentos['Comissão'].apply(clean)
pagamentos = pagamentos.merge(vendas[['Nome do Vendedor', 'Comissao_final']], on='Nome do Vendedor', how='left')

pagamentos['Diferenca'] = pagamentos['Comissao_final'] - pagamentos['Comissão']
pagamentos_incorretos = pagamentos[pagamentos['Diferenca'] != 0]

print("\nSaída Esperada - Validação de Pagamentos:")
print(pagamentos_incorretos[['Nome do Vendedor', 'Diferenca', 'Comissao_final']])
