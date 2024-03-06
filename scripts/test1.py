import pandas as pd

def clean(value) -> float:
    return float(value.replace('R$ ', '').replace('.', '').replace(',', '.'))

vendas = pd.read_csv('./data/vendas.csv')
pagamentos = pd.read_csv('./data/pagamentos.csv')

# ------- Tarefa 1 -------
print('')
print('---- Tarefa 1 ----')
print('')

vendas['Valor da Venda'] = vendas['Valor da Venda'].apply(clean)

vendas['Comissao'] = vendas['Valor da Venda'] * 0.10

vendas['Canal_Online'] = vendas['Canal de Venda'] == 'Online'

vendas['Comissao_Marketing'] = vendas.apply(lambda row: row['Comissao'] * 0.20 if row['Canal_Online'] else 0, axis=1)

vendas_agrupadas = vendas.groupby('Nome do Vendedor')[['Comissao', 'Comissao_Marketing']].sum().reset_index()

vendas_agrupadas['Comissao_Gerente'] = vendas_agrupadas.apply(lambda row: row['Comissao'] * 0.10 if row['Comissao'] >= 1500 else 0, axis=1)

vendas_agrupadas['Valor A Ser Pago'] = vendas_agrupadas['Comissao'] - vendas_agrupadas['Comissao_Gerente'] - vendas_agrupadas['Comissao_Marketing']

print(vendas_agrupadas[['Nome do Vendedor', 'Comissao', 'Valor A Ser Pago']])

# ------- Tarefa 2 ------

print('')
print('---- Tarefa 2 ----')
print('')

pagamentos['Comissão'] = pagamentos['Comissão'].apply(clean)

pagamentos_comparacao = pd.merge(pagamentos, vendas_agrupadas, on='Nome do Vendedor', how='left')

pagamentos_incorretos = pagamentos_comparacao[pagamentos_comparacao['Comissão'] != pagamentos_comparacao['Valor A Ser Pago']]

# Erro ao mudar nome
#collums_map = {
#    "Valor A Ser Pago": "Valor Correto",
#    "Comissão": "Valor Pago",
#}
#pagamentos_incorretos.rename(columns=collums_map)

pagamentos_incorretos['Valor Pago'] = pagamentos_incorretos['Comissão']
pagamentos_incorretos['Valor Correto'] = pagamentos_incorretos['Valor A Ser Pago']

print(pagamentos_incorretos[['Nome do Vendedor', 'Valor Pago', 'Valor Correto']])

